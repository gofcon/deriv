import sqlite3
import pandas as pd

conn = sqlite3.connect('data/kis_api.db')
query = "SELECT * FROM krx_isin_mst WHERE api_name IN ('seibro_bond_KACD_list', 'KACD_list') LIMIT 5"
df = pd.read_sql_query(query, conn)
print("Data in krx_isin_mst:")
print(df)

# 필드 목록 확인 (seibro_bond_KACD_list 응답 필드와 비교용)
cur = conn.cursor()
cur.execute("PRAGMA table_info(krx_isin_mst)")
print("\nTable info for krx_isin_mst:")
for col in cur.fetchall():
    print(col[1])

conn.close()
