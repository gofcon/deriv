import sqlite3
import pandas as pd
import json

def get_db_info():
    db_path = 'data/kis_api.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Correct table name from previous run: SEIBRO_BOND_KACD_LIST
    table_name = 'SEIBRO_BOND_KACD_LIST'
    
    print(f"--- 1. Checking {table_name} Schema ---")
    cursor.execute(f"PRAGMA table_info({table_name})")
    cols = cursor.fetchall()
    for col in cols:
        print(f"  Column: {col[1]} ({col[2]})")
    
    print(f"\n--- 2. {table_name} Sample (5 rows) ---")
    df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 5", conn)
    print(df)

    print("\n--- 3. api_job_mst Sample for seibro_bond_isin_by_KACD ---")
    df_job = pd.read_sql_query("SELECT * FROM api_job_mst WHERE api_id = 'seibro_bond_isin_by_KACD' LIMIT 1", conn)
    if not df_job.empty:
        print(df_job.to_dict('records')[0])
    else:
        print("No job found for seibro_bond_isin_by_KACD")

    conn.close()

if __name__ == "__main__":
    get_db_info()
