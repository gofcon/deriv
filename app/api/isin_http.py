import logging
import requests
from bs4 import BeautifulSoup
from typing import Dict, Any, Optional
from collections import namedtuple

class IsinAPIResponse:
    """KRX ISIN 상세 정보 HTML 파서"""
    
    def __init__(self, response: requests.Response):
        self._response = response
        self._status_code = response.status_code
        self._body = self._parse_html()
        
    def _parse_html(self):
        text = self._response.text
        if not text:
            return None
            
        try:
            soup = BeautifulSoup(text, 'html.parser')
            parsed_data = {}
            
            # 모든 상세정보 테이블(type-01 detail) 순회
            tables = soup.find_all('table', class_='detail')
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    ths = row.find_all('th')
                    tds = row.find_all('td')
                    
                    # th와 td가 쌍으로 존재하는 경우 추출
                    for i in range(min(len(ths), len(tds))):
                        key = ths[i].get_text(strip=True)
                        value = tds[i].get_text(strip=True)
                        if key:
                            parsed_data[key] = value
            
            if not parsed_data:
                # 파싱된 데이터가 없는 경우 원본 텍스트 반환
                parsed_data = {"raw_html": text}
                
            return parsed_data
            
        except Exception as e:
            logging.error(f"[Isin Parser Error] {str(e)}")
            return {"raw_html": text}

    def is_ok(self) -> bool:
        return 200 <= self._status_code < 300
        
    def get_body(self):
        return self._body

    def get_status_code(self):
        return self._status_code
        
    def get_error_message(self):
        return self._response.text

class IsinAPIResponseError(IsinAPIResponse):
    def __init__(self, status_code: int, error_text: str):
        self._status_code = status_code
        self.error_text = error_text
        self._body = None

    def is_ok(self) -> bool:
        return False
        
    def get_error_message(self):
        return self.error_text

class IsinHttpClient:
    """KRX ISIN 전용 HTTP 클라이언트 (세션 워밍업 적용)"""
    
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.session = requests.Session()
        self.warmed_up = False
        
    def fetch(
        self,
        api_url: str,
        api_id: str,
        header_json: dict = None,
        params: Dict[str, Any] = None,
        additional_headers: Dict[str, str] = None,
        method: str = "GET",
        use_hash: bool = False
    ):
        if params is None:
            params = {}
        
        # KRX 서버는 파라미터 키의 대소문자(e.g., method)에 민감함.
        # DatabaseManager에 의해 대문자로 변환된 키를 소문자로 복원.
        params = {k.lower(): v for k, v in params.items()}
            
        # 브라우저 정밀 분석 기반 헤더 구성
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Referer": "https://isin.krx.co.kr/srch/srch.do?method=srchList",
            "Connection": "keep-alive"
        }
        
        if header_json:
            headers.update(header_json)
        if additional_headers:
            headers.update(additional_headers)
            
        try:
            # 1. 세션 워밍업 (메인 검색 페이지 방문하여 JSESSIONID 확보)
            if not self.warmed_up:
                warmup_url = "https://isin.krx.co.kr/srch/srch.do?method=srchList"
                if self.debug:
                    logging.debug(f"[Isin Warm-up] Initializing session via {warmup_url}")
                self.session.get(warmup_url, headers=headers, timeout=10)
                self.warmed_up = True

            # 2. 실제 데이터 요청
            if method.upper() == "GET":
                response = self.session.get(api_url, params=params, headers=headers, timeout=10)
            else:
                response = self.session.post(api_url, data=params, headers=headers, timeout=10)
                
            return IsinAPIResponse(response)
            
        except requests.exceptions.RequestException as e:
            logging.error(f"[Isin HTTP Error] {api_url}: {str(e)}")
            return IsinAPIResponseError(500, str(e))
