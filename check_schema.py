import sqlite3
import os

def check_schema():
    db_path = 'data/kis_api.db'
    if not os.path.exists(db_path):
        print(f"Error: Database file {db_path} not found.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    for table in ['api_mst', 'api_job_mst', 'api_param', 'seibro_bond_KACD_list']:
        print(f"\n--- Schema for table: {table} ---")
        try:
            cursor.execute(f"PRAGMA table_info({table})")
            columns = cursor.fetchall()
            for col in columns:
                print(col)
        except Exception as e:
            print(f"Error checking {table}: {e}")
            
    conn.close()

if __name__ == '__main__':
    check_schema()
