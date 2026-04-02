import sqlite3

def check_dart_master_data():
    db_path = 'data/kis_api.db'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    print("--- API_MST ---")
    cur.execute("SELECT api_id, api_name, api_type, output_table_name FROM api_mst WHERE api_id LIKE '%dart%'")
    for r in cur.fetchall(): print(r)

    print("\n--- API_SCHEDULE_MST ---")
    cur.execute("SELECT schedule_id, api_id, execution_cycle FROM api_schedule_mst WHERE api_id LIKE '%dart%'")
    for r in cur.fetchall(): print(r)

    print("\n--- API_JOB_MST ---")
    cur.execute("SELECT job_id, api_id, status FROM api_job_mst WHERE api_id LIKE '%dart%'")
    for r in cur.fetchall(): print(r)

    conn.close()

if __name__ == "__main__":
    check_dart_master_data()
