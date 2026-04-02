import sqlite3
import json

def check_params():
    conn = sqlite3.connect('data/kis_api.db')
    cursor = conn.cursor()
    
    api_id = 'seibro_open_getBondStatInfo'
    cursor.execute("SELECT job_id, params_json FROM api_job_mst WHERE api_id = ?", (api_id,))
    rows = cursor.fetchall()
    
    for job_id, params_json_str in rows:
        print(f"Job ID: {job_id}")
        params = json.loads(params_json_str) if isinstance(params_json_str, str) else params_json_str
        print(f"Raw Params: {repr(params)}")
        
        # 공백 여부 확인 
        for k, v in params.items():
            if v and isinstance(v, str) and ' ' in v:
                print(f"WARNING: Key '{k}' has value with space: '{v}'")
            elif v and isinstance(v, str):
                print(f"Key '{k}' value is clean: '{v}'")

    conn.close()

if __name__ == "__main__":
    check_params()
