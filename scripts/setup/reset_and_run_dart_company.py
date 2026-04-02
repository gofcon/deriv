import sqlite3
import subprocess
import os

def reset_and_run():
    db_path = 'data/kis_api.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. 'dart_company' 관련 작업 상태를 READY로 변경
    cursor.execute("UPDATE api_job_mst SET status='READY' WHERE api_id='dart_company'")
    affected_jobs = cursor.rowcount
    
    # 2. 관련 스케줄을 'once'로 임시 변경 (테스트용)
    # DART_COMPANY_DAILY 등 연관된 스케줄 모두 포함
    cursor.execute("UPDATE api_schedule_mst SET execution_cycle='once' WHERE api_id='dart_company' OR schedule_id='dart_company_daily'")
    affected_schedules = cursor.rowcount
    
    conn.commit()
    conn.close()
    
    print(f"Reset {affected_jobs} jobs and {affected_schedules} schedules for 'dart_company'.")
    
    # 3. main.py 실행 (once 사이클만)
    main_py = os.path.join(os.getcwd(), "main.py")
    python_exe = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")
    
    print(f"Running main.py with --cycle once...")
    subprocess.run([python_exe, main_py, "--cycle", "once"])

if __name__ == "__main__":
    reset_and_run()
