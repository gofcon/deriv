import sqlite3
import os

db_path = 'data/kis_api.db'

def debug_config():
    if not os.path.exists(db_path):
        print(f"Error: Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    print("--- Detailed Job Configuration ---")
    # KR6004945G31 (isin_bond) 및 KR6268761881 (seibro_open) 관련 작업 조회
    cur.execute("""
        SELECT job_id, is_active, status, execution_cycle, updated_at 
        FROM api_job_mst 
        WHERE job_id LIKE '%KR6004945G31%' OR job_id LIKE '%KR6268761881%'
    """)
    rows = cur.fetchall()
    
    if not rows:
        print("No matching jobs found.")
    else:
        for r in rows:
            print(f"Job: {r[0]}")
            print(f"  Active: {r[1]} (type: {type(r[1])})")
            print(f"  Status: {r[2]}")
            print(f"  Cycle:  {r[3]}")
            print(f"  Updated: {r[4]}")
            print("-" * 20)

    conn.close()

if __name__ == '__main__':
    debug_config()
