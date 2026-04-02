import sqlite3

def add_api_param():
    conn = sqlite3.connect('data/kis_api.db')
    cursor = conn.cursor()
    
    # 1. seibro_open_getBondStatInfo의 파라미터명 대문자로 통일 (시스템 검증 규칙)
    # 기존 ISIN 파라미터를 대문자로 확인 및 추가
    api_id = 'seibro_open_getBondStatInfo'
    
    # apiId 파라미터 추가
    cursor.execute("""
        INSERT OR REPLACE INTO api_param (api_id, param_name, is_required, default_value, description)
        VALUES (?, ?, ?, ?, ?)
    """, (api_id, 'apiId', 1, 'getBondStatInfo', 'Seibro API 서비스 식별자'))
    
    # ISIN 파라미터도 대문자로 확실히 존재하도록 추가
    cursor.execute("""
        INSERT OR REPLACE INTO api_param (api_id, param_name, is_required, default_value, description)
        VALUES (?, ?, ?, ?, ?)
    """, (api_id, 'ISIN', 1, '', '채권 종목코드'))
    
    # 2. 테스트 잡의 파라미터 업데이트
    cursor.execute("SELECT job_id, params_json FROM api_job_mst WHERE api_id = ?", (api_id,))
    jobs = cursor.fetchall()
    import json
    for job_id, params_json_str in jobs:
        params = json.loads(params_json_str) if isinstance(params_json_str, str) else params_json_str
        # apiId 추가 및 키 대문자화
        new_params = {k.upper() if k != 'apiId' else 'apiId': v for k, v in params.items()}
        if 'apiId' not in new_params:
            new_params['apiId'] = 'getBondStatInfo'
        
        cursor.execute("UPDATE api_job_mst SET params_json = ? WHERE job_id = ?", (json.dumps(new_params), job_id))
    
    conn.commit()
    print("Done adding apiId and normalizing params.")
    conn.close()

if __name__ == "__main__":
    add_api_param()
