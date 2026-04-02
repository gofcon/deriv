import sqlite3
import os
import sys

# 현재 디렉토리를 path에 추가하여 app 모듈을 불러올 수 있게 함
sys.path.append(os.getcwd())

from app.database import DatabaseManager
from app.models_dart import DartCompany
from sqlmodel import SQLModel, create_engine

def recreate_table():
    db_path = 'data/kis_api.db'
    if not os.path.exists(db_path):
        print(f"DB file not found: {db_path}")
        return

    # 1. 기존 테이블 Drop (직접 SQL 실행)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE IF EXISTS dart_company")
        cur.execute("DROP TABLE IF EXISTS dart_corp_code")
        print("✓ Tables 'dart_company' and 'dart_corp_code' dropped.")
    except Exception as e:
        print(f"✗ Error dropping table: {e}")
    finally:
        conn.commit()
        conn.close()

    # 2. SQLModel을 통해 테이블 재생성
    # DatabaseManager 인스턴스를 통해 엔진 획득
    db_manager = DatabaseManager()
    
    # DartCompany 모델이 포함된 metadata를 사용하여 테이블 생성
    try:
        # SQLModel.metadata.create_all()은 이미 존재하는 테이블은 건너뜁니다.
        # 위에서 Drop했으므로 DartCompany 테이블이 새로 생성됩니다.
        SQLModel.metadata.create_all(db_manager.engine)
        print("✓ Table 'dart_company' recreated with new schema.")
    except Exception as e:
        print(f"✗ Error creating table: {e}")

if __name__ == "__main__":
    recreate_table()
