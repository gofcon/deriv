"""
database.py - 데이터베이스 매니저 클래스
"""

import logging
from typing import Optional, List, Dict, Any
from datetime import datetime

from sqlmodel import Session, SQLModel, create_engine, select
from sqlalchemy.exc import IntegrityError

from .models_gofcon import (
    ApiMst, 
    ApiParam, 
    ApiJobMst,
    BrowserMst,
    BrowserJobMst,
    BrowserRst,
    KrxIsinMst,
    ValidationResult,
    StockPrice,
    DailyPrice,
    DisplayBoardTop,
)
# from .models import (
#     ValidationResult,
#     StockPrice,
#     DailyPrice,
#     DisplayBoardTop,
# )
import pandas as pd


from app.config import DB_PATH, get_engine_kwargs

class DatabaseManager:
    """SQLModel based Database Manager"""
    
    def __init__(self, db_path: str = None):
        kwargs = get_engine_kwargs()
        url = kwargs.pop("url")
        
        # 만약 명시적으로 경로가 주어지고 (CLI), 설정이 sqlite인 경우에만 URL 덮어쓰기
        from app.config import DB_TYPE
        if db_path is not None and DB_TYPE == "sqlite":
            url = f"sqlite:///{db_path}"
            
        self.engine = create_engine(url, **kwargs)
        # OracleDialect workaround for JSON deserialization
        import json
        if not hasattr(self.engine.dialect, '_json_deserializer'):
            self.engine.dialect._json_deserializer = lambda x: json.loads(x) if isinstance(x, (str, bytes, bytearray)) else x
        if not hasattr(self.engine.dialect, '_json_serializer'):
            self.engine.dialect._json_serializer = json.dumps

    
    def get_session(self) -> Session:
        """세션 생성"""
        return Session(self.engine)
    
    # ==================== API Definition 관리 ====================
    
    def add_api_mst(
        self,
        api_id: str,
        api_name: str,
        api_type: str,
        api_url: str,
        header_json: dict,
        request_type: str = "GET",
        description: Optional[str] = None,
        output_table_name: Optional[str] = None,
      
    ) -> Optional[ApiMst]:
        """API 정의 추가"""
        with self.get_session() as session:
            try:
                api_def = ApiMst(
                    api_id=api_id,
                    api_name=api_name,
                    api_type=api_type,
                    api_url=api_url,
                    header_json=header_json,
                    request_type=request_type,
                    description=description,
                    output_table_name=output_table_name,
                    
                )
                session.add(api_def)
                session.commit()
                session.refresh(api_def)
                logging.info(f"✓ API 정의 추가: {api_name} (API_ID: {api_id})")
                return api_def
            except IntegrityError:
                logging.error(f"✗ 이미 존재하는 프로그램: {api_id}")
                return None
    
    def get_api_mst(self, api_id: str) -> Optional[ApiMst]:
        """API 정의 조회"""
        with self.get_session() as session:
            statement = select(ApiMst).where(
                ApiMst.api_id == api_id
            )
            return session.exec(statement).first()
    
    def list_api_msts(self) -> List[ApiMst]:
        """모든 활성 API 목록"""
        with self.get_session() as session:
            statement = select(ApiMst)
            return list(session.exec(statement).all())
    
    # ==================== Parameter Definition 관리 ====================
    
    def add_api_param(
        self,
        api_id: str,
        param_name: str,
        is_required: bool = False,
        default_value: Optional[str] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        allowed_values: Optional[str] = None,
        description: Optional[str] = None
    ) -> Optional[ApiParam]:
        """파라미터 정의 추가 (검증 룰 포함)"""
        api_def = self.get_api_mst(api_id)
        if not api_def:
            logging.error(f"✗ API 정의 없음: {api_id}")
            return None
        
        # 파라미터 이름 대문자 정규화
        param_name = param_name.upper()
        
        with self.get_session() as session:
            param_def = ApiParam(
                api_id=api_id,
                param_name=param_name,
                is_required=is_required,
                default_value=default_value,
                min_length=min_length,
                max_length=max_length,
                allowed_values=allowed_values,
                description=description
            )
            session.add(param_def)
            session.commit()
            session.refresh(param_def)
            logging.info(f"✓ 파라미터 정의: {api_id}.{param_name}")
            return param_def
    
    def get_api_params(self, api_id: str) -> List[ApiParam]:
        """파라미터 정의 목록 조회"""
        api_def = self.get_api_mst(api_id)
        if not api_def:
            return []
        
        with self.get_session() as session:
            statement = select(ApiParam).where(
                ApiParam.api_id == api_id
            )
            return list(session.exec(statement).all())
    
    # ==================== User Input 관리 (JSON 형식) ====================
    
    def add_api_job_mst(
        self,
        job_id: str,
        api_id: str,
        params: Dict[str, Any],
        description: Optional[str] = None,
        is_active: bool = True,
        save_mode: str = "append",
        execution_cycle: str = "5min"
    ) -> ApiJobMst:
        """
        사용자 입력 추가/업데이트 (JSON 형식)
        
        ✨ 핵심: params는 딕셔너리 {"KEY": "VALUE", ...}
        """
        import json
        with self.get_session() as session:
            # 기존 입력 확인
            statement = select(ApiJobMst).where(
                ApiJobMst.job_id == job_id
            )
            existing = session.exec(statement).first()
            
            if existing:
                # 업데이트
                existing.params_json = params
                existing.api_id = api_id
                existing.description = description
                existing.is_active = is_active
                existing.save_mode = save_mode
                existing.execution_cycle = execution_cycle
                existing.updated_at = datetime.now()
                session.add(existing)
                session.commit()
                session.refresh(existing)
                logging.info(f"✓ 사용자 입력 업데이트: {job_id} ({len(params)}개, Active={is_active})")
                return existing
            else:
                # 새로 추가
                user_input = ApiJobMst(
                    job_id=job_id,
                    api_id=api_id,
                    description=description,
                    is_active=is_active,
                    save_mode=save_mode,
                    execution_cycle=execution_cycle
                )
                user_input.params_json = params
                session.add(user_input)
                session.commit()
                session.refresh(user_input)
                logging.info(f"✓ 사용자 입력 추가: {job_id} ({len(params)}개, Active={is_active})")
                return user_input
    
    def get_api_job_mst(self, job_id: str) -> Optional[ApiJobMst]:
        """API 사용자 입력(Job) 조회"""
        with self.get_session() as session:
            statement = select(ApiJobMst).where(
                ApiJobMst.job_id == job_id
            )
            return session.exec(statement).first()
    
    def list_api_job_msts(self) -> List[ApiJobMst]:
        """모든 API 사용자 입력(Job) 목록"""
        with self.get_session() as session:
            statement = select(ApiJobMst)
            return list(session.exec(statement).all())

    def list_active_api_job_msts(self, cycle: str = None) -> List[ApiJobMst]:
        """
        활성화된 API 사용자 입력(Job) 목록 조회
        :param cycle: 실행 주기 필터 (None이면 전체)
        """
        with self.get_session() as session:
            statement = select(ApiJobMst).where(ApiJobMst.is_active == True)
            
            if cycle:
                statement = statement.where(ApiJobMst.execution_cycle == cycle)
                
            return list(session.exec(statement).all())
    
    def delete_api_job_mst(self, job_id: str) -> bool:
        """API 사용자 입력(Job) 삭제"""
        with self.get_session() as session:
            statement = select(ApiJobMst).where(
                ApiJobMst.job_id == job_id
            )
            job_input = session.exec(statement).first()
            
            if job_input:
                session.delete(job_input)
                session.commit()
                logging.info(f"✓ 사용자 입력 삭제: {job_id}")
                return True
            return False
            
    # ==================== Browser 스펙 통제 관리 ====================

    def add_browser_mst(
        self,
        browser_id: str,
        browser_name: str,
        target_url: str,
        output_table_name: str = None,
        selector_json: dict = None,
        behavior_json: list = None,
        pagination_json: dict = None,
        human_like: bool = False,
        description: str = None
    ) -> BrowserMst:
        """Browser 스크래핑 템플릿 추가/업데이트"""
        with self.get_session() as session:
            statement = select(BrowserMst).where(BrowserMst.browser_id == browser_id)
            existing = session.exec(statement).first()
            
            if existing:
                existing.browser_name = browser_name
                existing.target_url = target_url
                existing.output_table_name = output_table_name
                if selector_json is not None: existing.selector_json = selector_json
                if behavior_json is not None: existing.behavior_json = behavior_json
                if pagination_json is not None: existing.pagination_json = pagination_json
                existing.human_like = human_like
                if description: existing.description = description
                session.add(existing)
                session.commit()
                session.refresh(existing)
                logging.info(f"✓ Browser 정의 업데이트: {browser_name} (ID: {browser_id})")
                return existing
            else:
                new_def = BrowserMst(
                    browser_id=browser_id,
                    browser_name=browser_name,
                    target_url=target_url,
                    output_table_name=output_table_name,
                    selector_json=selector_json or {},
                    behavior_json=behavior_json or [],
                    pagination_json=pagination_json or {},
                    human_like=human_like,
                    description=description
                )
                session.add(new_def)
                session.commit()
                session.refresh(new_def)
                logging.info(f"✓ Browser 정의 추가: {browser_name} (ID: {browser_id})")
                return new_def

    def get_browser_mst(self, browser_id: str) -> Optional[BrowserMst]:
        """Browser 정의 조회"""
        with self.get_session() as session:
            statement = select(BrowserMst).where(BrowserMst.browser_id == browser_id)
            return session.exec(statement).first()

    # ==================== Browser 스크래핑 작업(Job) 관리 ====================

    def add_browser_job_mst(
        self,
        job_id: str,
        browser_id: str,
        params: Dict[str, Any],
        description: str = None,
        is_active: bool = True,
        save_mode: str = "append",
        execution_cycle: str = "daily"
    ) -> BrowserJobMst:
        """Browser 스크래핑 인스턴스 추가/업데이트"""
        import json
        with self.get_session() as session:
            statement = select(BrowserJobMst).where(BrowserJobMst.job_id == job_id)
            existing = session.exec(statement).first()
            
            if existing:
                existing.browser_id = browser_id
                existing.params_json = params
                existing.description = description
                existing.is_active = is_active
                existing.save_mode = save_mode
                existing.execution_cycle = execution_cycle
                session.add(existing)
                session.commit()
                session.refresh(existing)
                logging.info(f"✓ Browser 작업 업데이트: {job_id}")
                return existing
            else:
                new_job = BrowserJobMst(
                    job_id=job_id,
                    browser_id=browser_id,
                    description=description,
                    params_json=params,
                    is_active=is_active,
                    save_mode=save_mode,
                    execution_cycle=execution_cycle
                )
                session.add(new_job)
                session.commit()
                session.refresh(new_job)
                logging.info(f"✓ Browser 작업 추가: {job_id} ({len(params)}개 파라미터, Active={is_active})")
                return new_job

    def get_browser_job_mst(self, job_id: str) -> Optional[BrowserJobMst]:
        """Browser 작업(Job) 조회"""
        with self.get_session() as session:
            statement = select(BrowserJobMst).where(BrowserJobMst.job_id == job_id)
            return session.exec(statement).first()

    def list_active_browser_job_msts(self, cycle: str = None) -> List[BrowserJobMst]:
        """활성화된 Browser 작업(Job) 목록 조회"""
        with self.get_session() as session:
            statement = select(BrowserJobMst).where(BrowserJobMst.is_active == True)
            if cycle:
                statement = statement.where(BrowserJobMst.execution_cycle == cycle)
            return list(session.exec(statement).all())
    
    # ==================== 검증 엔진 ====================
    
    def validate_job_inputs(self, api_id: str, job_id: str) -> ValidationResult:
        """
        사용자 입력 검증
        
        검증 항목:
        1. 필수 파라미터 누락 체크
        2. 허용값 체크
        3. 길이 체크 (min/max)
        4. 정의되지 않은 파라미터 경고
        
        Note: 파라미터 이름은 대소문자 구분 없이 모두 대문자로 처리됩니다.
        """
        result = ValidationResult(
            is_valid=True, 
            errors=[], 
            warnings=[], 
            validated_params={}
        )
        
        # 1. API 정의 확인
        api_def = self.get_api_mst(api_id)
        if not api_def:
            result.is_valid = False
            result.errors.append(f"API 정의 없음: {api_id}")
            return result
        
        # 2. 파라미터 정의 조회
        param_defs = self.get_api_params(api_id)
        if not param_defs:
            result.warnings.append("파라미터 정의 없음 - 검증 생략")
            return result
        
        # 3. 사용자 입력 조회 (JSON → Dict) 및 대문자로 정규화
        job_input = self.get_api_job_mst(job_id)
        raw_user_params = job_input.params_json if job_input else {}
        if isinstance(raw_user_params, str):
            import json
            raw_user_params = json.loads(raw_user_params) if raw_user_params else {}
        # 파라미터 키를 모두 대문자로 변환
        user_params = {k.upper(): v for k, v in raw_user_params.items()}
        
        # 4. 각 파라미터 검증 및 기본값 적용
        for param_def in param_defs:
            param_name = param_def.param_name  # 이미 대문자로 저장됨
            param_value = user_params.get(param_name)
            
            # 4-1. 필수 파라미터 체크
            if param_def.is_required:
                if param_value is None or param_value == "":
                    result.is_valid = False
                    result.errors.append(f"필수 파라미터 누락: {param_name}")
                    continue
            
            # 4-2. 값이 없으면 기본값 사용 (optional 파라미터)
            if param_value is None or param_value == "":
                if param_def.default_value:
                    param_value = param_def.default_value
                else:
                    param_value = ""  # 기본값이 없으면 공백으로
                result.validated_params[param_name] = param_value
                continue
            
            # 4-3. 길이 체크
            if param_def.min_length and len(str(param_value)) < param_def.min_length:
                result.is_valid = False
                result.errors.append(
                    f"{param_name}: 최소 길이 {param_def.min_length} 미만 "
                    f"(현재: {len(str(param_value))})"
                )
            
            if param_def.max_length and len(str(param_value)) > param_def.max_length:
                result.is_valid = False
                result.errors.append(
                    f"{param_name}: 최대 길이 {param_def.max_length} 초과 "
                    f"(현재: {len(str(param_value))})"
                )
            
            # 4-4. 허용값 체크
            if param_def.allowed_values:
                allowed = [v.strip() for v in param_def.allowed_values.split(',')]
                if str(param_value) not in allowed:
                    result.is_valid = False
                    result.errors.append(
                        f"{param_name}: 허용되지 않은 값 '{param_value}' "
                        f"(허용: {allowed})"
                    )
            
            # 검증 통과 - validated_params에 추가 (대문자 키로)
            result.validated_params[param_name] = str(param_value)
        
        # 5. 정의되지 않은 파라미터 경고
        defined_params = {pd.param_name for pd in param_defs}
        for param_name in user_params.keys():
            if param_name not in defined_params:
                result.warnings.append(f"정의되지 않은 파라미터: {param_name}")
                result.validated_params[param_name] = str(user_params[param_name])
        
        return result

    def insert_output_data(self, api_id: str, job_id: str, df: pd.DataFrame) -> int:
        """DataFrame을 output 테이블에 삽입"""
        api_def = self.get_api_mst(api_id)
        job_input = self.get_api_job_mst(job_id)
        if not api_def or not api_def.output_table_name:
            logging.warning(f"Output table not defined for API_ID: {api_id}")
            return 0
        
        # Get output model class dynamically
        output_model = self._get_output_model(api_def.output_table_name)
        if not output_model:
            logging.warning(f"Output model not found for table: {api_def.output_table_name}")
            return 0
        
        try:
            # Overwrite 모드인 경우 기존 데이터 삭제
            if job_input and job_input.save_mode == "overwrite":
                with self.get_session() as session:
                    # Depending on how the output table identifies records, 
                    # usually it was linked by api_name. Assuming it's now api_id.
                    if hasattr(output_model, "api_id"):
                        statement = select(output_model).where(output_model.api_id == api_id)
                    elif hasattr(output_model, "tr_id"):
                        statement = select(output_model).where(output_model.tr_id == api_id)
                    else:
                        statement = select(output_model).where(output_model.api_name == api_def.api_name)
                    
                    results = session.exec(statement).all()
                    if results:
                        for row in results:
                            session.delete(row)
                        session.commit()
                        logging.info(f"Overwrote existing data for {api_id} ({len(results)} rows deleted)")


            # valid keys caching
            valid_keys = output_model.model_fields.keys() if hasattr(output_model, 'model_fields') else None

            # Insert rows
            with self.get_session() as session:
                count = 0
                for _, row in df.iterrows():
                    # Convert row to dict
                    row_dict = row.to_dict()
                    
                    # Convert all values to strings as per model definition
                    model_data = {}
                    for k, v in row_dict.items():
                        if pd.notna(v) and (valid_keys is None or k in valid_keys):
                             model_data[k] = str(v)
                    
                    # Create record with api_id and api_name depending on model
                    if hasattr(output_model, "api_id"):
                        model_data["api_id"] = api_id
                    elif hasattr(output_model, "tr_id"): # Fallback for old models if any
                        model_data["tr_id"] = api_id
                    if hasattr(output_model, "api_name"):
                        model_data["api_name"] = api_def.api_name
                        
                    record = output_model(**model_data)
                    session.add(record)
                    count += 1
                session.commit()
                return count
        except Exception as e:
            logging.error(f"Error inserting output data: {e}")
            import traceback
            logging.error(traceback.format_exc())
            return 0

    def insert_browser_output_data(self, browser_id: str, job_id: str, df: pd.DataFrame) -> int:
        """Browser DataFrame을 output 테이블에 삽입"""
        browser_def = self.get_browser_mst(browser_id)
        job_input = self.get_browser_job_mst(job_id)
        if not browser_def or not browser_def.output_table_name:
            logging.warning(f"Output table not defined for BROWSER_ID: {browser_id}")
            return 0
        
        output_model = self._get_output_model(browser_def.output_table_name.upper() if browser_def.output_table_name else "")
        if not output_model:
            logging.warning(f"Output model not found for table: {browser_def.output_table_name}")
            return 0
        
        try:
            # === Generalized JSON Table Branch ===
            if browser_def.output_table_name.upper() == "BROWSER_RST":
                if job_input and job_input.save_mode == "overwrite":
                    with self.get_session() as session:
                        statement = select(BrowserRst).where(BrowserRst.browser_id == browser_id)
                        results = session.exec(statement).all()
                        if results:
                            for row in results:
                                session.delete(row)
                            session.commit()
                            logging.info(f"Overwrote existing general data for {browser_id} ({len(results)} rows deleted)")

                with self.get_session() as session:
                    count = 0
                    for _, row in df.iterrows():
                        row_dict = row.to_dict()
                        
                        # Clean out NaNs for JSON serialization
                        clean_dict = {k: v for k, v in row_dict.items() if pd.notna(v)}
                        
                        record = BrowserRst(
                            browser_id=browser_id,
                            job_id=job_id,
                            result_json=clean_dict
                        )
                        session.add(record)
                        count += 1
                    session.commit()
                    return count
            
            # === Specific Schema Branch ===
            if job_input and job_input.save_mode == "overwrite":
                with self.get_session() as session:
                    # Depending on how the output table identifies records
                    if hasattr(output_model, "api_id"):
                        statement = select(output_model).where(output_model.api_id == browser_id)
                    elif hasattr(output_model, "tr_id"):
                        statement = select(output_model).where(output_model.tr_id == browser_id)
                    else:
                        statement = select(output_model).where(output_model.api_name == browser_def.browser_name)
                    
                    results = session.exec(statement).all()
                    if results:
                        for row in results:
                            session.delete(row)
                        session.commit()
                        logging.info(f"Overwrote existing data for {browser_id} ({len(results)} rows deleted)")

            valid_keys = output_model.model_fields.keys() if hasattr(output_model, 'model_fields') else None

            with self.get_session() as session:
                count = 0
                for _, row in df.iterrows():
                    row_dict = row.to_dict()
                    
                    model_data = {}
                    for k, v in row_dict.items():
                        if pd.notna(v) and (valid_keys is None or k in valid_keys):
                             model_data[k] = str(v)
                    
                    if hasattr(output_model, "api_id"):
                        model_data["api_id"] = browser_id
                    elif hasattr(output_model, "tr_id"):
                        model_data["tr_id"] = browser_id
                    if hasattr(output_model, "api_name"):
                        model_data["api_name"] = browser_def.browser_name
                        
                    record = output_model(**model_data)
                    session.add(record)
                    count += 1
                session.commit()
                return count
        except Exception as e:
            logging.error(f"Error inserting browser output data: {e}")
            import traceback
            logging.error(traceback.format_exc())
            return 0

    def _get_output_model(self, table_name: str):
        """Get output model class by table name"""
        mapping = {
            "KIS_STOCK_PRICE": StockPrice,
            "KIS_DAILY_PRICE": DailyPrice,
            "KRX_ISIN_MST": KrxIsinMst,
            "BROWSER_RST": BrowserRst
        }
        return mapping.get(table_name)
