"""
execute_sql_script.py - SQL 스크립트 파일을 읽어 데이터베이스에 실행
"""

import os
import sys
import logging

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import get_engine_kwargs
from scripts.log_setup import setup_logging
from sqlmodel import create_engine, text

setup_logging()

def execute_script(file_path: str):
    """지정된 SQL 파일을 읽어서 실행"""
    
    if not os.path.exists(file_path):
        print(f"오류: 파일을 찾을 수 없습니다 - {file_path}")
        return

    print(f"SQL 스크립트 실행 준비: {file_path}")
    
    # Create engine
    kwargs = get_engine_kwargs()
    url = kwargs.pop("url")
    engine = create_engine(url, **kwargs)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    # DBeaver 등에서 내보낸 Oracle SQL 스크립트는 '/' 기호로 명령어를 구분함
    # 줄바꿈 문자를 고려하여 분리
    statements = []
    current_stmt = []
    
    for line in sql_content.splitlines():
        trimmed = line.strip()
        if trimmed == '/':
            if current_stmt:
                statements.append("\n".join(current_stmt))
                current_stmt = []
        else:
            current_stmt.append(line)
            
    # 마지막 문장이 '/'로 끝나지 않은 경우 처리
    if current_stmt and "".join(current_stmt).strip():
        statements.append("\n".join(current_stmt))

    print(f"총 {len(statements)}개의 SQL 문장을 찾았습니다. 실행을 시작합니다...")

    success_count = 0
    fail_count = 0
    
    try:
        with engine.begin() as conn: # Transaction block
            for idx, stmt in enumerate(statements, 1):
                stmt_clean = stmt.strip()
                if not stmt_clean:
                    continue
                
                try:
                    conn.execute(text(stmt_clean))
                    success_count += 1
                    if idx % 10 == 0:
                        print(f"진행 상황: {idx}/{len(statements)} 완료")
                except Exception as e:
                    fail_count += 1
                    print(f"에러 발생 (문장 {idx}): {str(e).splitlines()[0]}")
                    print(f"오류가 발생한 SQL 미리보기: {stmt_clean[:100]}...\n")
                    
        print("=" * 80)
        print(f"실행 완료! (성공: {success_count}, 실패: {fail_count})")
        print("=" * 80)
        
    except Exception as e:
        print(f"치명적인 오류 발생: {e}")

if __name__ == "__main__":
    script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "script_gof.sql")
    execute_script(script_path)
