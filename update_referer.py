import sqlite3
import json

conn = sqlite3.connect('data/kis_api.db')
cur = conn.cursor()

# Set Referer for all seibro_bond APIs
cur.execute("SELECT api_id, header_json FROM api_mst WHERE api_id LIKE 'seibro_bond_%'")
rows = cur.fetchall()

for api_id, header_str in rows:
    headers = json.loads(header_str)
    changed = False
    
    if 'Referer' not in headers:
        headers['Referer'] = 'https://seibro.or.kr/websquare/control.jsp?w2xPath=/IPORTAL/user/bond/BIP_CNTS03005V.xml&menuNo=88'
        changed = True
        
    if changed:
        cur.execute("UPDATE api_mst SET header_json = ? WHERE api_id = ?", (json.dumps(headers, ensure_ascii=False), api_id))
        print(f"Updated Referer for {api_id}")

conn.commit()
conn.close()
