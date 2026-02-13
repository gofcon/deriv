"""
init_database.py - 데이터베이스 초기화 및 샘플 데이터
"""

import os
import logging
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import DatabaseManager
from app.config import DB_PATH
from logs.log_setup import setup_logging

setup_logging()


from sqlmodel import SQLModel

def init_sample_data():
    """샘플 데이터 초기화"""
    
    # Absolute path to DB
    db_path = DB_PATH
    
    # 기존 DB 삭제 (스키마 변경 적용을 위해)
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
            print(f"기존 DB 삭제: {db_path}")
        except Exception as e:
            print(f"DB 삭제 실패: {e}")
    
    db = DatabaseManager(db_path)
    
    # 테이블 생성
    print("테이블 생성 중...")
    SQLModel.metadata.create_all(db.engine)

    
    print("="*80)
    print("✓ 테이블 생성 완료")
    print("="*80)
    print("※ 데이터를 적재하려면 'scripts/insert_sample_data.py' 또는 'scripts/load_api_data.py'를 실행하세요.")


if __name__ == "__main__":
    init_sample_data()
