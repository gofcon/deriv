import sqlite3
import json
import pandas as pd
import os

def check_data():
    db_path = 'data/kis_api.db'
    if not os.path.exists(db_path):
        print(f"Error: Database file not found: {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 해당 job_id의 데이터를 조회합니다.
    job_id = 'seibro_bond_isin_by_KACD_daily_110110'
    cursor.execute("SELECT result_json FROM api_rst WHERE job_id = ?", (job_id,))
    row = cursor.fetchone()
    
    if row:
        data = json.loads(row[0])
        # data는 보통 {"data": [...]} 형태이거나 직접 리스트일 수 있습니다.
        if isinstance(data, dict) and 'data' in data:
            records = data['data']
        elif isinstance(data, list):
            records = data
        else:
            print("Unexpected JSON format:", data)
            return
            
        if records:
            df = pd.DataFrame(records)
            print(f"--- Data Summary for {job_id} ---")
            print(f"Total records: {len(df)}")
            print("\n--- Columns ---")
            print(df.columns.tolist())
            print("\n--- Sample Row ---")
            print(df.iloc[0].to_dict())
        else:
            print("No records found in JSON.")
    else:
        print(f"No entry found in api_rst for job_id: {job_id}")
    
    conn.close()

if __name__ == "__main__":
    check_data()
