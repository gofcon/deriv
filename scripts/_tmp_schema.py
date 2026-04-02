import sqlite3
DB_PATH = r'd:\Python\deriv\data\kis_api.db'
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
for tbl in ['api_mst', 'api_param', 'api_schedule_mst']:
    cur.execute(f'PRAGMA table_info("{tbl}")')
    cols = cur.fetchall()
    print(f'\n[{tbl}]')
    for c in cols:
        print(f'  {c[1]} ({c[2]}) notnull={c[3]} default={c[4]} pk={c[5]}')
conn.close()
