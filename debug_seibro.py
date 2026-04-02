import sqlite3
import pandas as pd
import json

def debug_db():
    conn = sqlite3.connect('data/kis_api.db')
    
    print("--- API MST for seibro_bond ---")
    query = "SELECT api_id, api_type, api_name, api_url FROM api_mst WHERE api_id LIKE 'seibro_bond%'"
    df_mst = pd.read_sql_query(query, conn)
    print(df_mst)
    
    print("\n--- Latest API RST for Seibro ---")
    query = "SELECT job_id, result_json FROM api_rst WHERE api_id LIKE 'seibro_bond%' ORDER BY updated_at DESC LIMIT 1"
    df_rst = pd.read_sql_query(query, conn)
    if not df_rst.empty:
        print(f"Job ID: {df_rst.iloc[0]['job_id']}")
        print(f"Result JSON: {df_rst.iloc[0]['result_json']}")
    else:
        print("No results found in api_rst.")
        
    conn.close()

if __name__ == "__main__":
    debug_db()
