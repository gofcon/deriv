import sqlite3

def fix_dart_params():
    conn = sqlite3.connect('data/kis_api.db')
    cursor = conn.cursor()

    api_id = 'dart_bond_issue_record'
    
    # 1. 기존 파라미터 삭제 (대소문자 혼재 방지)
    cursor.execute("DELETE FROM api_param WHERE api_id = ?", (api_id,))
    
    # 2. 대문자로 재삽입
    params = [
        (api_id, 'CORP_CODE', 1, '00858364', '법인코드'),
        (api_id, 'BGN_DE', 1, '20190101', '시작일자(YYYYMMDD)'),
        (api_id, 'END_DE', 1, '20191231', '종료일자(YYYYMMDD)')
    ]
    
    for p in params:
        cursor.execute("""
            INSERT INTO api_param (api_id, param_name, is_required, default_value, description)
            VALUES (?, ?, ?, ?, ?)
        """, p)
        print(f"Fixed param: {p[1]}")

    # 3. Job params_json 도 대문자로 확인
    cursor.execute("SELECT job_id, params_json FROM api_job_mst WHERE api_id = ?", (api_id,))
    jobs = cursor.fetchall()
    for job_id, params_json_str in jobs:
        import json
        params = json.loads(params_json_str) if isinstance(params_json_str, str) else params_json_str
        new_params = {k.upper(): v for k, v in params.items()}
        cursor.execute("UPDATE api_job_mst SET params_json = ? WHERE job_id = ?", (json.dumps(new_params), job_id))
        print(f"Fixed job params: {job_id}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    fix_dart_params()
