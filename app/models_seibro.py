"""
models_seibro.py - Seibro (세이브로) API 관련 SQLModel 클래스 정의
"""

from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime, func, Integer, Identity

try:
    from . import oracle_mapping  # noqa: F401
except ImportError:
    import oracle_mapping  # noqa: F401


class SeibroBondKacdList(SQLModel, table=True):
    """Output table for KACD List (seibro_bond_KACD_list)"""
    __tablename__ = "seibro_bond_kacd_list"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))
    api_id: str = Field(index=True, max_length=150)
    api_name: str = Field(index=True, max_length=150)

    # Note: Using standard bond fields. Extra fields from api can be mapped here.
    isin: Optional[str] = Field(default=None, max_length=100)
    kacd_cd: Optional[str] = Field(default=None, max_length=100)
    bond_kor_nm: Optional[str] = Field(default=None, max_length=200)
    bond_isin_nm: Optional[str] = Field(default=None, max_length=200)
    issue_dt: Optional[str] = Field(default=None, max_length=100)
    record_json: Optional[str] = Field(default=None, description="Fallback raw JSON representation")

    updated_at: Optional[datetime] = Field(default=None,
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()))


class SeibroBondIsinList(SQLModel, table=True):
    """Output table for ISIN List extracted from api_rst (seibro_bond_isin_list)"""
    __tablename__ = "seibro_bond_isin_list"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))
    job_id: str = Field(index=True, max_length=150)
    
    isin: Optional[str] = Field(default=None, max_length=100)
    bond_kor_nm: Optional[str] = Field(default=None, max_length=200)
    issue_dt: Optional[str] = Field(default=None, max_length=100)

    updated_at: Optional[datetime] = Field(default=None,
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()))
