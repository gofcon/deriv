import os
import requests
from dotenv import load_dotenv

load_dotenv()
seibro_key = os.getenv('SEIBRO_KEY')
print(f'SEIBRO_KEY loaded: {bool(seibro_key)}')

if seibro_key:
    url = f'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp?key={seibro_key}&apiId=getBondStatInfo&params=ISIN:KR6268761881'
    print(f'Fetching: {url}')
    try:
        res = requests.get(url)
        print('Status:', res.status_code)
        print('Response Text Preview:')
        print(res.text[:500])
    except Exception as e:
        print('Error:', e)
