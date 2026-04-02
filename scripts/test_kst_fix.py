import sqlite3

def reset_jobs():
    conn = sqlite3.connect('data/kis_api.db')
    cursor = conn.cursor()
    
    # DART 작업 및 특정 Seibro 작업을 READY로 리셋하여 강제 재실행 유도
    cursor.execute("UPDATE api_job_mst SET status='READY', is_active=1 WHERE api_id='dart_bond_issue_record'")
    cursor.execute("UPDATE api_job_mst SET status='READY', is_active=1 WHERE api_id='seibro_open_getBondStatInfo'")
    
    conn.commit()
    print(f"Reset {cursor.rowcount} jobs to READY.")
    conn.close()

if __name__ == "__main__":
    reset_jobs()
