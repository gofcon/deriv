"""
Auto-generated SQLModel classes from Oracle DDL.
"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, JSON, DateTime, func

import app.oracle_mapping  # noqa: F401

class ApiMst(SQLModel, table=True):
    __tablename__ = "api_mst"

    tr_id: str = Field(primary_key=True)
    api_name: str
    api_url: str = Field(max_length=100)
    tr_cont: str
    request_type: str
    description: Optional[str] = Field(default=None, max_length=100)
    output_table_name: Optional[str] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )

    api_params: list["ApiParam"] = Relationship(back_populates="api_mst")
    job_msts: list["JobMst"] = Relationship(back_populates="api_mst")


class ApiParam(SQLModel, table=True):
    __tablename__ = "api_param"

    tr_id: str = Field(foreign_key="api_mst.tr_id", primary_key=True)
    param_name: str = Field(primary_key=True)
    is_required: bool = Field(default=False)
    default_value: Optional[str] = Field(default=None)
    min_length: Optional[int] = Field(default=None)
    max_length: Optional[int] = Field(default=None)
    allowed_values: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None, max_length=100)
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )

    api_mst: Optional["ApiMst"] = Relationship(back_populates="api_params")


class JobMst(SQLModel, table=True):
    __tablename__ = "job_mst"

    job_id: str = Field(primary_key=True)
    tr_id: str = Field(foreign_key="api_mst.tr_id")
    params_json: dict = Field(sa_column=Column(JSON))
    is_active: bool = Field(default=False)
    save_mode: Optional[str] = Field(default="overwrite")
    execution_cycle: Optional[str] = Field(default="daily")
    description: Optional[str] = Field(default=None, max_length=100)
    updated_at: Optional[datetime] = Field(default=None,  
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()) )

    api_mst: Optional["ApiMst"] = Relationship(back_populates="job_msts")


