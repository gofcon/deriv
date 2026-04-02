import sqlite3
import json
import os

db_path = 'data/kis_api.db'

def check_status():
    if not os.path.exists(db_path):
        print(f"Error: Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 1. 최신 Job 상태 확인
    print("--- Latest API Job Status ---")
    cur.execute("""
        SELECT job_id, status, error_message, updated_at 
        FROM api_job_mst 
        ORDER BY updated_at DESC LIMIT 5
    """)
    rows = cur.fetchall()
    for row in rows:
        print(f"Job: {row[0]}, Status: {row[1]}, Update: {row[3]}")
        if row[2]:
            print(f"  Error: {row[2][:200]}")

    # 2. api_rst 데이터 적재 확인 (Seibro Open)
    print("\n--- Seibro Open Result (api_rst) ---")
    cur.execute("""
        SELECT job_id, updated_at, result_json 
        FROM api_rst 
        WHERE api_id LIKE '%seibro_open%' 
        ORDER BY updated_at DESC LIMIT 1
    """)
    row = cur.fetchone()
    if row:
        print(f"Job: {row[0]}, Update: {row[1]}")
        # print(f"Data: {row[2][:100]}...")
    else:
        print("No Seibro Open data found.")

    conn.close()

if __name__ == '__main__':
    check_status()
