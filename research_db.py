import sqlite3
import pandas as pd
import json

def research_db(db_path='data/kis_api.db'):
    conn = sqlite3.connect(db_path)
    
    print("--- 1. Checking seibro_bond_KACD_list ---")
    try:
        kacd_df = pd.read_sql_query("SELECT KACD_CD, KOR_SECN_NM FROM seibro_bond_KACD_list", conn)
        print(f"Total KACD codes found: {len(kacd_df)}")
        print(kacd_df.head())
    except Exception as e:
        print(f"Error reading seibro_bond_KACD_list: {e}")

    print("\n--- 2. Checking api_mst for seibro_bond_isin_by_KACD ---")
    try:
        api_mst_df = pd.read_sql_query("SELECT * FROM api_mst WHERE api_id = 'seibro_bond_isin_by_KACD'", conn)
        print(api_mst_df)
    except Exception as e:
        print(f"Error reading api_mst: {e}")

    print("\n--- 3. Checking api_job_mst Schema ---")
    try:
        job_mst_df = pd.read_sql_query("SELECT * FROM api_job_mst LIMIT 1", conn)
        print(job_mst_df.columns.tolist())
        if not job_mst_df.empty:
            print("Sample params_json:")
            print(job_mst_df['params_json'].iloc[0])
    except Exception as e:
        print(f"Error reading api_job_mst: {e}")

    conn.close()

if __name__ == "__main__":
    research_db()
