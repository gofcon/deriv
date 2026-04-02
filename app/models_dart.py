from typing import Optional
from datetime import datetime, timezone, timedelta
from sqlmodel import Field, SQLModel

class DartCorpCode(SQLModel, table=True):
    """OpenDART 회사 고유번호 모델"""
    __tablename__ = "dart_corp_code"
    
    api_id: str = Field(primary_key=True, index=True, description="API 식별자")
    corp_code: str = Field(primary_key=True, index=True, description="고유번호 (8자리)")
    corp_name: str = Field(index=True, description="종목명(법인명)")
    corp_eng_name: Optional[str] = Field(default=None, description="영문법인명")
    stock_code: Optional[str] = Field(default=None, index=True, description="종목코드 (상장사 6자리)")
    modify_date: str = Field(description="최종변경일자")
    
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone(timedelta(hours=9))).replace(tzinfo=None),
        description="데이터 갱신 시각 (KST)"
    )

class DartCompany(SQLModel, table=True):
    """OpenDART 기업개황 모델"""
    __tablename__ = "dart_company"
    
    api_id: str = Field(primary_key=True, index=True, description="API 식별자")
    corp_code: str = Field(primary_key=True, index=True, description="고유번호 (8자리)")
    corp_name: str = Field(index=True, description="정식명칭")
    corp_name_eng: Optional[str] = Field(default=None, description="영문명칭")
    stock_name: Optional[str] = Field(default=None, description="종목명 또는 약식명칭")
    stock_code: Optional[str] = Field(default=None, index=True, description="주식 종목코드 (6자리)")
    ceo_nm: Optional[str] = Field(default=None, description="대표자명")
    corp_cls: Optional[str] = Field(default=None, description="법인구분 (Y:유가, K:코스닥, N:코넥스, E:기타)")
    jurir_no: Optional[str] = Field(default=None, description="법인등록번호")
    bizr_no: Optional[str] = Field(default=None, description="사업자등록번호")
    adres: Optional[str] = Field(default=None, description="주소")
    hm_url: Optional[str] = Field(default=None, description="홈페이지")
    ir_url: Optional[str] = Field(default=None, description="IR홈페이지")
    phn_no: Optional[str] = Field(default=None, description="전화번호")
    fax_no: Optional[str] = Field(default=None, description="팩스번호")
    induty_code: Optional[str] = Field(default=None, description="업종코드")
    est_dt: Optional[str] = Field(default=None, description="설립일 (YYYYMMDD)")
    acc_mt: Optional[str] = Field(default=None, description="결산월 (MM)")
    
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone(timedelta(hours=9))).replace(tzinfo=None),
        description="데이터 갱신 시각 (KST)"
    )
