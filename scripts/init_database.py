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

def init_database(drop_tables=False):
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
    # import app.models  # noqa: F401
    import app.models_gof as target_models  # noqa: F401
    
    if drop_tables:
        print("기존 테이블 삭제 중...")
        SQLModel.metadata.drop_all(engine)
        
    # 테이블 생성
    print("테이블 생성 중...")
    SQLModel.metadata.create_all(engine)

    if DB_TYPE == "oracle":
        # Oracle 코멘트 추가 (Table/Column)
        import inspect
        from sqlalchemy import text
        print("Oracle 테이블/컬럼 코멘트 추가 중...")
        with engine.begin() as conn:
            for name, obj in inspect.getmembers(target_models):
                if inspect.isclass(obj) and issubclass(obj, SQLModel) and obj != SQLModel:
                    table_name = getattr(obj, "__tablename__", None)
                    if not table_name:
                        continue
                    
                    # 1. 테이블 코멘트
                    if obj.__doc__:
                        t_comment = obj.__doc__.strip().replace("'", "''")
                        if t_comment:
                            try:
                                conn.execute(text(f"COMMENT ON TABLE {table_name} IS '{t_comment}'"))
                            except Exception as e:
                                pass
                    
                    # 2. 컬럼 코멘트
                    fields = getattr(obj, "model_fields", getattr(obj, "__fields__", {}))
                    for fname, finfo in fields.items():
                        # Pydantic v1 vs v2 compatibility
                        desc = getattr(finfo, "description", None)
                        if not desc and getattr(finfo, "field_info", None):
                            desc = getattr(finfo.field_info, "description", None)
                            
                        if desc:
                            c_comment = desc.replace("'", "''")
                            try:
                                conn.execute(text(f"COMMENT ON COLUMN {table_name}.{fname} IS '{c_comment}'"))
                            except Exception as e:
                                pass


    print("=" * 80)
    print("✓ 테이블 생성 완료")
    print("=" * 80)
    print("※ 데이터를 적재하려면 'scripts/insert_sample_data.py' 또는 'scripts/load_api_data.py'를 실행하세요.")


if __name__ == "__main__":
    drop_tables = "--drop" in sys.argv
    init_database(drop_tables=drop_tables)
