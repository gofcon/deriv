import sqlite3
conn = sqlite3.connect('data/kis_api.db')
cur = conn.cursor()
cur.execute("SELECT api_id, api_name, output_table_name FROM api_mst WHERE api_id = 'seibro_bond_KACD_list'")
print(cur.fetchone())

print("\n--- Check all tables ---")
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print([r[0] for r in cur.fetchall()])

conn.close()
