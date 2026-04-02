import sqlite3
import subprocess
import os
import sys

db_path = 'data/kis_api.db'

def run_test():
    if not os.path.exists(db_path):
        print(f"Error: Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 1. Job 상태 초기화 (READY, is_active=1)
    job_id = 'test_isin_KR6004945G31'
    print(f"Reactivating job: {job_id}...")
    cur.execute("UPDATE api_job_mst SET status = 'READY', is_active = 1 WHERE job_id = ?", (job_id,))
    conn.commit()
    conn.close()

    # 2. main.py 실행 (subprocess 호출)
    print("Running main.py --cycle once...")
    python_exe = sys.executable
    result = subprocess.run([python_exe, 'main.py', '--cycle', 'once'], capture_output=True, text=True)
    
    print("\n--- STDOUT ---")
    print(result.stdout)
    if result.stderr:
        print("\n--- STDERR ---")
        print(result.stderr)

    # 3. 데이터베이스 결과 확인
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT result_json FROM api_rst WHERE job_id = ? ORDER BY updated_at DESC LIMIT 1", (job_id,))
    row = cur.fetchone()
    if row:
        import json
        data = json.loads(row[0])
        if "raw_html" in data:
            print("\n[FAIL] Still captured error page or failed to parse.")
        else:
            print("\n[SUCCESS] Final Parsed Data (Sample):")
            print(json.dumps(data, indent=2, ensure_ascii=False)[:1000] + "...")
    else:
        print("\n[FAIL] No data found in api_rst for this job.")
    conn.close()

if __name__ == '__main__':
    run_test()
