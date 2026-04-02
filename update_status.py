import sqlite3

conn = sqlite3.connect('data/kis_api.db')
cur = conn.cursor()
cur.execute("UPDATE api_job_mst SET status='PENDING' WHERE api_id='seibro_bond_KACD_list'")
cur.execute("UPDATE api_mst SET output_table_name='seibro_bond_kacd_list' WHERE api_id='seibro_bond_KACD_list'")
conn.commit()
conn.close()
print("Updated successfully")
