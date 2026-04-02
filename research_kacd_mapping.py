import sqlite3
import json
import os

def research():
    db_path = 'data/kis_api.db'
    if not os.path.exists(db_path):
        print(f"Error: Database file {db_path} not found.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Check KACDs from seibro_bond_KACD_list table
    kacds = []
    try:
        cursor.execute("SELECT KACD_CD FROM seibro_bond_KACD_list")
        kacds = [row[0] for row in cursor.fetchall() if row[0]]
        print(f"Found {len(kacds)} KACDs in specific table 'seibro_bond_KACD_list'.")
    except Exception as e:
        print(f"Notice: Specific table 'seibro_bond_KACD_list' error or not found: {e}")
        # Check API_RST if table doesn't exist or column missing
        try:
            cursor.execute("SELECT result_json FROM api_rst WHERE api_id = 'seibro_bond_KACD_list' ORDER BY id DESC LIMIT 1")
            row = cursor.fetchone()
            if row:
                data = json.loads(row[0])
                # data might be {'data': [...]} or a list
                if isinstance(data, dict) and 'data' in data:
                    kacds = [item.get('KACD_CD') for item in data['data'] if item.get('KACD_CD')]
                elif isinstance(data, list):
                    kacds = [item.get('KACD_CD') for item in data if item.get('KACD_CD')]
                print(f"Found {len(kacds)} KACDs in API_RST.")
        except Exception as ex:
             print(f"Error checking API_RST: {ex}")

    # 2. Template job from api_job_mst for the target API
    cursor.execute("SELECT job_id, params_json FROM api_job_mst WHERE api_id = 'seibro_bond_isin_by_KACD' LIMIT 1")
    row = cursor.fetchone()
    if row:
        print(f"Template Job: {row[0]}")
        print(f"Template Params: {row[1]}")
    else:
        print("Warning: No template job found for 'seibro_bond_isin_by_KACD' in api_job_mst.")

    # 3. Check api_mst entry
    cursor.execute("SELECT api_id, base_url, api_url FROM api_mst WHERE api_id = 'seibro_bond_isin_by_KACD'")
    api_info = cursor.fetchone()
    if api_info:
        print(f"API Info - ID: {api_info[0]}, Base: {api_info[1]}, URL: {api_info[2]}")
    else:
        print("Error: API 'seibro_bond_isin_by_KACD' NOT FOUND in api_mst.")

    # 4. Check existing jobs for this API to avoid duplicates or identify pattern
    cursor.execute("SELECT count(*) FROM api_job_mst WHERE api_id = 'seibro_bond_isin_by_KACD'")
    job_count = cursor.fetchone()[0]
    print(f"Current job count for 'seibro_bond_isin_by_KACD': {job_count}")

    print(f"Sample KACDs: {kacds[:10]}")
    conn.close()

if __name__ == '__main__':
    research()
