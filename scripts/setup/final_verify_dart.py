import sqlite3
import json
import os
import subprocess
import sys

# app 모듈 로드를 위한 경로 추가
sys.path.append(os.getcwd())

def final_test():
    db_path = 'data/kis_api.db'
    python_exe = os.path.join(os.getcwd(), '.venv', 'Scripts', 'python.exe')
    main_py = os.path.join(os.getcwd(), 'main.py')

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # 1. Job 초기화 (삼성전자 00126380)
    job_id = 'test_samsung_final_v2'
    params = json.dumps({'CORP_CODE': '00126380'})
    cur.execute("DELETE FROM api_job_mst WHERE job_id=?", (job_id,))
    cur.execute("""
        INSERT INTO api_job_mst (job_id, api_id, status, is_active, execution_cycle, params_json, save_mode)
        VALUES (?, 'dart_company', 'READY', 1, 'once', ?, 'overwrite')
    """, (job_id, params))
    
    # 2. 스케줄 활성화
    cur.execute("UPDATE api_schedule_mst SET is_active=1, execution_cycle='once' WHERE api_id='dart_company'")
    
    conn.commit()
    conn.close()

    print(f"\n>>> Running Final Test: DART Company Load (Job: {job_id})")
    subprocess.run([python_exe, main_py, '--cycle', 'once'])

    # 3. 결과 확인
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT api_id, corp_code, corp_name, updated_at FROM dart_company WHERE corp_code='00126380'")
    row = cur.fetchone()
    
    print("\n" + "="*60)
    print("FINAL VERIFICATION RESULT")
    print("="*60)
    if row:
        print(f"✓ SUCCESS: Samsung Electronics data loaded with Composite PK.")
        print(f"  - API ID   : {row[0]}")
        print(f"  - Corp Code: {row[1]}")
        print(f"  - Name     : {row[2]}")
        print(f"  - Updated  : {row[3]}")
    else:
        print(f"✗ FAILURE: Data not found in dart_company table.")
    print("="*60 + "\n")
    
    conn.close()

if __name__ == '__main__':
    final_test()
