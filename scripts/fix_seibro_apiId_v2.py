import sqlite3
import json

def fix_seibro_apiId():
    conn = sqlite3.connect('data/kis_api.db')
    cursor = conn.cursor()
    
    api_id = 'seibro_open_getBondStatInfo'
    
    # 1. api_param 수정 (APIID 로 통일)
    cursor.execute("DELETE FROM api_param WHERE api_id = ? AND param_name = 'apiId'", (api_id,))
    cursor.execute("DELETE FROM api_param WHERE api_id = ? AND param_name = 'APIID'", (api_id,))
    
    cursor.execute("""
        INSERT INTO api_param (api_id, param_name, is_required, default_value, description)
        VALUES (?, ?, ?, ?, ?)
    """, (api_id, 'APIID', 1, 'getBondStatInfo', 'Seibro API 서비스 식별자'))
    
    # 2. api_job_mst 수정
    cursor.execute("SELECT job_id, params_json FROM api_job_mst WHERE api_id = ?", (api_id,))
    jobs = cursor.fetchall()
    for job_id, params_json_str in jobs:
        params = json.loads(params_json_str) if isinstance(params_json_str, str) else params_json_str
        # 모든 키를 대문자로 변환하면서 APIID 추가
        new_params = {k.upper(): v for k, v in params.items()}
        if 'APIID' not in new_params:
            new_params['APIID'] = 'getBondStatInfo'
        
        cursor.execute("UPDATE api_job_mst SET params_json = ? WHERE job_id = ?", (json.dumps(new_params), job_id))
    
    conn.commit()
    print("Database updated: api_param and api_job_mst use APIID (UPPERCASE).")
    conn.close()

if __name__ == "__main__":
    fix_seibro_apiId()
