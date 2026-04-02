import sqlite3
import subprocess
import sys
import os

db_path = 'data/kis_api.db'

def run_integration_test():
    if not os.path.exists(db_path):
        print(f"Error: Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 1. 대상 작업 초기화 (isin_bond 및 seibro_open)
    job_ids = ['seibro_open_getBondStatInfo_daily_KR6268761881', 'isin_bond_KR6004945G31']
    print(f"Resetting {len(job_ids)} jobs to READY/once cycle...")
    
    for jid in job_ids:
        cur.execute("""
            UPDATE api_job_mst 
            SET execution_cycle = 'once', status = 'READY', is_active = 1 
            WHERE job_id = ?
        """, (jid,))
    
    conn.commit()
    conn.close()

    # 2. main.py 실행
    print("Running: main.py --cycle once")
    python_exe = sys.executable
    result = subprocess.run([python_exe, 'main.py', '--cycle', 'once'], capture_output=True, text=True)
    
    print("\n--- STDOUT ---")
    print(result.stdout)
    if result.stderr:
        print("\n--- STDERR ---")
        print(result.stderr)

    # 3. 결과 확인 (api_job_mst 및 api_rst)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    print("\n--- Verification Results ---")
    for jid in job_ids:
        cur.execute("SELECT status, error_message, updated_at FROM api_job_mst WHERE job_id = ?", (jid,))
        row = cur.fetchone()
        if row:
            print(f"Job: {jid}")
            print(f"  Final Status: {row[0]}")
            print(f"  Updated At:   {row[2]}")
            if row[1]:
                print(f"  Error: {row[1]}")
            
            # api_rst 에 실제 데이터 적재 확인
            cur.execute("SELECT COUNT(*) FROM api_rst WHERE job_id = ?", (jid,))
            count = cur.fetchone()[0]
            print(f"  Data in api_rst: {count} row(s)")
            print("-" * 20)
    
    conn.close()

if __name__ == '__main__':
    run_integration_test()
