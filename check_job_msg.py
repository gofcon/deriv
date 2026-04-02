import sqlite3
conn = sqlite3.connect('data/kis_api.db')
cur = conn.cursor()
cur.execute("SELECT status, error_message FROM api_job_mst WHERE job_id='seibro_bond_KACD_list_daily_202603_1'")
print(cur.fetchone())
conn.close()
