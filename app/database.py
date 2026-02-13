"""
database.py - 데이터베이스 매니저 클래스
"""

import logging
from typing import Optional, List, Dict, Any
from datetime import datetime

from sqlmodel import Session, SQLModel, create_engine, select
from sqlalchemy.exc import IntegrityError

from .models import (
    APIMst, 
    APIParam, 
    JobMst, 
    ValidationResult,
    StockPrice,
    DailyPrice,
    DisplayBoardTop,
)
import pandas as pd


from app.config import DB_PATH

class DatabaseManager:
    """SQLModel based Database Manager"""
    
    def __init__(self, db_path: str = None):
        if db_path is None:
            self.db_path = DB_PATH
        else:
            self.db_path = db_path
            
        self.engine = create_engine(f"sqlite:///{self.db_path}", echo=False)

    
    def get_session(self) -> Session:
        """세션 생성"""
        return Session(self.engine)
    
    # ==================== API Definition 관리 ====================
    
    def add_api_definition(
        self,
        api_name: str,
        api_url: str,
        tr_id: str,
        tr_cont: str = "",
        description: Optional[str] = None,
        output_table_name: Optional[str] = None,
      
    ) -> Optional[APIMst]:
        """API 정의 추가"""
        with self.get_session() as session:
            try:
                api_def = APIMst(
                    api_name=api_name,
                    api_url=api_url,
                    tr_id=tr_id,
                    tr_cont=tr_cont,
                    description=description,
                    output_table_name=output_table_name,
                    
                )
                session.add(api_def)
                session.commit()
                session.refresh(api_def)
                logging.info(f"✓ API 정의 추가: {api_name}")
                return api_def
            except IntegrityError:
                logging.error(f"✗ 이미 존재하는 프로그램: {api_name}")
                return None
    
    def get_api_definition(self, api_name: str) -> Optional[APIMst]:
        """API 정의 조회"""
        with self.get_session() as session:
            statement = select(APIMst).where(
                APIMst.api_name == api_name,
                # APIMst.is_active == True
            )
            return session.exec(statement).first()
    
    def list_api_definitions(self) -> List[APIMst]:
        """모든 활성 API 목록"""
        with self.get_session() as session:
            # statement = select(APIMst).where(APIMst.is_active == True)
            statement = select(APIMst)
            return list(session.exec(statement).all())
    
    # ==================== Parameter Definition 관리 ====================
    
    def add_parameter_definition(
        self,
        api_name: str,
        param_name: str,
        param_type: str = "string",
        is_required: bool = False,
        default_value: Optional[str] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        allowed_values: Optional[str] = None,
        description: Optional[str] = None
    ) -> Optional[APIParam]:
        """파라미터 정의 추가 (검증 룰 포함)"""
        api_def = self.get_api_definition(api_name)
        if not api_def:
            logging.error(f"✗ API 정의 없음: {api_name}")
            return None
        
        # 파라미터 이름 대문자 정규화
        param_name = param_name.upper()
        
        with self.get_session() as session:
            param_def = APIParam(
                api_name=api_def.api_name,
                param_name=param_name,
                param_type=param_type,
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
            logging.info(f"✓ 파라미터 정의: {api_name}.{param_name}")
            return param_def
    
    def get_parameter_definitions(self, api_name: str) -> List[APIParam]:
        """파라미터 정의 목록 조회"""
        api_def = self.get_api_definition(api_name)
        if not api_def:
            return []
        
        with self.get_session() as session:
            statement = select(APIParam).where(
                APIParam.api_name == api_def.api_name
            )
            return list(session.exec(statement).all())
    
    # ==================== User Input 관리 (JSON 형식) ====================
    
    def add_user_input(
        self,
        api_name: str,
        params: Dict[str, Any],
        description: Optional[str] = None,
        is_active: bool = True,
        save_mode: str = "append",
        execution_cycle: str = "5min"
    ) -> JobMst:
        """
        사용자 입력 추가/업데이트 (JSON 형식)
        
        ✨ 핵심: params는 딕셔너리 {"KEY": "VALUE", ...}
        """
        with self.get_session() as session:
            # 기존 입력 확인
            statement = select(JobMst).where(
                JobMst.api_name == api_name
            )
            existing = session.exec(statement).first()
            
            if existing:
                # 업데이트
                existing.set_params_dict(params)
                existing.description = description
                existing.is_active = is_active
                existing.save_mode = save_mode
                existing.execution_cycle = execution_cycle
                existing.updated_at = datetime.now()
                session.add(existing)
                session.commit()
                session.refresh(existing)
                logging.info(f"✓ 사용자 입력 업데이트: {api_name} ({len(params)}개, Active={is_active})")
                return existing
            else:
                # 새로 추가
                user_input = JobMst(
                    api_name=api_name,
                    params_json="",
                    description=description,
                    is_active=is_active,
                    save_mode=save_mode,
                    execution_cycle=execution_cycle
                )
                user_input.set_params_dict(params)
                session.add(user_input)
                session.commit()
                session.refresh(user_input)
                logging.info(f"✓ 사용자 입력 추가: {api_name} ({len(params)}개, Active={is_active})")
                return user_input
    
    def get_user_input(self, api_name: str) -> Optional[JobMst]:
        """사용자 입력 조회"""
        with self.get_session() as session:
            statement = select(JobMst).where(
                JobMst.api_name == api_name
            )
            return session.exec(statement).first()
    
    def list_user_inputs(self) -> List[JobMst]:
        """모든 사용자 입력 목록"""
        with self.get_session() as session:
            statement = select(JobMst)
            return list(session.exec(statement).all())

    def list_active_user_inputs(self, cycle: str = None) -> List[JobMst]:
        """
        활성화된 사용자 입력 목록 조회
        :param cycle: 실행 주기 필터 (None이면 전체)
        """
        with self.get_session() as session:
            statement = select(JobMst).where(JobMst.is_active == True)
            
            if cycle:
                statement = statement.where(JobMst.execution_cycle == cycle)
                
            return list(session.exec(statement).all())
    
    def delete_user_input(self, api_name: str) -> bool:
        """사용자 입력 삭제"""
        with self.get_session() as session:
            statement = select(JobMst).where(
                JobMst.api_name == api_name
            )
            user_input = session.exec(statement).first()
            
            if user_input:
                session.delete(user_input)
                session.commit()
                logging.info(f"✓ 사용자 입력 삭제: {api_name}")
                return True
            return False
    
    # ==================== 검증 엔진 ====================
    
    def validate_user_inputs(self, api_name: str) -> ValidationResult:
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
        api_def = self.get_api_definition(api_name)
        if not api_def:
            result.is_valid = False
            result.errors.append(f"API 정의 없음: {api_name}")
            return result
        
        # 2. 파라미터 정의 조회
        param_defs = self.get_parameter_definitions(api_name)
        if not param_defs:
            result.warnings.append("파라미터 정의 없음 - 검증 생략")
            return result
        
        # 3. 사용자 입력 조회 (JSON → Dict) 및 대문자로 정규화
        user_input = self.get_user_input(api_name)
        raw_user_params = user_input.get_params_dict() if user_input else {}
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

    def insert_output_data(self, api_name: str, df: pd.DataFrame) -> int:
        """DataFrame을 output 테이블에 삽입"""
        api_def = self.get_api_definition(api_name)
        user_input = self.get_user_input(api_name)
        if not api_def or not api_def.output_table_name:
            logging.warning(f"Output table not defined for {api_name}")
            return 0
        
        # Get output model class dynamically
        output_model = self._get_output_model(api_def.output_table_name)
        if not output_model:
            logging.warning(f"Output model not found for table: {api_def.output_table_name}")
            return 0
        
        try:
            # Overwrite 모드인 경우 기존 데이터 삭제
            if user_input.save_mode == "overwrite":
                with self.get_session() as session:
                    statement = select(output_model).where(output_model.api_name == api_name)
                    results = session.exec(statement).all()
                    if results:
                        for row in results:
                            session.delete(row)
                        session.commit()
                        logging.info(f"Overwrote existing data for {api_name} ({len(results)} rows deleted)")

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
                    
                    # Create record with api_name
                    record = output_model(
                        api_name=api_name,
                        **model_data
                    )
                    session.add(record)
                    count += 1
                session.commit()
                return count
        except Exception as e:
            logging.error(f"Error inserting output data: {e}")
            import traceback
            logging.error(traceback.format_exc())
            return 0

    def _get_output_model(self, table_name: str):
        """Get output model class by table name"""
        mapping = {
            "stock_price": StockPrice,
            "daily_price": DailyPrice,
            "display_board_top": DisplayBoardTop,
        }
        return mapping.get(table_name)
