import sqlite3
import json
import os

db_path = 'data/kis_api.db'

def setup():
    if not os.path.exists(db_path):
        print(f"Error: Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 1. api_mst 업데이트
    api_id = 'isin_bond'
    cur.execute("SELECT api_id, output_table_name FROM api_mst WHERE api_id = ?", (api_id,))
    row = cur.fetchone()
    if not row:
        print(f"API {api_id} not found. Creating it.")
        cur.execute("""
            INSERT INTO api_mst (api_id, api_name, api_type, api_url, header_json, request_type, output_table_name)
            VALUES (?, ?, 'isin', 'https://isin.krx.co.kr/srch/srch.do', '{}', 'GET', 'api_rst')
        """, (api_id, api_id))
    else:
        cur.execute("UPDATE api_mst SET output_table_name = 'api_rst', api_type = 'isin' WHERE api_id = ?", (api_id,))
        print(f"Updated {api_id} settings.")

    # 2. 테스트 Job 등록 (std_cd=KR6004945G31)
    job_id = 'test_isin_KR6004945G31'
    params = {
        'method': 'srchPopup3',
        'std_cd': 'KR6004945G31'
    }
    cur.execute("DELETE FROM api_job_mst WHERE job_id = ?", (job_id,))
    cur.execute("""
        INSERT INTO api_job_mst (job_id, api_id, status, is_active, execution_cycle, params_json, save_mode)
        VALUES (?, ?, 'READY', 1, 'once', ?, 'overwrite')
    """, (job_id, api_id, json.dumps(params)))

    conn.commit()
    conn.close()
    print(f"Successfully set up test job: {job_id}")

if __name__ == '__main__':
    setup()
