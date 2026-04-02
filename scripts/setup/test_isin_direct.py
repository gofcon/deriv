import logging
import sys
import os

# 프로젝트 루트를 경로에 추가
sys.path.append(os.getcwd())

from app.api.isin_http import IsinHttpClient

# 로그 설정 (디버그 모드 활성)
logging.basicConfig(level=logging.DEBUG)

def test_isin_direct():
    client = IsinHttpClient(debug=True)
    
    # 1. 대상 URL 및 파라미터 (하나은행 채권 예시)
    api_url = "https://isin.krx.co.kr/srch/srch.do"
    params = {
        'method': 'srchPopup3',
        'std_cd': 'KR6004945G31'
    }
    
    print(f"\n>>> Requesting KRX ISIN data for {params['std_cd']}...")
    res = client.fetch(api_url, "isin_bond", params=params)
    
    if res.is_ok():
        body = res.get_body()
        if isinstance(body, dict):
            if "raw_html" in body:
                print("\n[FAIL] Still got error page or raw HTML:")
                print(body["raw_html"][:500])
            else:
                print("\n[SUCCESS] Parsed keys:")
                print(list(body.keys()))
                print("\nIssuer Name (발행기관명):", body.get("발행기관명"))
        else:
            print("\n[FAIL] Unexpected body type:", type(body))
    else:
        print("\n[ERROR] HTTP Status:", res.get_status_code())
        print(res.get_error_message())

if __name__ == "__main__":
    test_isin_direct()
