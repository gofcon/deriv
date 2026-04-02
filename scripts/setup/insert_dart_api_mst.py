import sqlite3
import json
from datetime import datetime

def insert_dart_api_mst():
    conn = sqlite3.connect('data/kis_api.db')
    cursor = conn.cursor()

    # 1. api_mst 삽입
    api_id = 'dart_bond_issue_record'
    api_name = 'DART 사채발행실적'
    api_type = 'dart_open'
    api_url = 'https://opendart.fss.or.kr/api/bdRs.json'
    output_table_name = 'API_RST'
    
    cursor.execute("SELECT api_id FROM api_mst WHERE api_id = ?", (api_id,))
    cursor.execute("""
        INSERT OR REPLACE INTO api_mst (api_id, api_name, api_type, api_url, request_type, output_table_name, header_json)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (api_id, api_name, api_type, api_url, 'GET', output_table_name, '{}'))
    print(f"Upserted api_mst: {api_id}")

    # 2. api_param 삽입
    params = [
        (api_id, 'CORP_CODE', 1, '00858364', '법인코드'),
        (api_id, 'BGN_DE', 1, '20190101', '시작일자(YYYYMMDD)'),
        (api_id, 'END_DE', 1, '20191231', '종료일자(YYYYMMDD)')
    ]
    
    for p in params:
        cursor.execute("""
            INSERT OR REPLACE INTO api_param (api_id, param_name, is_required, default_value, description)
            VALUES (?, ?, ?, ?, ?)
        """, p)
        print(f"Upserted api_param: {p[1]}")

    # 3. api_schedule_mst 및 api_job_mst (테스트용)
    schedule_id = f"{api_id}_daily"
    cursor.execute("""
        INSERT OR REPLACE INTO api_schedule_mst (schedule_id, api_id, macro_params_json, is_active, execution_cycle)
        VALUES (?, ?, ?, ?, ?)
    """, (schedule_id, api_id, '{}', 1, 'daily'))
    
    # job 생성
    job_id = f"{schedule_id}_test"
    params_json = json.dumps({
        "CORP_CODE": "00858364",
        "BGN_DE": "20190101",
        "END_DE": "20191231"
    })
    cursor.execute("""
        INSERT OR REPLACE INTO api_job_mst (job_id, api_id, schedule_id, params_json, status, is_active)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (job_id, api_id, schedule_id, params_json, 'READY', 1))
    print(f"Upserted schedule and job: {job_id}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_dart_api_mst()
