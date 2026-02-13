# KIS API 데이터베이스 검증 시스템 구축 스킬 (최종 버전)

## 📋 목차
1. [시스템 개요](#시스템-개요)
2. [전체 아키텍처](#전체-아키텍처)
3. [필수 파일 및 구조](#필수-파일-및-구조)
4. [단계별 구현 가이드](#단계별-구현-가이드)
5. [완전한 코드 예제](#완전한-코드-예제)
6. [사용 방법](#사용-방법)
7. [검증 로직 상세](#검증-로직-상세)
8. [트러블슈팅](#트러블슈팅)
9. [확장 및 커스터마이징](#확장-및-커스터마이징)

---

## 시스템 개요

### 목적
한국투자증권(KIS) API를 위한 완전한 데이터베이스 기반 파라미터 검증 및 실행 시스템 구축

### 핵심 기능
- ✅ SQLite + SQLModel 기반 API 메타데이터 중앙 관리
- ✅ 파라미터 사전 정의 및 자동 검증 (필수값, 허용값, 길이)
- ✅ JSON 형식의 효율적인 사용자 입력 관리
- ✅ 설정과 실행의 완전한 분리
- ✅ CSV 파일을 통한 대량 임포트/익스포트

### 주요 개선 사항
```
v1 (CSV 기반) 
  → v2 (DB 기반, 개별 행) 
    → v3 (DB 기반, JSON 형식) ✨ 최종
```

**v3의 혁신:**
- UserInput을 JSON으로 저장하여 program_name 중복 입력 제거
- 완전 DB 중심 동작 (CSV/JSON 파일 불필요)
- 설정(--set-input)과 실행을 명확히 분리

---

## 전체 아키텍처

```
┌─────────────────────────────────────────────────────────────────┐
│                     KIS API 검증 시스템                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────┐                                            │
│  │ APIDefinition    │  ← API 메타데이터 저장                     │
│  ├──────────────────┤                                            │
│  │ - program_name   │  (유니크 키)                               │
│  │ - api_url        │  (엔드포인트)                              │
│  │ - tr_id          │  (거래 ID)                                 │
│  │ - tr_cont        │  (연속 조회)                               │
│  │ - description    │                                            │
│  └────────┬─────────┘                                            │
│           │ 1:N                                                  │
│           ▼                                                      │
│  ┌──────────────────────┐                                        │
│  │ ParameterDefinition  │  ← 검증 룰 정의                        │
│  ├──────────────────────┤                                        │
│  │ - param_name         │                                        │
│  │ - is_required        │  (필수 여부)                           │
│  │ - allowed_values     │  (허용값: "A,B,C")                    │
│  │ - min_length         │  (최소 길이)                           │
│  │ - max_length         │  (최대 길이)                           │
│  │ - default_value      │                                        │
│  │ - description        │                                        │
│  └──────────────────────┘                                        │
│                                                                   │
│  ┌──────────────────────┐                                        │
│  │ UserInput            │  ← 실제 파라미터 값 (JSON)             │
│  ├──────────────────────┤                                        │
│  │ - program_name       │  (유니크 키)                           │
│  │ - params_json        │  {"KEY":"VALUE",...}                  │
│  │ - description        │                                        │
│  └──────────────────────┘                                        │
│           │                                                      │
│           ▼                                                      │
│  ┌──────────────────────┐                                        │
│  │ Validation Engine    │  ← 검증 로직                           │
│  ├──────────────────────┤                                        │
│  │ 1. 필수값 체크       │                                        │
│  │ 2. 허용값 체크       │                                        │
│  │ 3. 길이 체크         │                                        │
│  │ 4. 타입 체크         │                                        │
│  └──────────────────────┘                                        │
│           │                                                      │
│           ▼                                                      │
│  ┌──────────────────────┐                                        │
│  │ KIS API Call         │  ← kis_auth._url_fetch()              │
│  └──────────────────────┘                                        │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 필수 파일 및 구조

### 프로젝트 구조
```
kis_api_project/
├── models.py                 # SQLModel 데이터 모델 정의
├── database.py               # DatabaseManager 클래스
├── main_v3.py                # 메인 실행 프로그램
├── csv_importer.py           # CSV ↔ DB 변환 도구
├── requirements.txt          # Python 패키지 의존성
├── kis_auth.py               # KIS 인증 모듈 (기존)
├── kis_api.db                # SQLite DB (자동 생성)
├── SKILL.md                  # 이 문서
├── README.md                 # 사용 설명서
└── QUICKSTART_V3.md          # 빠른 시작 가이드
```

### 의존성 (requirements.txt)
```txt
# 데이터베이스
sqlmodel>=0.0.14
sqlalchemy>=2.0.0

# 데이터 처리
pandas>=2.0.0

# KIS API 통신 (kis_auth.py에서 사용)
requests>=2.31.0
PyYAML>=6.0
pycryptodome>=3.19.0
websockets>=12.0
```

---

## 단계별 구현 가이드

### 🔧 1단계: models.py - 데이터 모델 정의

**목적:** SQLModel을 사용하여 3개 테이블 + 검증 결과 모델 정의

**핵심 설계:**
- APIDefinition: 1개 API = 1개 행
- ParameterDefinition: 1개 파라미터 = 1개 행 (검증 룰 포함)
- UserInput: 1개 프로그램 = 1개 행 (JSON 형식) ✨

```python
"""
models.py - SQLModel 기반 데이터베이스 모델 정의
"""

import json
from typing import Optional, List, Dict, Any
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship


class APIDefinition(SQLModel, table=True):
    """
    API 정의 테이블
    각 KIS API의 메타데이터를 저장
    """
    
    __tablename__ = "api_definitions"
    
    # 기본 필드
    id: Optional[int] = Field(default=None, primary_key=True)
    program_name: str = Field(index=True, unique=True, description="프로그램 식별자")
    api_url: str = Field(description="API 엔드포인트 URL")
    tr_id: str = Field(description="거래 ID")
    tr_cont: str = Field(default="", description="연속 조회 키")
    description: Optional[str] = Field(default=None, description="API 설명")
    
    # 관리 필드
    is_active: bool = Field(default=True, description="활성화 여부")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    # 관계 정의
    parameters: List["ParameterDefinition"] = Relationship(back_populates="api")


class ParameterDefinition(SQLModel, table=True):
    """
    파라미터 정의 테이블
    각 파라미터의 검증 룰을 저장
    """
    
    __tablename__ = "parameter_definitions"
    
    # 기본 필드
    id: Optional[int] = Field(default=None, primary_key=True)
    api_id: int = Field(foreign_key="api_definitions.id", description="API ID")
    param_name: str = Field(index=True, description="파라미터 이름")
    param_type: str = Field(default="string", description="파라미터 타입")
    
    # 검증 관련 필드
    is_required: bool = Field(default=False, description="필수 여부")
    default_value: Optional[str] = Field(default=None, description="기본값")
    min_length: Optional[int] = Field(default=None, description="최소 길이")
    max_length: Optional[int] = Field(default=None, description="최대 길이")
    allowed_values: Optional[str] = Field(default=None, description="허용값 (콤마 구분)")
    
    # 메타 필드
    description: Optional[str] = Field(default=None, description="파라미터 설명")
    created_at: datetime = Field(default_factory=datetime.now)
    
    # 관계 정의
    api: APIDefinition = Relationship(back_populates="parameters")


class UserInput(SQLModel, table=True):
    """
    사용자 입력 테이블 (JSON 형식)
    각 프로그램의 실제 파라미터 값을 JSON으로 저장
    
    ✨ 핵심: 1개 프로그램 = 1개 행 (중복 입력 제거)
    """
    
    __tablename__ = "user_inputs"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    program_name: str = Field(index=True, unique=True, description="프로그램 식별자")
    params_json: str = Field(description="파라미터 JSON 문자열")
    description: Optional[str] = Field(default=None, description="입력 설명")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    def get_params_dict(self) -> Dict[str, str]:
        """JSON 문자열 → 딕셔너리 변환"""
        try:
            return json.loads(self.params_json) if self.params_json else {}
        except json.JSONDecodeError:
            return {}
    
    def set_params_dict(self, params: Dict[str, Any]) -> None:
        """딕셔너리 → JSON 문자열 변환 및 저장"""
        self.params_json = json.dumps(params, ensure_ascii=False)


class ValidationResult(SQLModel):
    """
    검증 결과 모델 (테이블 아님, 반환용)
    """
    
    is_valid: bool
    errors: List[str] = []
    warnings: List[str] = []
    validated_params: dict = {}
```

**주요 포인트:**
- `UserInput.params_json`: 모든 파라미터를 하나의 JSON 문자열로 저장
- `get_params_dict()`, `set_params_dict()`: JSON ↔ Dict 변환 헬퍼 메서드
- `allowed_values`: 콤마로 구분된 문자열 (예: "J,K,M")

---

### 🔧 2단계: database.py - 데이터베이스 매니저

**목적:** CRUD 작업 + 검증 로직 구현

**핵심 기능:**
1. API 정의 관리 (add, get, list, delete)
2. 파라미터 정의 관리
3. 사용자 입력 관리 (JSON 형식)
4. 검증 엔진 (validate_user_inputs)
5. 데이터베이스 생성 및 초기 데이터 입력을 처리하는 py 는 생성하고 내부적으로 한번 실행

```python
"""
database.py - 데이터베이스 매니저 클래스
"""

import logging
from typing import Optional, List, Dict, Any
from datetime import datetime

from sqlmodel import Session, SQLModel, create_engine, select
from sqlalchemy.exc import IntegrityError

from models import (
    APIDefinition, 
    ParameterDefinition, 
    UserInput, 
    ValidationResult
)


class DatabaseManager:
    """데이터베이스 관리 클래스"""
    
    def __init__(self, db_path: str = "kis_api.db"):
        self.db_path = db_path
        self.engine = create_engine(f"sqlite:///{db_path}", echo=False)
        self.create_tables()
    
    def create_tables(self):
        """테이블 생성"""
        SQLModel.metadata.create_all(self.engine)
        logging.info(f"데이터베이스 초기화: {self.db_path}")
    
    def get_session(self) -> Session:
        """세션 생성"""
        return Session(self.engine)
    
    # ==================== API Definition 관리 ====================
    
    def add_api_definition(
        self,
        program_name: str,
        api_url: str,
        tr_id: str,
        tr_cont: str = "",
        description: Optional[str] = None
    ) -> Optional[APIDefinition]:
        """API 정의 추가"""
        with self.get_session() as session:
            try:
                api_def = APIDefinition(
                    program_name=program_name,
                    api_url=api_url,
                    tr_id=tr_id,
                    tr_cont=tr_cont,
                    description=description
                )
                session.add(api_def)
                session.commit()
                session.refresh(api_def)
                logging.info(f"✓ API 정의 추가: {program_name}")
                return api_def
            except IntegrityError:
                logging.error(f"✗ 이미 존재하는 프로그램: {program_name}")
                return None
    
    def get_api_definition(self, program_name: str) -> Optional[APIDefinition]:
        """API 정의 조회"""
        with self.get_session() as session:
            statement = select(APIDefinition).where(
                APIDefinition.program_name == program_name,
                APIDefinition.is_active == True
            )
            return session.exec(statement).first()
    
    def list_api_definitions(self) -> List[APIDefinition]:
        """모든 활성 API 목록"""
        with self.get_session() as session:
            statement = select(APIDefinition).where(APIDefinition.is_active == True)
            return list(session.exec(statement).all())
    
    # ==================== Parameter Definition 관리 ====================
    
    def add_parameter_definition(
        self,
        program_name: str,
        param_name: str,
        param_type: str = "string",
        is_required: bool = False,
        default_value: Optional[str] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        allowed_values: Optional[str] = None,
        description: Optional[str] = None
    ) -> Optional[ParameterDefinition]:
        """파라미터 정의 추가 (검증 룰 포함)"""
        api_def = self.get_api_definition(program_name)
        if not api_def:
            logging.error(f"✗ API 정의 없음: {program_name}")
            return None
        
        with self.get_session() as session:
            param_def = ParameterDefinition(
                api_id=api_def.id,
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
            logging.info(f"✓ 파라미터 정의: {program_name}.{param_name}")
            return param_def
    
    def get_parameter_definitions(self, program_name: str) -> List[ParameterDefinition]:
        """파라미터 정의 목록 조회"""
        api_def = self.get_api_definition(program_name)
        if not api_def:
            return []
        
        with self.get_session() as session:
            statement = select(ParameterDefinition).where(
                ParameterDefinition.api_id == api_def.id
            )
            return list(session.exec(statement).all())
    
    # ==================== User Input 관리 (JSON 형식) ====================
    
    def add_user_input(
        self,
        program_name: str,
        params: Dict[str, Any],
        description: Optional[str] = None
    ) -> UserInput:
        """
        사용자 입력 추가/업데이트 (JSON 형식)
        
        ✨ 핵심: params는 딕셔너리 {"KEY": "VALUE", ...}
        """
        with self.get_session() as session:
            # 기존 입력 확인
            statement = select(UserInput).where(
                UserInput.program_name == program_name
            )
            existing = session.exec(statement).first()
            
            if existing:
                # 업데이트
                existing.set_params_dict(params)
                existing.description = description
                existing.updated_at = datetime.now()
                session.add(existing)
                session.commit()
                session.refresh(existing)
                logging.info(f"✓ 사용자 입력 업데이트: {program_name} ({len(params)}개)")
                return existing
            else:
                # 새로 추가
                user_input = UserInput(
                    program_name=program_name,
                    params_json="",
                    description=description
                )
                user_input.set_params_dict(params)
                session.add(user_input)
                session.commit()
                session.refresh(user_input)
                logging.info(f"✓ 사용자 입력 추가: {program_name} ({len(params)}개)")
                return user_input
    
    def get_user_input(self, program_name: str) -> Optional[UserInput]:
        """사용자 입력 조회"""
        with self.get_session() as session:
            statement = select(UserInput).where(
                UserInput.program_name == program_name
            )
            return session.exec(statement).first()
    
    def list_user_inputs(self) -> List[UserInput]:
        """모든 사용자 입력 목록"""
        with self.get_session() as session:
            statement = select(UserInput)
            return list(session.exec(statement).all())
    
    def delete_user_input(self, program_name: str) -> bool:
        """사용자 입력 삭제"""
        with self.get_session() as session:
            statement = select(UserInput).where(
                UserInput.program_name == program_name
            )
            user_input = session.exec(statement).first()
            
            if user_input:
                session.delete(user_input)
                session.commit()
                logging.info(f"✓ 사용자 입력 삭제: {program_name}")
                return True
            return False
    
    # ==================== 검증 엔진 ====================
    
    def validate_user_inputs(self, program_name: str) -> ValidationResult:
        """
        사용자 입력 검증
        
        검증 항목:
        1. 필수 파라미터 누락 체크
        2. 허용값 체크
        3. 길이 체크 (min/max)
        4. 정의되지 않은 파라미터 경고
        """
        result = ValidationResult(
            is_valid=True, 
            errors=[], 
            warnings=[], 
            validated_params={}
        )
        
        # 1. API 정의 확인
        api_def = self.get_api_definition(program_name)
        if not api_def:
            result.is_valid = False
            result.errors.append(f"API 정의 없음: {program_name}")
            return result
        
        # 2. 파라미터 정의 조회
        param_defs = self.get_parameter_definitions(program_name)
        if not param_defs:
            result.warnings.append("파라미터 정의 없음 - 검증 생략")
            return result
        
        # 3. 사용자 입력 조회 (JSON → Dict)
        user_input = self.get_user_input(program_name)
        user_params = user_input.get_params_dict() if user_input else {}
        
        # 4. 각 파라미터 검증
        for param_def in param_defs:
            param_name = param_def.param_name
            param_value = user_params.get(param_name, param_def.default_value)
            
            # 4-1. 필수 파라미터 체크
            if param_def.is_required and not param_value:
                result.is_valid = False
                result.errors.append(f"필수 파라미터 누락: {param_name}")
                continue
            
            # 4-2. 값이 없으면 기본값 사용
            if not param_value:
                if param_def.default_value:
                    param_value = param_def.default_value
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
            
            # 검증 통과
            result.validated_params[param_name] = str(param_value)
        
        # 5. 정의되지 않은 파라미터 경고
        defined_params = {pd.param_name for pd in param_defs}
        for param_name in user_params.keys():
            if param_name not in defined_params:
                result.warnings.append(f"정의되지 않은 파라미터: {param_name}")
                result.validated_params[param_name] = str(user_params[param_name])
        
        return result
```

**주요 포인트:**
- `add_user_input()`: 딕셔너리를 받아서 JSON으로 저장
- `validate_user_inputs()`: 4단계 검증 수행
- JSON 형식이므로 program_name당 1번의 DB 작업

---

### 🔧 3단계: main_v3.py - 메인 실행 프로그램

**목적:** 완전 DB 중심 동작, 설정과 실행 분리

**핵심 명령:**
- `--list`: API 목록
- `--show-info`: API 상세 정보
- `--set-input`: 사용자 입력 설정
- `--program <name>`: API 실행

```python
"""
main_v3.py - 완전 DB 중심 KIS API 실행 프로그램
"""

import sys
import logging
import argparse
import json
from typing import Dict, Any, Optional

import pandas as pd

sys.path.extend(['../..', '.'])
import kis_auth as ka
from database import DatabaseManager

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class APIManager:
    """API 관리 및 실행 클래스"""
    
    def __init__(self, db_path: str = "kis_api.db"):
        self.db = DatabaseManager(db_path)
    
    def execute(self, program_name: str, skip_validation: bool = False) -> pd.DataFrame:
        """
        DB에 저장된 정보로 API 실행
        
        프로세스:
        1. DB에서 API 정의 조회
        2. DB에서 사용자 입력 조회 (JSON)
        3. 검증 (skip_validation=False인 경우)
        4. KIS API 호출
        """
        
        # 1. API 정의
        api_def = self.db.get_api_definition(program_name)
        if not api_def:
            raise ValueError(f"API 정의 없음: {program_name}")
        
        logging.info("="*80)
        logging.info(f"API 실행: {program_name}")
        logging.info("="*80)
        logging.info(f"URL: {api_def.api_url}")
        logging.info(f"TR_ID: {api_def.tr_id}")
        
        # 2. 사용자 입력
        user_input = self.db.get_user_input(program_name)
        if not user_input:
            raise ValueError(
                f"사용자 입력 없음: {program_name}\n"
                f"먼저 입력 설정: python main_v3.py --program {program_name} --set-input --params ..."
            )
        
        params = user_input.get_params_dict()
        logging.info(f"파라미터: {json.dumps(params, ensure_ascii=False)}")
        
        # 3. 검증
        if not skip_validation:
            validation = self.db.validate_user_inputs(program_name)
            
            if not validation.is_valid:
                logging.error("검증 실패:")
                for error in validation.errors:
                    logging.error(f"  ✗ {error}")
                raise ValueError("파라미터 검증 실패")
            
            if validation.warnings:
                for warning in validation.warnings:
                    logging.warning(f"  ⚠ {warning}")
            
            params = validation.validated_params
            logging.info("✓ 검증 통과")
        
        # 4. API 호출
        logging.info("API 호출 중...")
        try:
            res = ka._url_fetch(
                api_def.api_url,
                api_def.tr_id,
                api_def.tr_cont,
                params
            )
            
            if res.isOK():
                data = pd.DataFrame(res.getBody().output)
                logging.info(f"✓ 성공: {len(data)}건")
                return data
            else:
                logging.error("✗ API 호출 실패")
                res.printError(url=api_def.api_url)
                return pd.DataFrame()
        
        except Exception as e:
            logging.error(f"✗ 오류: {e}")
            raise
    
    def set_user_input(
        self,
        program_name: str,
        params: Dict[str, Any],
        description: Optional[str] = None
    ) -> None:
        """사용자 입력 설정"""
        
        # API 정의 확인
        api_def = self.db.get_api_definition(program_name)
        if not api_def:
            raise ValueError(f"API 정의 없음: {program_name}")
        
        # 저장
        self.db.add_user_input(program_name, params, description)
        logging.info(f"✓ 사용자 입력 저장: {program_name}")
        logging.info(f"  {json.dumps(params, ensure_ascii=False)}")
    
    def show_info(self, program_name: str) -> Dict[str, Any]:
        """API 전체 정보 조회"""
        
        api_def = self.db.get_api_definition(program_name)
        if not api_def:
            return {"error": f"API 정의 없음: {program_name}"}
        
        param_defs = self.db.get_parameter_definitions(program_name)
        user_input = self.db.get_user_input(program_name)
        validation = self.db.validate_user_inputs(program_name)
        
        return {
            "api": {
                "program_name": api_def.program_name,
                "api_url": api_def.api_url,
                "tr_id": api_def.tr_id,
                "tr_cont": api_def.tr_cont,
                "description": api_def.description
            },
            "parameters": [
                {
                    "name": p.param_name,
                    "type": p.param_type,
                    "required": p.is_required,
                    "default": p.default_value,
                    "allowed_values": p.allowed_values,
                    "min_length": p.min_length,
                    "max_length": p.max_length,
                    "description": p.description
                }
                for p in param_defs
            ],
            "user_input": {
                "params": user_input.get_params_dict() if user_input else {},
                "description": user_input.description if user_input else None,
                "updated_at": str(user_input.updated_at) if user_input else None
            },
            "validation": {
                "is_valid": validation.is_valid,
                "errors": validation.errors,
                "warnings": validation.warnings,
                "validated_params": validation.validated_params
            }
        }
    
    def list_apis(self) -> None:
        """API 목록 출력"""
        
        apis = self.db.list_api_definitions()
        
        if not apis:
            print("등록된 API가 없습니다.")
            return
        
        print(f"\n{'='*80}")
        print(f"등록된 API 목록 ({len(apis)}개)")
        print(f"{'='*80}\n")
        
        for i, api in enumerate(apis, 1):
            user_input = self.db.get_user_input(api.program_name)
            param_defs = self.db.get_parameter_definitions(api.program_name)
            
            print(f"[{i}] {api.program_name}")
            print(f"    URL: {api.api_url}")
            print(f"    TR_ID: {api.tr_id}")
            print(f"    설명: {api.description or '없음'}")
            print(f"    파라미터 정의: {len(param_defs)}개")
            
            if user_input:
                params = user_input.get_params_dict()
                print(f"    사용자 입력: {len(params)}개")
                print(f"      → {json.dumps(params, ensure_ascii=False)}")
            else:
                print(f"    사용자 입력: 없음")
            
            print()


def main():
    """메인 함수"""
    
    parser = argparse.ArgumentParser(
        description='DB 중심 KIS API 실행 프로그램 v3.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예제:

  # API 목록
  python main_v3.py --list

  # API 정보
  python main_v3.py --program stock_price --show-info

  # 사용자 입력 설정 (JSON)
  python main_v3.py --program stock_price --set-input \\
    --params '{"FID_COND_MRKT_DIV_CODE":"J","FID_INPUT_ISCD":"005930"}'

  # 사용자 입력 설정 (key=value)
  python main_v3.py --program stock_price --set-input \\
    --params FID_COND_MRKT_DIV_CODE=J FID_INPUT_ISCD=005930

  # API 실행
  python main_v3.py --program stock_price

  # 결과 저장
  python main_v3.py --program stock_price --output result.csv
        """
    )
    
    parser.add_argument('--db', default='kis_api.db', help='DB 파일')
    parser.add_argument('--program', help='프로그램명')
    parser.add_argument('--list', action='store_true', help='API 목록')
    parser.add_argument('--show-info', action='store_true', help='API 정보')
    parser.add_argument('--set-input', action='store_true', help='입력 설정')
    parser.add_argument('--params', nargs='*', help='파라미터')
    parser.add_argument('--description', help='입력 설명')
    parser.add_argument('--output', help='결과 CSV')
    parser.add_argument('--skip-validation', action='store_true', help='검증 생략')
    
    args = parser.parse_args()
    
    # pandas 설정
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_rows', 50)
    
    try:
        manager = APIManager(args.db)
        
        # 1. 목록
        if args.list:
            manager.list_apis()
            return
        
        # 2. program 필수 (list 제외)
        if not args.program:
            parser.error("--program 필요 (--list 제외)")
        
        # 3. 정보
        if args.show_info:
            info = manager.show_info(args.program)
            print("\n" + "="*80)
            print(f"API 정보: {args.program}")
            print("="*80)
            print(json.dumps(info, indent=2, ensure_ascii=False))
            print("="*80)
            return
        
        # 4. 입력 설정
        if args.set_input:
            if not args.params:
                parser.error("--set-input 시 --params 필요")
            
            # 파라미터 파싱
            params_dict = {}
            
            if len(args.params) == 1 and args.params[0].startswith('{'):
                # JSON 문자열
                params_dict = json.loads(args.params[0])
            else:
                # key=value 형식
                for param in args.params:
                    if '=' not in param:
                        raise ValueError(f"잘못된 형식: {param} (key=value 필요)")
                    key, value = param.split('=', 1)
                    params_dict[key] = value
            
            manager.set_user_input(args.program, params_dict, args.description)
            
            # 검증 결과 표시
            validation = manager.db.validate_user_inputs(args.program)
            print(f"\n검증: {'✓ 통과' if validation.is_valid else '✗ 실패'}")
            for error in validation.errors:
                print(f"  ✗ {error}")
            for warning in validation.warnings:
                print(f"  ⚠ {warning}")
            
            return
        
        # 5. 실행
        ka.auth()
        result = manager.execute(args.program, args.skip_validation)
        
        if not result.empty:
            print(f"\n{'='*80}")
            print(f"결과 ({len(result)}건)")
            print(f"{'='*80}\n")
            print(result)
            
            if args.output:
                result.to_csv(args.output, index=False, encoding='utf-8-sig')
                logging.info(f"\n✓ 저장: {args.output}")
        else:
            logging.warning("데이터 없음")
    
    except Exception as e:
        logging.error(f"오류: {e}")
        raise


if __name__ == "__main__":
    main()
```

**주요 포인트:**
- 설정(`--set-input`)과 실행을 완전히 분리
- JSON 또는 key=value 형식 모두 지원
- DB에서만 모든 정보 조회 (파일 불필요)

---

### 🔧 4단계: init_database.py - 초기화 스크립트

**목적:** 샘플 데이터로 DB 초기화

```python
"""
init_database.py - 데이터베이스 초기화 및 샘플 데이터
"""

import logging
from database import DatabaseManager

logging.basicConfig(level=logging.INFO)


def init_sample_data():
    """샘플 데이터 초기화"""
    
    db = DatabaseManager("kis_api.db")
    
    print("="*80)
    print("데이터베이스 초기화")
    print("="*80)
    
    # 1. display_board_option_list
    print("\n[1] display_board_option_list")
    db.add_api_definition(
        program_name="display_board_option_list",
        api_url="/uapi/domestic-futureoption/v1/quotations/display-board-option-list",
        tr_id="FHPIO056104C0",
        description="국내옵션전광판_옵션월물리스트"
    )
    
    db.add_parameter_definition(
        program_name="display_board_option_list",
        param_name="FID_COND_SCR_DIV_CODE",
        is_required=True,
        default_value="509",
        allowed_values="509,510,511",
        description="조건 화면 분류 코드"
    )
    
    db.add_parameter_definition(
        program_name="display_board_option_list",
        param_name="FID_COND_MRKT_DIV_CODE",
        is_required=False,
        max_length=10,
        description="조건 시장 분류 코드"
    )
    
    db.add_parameter_definition(
        program_name="display_board_option_list",
        param_name="FID_COND_MRKT_CLS_CODE",
        is_required=False,
        max_length=10,
        description="조건 시장 구분 코드"
    )
    
    # 사용자 입력 (JSON 형식)
    db.add_user_input(
        program_name="display_board_option_list",
        params={
            "FID_COND_SCR_DIV_CODE": "509",
            "FID_COND_MRKT_DIV_CODE": "",
            "FID_COND_MRKT_CLS_CODE": ""
        },
        description="옵션 월물 조회"
    )
    
    # 2. stock_price
    print("\n[2] stock_price")
    db.add_api_definition(
        program_name="stock_price",
        api_url="/uapi/domestic-stock/v1/quotations/inquire-price",
        tr_id="FHKST01010100",
        description="주식 현재가 시세"
    )
    
    db.add_parameter_definition(
        program_name="stock_price",
        param_name="FID_COND_MRKT_DIV_CODE",
        is_required=True,
        allowed_values="J,K",
        description="시장 분류 (J:주식, K:ETF)"
    )
    
    db.add_parameter_definition(
        program_name="stock_price",
        param_name="FID_INPUT_ISCD",
        is_required=True,
        min_length=6,
        max_length=6,
        description="종목 코드 (6자리)"
    )
    
    db.add_user_input(
        program_name="stock_price",
        params={
            "FID_COND_MRKT_DIV_CODE": "J",
            "FID_INPUT_ISCD": "005930"
        },
        description="삼성전자"
    )
    
    # 3. daily_price
    print("\n[3] daily_price")
    db.add_api_definition(
        program_name="daily_price",
        api_url="/uapi/domestic-stock/v1/quotations/inquire-daily-price",
        tr_id="FHKST01010400",
        description="주식 일별 시세"
    )
    
    db.add_parameter_definition(
        program_name="daily_price",
        param_name="FID_COND_MRKT_DIV_CODE",
        is_required=True,
        allowed_values="J,K",
        description="시장 분류"
    )
    
    db.add_parameter_definition(
        program_name="daily_price",
        param_name="FID_INPUT_ISCD",
        is_required=True,
        min_length=6,
        max_length=6,
        description="종목 코드"
    )
    
    db.add_parameter_definition(
        program_name="daily_price",
        param_name="FID_PERIOD_DIV_CODE",
        is_required=False,
        default_value="D",
        allowed_values="D,W,M",
        description="기간 (D:일, W:주, M:월)"
    )
    
    db.add_parameter_definition(
        program_name="daily_price",
        param_name="FID_ORG_ADJ_PRC",
        is_required=False,
        default_value="0",
        allowed_values="0,1",
        description="수정주가 (0:미수정, 1:수정)"
    )
    
    db.add_user_input(
        program_name="daily_price",
        params={
            "FID_COND_MRKT_DIV_CODE": "J",
            "FID_INPUT_ISCD": "000660",
            "FID_PERIOD_DIV_CODE": "D",
            "FID_ORG_ADJ_PRC": "0"
        },
        description="SK하이닉스 일봉"
    )
    
    print("\n" + "="*80)
    print("✓ 초기화 완료")
    print("="*80)


if __name__ == "__main__":
    init_sample_data()
```

---

### 🔧 5단계: csv_importer.py - CSV 변환 도구

**목적:** CSV ↔ DB 대량 임포트/익스포트

```python
"""
csv_importer.py - CSV와 DB 간 변환
"""

import logging
import argparse
import pandas as pd
from database import DatabaseManager

logging.basicConfig(level=logging.INFO)


def import_from_csv(csv_file: str, db_path: str = "kis_api.db") -> None:
    """CSV → DB 임포트"""
    
    db = DatabaseManager(db_path)
    
    print("="*80)
    print(f"CSV 임포트: {csv_file}")
    print("="*80)
    
    df = pd.read_csv(csv_file)
    
    api_count = 0
    param_count = 0
    
    for program_name, group in df.groupby('program_name'):
        first_row = group.iloc[0]
        
        # API 정의
        api_def = db.add_api_definition(
            program_name=program_name,
            api_url=first_row['api_url'],
            tr_id=first_row['tr_id'],
            tr_cont=first_row.get('tr_cont', '') if pd.notna(first_row.get('tr_cont')) else '',
            description=first_row.get('api_description') if pd.notna(first_row.get('api_description')) else None
        )
        
        if api_def:
            api_count += 1
            print(f"\n[{api_count}] {program_name}")
            
            # 파라미터 정의
            for _, row in group.iterrows():
                param_name = row['param_name']
                param_value = row.get('param_value', '')
                param_required = row.get('param_required', 'N')
                allowed_values = row.get('allowed_values')
                min_length = row.get('min_length')
                max_length = row.get('max_length')
                
                # NaN 처리
                if pd.isna(param_value):
                    param_value = ''
                if pd.isna(allowed_values):
                    allowed_values = None
                if pd.isna(min_length):
                    min_length = None
                else:
                    min_length = int(min_length)
                if pd.isna(max_length):
                    max_length = None
                else:
                    max_length = int(max_length)
                
                is_required = str(param_required).upper() == 'Y'
                
                param_def = db.add_parameter_definition(
                    program_name=program_name,
                    param_name=param_name,
                    is_required=is_required,
                    default_value=param_value if param_value else None,
                    allowed_values=allowed_values,
                    min_length=min_length,
                    max_length=max_length,
                    description=row.get('param_description')
                )
                
                if param_def:
                    param_count += 1
                    print(f"  - {param_name}")
    
    print(f"\n{'='*80}")
    print(f"✓ 임포트 완료: API {api_count}개, 파라미터 {param_count}개")
    print(f"{'='*80}")


def export_to_csv(db_path: str = "kis_api.db", output_file: str = "export.csv") -> None:
    """DB → CSV 익스포트"""
    
    db = DatabaseManager(db_path)
    
    print("="*80)
    print(f"CSV 익스포트: {output_file}")
    print("="*80)
    
    rows = []
    
    for api in db.list_api_definitions():
        params = db.get_parameter_definitions(api.program_name)
        
        for param in params:
            rows.append({
                'program_name': api.program_name,
                'api_url': api.api_url,
                'tr_id': api.tr_id,
                'tr_cont': api.tr_cont,
                'api_description': api.description,
                'param_name': param.param_name,
                'param_value': param.default_value or '',
                'param_required': 'Y' if param.is_required else 'N',
                'allowed_values': param.allowed_values or '',
                'min_length': param.min_length if param.min_length else '',
                'max_length': param.max_length if param.max_length else '',
                'param_description': param.description or ''
            })
    
    if rows:
        df = pd.DataFrame(rows)
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"✓ 익스포트 완료: {len(rows)}개 행")
    else:
        print("! 데이터 없음")
    
    print("="*80)


def main():
    parser = argparse.ArgumentParser(description='CSV ↔ DB 변환')
    
    parser.add_argument('action', choices=['import', 'export'])
    parser.add_argument('--file', required=True)
    parser.add_argument('--db', default='kis_api.db')
    
    args = parser.parse_args()
    
    if args.action == 'import':
        import_from_csv(args.file, args.db)
    else:
        export_to_csv(args.db, args.file)


if __name__ == "__main__":
    main()
```

**CSV 형식:**
```csv
program_name,api_url,tr_id,tr_cont,api_description,param_name,param_value,param_required,allowed_values,min_length,max_length,param_description
stock_price,/url,TR001,,주식시세,FID_COND_MRKT_DIV_CODE,J,Y,"J,K",,,시장분류
stock_price,/url,TR001,,주식시세,FID_INPUT_ISCD,,Y,,6,6,종목코드
```

---

## 완전한 코드 예제

### 전체 시스템 구축 (한 번에)

```bash
# 1. 프로젝트 폴더 생성
mkdir kis_api_system
cd kis_api_system

# 2. 필수 파일 생성
touch models.py database.py main_v3.py init_database.py csv_importer.py
touch requirements.txt

# 3. 패키지 설치
pip install sqlmodel pandas requests pyyaml pycryptodome

# 4. 코드 작성
# (위의 코드를 각 파일에 복사)

# 5. DB 초기화
python init_database.py

# 6. 확인
python main_v3.py --list
```

---

## 사용 방법

### 초기 설정

```bash
# 1. DB 초기화 (샘플 데이터)
python init_database.py

# 2. API 목록 확인
python main_v3.py --list

# 3. API 상세 정보
python main_v3.py --program stock_price --show-info
```

### 사용자 입력 설정

```bash
# 방법 1: JSON 형식 (추천)
python main_v3.py --program stock_price --set-input \
  --params '{"FID_COND_MRKT_DIV_CODE":"J","FID_INPUT_ISCD":"005930"}' \
  --description "삼성전자"

# 방법 2: key=value 형식
python main_v3.py --program stock_price --set-input \
  --params FID_COND_MRKT_DIV_CODE=J FID_INPUT_ISCD=005930 \
  --description "삼성전자"
```

### API 실행

```bash
# 기본 실행
python main_v3.py --program stock_price

# 결과 저장
python main_v3.py --program stock_price --output samsung.csv

# 검증 생략
python main_v3.py --program stock_price --skip-validation
```

### 배치 처리

```bash
#!/bin/bash
# batch.sh

# 여러 종목 처리
for code in 005930 000660 035720; do
    python main_v3.py --program stock_price --set-input \
      --params FID_INPUT_ISCD=$code
    
    python main_v3.py --program stock_price --output ${code}.csv
done
```

### CSV 임포트/익스포트

```bash
# CSV → DB
python csv_importer.py import --file api_config.csv

# DB → CSV (백업)
python csv_importer.py export --file backup.csv
```

---

## 검증 로직 상세

### 검증 순서

```
1. API 정의 존재 확인
   └─ 없으면 에러

2. 파라미터 정의 조회
   └─ 없으면 경고 후 검증 생략

3. 사용자 입력 조회 (JSON → Dict)

4. 각 파라미터별 검증
   ├─ 필수 체크 (is_required=True)
   ├─ 길이 체크 (min_length, max_length)
   └─ 허용값 체크 (allowed_values)

5. 정의되지 않은 파라미터 경고

6. 검증 결과 반환 (ValidationResult)
```

### 검증 규칙 예제

```python
# 예제 1: 필수 + 허용값
ParameterDefinition(
    param_name="FID_COND_MRKT_DIV_CODE",
    is_required=True,
    allowed_values="J,K"
)
# → 값이 없거나 J, K가 아니면 에러

# 예제 2: 필수 + 길이
ParameterDefinition(
    param_name="FID_INPUT_ISCD",
    is_required=True,
    min_length=6,
    max_length=6
)
# → 값이 없거나 6자리가 아니면 에러

# 예제 3: 선택 + 기본값
ParameterDefinition(
    param_name="FID_PERIOD_DIV_CODE",
    is_required=False,
    default_value="D",
    allowed_values="D,W,M"
)
# → 값이 없으면 "D" 사용, 있으면 D/W/M 체크
```

---

## 트러블슈팅

### 문제 1: "API 정의를 찾을 수 없습니다"

**원인:** DB에 API 미등록

**해결:**
```bash
# 초기화
python init_database.py

# 또는 CSV 임포트
python csv_importer.py import --file api_config.csv

# 확인
python main_v3.py --list
```

### 문제 2: "사용자 입력을 찾을 수 없습니다"

**원인:** 사용자 입력 미설정

**해결:**
```bash
python main_v3.py --program stock_price --set-input \
  --params FID_COND_MRKT_DIV_CODE=J FID_INPUT_ISCD=005930
```

### 문제 3: "필수 파라미터 누락: XXX"

**원인:** 필수 파라미터 값 없음

**해결:**
```bash
# 상세 정보 확인
python main_v3.py --program stock_price --show-info

# 필수 파라미터 포함하여 재설정
python main_v3.py --program stock_price --set-input \
  --params '{"FID_COND_MRKT_DIV_CODE":"J","FID_INPUT_ISCD":"005930"}'
```

### 문제 4: "허용되지 않은 값"

**원인:** allowed_values 위반

**해결:**
```bash
# 허용값 확인
python main_v3.py --program stock_price --show-info

# 허용값으로 수정 (예: J 또는 K만 가능)
python main_v3.py --program stock_price --set-input \
  --params FID_COND_MRKT_DIV_CODE=J FID_INPUT_ISCD=005930
```

### 문제 5: "최소/최대 길이 위반"

**원인:** min_length, max_length 위반

**해결:**
```bash
# 종목코드는 정확히 6자리
python main_v3.py --program stock_price --set-input \
  --params FID_INPUT_ISCD=005930  # OK
  # --params FID_INPUT_ISCD=5930  # 에러 (4자리)
```

---

## 확장 및 커스터마이징

### 1. 새로운 API 추가

```python
from database import DatabaseManager

db = DatabaseManager()

# API 정의
db.add_api_definition(
    program_name="my_new_api",
    api_url="/uapi/my/endpoint",
    tr_id="MYTR001",
    description="내 API"
)

# 파라미터 정의
db.add_parameter_definition(
    program_name="my_new_api",
    param_name="MY_PARAM",
    is_required=True,
    allowed_values="A,B,C",
    description="내 파라미터"
)

# 사용자 입력
db.add_user_input(
    program_name="my_new_api",
    params={"MY_PARAM": "A"}
)
```

### 2. 웹 인터페이스 추가

```python
# FastAPI 예제
from fastapi import FastAPI
from main_v3 import APIManager

app = FastAPI()
manager = APIManager()

@app.get("/apis")
def list_apis():
    return {"apis": [api.program_name for api in manager.db.list_api_definitions()]}

@app.post("/execute/{program_name}")
def execute(program_name: str):
    result = manager.execute(program_name)
    return result.to_dict()
```

### 3. 스케줄러 통합

```python
# APScheduler 예제
from apscheduler.schedulers.background import BackgroundScheduler
from main_v3 import APIManager
import kis_auth as ka

ka.auth()
manager = APIManager()
scheduler = BackgroundScheduler()

@scheduler.scheduled_job('cron', hour=9, minute=0)
def daily_stock_check():
    result = manager.execute("stock_price")
    # 결과 처리...
    
scheduler.start()
```

### 4. 알림 기능

```python
def execute_with_notification(program_name: str):
    try:
        result = manager.execute(program_name)
        send_success_email(program_name, result)
    except ValueError as e:
        send_error_email(program_name, str(e))
```

### 5. 커스텀 검증 룰

```python
# database.py의 validate_user_inputs()에 추가

# 예: 날짜 형식 검증
if param_def.param_name == "DATE_FIELD":
    try:
        datetime.strptime(param_value, "%Y%m%d")
    except ValueError:
        result.is_valid = False
        result.errors.append(f"{param_name}: 잘못된 날짜 형식 (YYYYMMDD 필요)")
```

---

## 체크리스트

### 구현 체크리스트
- [ ] models.py 작성 (3개 테이블 + ValidationResult)
- [ ] database.py 작성 (DatabaseManager)
- [ ] main_v3.py 작성 (APIManager + argparse)
- [ ] init_database.py 작성 (샘플 데이터)
- [ ] csv_importer.py 작성 (선택)
- [ ] requirements.txt 작성
- [ ] kis_auth.py 준비 (기존)

### 테스트 체크리스트
- [ ] `python init_database.py` 실행
- [ ] `python main_v3.py --list` 확인
- [ ] `python main_v3.py --program stock_price --show-info` 확인
- [ ] `python main_v3.py --program stock_price --set-input --params ...` 테스트
- [ ] `python main_v3.py --program stock_price` 실행 테스트
- [ ] 검증 실패 시나리오 테스트
  - [ ] 필수 파라미터 누락
  - [ ] 허용값 위반
  - [ ] 길이 위반
- [ ] CSV 임포트/익스포트 테스트
- [ ] 배치 처리 테스트

### 운영 체크리스트
- [ ] DB 백업 전략 수립
- [ ] 로그 수집 및 모니터링
- [ ] API Rate Limit 고려
- [ ] 에러 알림 설정
- [ ] 문서화 완료

---

## 마무리

### 이 스킬로 얻는 것

1. **완전한 재현 가능성**
   - 이 문서만으로 전체 시스템 구축 가능
   - 각 단계별 완전한 코드 제공

2. **실용적인 검증 시스템**
   - 필수값, 허용값, 길이 자동 검증
   - API 호출 전 에러 조기 발견

3. **효율적인 관리**
   - JSON 형식으로 중복 입력 제거
   - DB 중심으로 중앙 집중 관리

4. **확장 가능한 구조**
   - 웹 인터페이스 쉽게 추가
   - 스케줄러, 알림 등 통합 용이

### 다음 단계

1. 이 문서를 처음부터 끝까지 따라하기
2. 자신의 API 추가해보기
3. 검증 룰 커스터마이징
4. 웹 인터페이스나 스케줄러 연동
5. 운영 환경 배포

---

**버전:** 3.0 (최종)  
**작성일:** 2025-02-10  
**라이센스:** MIT  

**주의사항:**
- KIS API 이용약관 준수
- API 키는 절대 하드코딩 금지
- 운영 환경에서는 반드시 DB 백업
- Rate limit 고려하여 적절한 간격으로 호출


## 목표
- SQLite + SQLModel 기반 API 메타데이터 관리
- 파라미터 사전 정의 및 자동 검증
- JSON 형식의 사용자 입력 관리
- 완전 DB 중심 동작 방식

## 시스템 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│                     KIS API 시스템                           │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐         ┌──────────────┐                  │
│  │ API          │ 1    ∞  │ Parameter    │                  │
│  │ Definition   ├─────────┤ Definition   │                  │
│  │              │         │              │                  │
│  │ - program    │         │ - param_name │                  │
│  │ - api_url    │         │ - required   │                  │
│  │ - tr_id      │         │ - allowed    │                  │
│  └──────────────┘         │ - min/max    │                  │
│         │                 └──────────────┘                  │
│         │                                                    │
│         │ 1                                                  │
│         │                                                    │
│         │ ∞                                                  │
│  ┌──────────────┐                                           │
│  │ User Input   │                                           │
│  │              │                                           │
│  │ - program    │                                           │
│  │ - params_json│  {"KEY":"VALUE",...}                     │
│  └──────────────┘                                           │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────┐                                           │
│  │ Validation   │                                           │
│  │ Engine       │                                           │
│  └──────────────┘                                           │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────┐                                           │
│  │ KIS API Call │                                           │
│  └──────────────┘                                           │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## 단계별 구현 가이드

### 1단계: 데이터 모델 정의 (models.py)

```python
"""
SQLModel 기반 데이터베이스 모델 정의
"""

import json
from typing import Optional, List, Dict, Any
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship


class APIDefinition(SQLModel, table=True):
    """API 정의 테이블"""
    
    __tablename__ = "api_definitions"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    program_name: str = Field(index=True, unique=True)
    api_url: str
    tr_id: str
    tr_cont: str = Field(default="")
    description: Optional[str] = Field(default=None)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    # Relationship
    parameters: List["ParameterDefinition"] = Relationship(back_populates="api")


class ParameterDefinition(SQLModel, table=True):
    """파라미터 정의 테이블 - 검증 룰"""
    
    __tablename__ = "parameter_definitions"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_id: int = Field(foreign_key="api_definitions.id")
    param_name: str = Field(index=True)
    param_type: str = Field(default="string")
    is_required: bool = Field(default=False)
    default_value: Optional[str] = Field(default=None)
    min_length: Optional[int] = Field(default=None)
    max_length: Optional[int] = Field(default=None)
    allowed_values: Optional[str] = Field(default=None)  # 콤마 구분
    description: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    
    # Relationship
    api: APIDefinition = Relationship(back_populates="parameters")


class UserInput(SQLModel, table=True):
    """사용자 입력 테이블 - JSON 형식"""
    
    __tablename__ = "user_inputs"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    program_name: str = Field(index=True, unique=True)
    params_json: str = Field(description="파라미터 JSON")
    description: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    def get_params_dict(self) -> Dict[str, str]:
        """JSON 문자열을 딕셔너리로 변환"""
        try:
            return json.loads(self.params_json) if self.params_json else {}
        except json.JSONDecodeError:
            return {}
    
    def set_params_dict(self, params: Dict[str, Any]) -> None:
        """딕셔너리를 JSON 문자열로 변환"""
        self.params_json = json.dumps(params, ensure_ascii=False)


class ValidationResult(SQLModel):
    """검증 결과 모델 (반환용)"""
    
    is_valid: bool
    errors: List[str] = []
    warnings: List[str] = []
    validated_params: dict = {}
```

**핵심 포인트:**
- APIDefinition: 1개 API당 1개 행
- ParameterDefinition: 1개 파라미터당 1개 행 (검증 룰 포함)
- UserInput: 1개 프로그램당 1개 행 (JSON 형식으로 모든 파라미터 저장)

### 2단계: 데이터베이스 매니저 (database.py)

```python
"""
데이터베이스 CRUD 및 검증 로직
"""

from sqlmodel import Session, SQLModel, create_engine, select
from models import APIDefinition, ParameterDefinition, UserInput, ValidationResult


class DatabaseManager:
    
    def __init__(self, db_path: str = "kis_api.db"):
        self.db_path = db_path
        self.engine = create_engine(f"sqlite:///{db_path}", echo=False)
        self.create_tables()
    
    def create_tables(self):
        """테이블 생성"""
        SQLModel.metadata.create_all(self.engine)
    
    # ==================== API Definition 관리 ====================
    
    def add_api_definition(self, program_name, api_url, tr_id, ...):
        """API 정의 추가"""
        # 구현...
    
    def get_api_definition(self, program_name):
        """API 정의 조회"""
        # 구현...
    
    # ==================== Parameter Definition 관리 ====================
    
    def add_parameter_definition(self, program_name, param_name, ...):
        """파라미터 정의 추가 (검증 룰 포함)"""
        # is_required, allowed_values, min_length, max_length 등
        # 구현...
    
    def get_parameter_definitions(self, program_name):
        """파라미터 정의 조회"""
        # 구현...
    
    # ==================== User Input 관리 ====================
    
    def add_user_input(self, program_name, params: Dict, description=None):
        """사용자 입력 추가/업데이트 (JSON 형식)"""
        # params = {"KEY1": "VALUE1", "KEY2": "VALUE2"}
        # 구현...
    
    def get_user_input(self, program_name):
        """사용자 입력 조회"""
        # 구현...
    
    # ==================== 검증 ====================
    
    def validate_user_inputs(self, program_name) -> ValidationResult:
        """사용자 입력 검증"""
        result = ValidationResult(is_valid=True, errors=[], warnings=[])
        
        # 1. API 정의 확인
        # 2. 파라미터 정의 조회
        # 3. 사용자 입력 조회
        # 4. 각 파라미터별 검증
        #    - 필수 파라미터 체크
        #    - 허용값 체크 (allowed_values)
        #    - 길이 체크 (min_length, max_length)
        # 5. 검증 결과 반환
        
        return result
```

**핵심 포인트:**
- UserInput은 JSON 형식으로 저장/조회
- validate_user_inputs()가 모든 검증 수행
- 필수 체크, 허용값 체크, 길이 체크 구현

### 3단계: 메인 프로그램 (main_v3.py)

```python
"""
완전 DB 중심 동작 방식
"""

import kis_auth as ka
from database import DatabaseManager


class APIManager:
    
    def __init__(self, db_path="kis_api.db"):
        self.db = DatabaseManager(db_path)
    
    def execute(self, program_name, skip_validation=False):
        """API 실행"""
        
        # 1. DB에서 API 정의 조회
        api_def = self.db.get_api_definition(program_name)
        
        # 2. DB에서 사용자 입력 조회
        user_input = self.db.get_user_input(program_name)
        params = user_input.get_params_dict()
        
        # 3. 검증
        if not skip_validation:
            validation = self.db.validate_user_inputs(program_name)
            if not validation.is_valid:
                raise ValueError("검증 실패")
            params = validation.validated_params
        
        # 4. API 호출
        res = ka._url_fetch(api_def.api_url, api_def.tr_id, 
                           api_def.tr_cont, params)
        
        return pd.DataFrame(res.getBody().output)
    
    def set_user_input(self, program_name, params, description=None):
        """사용자 입력 설정"""
        self.db.add_user_input(program_name, params, description)
    
    def show_info(self, program_name):
        """API 정보 조회"""
        # API 정의, 파라미터 정의, 사용자 입력, 검증 결과 반환
        # 구현...
    
    def list_apis(self):
        """API 목록 출력"""
        # 구현...


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--program', help='프로그램명')
    parser.add_argument('--list', action='store_true', help='API 목록')
    parser.add_argument('--show-info', action='store_true', help='API 정보')
    parser.add_argument('--set-input', action='store_true', help='입력 설정')
    parser.add_argument('--params', nargs='*', help='파라미터')
    parser.add_argument('--output', help='결과 저장')
    parser.add_argument('--skip-validation', action='store_true')
    
    args = parser.parse_args()
    manager = APIManager()
    
    if args.list:
        manager.list_apis()
    elif args.show_info:
        print(json.dumps(manager.show_info(args.program), indent=2))
    elif args.set_input:
        # 파라미터 파싱 (JSON 또는 key=value)
        params = parse_params(args.params)
        manager.set_user_input(args.program, params)
    else:
        # API 실행
        ka.auth()
        result = manager.execute(args.program, args.skip_validation)
        print(result)
        if args.output:
            result.to_csv(args.output, index=False)
```

**핵심 포인트:**
- 설정(--set-input)과 실행을 분리
- DB에서만 모든 정보 조회
- CSV, JSON 파일 불필요

### 4단계: 데이터베이스 초기화 (init_database.py)

```python
"""
샘플 데이터 초기화
"""

from database import DatabaseManager


def init_sample_data():
    db = DatabaseManager("kis_api.db")
    
    # 1. API 정의 추가
    db.add_api_definition(
        program_name="stock_price",
        api_url="/uapi/domestic-stock/v1/quotations/inquire-price",
        tr_id="FHKST01010100",
        description="주식 현재가 시세 조회"
    )
    
    # 2. 파라미터 정의 추가 (검증 룰 포함)
    db.add_parameter_definition(
        program_name="stock_price",
        param_name="FID_COND_MRKT_DIV_CODE",
        param_type="string",
        is_required=True,
        allowed_values="J,K",  # J 또는 K만 허용
        description="시장 분류 코드"
    )
    
    db.add_parameter_definition(
        program_name="stock_price",
        param_name="FID_INPUT_ISCD",
        param_type="string",
        is_required=True,
        min_length=6,
        max_length=6,  # 정확히 6자리
        description="종목 코드"
    )
    
    # 3. 사용자 입력 추가 (JSON 형식)
    db.add_user_input(
        program_name="stock_price",
        params={
            "FID_COND_MRKT_DIV_CODE": "J",
            "FID_INPUT_ISCD": "005930"
        },
        description="삼성전자 현재가 조회"
    )
```

**핵심 포인트:**
- 각 API에 대해 정의 + 파라미터 정의 + 샘플 입력 추가
- 검증 룰(allowed_values, min/max_length) 명시
- JSON 형식으로 사용자 입력 저장

### 5단계: CSV 임포트 도구 (csv_importer.py)

CSV에서 DB로 대량 임포트하는 도구:

```python
"""
CSV → DB 변환
"""

def import_from_csv(csv_file, db_path="kis_api.db"):
    db = DatabaseManager(db_path)
    df = pd.read_csv(csv_file)
    
    for program_name, group in df.groupby('program_name'):
        # API 정의 추가
        first_row = group.iloc[0]
        db.add_api_definition(
            program_name=program_name,
            api_url=first_row['api_url'],
            tr_id=first_row['tr_id'],
            # ...
        )
        
        # 파라미터 정의 추가
        for _, row in group.iterrows():
            db.add_parameter_definition(
                program_name=program_name,
                param_name=row['param_name'],
                is_required=(row['param_required'] == 'Y'),
                allowed_values=row.get('allowed_values'),
                min_length=row.get('min_length'),
                max_length=row.get('max_length'),
                # ...
            )
```

**CSV 형식:**
```csv
program_name,api_url,tr_id,param_name,param_required,allowed_values,min_length,max_length
stock_price,/url,TR001,FID_COND_MRKT_DIV_CODE,Y,"J,K",,
stock_price,/url,TR001,FID_INPUT_ISCD,Y,,6,6
```

## 사용 워크플로우

### 초기 설정
```bash
# 1. 패키지 설치
pip install sqlmodel pandas requests pyyaml pycryptodome

# 2. DB 초기화
python init_database.py

# 또는 CSV에서 임포트
python csv_importer.py import --file api_config.csv
```

### 일상 사용
```bash
# 1. API 목록 확인
python main_v3.py --list

# 2. API 정보 확인
python main_v3.py --program stock_price --show-info

# 3. 사용자 입력 설정
python main_v3.py --program stock_price --set-input \
  --params '{"FID_COND_MRKT_DIV_CODE":"J","FID_INPUT_ISCD":"005930"}'

# 4. 실행
python main_v3.py --program stock_price --output result.csv
```

## 핵심 설계 결정

### 1. UserInput을 JSON 형식으로 저장한 이유
**문제:** 
```sql
-- 기존: 파라미터마다 별도 행
program_name | param_name | param_value
stock_price  | PARAM1     | value1
stock_price  | PARAM2     | value2
stock_price  | PARAM3     | value3
```
→ program_name을 3번 반복 입력

**해결:**
```sql
-- 신규: JSON으로 한 행에 저장
program_name | params_json
stock_price  | {"PARAM1":"value1","PARAM2":"value2","PARAM3":"value3"}
```
→ program_name 1번만 입력

### 2. 설정과 실행을 분리한 이유
**장점:**
- 사용자 입력을 DB에 저장 → 재사용 가능
- 같은 설정으로 여러 번 실행 가능
- 설정 변경 이력 관리 가능

### 3. 검증 룰을 DB에 저장한 이유
**장점:**
- API 호출 전에 에러 조기 발견
- 중앙 집중식 검증 규칙 관리
- 검증 로직 재사용

## 검증 규칙 예제

```python
# 필수 파라미터
is_required = True
→ 값이 없으면 에러

# 허용값 제한
allowed_values = "J,K"
→ J 또는 K가 아니면 에러

# 길이 제한
min_length = 6
max_length = 6
→ 정확히 6자리가 아니면 에러

# 조합 예제
ParameterDefinition(
    param_name="FID_INPUT_ISCD",
    is_required=True,      # 필수
    min_length=6,           # 최소 6자리
    max_length=6,           # 최대 6자리
    description="종목코드"
)
```

## 파일 구조

```
project/
├── models.py              # SQLModel 데이터 모델
├── database.py            # DatabaseManager 클래스
├── main_v3.py             # 메인 실행 프로그램
├── init_database.py       # 초기화 스크립트
├── csv_importer.py        # CSV 임포트 도구
├── requirements.txt       # 패키지 목록
├── kis_api.db            # SQLite 데이터베이스 (자동 생성)
└── README.md             # 사용 설명서
```

## 의존성 패키지

```txt
# requirements.txt
sqlmodel>=0.0.14
sqlalchemy>=2.0.0
pandas>=2.0.0
requests>=2.31.0
PyYAML>=6.0
pycryptodome>=3.19.0
```

## 버전 히스토리

### v1.0 - CSV 기반
- CSV 파일로 API 정의
- 파라미터 검증 없음
- 명령줄/JSON 파일로 파라미터 입력

### v2.0 - DB 도입
- SQLite + SQLModel
- 파라미터 검증 기능 추가
- UserInput 개별 행 저장

### v3.0 - JSON 형식 (현재)
- UserInput JSON 형식으로 변경
- 완전 DB 중심 동작
- 설정/실행 분리

## 확장 가능성

### 1. 웹 인터페이스
```python
# FastAPI 예제
from fastapi import FastAPI
from database import DatabaseManager

app = FastAPI()
db = DatabaseManager()

@app.get("/apis")
def list_apis():
    return db.list_api_definitions()

@app.post("/execute/{program_name}")
def execute_api(program_name: str):
    # 구현...
```

### 2. 스케줄러 통합
```python
# APScheduler 예제
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

@scheduler.scheduled_job('cron', hour=9, minute=0)
def daily_stock_check():
    manager = APIManager()
    result = manager.execute("stock_price")
    # 결과 처리...
```

### 3. 알림 기능
```python
# 검증 실패 시 이메일 알림
def execute_with_notification(program_name):
    try:
        validation = db.validate_user_inputs(program_name)
        if not validation.is_valid:
            send_email(f"검증 실패: {validation.errors}")
    except Exception as e:
        send_email(f"실행 오류: {e}")
```

## 트러블슈팅

### 문제 1: "API 정의를 찾을 수 없습니다"
**원인:** DB에 API가 등록되지 않음
**해결:** 
```bash
python init_database.py
# 또는
python csv_importer.py import --file api_config.csv
```

### 문제 2: "파라미터 검증 실패"
**원인:** 사용자 입력이 검증 룰 위반
**해결:**
```bash
# 상세 정보 확인
python main_v3.py --program stock_price --show-info

# 허용값, 길이 확인 후 올바른 값으로 재설정
python main_v3.py --program stock_price --set-input \
  --params FID_INPUT_ISCD=005930  # 6자리 종목코드
```

### 문제 3: "사용자 입력을 찾을 수 없습니다"
**원인:** 사용자 입력이 DB에 없음
**해결:**
```bash
python main_v3.py --program stock_price --set-input \
  --params '{"FID_COND_MRKT_DIV_CODE":"J","FID_INPUT_ISCD":"005930"}'
```

## 모범 사례

### 1. API 정의 추가 시
```python
# 항상 설명(description) 포함
db.add_api_definition(
    program_name="my_api",
    api_url="/url",
    tr_id="TRID",
    description="API가 무엇을 하는지 명확하게 설명"  # 중요!
)
```

### 2. 파라미터 정의 시
```python
# 가능한 모든 검증 룰 명시
db.add_parameter_definition(
    program_name="my_api",
    param_name="MY_PARAM",
    is_required=True,           # 필수 여부
    allowed_values="A,B,C",     # 허용값
    min_length=6,                # 최소 길이
    max_length=6,                # 최대 길이
    description="파라미터 설명"  # 설명
)
```

### 3. 에러 처리
```python
# 항상 try-except 사용
try:
    result = manager.execute("stock_price")
except ValueError as e:
    logging.error(f"검증 실패: {e}")
except Exception as e:
    logging.error(f"실행 오류: {e}")
```

## 성능 최적화

### 1. 인덱스 추가
```python
# models.py에서
program_name: str = Field(index=True, unique=True)
param_name: str = Field(index=True)
```

### 2. 배치 처리
```python
# 여러 종목 처리 시
symbols = ["005930", "000660", "035720"]
for symbol in symbols:
    manager.set_user_input("stock_price", 
                          {"FID_INPUT_ISCD": symbol})
    result = manager.execute("stock_price")
    # 처리...
```

### 3. 캐싱
```python
# API 정의는 자주 변경되지 않으므로 캐싱 가능
from functools import lru_cache

@lru_cache(maxsize=100)
def get_api_definition_cached(program_name):
    return db.get_api_definition(program_name)
```

## 마무리 체크리스트

- [ ] models.py 작성 (3개 테이블 + ValidationResult)
- [ ] database.py 작성 (DatabaseManager 클래스)
- [ ] main_v3.py 작성 (APIManager + argparse)
- [ ] init_database.py 작성 (샘플 데이터)
- [ ] csv_importer.py 작성 (선택사항)
- [ ] requirements.txt 작성
- [ ] 초기화 테스트 (`python init_database.py`)
- [ ] 목록 확인 (`python main_v3.py --list`)
- [ ] 사용자 입력 설정 테스트
- [ ] API 실행 테스트
- [ ] 검증 실패 시나리오 테스트
- [ ] 문서화 (README, 가이드)

## 참고 자료

- SQLModel 공식 문서: https://sqlmodel.tiangolo.com/
- SQLAlchemy 문서: https://docs.sqlalchemy.org/
- Python argparse: https://docs.python.org/3/library/argparse.html
- JSON 처리: https://docs.python.org/3/library/json.html

## 라이센스 및 주의사항

- 한국투자증권 KIS API 사용 시 API 이용약관 준수 필요
- API 키는 절대 코드에 하드코딩하지 말 것
- 운영 환경에서는 DB 백업 필수
- Rate limit 고려하여 API 호출 간격 조절

---

이 스킬 문서를 따라하면 동일한 시스템을 재구축할 수 있습니다.
