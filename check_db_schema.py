import sqlite3
import pandas as pd

def check_schema():
    conn = sqlite3.connect('data/kis_api.db')
    
    print("--- seibro_bond_KACD_list schema ---")
    df_kacd = pd.read_sql_query("SELECT * FROM seibro_bond_KACD_list LIMIT 1", conn)
    print(df_kacd.columns.tolist())
    print(df_kacd.head(1).to_dict('records'))
    
    print("\n--- api_job_mst schema ---")
    df_job = pd.read_sql_query("SELECT * FROM api_job_mst LIMIT 1", conn)
    print(df_job.columns.tolist())
    print(df_job.head(1).to_dict('records'))
    
    conn.close()

if __name__ == "__main__":
    check_schema()
