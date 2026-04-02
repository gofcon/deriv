import sqlite3
import os

def check_status():
    db_path = 'data/kis_api.db'
    if not os.path.exists(db_path):
        print(f"DB file not found: {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    print("\n" + "="*50)
    print("FINAL INTEGRATION STATUS CHECK")
    print("="*50)

    # 1. DART Corp Codes (115k+)
    cur.execute("SELECT COUNT(*) FROM dart_corp_code")
    print(f"✓ DART Corp Codes: {cur.fetchone()[0]} records")

    # 2. DART Company (with Composite PK)
    cur.execute("SELECT COUNT(*) FROM dart_company")
    company_count = cur.fetchone()[0]
    print(f"✓ DART Company records: {company_count}")
    
    if company_count > 0:
        cur.execute("SELECT api_id, corp_code, corp_name FROM dart_company LIMIT 5")
        for r in cur.fetchall():
            print(f"  - [{r[0]}] {r[1]}: {r[2]}")

    # 3. Seibro Data (EUC-KR Test)
    # seibro_open 혹은 api_rst 테이블에 데이터가 있는지 확인
    try:
        cur.execute("SELECT COUNT(*) FROM api_rst WHERE api_id LIKE 'seibro%'")
        print(f"✓ Seibro records (in api_rst): {cur.fetchone()[0]}")
    except:
        print("  - api_rst table check failed (might not exist)")

    # 4. Schema Check (Composite PK for dart_company)
    print("\n--- Schema Check: dart_company ---")
    cur.execute("PRAGMA table_info(dart_company)")
    cols = cur.fetchall()
    for c in cols:
        pk_mark = " (PRIMARY KEY)" if c[5] > 0 else ""
        print(f"  [{c[0]}] {c[1]}: {c[2]}{pk_mark}")

    print("="*50 + "\n")
    conn.close()

if __name__ == "__main__":
    check_status()
