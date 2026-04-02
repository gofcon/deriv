import sqlite3
import json
import os
import subprocess

def final_load():
    db_path = 'data/kis_api.db'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 1. 찌꺼기 제거
    cur.execute("DELETE FROM api_job_mst WHERE api_id='dart_company'")
    
    # 2. 실행 가능한 Job 삽입 (삼성전자: 00126380)
    params_json = json.dumps({'CORP_CODE': '00126380'})
    cur.execute("""
        INSERT INTO api_job_mst (job_id, api_id, status, is_active, execution_cycle, params_json)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ('dart_company_final_fix', 'dart_company', 'READY', 1, 'once', params_json))
    
    conn.commit()
    conn.close()
    print("Final Job inserted. Executing main.py...")

    # 3. main.py 실행
    python_exe = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")
    main_py = os.path.join(os.getcwd(), "main.py")
    
    subprocess.run([python_exe, main_py, "--cycle", "once"])

if __name__ == "__main__":
    final_load()
