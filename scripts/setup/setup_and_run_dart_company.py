import sqlite3
import json
import os
import subprocess

def setup_and_run():
    db_path = 'data/kis_api.db'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 1. API_MST 설정 (DART_COMPANY 출력 보장)
    cur.execute("UPDATE api_mst SET output_table_name = 'DART_COMPANY' WHERE api_id = 'dart_company'")

    # 2. API_SCHEDULE_MST 등록 (테스트를 위해 once로 설정)
    cur.execute("""
        INSERT OR REPLACE INTO api_schedule_mst (schedule_id, api_id, execution_cycle, is_active, macro_params_json)
        VALUES (?, ?, ?, ?, ?)
    """, ('dart_company_once', 'dart_company', 'once', 1, '{}'))

    # 3. API_JOB_MST 등록 (삼성전자 고유번호: 00126380)
    params_json = json.dumps({"CORP_CODE": "00126380"})
    cur.execute("""
        INSERT OR REPLACE INTO api_job_mst (job_id, api_id, schedule_id, status, params_json, is_active)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ('dart_company_test_v3', 'dart_company', 'dart_company_once', 'READY', params_json, 1))

    conn.commit()
    conn.close()
    print("Pipeline for 'dart_company' configured: Schedule and Job are READY.")

    # 4. main.py 실행
    python_exe = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")
    main_py = os.path.join(os.getcwd(), "main.py")
    
    print("Executing main.py --cycle once...")
    subprocess.run([python_exe, main_py, "--cycle", "once"])

if __name__ == "__main__":
    setup_and_run()
