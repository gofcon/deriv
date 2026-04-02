"""
Auto-generated SQLModel classes from Oracle DDL.
"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, JSON, DateTime, func, Integer, Identity

try:
    from . import oracle_mapping  # noqa: F401
except ImportError:
    import oracle_mapping  # noqa: F401


class ValidationResult(SQLModel):
    """
    검증 결과 모델 (테이블 아님, 반환용)
    """

    is_valid: bool
    errors: List[str] = []
    warnings: List[str] = []
    validated_params: dict = {}



class ApiMst(SQLModel, table=True):
    __tablename__ = "api_mst"

    api_id: str = Field(primary_key=True)
    api_name: str = Field(max_length=100)
    api_type: str = Field(max_length=100)
    api_url: str = Field(max_length=100)
    header_json: dict = Field(sa_column=Column(JSON))
    request_type: str = Field(max_length=20)
    description: Optional[str] = Field(default=None, max_length=100)
    output_table_name: Optional[str] = Field(default=None, max_length=100)
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )

    api_params: list["ApiParam"] = Relationship(back_populates="api_mst")
    api_job_msts: list["ApiJobMst"] = Relationship(back_populates="api_mst")


class ApiParam(SQLModel, table=True):
    __tablename__ = "api_param"

    api_id: str = Field(foreign_key="api_mst.api_id", primary_key=True)
    param_name: str = Field(primary_key=True, max_length=100)
    is_required: bool = Field(default=False)
    default_value: Optional[str] = Field(default=None, max_length=20)
    min_length: Optional[int] = Field(default=None)
    max_length: Optional[int] = Field(default=None)
    allowed_values: Optional[str] = Field(default=None, max_length=50)
    description: Optional[str] = Field(default=None, max_length=100)
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )

    api_mst: Optional["ApiMst"] = Relationship(back_populates="api_params")


class ApiScheduleMst(SQLModel, table=True):
    __tablename__ = "api_schedule_mst"

    schedule_id: str = Field(primary_key=True, max_length=50)
    api_id: str = Field(foreign_key="api_mst.api_id")
    macro_params_json: dict = Field(sa_column=Column(JSON))
    is_active: bool = Field(default=False)
    save_mode: Optional[str] = Field(default="overwrite", max_length=20)
    execution_cycle: Optional[str] = Field(default="daily", max_length=20)
    description: Optional[str] = Field(default=None, max_length=100)
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )

    api_mst: Optional["ApiMst"] = Relationship()
    api_job_msts: list["ApiJobMst"] = Relationship(back_populates="schedule_mst")


class ApiJobMst(SQLModel, table=True):
    __tablename__ = "api_job_mst"

    job_id: str = Field(primary_key=True, max_length=150)
    schedule_id: Optional[str] = Field(foreign_key="api_schedule_mst.schedule_id", default=None)
    base_yymm: Optional[str] = Field(default=None, max_length=6)
    api_id: str = Field(foreign_key="api_mst.api_id")
    params_json: dict = Field(sa_column=Column(JSON))
    status: str = Field(default="PENDING", max_length=20)
    error_message: Optional[str] = Field(default=None, max_length=4000)
    is_active: bool = Field(default=True)
    save_mode: Optional[str] = Field(default="overwrite", max_length=20)
    execution_cycle: Optional[str] = Field(default="daily", max_length=20)
    description: Optional[str] = Field(default=None, max_length=100)
    executed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime))
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )

    api_mst: Optional["ApiMst"] = Relationship(back_populates="api_job_msts")
    schedule_mst: Optional["ApiScheduleMst"] = Relationship(back_populates="api_job_msts")


class BrowserMst(SQLModel, table=True):
    __tablename__ = "browser_mst"

    browser_id: str = Field(primary_key=True, max_length=50)
    browser_name: str = Field(max_length=100)
    target_url: str = Field(max_length=500)
    output_table_name: Optional[str] = Field(default=None, max_length=100)
    
    selector_json: dict = Field(default_factory=dict, sa_column=Column(JSON))
    behavior_json: list = Field(default_factory=list, sa_column=Column(JSON))
    pagination_json: dict = Field(default_factory=dict, sa_column=Column(JSON))
    human_like: bool = Field(default=False)
    
    description: Optional[str] = Field(default=None, max_length=200)
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )

    browser_job_msts: list["BrowserJobMst"] = Relationship(back_populates="browser_mst")


class BrowserScheduleMst(SQLModel, table=True):
    __tablename__ = "browser_schedule_mst"

    schedule_id: str = Field(primary_key=True, max_length=100)
    browser_id: str = Field(foreign_key="browser_mst.browser_id")
    macro_params_json: dict = Field(default_factory=dict, sa_column=Column(JSON))
    is_active: bool = Field(default=False)
    save_mode: Optional[str] = Field(default="append", max_length=20)
    execution_cycle: Optional[str] = Field(default="daily", max_length=20)
    description: Optional[str] = Field(default=None, max_length=200)
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )

    browser_mst: Optional["BrowserMst"] = Relationship()
    browser_job_msts: list["BrowserJobMst"] = Relationship(back_populates="schedule_mst")


class BrowserJobMst(SQLModel, table=True):
    __tablename__ = "browser_job_mst"

    job_id: str = Field(primary_key=True, max_length=150)
    schedule_id: Optional[str] = Field(foreign_key="browser_schedule_mst.schedule_id", default=None)
    base_yymm: Optional[str] = Field(default=None, max_length=6)
    browser_id: str = Field(foreign_key="browser_mst.browser_id")
    params_json: dict = Field(default_factory=dict, sa_column=Column(JSON))
    status: str = Field(default="PENDING", max_length=20)
    error_message: Optional[str] = Field(default=None, max_length=4000)
    is_active: bool = Field(default=True)
    save_mode: Optional[str] = Field(default="append", max_length=20)
    execution_cycle: Optional[str] = Field(default="daily", max_length=20)
    description: Optional[str] = Field(default=None, max_length=200)
    executed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime))
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )

    browser_mst: Optional["BrowserMst"] = Relationship(back_populates="browser_job_msts")
    schedule_mst: Optional["BrowserScheduleMst"] = Relationship(back_populates="browser_job_msts")


class BrowserRst(SQLModel, table=True):
    """Generalized Output Table for Browser Scraping"""
    __tablename__ = "browser_rst"
    
    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))
    browser_id: str = Field(index=True, max_length=50)
    job_id: str = Field(index=True, max_length=100)
    
    result_json: dict = Field(default_factory=dict, sa_column=Column(JSON))
    
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )


class ApiRst(SQLModel, table=True):
    """Generalized Output Table for API Data"""
    __tablename__ = "api_rst"
    
    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))
    api_id: str = Field(index=True, max_length=150)
    job_id: str = Field(index=True, max_length=150)
    
    result_json: dict = Field(default_factory=dict, sa_column=Column(JSON))
    
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )


# ===== KIS API 관련 테이블은 models_kis.py 로 분리 =====
# 하위 호환성을 위해 re-export
try:
    from .models_kis import (  # noqa: F401
        KrxIsinMst,
        StockPrice, DailyPrice, DisplayBoardTop,
        DomFutureMst, OverFutureMst, DomStockFutureMst, OverStockMst,
        DomBondMst, DomCmeFutureMst, DomComFutureMst, DomElwMst,
        DomEurexOptionMst, DomKonexMst, DomKosdaqMst, DomKospiMst,
        MemberCodeMst, OverIndexMst, SectorMst, ThemeMst,
        MetaTableMst, MetaColumnMst
    )
    from .models_seibro import SeibroBondKacdList, SeibroBondIsinList # noqa: F401
except ImportError:
    from models_kis import (  # noqa: F401
        KrxIsinMst,
        StockPrice, DailyPrice, DisplayBoardTop,
        DomFutureMst, OverFutureMst, DomStockFutureMst, OverStockMst,
        DomBondMst, DomCmeFutureMst, DomComFutureMst, DomElwMst,
        DomEurexOptionMst, DomKonexMst, DomKosdaqMst, DomKospiMst,
        MemberCodeMst, OverIndexMst, SectorMst, ThemeMst,
        MetaTableMst, MetaColumnMst
    )
    from models_seibro import SeibroBondKacdList, SeibroBondIsinList # noqa: F401
