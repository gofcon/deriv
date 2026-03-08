"""
drop_all_tables.py - 데이터베이스 테이블 전체 삭제
"""

import os
import sys
import logging

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.config import DB_TYPE, get_engine_kwargs
from scripts.log_setup import setup_logging

setup_logging()

from sqlmodel import SQLModel, create_engine

def drop_database_tables():
    """데이터베이스 테이블 삭제"""
    
    print(f"DB Type: {DB_TYPE}")
    print("Connecting to database to drop tables...")
    
    # Create engine using centralized config
    kwargs = get_engine_kwargs()
    url = kwargs.pop("url")
    engine = create_engine(url, **kwargs)
    
    # Import all models to register them with SQLModel metadata
    import app.models  # noqa: F401
    
    # 테이블 삭제
    try:
        print("테이블 삭제 중...")
        SQLModel.metadata.drop_all(engine)
        print("=" * 80)
        print("✓ 테이블 삭제 완료")
        print("=" * 80)
    except Exception as e:
        print(f"테이블 삭제 실패: {e}")


if __name__ == "__main__":
    drop_database_tables()
