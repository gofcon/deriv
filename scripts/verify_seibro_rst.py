import sqlite3
import json

def verify_seibro():
    conn = sqlite3.connect('data/kis_api.db')
    cursor = conn.cursor()
    
    # 최근 Seibro 결과 확인
    cursor.execute("""
        SELECT api_id, result_json, updated_at 
        FROM api_rst 
        WHERE api_id LIKE 'seibro%' 
        ORDER BY id DESC LIMIT 1
    """)
    row = cursor.fetchone()
    
    if row:
        api_id, result_json_str, updated_at = row
        print(f"API_ID: {api_id}")
        print(f"Updated At: {updated_at}")
        
        # JSON 파싱 및 데이터 구조 확인
        result = json.loads(result_json_str) if isinstance(result_json_str, str) else result_json_str
        
        # 'header'나 'res'가 최상위에 있고 데이터가 없는지 확인
        if 'header' in result and 'data' not in result and len(result) <= 2:
            print("FAILED: Result still contains only metadata.")
            print(f"Content: {json.dumps(result, indent=2)}")
        else:
            print("SUCCESS: Result looks like actual data.")
            # 데이터 일부 출력
            print(f"Keys: {list(result.keys())}")
            # 첫 번째 값 샘플
            sample_key = list(result.keys())[0]
            print(f"Sample [{sample_key}]: {result[sample_key]}")
    else:
        print("No Seibro results found.")
    
    conn.close()

if __name__ == "__main__":
    verify_seibro()
