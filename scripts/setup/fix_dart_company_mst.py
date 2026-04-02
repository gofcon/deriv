import sqlite3

def check_and_fix_api_mst():
    conn = sqlite3.connect('data/kis_api.db')
    cursor = conn.cursor()
    
    # 1. 'dart_company' 관련 API 검색
    cursor.execute("SELECT api_id, output_table_name FROM api_mst WHERE api_id LIKE '%dart_company%'")
    rows = cursor.fetchall()
    
    if rows:
        for api_id, current_table in rows:
            print(f"Found API: {api_id}, Current Table: {current_table}")
            if current_table != 'DART_COMPANY':
                # 2. 전용 테이블로 업데이트
                cursor.execute("UPDATE api_mst SET output_table_name = 'DART_COMPANY' WHERE api_id = ?", (api_id,))
                print(f"Updated {api_id} output_table_name to 'DART_COMPANY'")
    else:
        print("No 'dart_company' API definition found in api_mst.")
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    check_and_fix_api_mst()
