import sqlite3
import os

def check_seibro_api():
    db_path = 'data/kis_api.db'
    if not os.path.exists(db_path):
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # seibro 타입 API의 구성을 확인
    cur.execute("SELECT api_id, api_name, header_json, macro_params_json FROM api_mst WHERE api_type='seibro' LIMIT 5")
    rows = cur.fetchall()
    
    print("\n--- Seibro Type API Configurations ---")
    for r in rows:
        print(f"ID: {r[0]} | Name: {r[1]}")
        print(f"  Headers: {r[2]}")
        print(f"  Macro Params: {r[3]}")
    print("--------------------------------------\n")
    
    conn.close()

if __name__ == "__main__":
    check_seibro_api()
