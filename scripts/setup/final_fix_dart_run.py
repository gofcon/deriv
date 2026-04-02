import sqlite3
import subprocess
import os

def fix_cycle_and_run():
    db_path = 'data/kis_api.db'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # 1. 모든 dart_company 관련 작업의 주기를 'once'로 변경하여 main.py가 즉시 인식하게 함
    cur.execute("UPDATE api_job_mst SET execution_cycle='once', status='READY' WHERE api_id='dart_company'")
    affected = cur.rowcount
    conn.commit()
    conn.close()
    print(f"Updated {affected} jobs for 'dart_company' to cycle=once and status=READY.")
    
    # 2. main.py 실행
    python_exe = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")
    main_py = os.path.join(os.getcwd(), "main.py")
    
    print("Executing main.py --cycle once...")
    subprocess.run([python_exe, main_py, "--cycle", "once"])

if __name__ == "__main__":
    fix_cycle_and_run()
