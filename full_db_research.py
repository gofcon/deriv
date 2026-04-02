import sqlite3
import pandas as pd
import json

def get_db_info():
    db_path = 'data/kis_api.db'
    conn = sqlite3.connect(db_path)
    
    print("--- 1. Tables in Database ---")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cursor.fetchall()]
    print(f"Tables: {tables}")

    if 'seibro_bond_KACD_list' in tables:
        print("\n--- 2. seibro_bond_KACD_list Schema ---")
        cursor.execute("PRAGMA table_info(seibro_bond_KACD_list)")
        for col in cursor.fetchall():
            print(f"  Column: {col[1]} ({col[2]})")
        
        print("\n--- 3. seibro_bond_KACD_list Sample (5 rows) ---")
        df = pd.read_sql_query("SELECT * FROM seibro_bond_KACD_list LIMIT 5", conn)
        print(df)
    else:
        print("\nWarning: seibro_bond_KACD_list table not found.")

    print("\n--- 4. api_job_mst Schema ---")
    cursor.execute("PRAGMA table_info(api_job_mst)")
    for col in cursor.fetchall():
        print(f"  Column: {col[1]} ({col[2]})")

    conn.close()

if __name__ == "__main__":
    get_db_info()
