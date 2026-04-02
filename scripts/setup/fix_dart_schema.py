import sqlite3
import os

def fix_schema():
    db_path = 'data/kis_api.db'
    if not os.path.exists(db_path):
        print(f"DB not found: {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    tables = ['dart_corp_code', 'dart_company']
    for table in tables:
        try:
            # api_id 컬럼 추가 시도
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN api_id TEXT")
            print(f"Successfully added 'api_id' column to {table}.")
        except sqlite3.OperationalError as e:
            if "duplicate column name" in str(e).lower():
                print(f"'api_id' column already exists in {table}.")
            else:
                print(f"Error updating {table}: {e}")
                
    conn.commit()
    conn.close()

if __name__ == "__main__":
    fix_schema()
