import sqlite3
import subprocess
import os

def force_reset_and_run():
    db_path = 'data/kis_api.db'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # 1. 기존의 모든 dart_company 작업 삭제 (중복 생성 방지 로직 우회)
    cur.execute("DELETE FROM api_job_mst WHERE api_id='dart_company'")
    deleted_jobs = cur.rowcount
    
    # 2. 스케줄 활성화 및 주기를 'once'로 변경
    cur.execute("UPDATE api_schedule_mst SET is_active=1, execution_cycle='once' WHERE api_id='dart_company'")
    updated_sch = cur.rowcount
    
    conn.commit()
    conn.close()
    
    print(f"Deleted {deleted_jobs} existing jobs and updated {updated_sch} schedules for 'dart_company'.")
    
    # 3. main.py 실행
    python_exe = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")
    main_py = os.path.join(os.getcwd(), "main.py")
    
    print("Executing main.py --cycle once...")
    subprocess.run([python_exe, main_py, "--cycle", "once"])

if __name__ == "__main__":
    force_reset_and_run()
