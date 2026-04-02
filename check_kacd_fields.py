import requests
import sqlite3
import json

conn = sqlite3.connect('data/kis_api.db')
cur = conn.cursor()
cur.execute("SELECT api_url, header_json FROM api_mst WHERE api_id='seibro_bond_KACD_list'")
url_postfix, header_str = cur.fetchone()
conn.close()

url = "https://seibro.or.kr" + url_postfix
headers = json.loads(header_str)

params = {
    "PAGE_ON_CNT": "1",
    "PAGE_NUM": "1",
    "ACTION": "bondKacdList",
    "TASK": "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask"
}

action = params.get("ACTION")
task = params.get("TASK")
xml_body = f'<reqParam action="{action}" task="{task}">'
for k, v in params.items():
    if k not in ("ACTION", "TASK"):
        xml_body += f'<{k} value="{v}"/>'
xml_body += '</reqParam>'

res = requests.post(url, headers=headers, data=xml_body.encode('utf-8'))
print("Status:", res.status_code)

import xml.etree.ElementTree as ET
try:
    root = ET.fromstring(res.text)
    for child in root.findall(".//output/row")[:1]:
        print("Keys (output):", child.attrib.keys())
    for child in root.findall(".//output1/row")[:1]:
        print("Keys (output1):", child.attrib.keys())
        print("Values:", child.attrib)
except Exception as e:
    print(e)
    print(res.text[:500])
