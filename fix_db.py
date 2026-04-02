import sqlite3
import json

conn = sqlite3.connect('data/kis_api.db')
cur = conn.cursor()

# Set allowed_values properly as a serialized JSON array representing a list of strings
cur.execute('''
    UPDATE api_param 
    SET allowed_values = '["searchBondList"]'
    WHERE api_id = 'seibro_bond_KACD_list' AND param_name = 'ACTION' 
''')

cur.execute('''
    UPDATE api_param 
    SET allowed_values = '["ksd.safe.bip.cmuc.User.process.SearchPTask"]'
    WHERE api_id = 'seibro_bond_KACD_list' AND param_name = 'TASK' 
''')

# Let's also enforce params_json just in case it's wrong again
# The user wants "searchBondList" exactly.
params_json = '{"ACTION": "searchBondList", "TASK": "ksd.safe.bip.cmuc.User.process.SearchPTask"}'
cur.execute('''
    UPDATE api_job_mst 
    SET params_json = ?
    WHERE api_id = 'seibro_bond_KACD_list'
''', (params_json,))

conn.commit()
conn.close()
print("Fixed double stringification of allowed_values")
