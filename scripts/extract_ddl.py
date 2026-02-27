"""
extract_ddl.py - 데이터베이스에 접속하여 현재 사용자의 테이블 DDL 추출 (최적화 버전)
"""

import os
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import get_engine_kwargs
from scripts.log_setup import setup_logging
from sqlmodel import create_engine, text

setup_logging()

def extract_ddl():
    print("데이터베이스에 연결하여 DDL 추출을 시작합니다...")
    
    kwargs = get_engine_kwargs()
    url = kwargs.pop("url")
    engine = create_engine(url, **kwargs)
    
    out_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "script_gof.sql")
    
    try:
        with engine.begin() as conn:
            # DBMS_METADATA 형식 설정
            conn.execute(text("BEGIN DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM, 'SQLTERMINATOR', true); END;"))
            conn.execute(text("BEGIN DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM, 'PRETTY', true); END;"))
            conn.execute(text("BEGIN DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM, 'SEGMENT_ATTRIBUTES', false); END;"))
            conn.execute(text("BEGIN DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM, 'STORAGE', false); END;"))
            # 스키마 이름 ("GOF" 등) 제거
            conn.execute(text("BEGIN DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM, 'EMIT_SCHEMA', false); END;"))
            
            print("데이터베이스 객체 분석 및 DDL 다운로드 중 이 작업은 1~2분 정도 소요될 수 있습니다...")
            
            with open(out_file, 'w', encoding='utf-8') as f:
                # 1. 모든 테이블 DDL을 단일 쿼리로 가져오기 (네트워크 지연 최소화)
                table_query = """
                SELECT DBMS_METADATA.GET_DDL('TABLE', TABLE_NAME) 
                FROM USER_TABLES 
                ORDER BY TABLE_NAME
                """
                
                table_results = conn.execute(text(table_query))
                table_count = 0
                for row in table_results:
                    ddl = row[0]
                    if ddl:
                        ddl_str = ddl.read() if hasattr(ddl, 'read') else str(ddl)
                        f.write(ddl_str)
                        f.write("\n")
                    table_count += 1
                
                print(f"✓ {table_count}개 테이블 DDL 추출 완료")
                
                # 2. 테이블 코멘트 가져오기
                tab_comment_query = """
                SELECT TABLE_NAME, COMMENTS FROM USER_TAB_COMMENTS WHERE COMMENTS IS NOT NULL ORDER BY TABLE_NAME
                """
                tab_comment_results = conn.execute(text(tab_comment_query))
                tab_comment_count = 0
                for row in tab_comment_results:
                    f.write(f"COMMENT ON TABLE \"{row[0]}\" IS '{row[1]}';\n")
                    tab_comment_count += 1
                
                f.write("\n")
                
                # 3. 컬럼 코멘트 가져오기
                col_comment_query = """
                SELECT TABLE_NAME, COLUMN_NAME, COMMENTS FROM USER_COL_COMMENTS WHERE COMMENTS IS NOT NULL ORDER BY TABLE_NAME, COLUMN_NAME
                """
                col_comment_results = conn.execute(text(col_comment_query))
                col_comment_count = 0
                for row in col_comment_results:
                    f.write(f"COMMENT ON COLUMN \"{row[0]}\".\"{row[1]}\" IS '{row[2]}';\n")
                    col_comment_count += 1
                
                f.write("\n")
                print(f"✓ {tab_comment_count}개 테이블 코멘트, {col_comment_count}개 컬럼 코멘트 추출 완료")

                # 4. 모든 인덱스 DDL을 단일 쿼리로 가져오기 (PK 관련 인덱스 및 LOB 인덱스 제외)
                index_query = """
                SELECT DBMS_METADATA.GET_DDL('INDEX', INDEX_NAME)
                FROM USER_INDEXES 
                WHERE INDEX_TYPE NOT LIKE '%LOB%'
                  AND INDEX_NAME NOT IN (
                      SELECT CONSTRAINT_NAME 
                      FROM USER_CONSTRAINTS 
                      WHERE CONSTRAINT_TYPE = 'P'
                  )
                ORDER BY TABLE_NAME, INDEX_NAME
                """
                
                try:
                    index_results = conn.execute(text(index_query))
                    index_count = 0
                    for row in index_results:
                        ddl = row[0]
                        if ddl:
                            ddl_str = ddl.read() if hasattr(ddl, 'read') else str(ddl)
                            f.write(ddl_str)
                            f.write("\n")
                        index_count += 1
                    print(f"✓ {index_count}개 인덱스 DDL 추출 완료")
                except Exception as e:
                    print(f"인덱스 추출 중 일부 오류 발생 (무시 가능): {e}")
                    
        print("=" * 80)
        print(f"성공적으로 전체 DDL을 {out_file}에 저장했습니다.")
        print("=" * 80)
        
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    extract_ddl()
