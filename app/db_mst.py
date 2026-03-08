from sqlmodel import SQLModel, create_engine, Session, select, delete
from sqlalchemy import text
import logging
import os
from contextlib import contextmanager
from typing import Optional, List, Type

# Import only master models
from .models import (
    DomFutureMst,
    OverFutureMst,
    DomStockFutureMst,
    OverStockMst,
    DomBondMst,
    DomCmeFutureMst,
    DomComFutureMst,
    DomElwMst,
    DomEurexOptionMst,
    DomKonexMst,
    DomKosdaqMst,
    DomKospiMst,
    MemberCodeMst,
    OverIndexMst,
    SectorMst,
    ThemeMst,
    MetaTableMst,  # New
    MetaColumnMst  # New
)
from .config import DB_PATH, get_engine_kwargs

class MasterDatabaseManager:
    """마스터 데이터 전용 데이터베이스 매니저"""
    
    def __init__(self, db_path: str = None):
        if db_path is not None:
            # Explicit SQLite path override
            self.engine = create_engine(f"sqlite:///{db_path}")
        else:
            # Use centralized config
            kwargs = get_engine_kwargs()
            url = kwargs.pop("url")
            self.engine = create_engine(url, **kwargs)
        
    @contextmanager
    def get_session(self):
        """세션 컨텍스트 매니저"""
        session = Session(self.engine)
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def init_master_tables(self):
        """마스터 데이터 테이블 생성"""
        # Create tables for all imported models
        # Note: This might create all tables if they share the same metadata, 
        # but SQLModel usually shares metadata. 
        # It's safer to create all, or just let init_database do it.
        # But if we want to ensure tables exist:
        SQLModel.metadata.create_all(self.engine)
        logging.info("Master data tables initialized")

    def delete_all_data(self, model_class: Type[SQLModel]):
        """테이블의 모든 데이터 삭제"""
        with self.get_session() as session:
            # Method 1: using delete() statement (SQLAlchemy 1.4/2.0 standard)
            statement = delete(model_class)
            result = session.exec(statement)
            # session.commit() is handled by context manager
            logging.info(f"Deleted all data from {model_class.__tablename__} ({result.rowcount} rows)")

    def insert_data(self, model_class: Type[SQLModel], data_list: List[dict], batch_size: int = 1000):
        """데이터 일괄 삽입 (기존 데이터 삭제 포함)"""
        if not data_list:
            logging.warning(f"No data to insert for {model_class.__tablename__}")
            return

        # 1. 기존 데이터 삭제
        self.delete_all_data(model_class)
        
        # 2. 신규 데이터 삽입
        try:
            with self.get_session() as session:
                total = len(data_list)
                for i in range(0, total, batch_size):
                    batch_data = data_list[i:i+batch_size]
                    
                    # Convert all non-None values to string to avoid DPY-3013 with Oracle
                    processed_batch = []
                    for row in batch_data:
                        processed_row = {k: (str(v) if v is not None else None) for k, v in row.items()}
                        processed_batch.append(processed_row)
                        
                    # 모델 인스턴스 생성을 통해 default_factory 실행 보장
                    instances = [model_class(**row) for row in processed_batch]
                    session.add_all(instances)
                    session.commit()
                    logging.info(f"Inserted {min(i+batch_size, total)}/{total} rows into {model_class.__tablename__}")
        except Exception as e:
            logging.error(f"Error inserting data into {model_class.__tablename__}: {e}")
            raise e

    def update_metadata_tables(self):
        """SQLModel 정의에서 메타데이터 추출하여 테이블에 저장"""
        logging.info("Updating metadata tables...")
        
        # 모델 리스트 (Meta 테이블 제외)
        models = [
            DomFutureMst, OverFutureMst, DomStockFutureMst, OverStockMst,
            DomBondMst, DomCmeFutureMst, DomComFutureMst, DomElwMst,
            DomEurexOptionMst, DomKonexMst, DomKosdaqMst, DomKospiMst,
            MemberCodeMst, OverIndexMst, SectorMst, ThemeMst
        ]
        
        try:
            with self.get_session() as session:
                # 기존 메타데이터 삭제 (선택적)
                session.exec(delete(MetaTableMst))
                session.exec(delete(MetaColumnMst))
                
                for model in models:
                    # 1. 테이블 정보 저장
                    table_name = model.__tablename__
                    table_doc = model.__doc__ if model.__doc__ else None
                    
                    # 첫 줄만 사용
                    if table_doc:
                        table_doc = table_doc.strip().split('\n')[0]
                        
                    session.add(MetaTableMst(table_name=table_name, description=table_doc))
                    
                    # 2. 컬럼 정보 저장
                    for field_name, field_info in model.model_fields.items():
                        # FieldInfo 객체에서 description 접근
                        col_desc = field_info.description
                        if col_desc:
                             session.add(MetaColumnMst(
                                 table_name=table_name,
                                 column_name=field_name,
                                 description=col_desc
                             ))
                
                session.commit()
                logging.info("Metadata tables updated successfully.")
                
        except Exception as e:
            logging.error(f"Failed to update metadata: {e}")
            raise e
