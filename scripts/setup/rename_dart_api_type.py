import sqlite3

def rename_dart_type():
    conn = sqlite3.connect('data/kis_api.db')
    cursor = conn.cursor()
    
    # 1. api_mst 테이블 변경
    cursor.execute("UPDATE api_mst SET api_type='dart_open' WHERE api_type='dart'")
    affected = cursor.rowcount
    
    conn.commit()
    print(f"Database updated: api_mst '{affected}' rows changed from 'dart' to 'dart_open'.")
    conn.close()

if __name__ == "__main__":
    rename_dart_type()
