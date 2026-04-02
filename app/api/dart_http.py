import logging
import requests
from typing import Dict, Any, Optional, List
from collections import namedtuple

class DartAPIResponse:
    """DART Open API 응답 래퍼 클래스"""
    
    def __init__(self, response: requests.Response):
        self._response = response
        self._status_code = response.status_code
        try:
            self._data = response.json()
        except:
            self._data = {}
            
    def is_ok(self) -> bool:
        # DART는 status가 "000"일 때 정상입니다.
        return self._status_code == 200 and self._data.get("status") == "000"
        
    def get_body(self):
        # 전체 JSON 데이터를 namedtuple 형태로 반환하여 점 표기법 사용 지원
        DataTuple = namedtuple("Data", self._data.keys())
        return DataTuple(**self._data)

    def get_status_code(self):
        return self._status_code
        
    def get_error_message(self):
        return self._data.get("message", self._response.text)

class DartAPIResponseError(DartAPIResponse):
    def __init__(self, status_code: int, error_text: str):
        self._status_code = status_code
        self._data = {"status": "999", "message": error_text}

    def is_ok(self) -> bool:
        return False

class DartHttpClient:
    """DART Open API 전용 HTTP 클라이언트"""
    
    def __init__(self, key: str, debug: bool = False):
        self.key = key
        self.debug = debug
        
    def fetch(
        self,
        api_url: str,
        api_id: str,
        header_json: dict = None,
        params: Dict[str, Any] = None,
        additional_headers: Dict[str, str] = None,
        method: str = "GET",
        use_hash: bool = False
    ) -> DartAPIResponse:
        
        if params is None:
            params = {}
            
        # 모든 파라미터 키를 소문자로 변환 (시스템 검증은 대문자로 수행됨)
        lower_params = {k.lower(): v for k, v in params.items()}
        
        # crtfc_key(인증키) 삽입
        lower_params["crtfc_key"] = self.key
        
        headers = header_json or {}
        if additional_headers:
            headers.update(additional_headers)
            
        try:
            if method.upper() == "GET":
                response = requests.get(api_url, params=lower_params, headers=headers)
            else:
                response = requests.post(api_url, data=lower_params, headers=headers)
                
            return DartAPIResponse(response)
            
        except requests.exceptions.RequestException as e:
            logging.error(f"[DART HTTP Error] {api_url}: {str(e)}")
            return DartAPIResponseError(500, str(e))
