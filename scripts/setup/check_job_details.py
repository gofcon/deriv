import sqlite3

def check_job_details():
    db_path = 'data/kis_api.db'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    print("--- API_JOB_MST Detailed Status ---")
    # job_id, api_id, status, is_active, execution_cycle 컬럼 조회
    cur.execute("SELECT job_id, api_id, status, is_active, execution_cycle FROM api_job_mst WHERE api_id LIKE '%dart_company%'")
    for r in cur.fetchall():
        print(f"Job ID: {r[0]}, API ID: {r[1]}, Status: {r[2]}, Active: {r[3]}, Cycle: {r[4]}")

    conn.close()

if __name__ == "__main__":
    check_job_details()
