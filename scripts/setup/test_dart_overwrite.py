import sqlite3
import json
import os
import subprocess
import sys

# app 모듈 로드를 위한 경로 추가
sys.path.append(os.getcwd())

def test_multi_load():
    db_path = 'data/kis_api.db'
    python_exe = os.path.join(os.getcwd(), '.venv', 'Scripts', 'python.exe')
    main_py = os.path.join(os.getcwd(), 'main.py')

    def run_for_corp(job_id, corp_code):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        
        # 1. Job 삽입 (overwrite 모드)
        params = json.dumps({'CORP_CODE': corp_code})
        cur.execute("DELETE FROM api_job_mst WHERE job_id=?", (job_id,))
        cur.execute("""
            INSERT INTO api_job_mst (job_id, api_id, status, is_active, execution_cycle, params_json, save_mode)
            VALUES (?, 'dart_company', 'READY', 1, 'once', ?, 'overwrite')
        """, (job_id, params))
        
        # 스케줄도 once로 활성화되어 있어야 함
        cur.execute("UPDATE api_schedule_mst SET is_active=1, execution_cycle='once' WHERE api_id='dart_company'")
        
        conn.commit()
        conn.close()
        
        # 2. 실행
        print(f"\n>>> Running for CORP_CODE: {corp_code} (Job: {job_id})")
        subprocess.run([python_exe, main_py, '--cycle', 'once'])

    # 기존 데이터 청소 (테스트 시작 전)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM dart_company WHERE api_id='dart_company'")
    conn.commit()
    conn.close()

    # 테스트 케이스 1: 삼성전자 적재
    run_for_corp('test_samsung', '00126380')
    
    # 테스트 케이스 2: SK하이닉스 적재
    # (수정 전에는 삼성전자 데이터가 지워졌어야 함, 수정 후에는 유지되어야 함)
    run_for_corp('test_skhynix', '00164779')

    # 결과 최종 확인
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT api_id, corp_code, corp_name FROM dart_company")
    rows = cur.fetchall()
    
    print("\n" + "="*50)
    print("FINAL VERIFICATION: Records in dart_company")
    print("="*50)
    if len(rows) >= 2:
        print(f"✓ SUCCESS: Found {len(rows)} records. Overwrite logic (api_id + corp_code) is working!")
    else:
        print(f"✗ FAILURE: Found only {len(rows)} records. Expected 2.")
        
    for r in rows:
        print(f"API: {r[0]} | Code: {r[1]} | Name: {r[2]}")
    print("="*50)
    
    conn.close()

if __name__ == '__main__':
    test_multi_load()
