"""
init_database.py - 데이터베이스 초기화 및 테이블 생성
"""

import os
import logging
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import DB_TYPE, DB_PATH, get_engine_kwargs
from scripts.log_setup import setup_logging

setup_logging()

from sqlmodel import SQLModel, create_engine

def init_database():
    """데이터베이스 테이블 초기화"""
    
    if DB_TYPE == "sqlite":
        # SQLite: 기존 DB 파일 삭제 후 재생성
        if os.path.exists(DB_PATH):
            try:
                os.remove(DB_PATH)
                print(f"기존 DB 삭제: {DB_PATH}")
            except Exception as e:
                print(f"DB 삭제 실패: {e}")
    else:
        print(f"DB Type: {DB_TYPE} (Oracle Cloud ADB)")
    
    # Create engine using centralized config
    kwargs = get_engine_kwargs()
    url = kwargs.pop("url")
    engine = create_engine(url, **kwargs)
    
    # Import all models to register them with SQLModel metadata
    import app.models  # noqa: F401
    
    # 테이블 생성
    print("테이블 생성 중...")
    SQLModel.metadata.create_all(engine)

    print("=" * 80)
    print("✓ 테이블 생성 완료")
    print("=" * 80)
    print("※ 데이터를 적재하려면 'scripts/insert_sample_data.py' 또는 'scripts/load_api_data.py'를 실행하세요.")


if __name__ == "__main__":
    init_database()
