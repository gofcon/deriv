import logging
import json
import xml.etree.ElementTree as ET
import requests
from typing import Dict, Any, Optional
from collections import namedtuple

class GeneralAPIResponse:
    """일반 API 응답 래퍼 클래스"""
    
    def __init__(self, response: requests.Response):
        self._response = response
        self._status_code = response.status_code
        self._body = self._parse_body()
    
    def _parse_body(self):
        text = self._response.text
        if not text:
            return None
            
        try:
            json_data = self._response.json()
            if isinstance(json_data, list):
                # list 형태이면 래핑
                json_data = {"output": json_data}
            BodyTuple = namedtuple("Body", json_data.keys())
            return BodyTuple(**json_data)
        except json.JSONDecodeError:
            # XML이나 일반 텍스트인 경우 파싱 없이 원문 반환 (Seibro와 분리)
            content_type = self._response.headers.get('Content-Type', '').lower()
            if 'xml' in content_type or text.strip().startswith('<'):
                parsed_data = {"raw_xml": text}
                BodyTuple = namedtuple("Body", parsed_data.keys())
                return BodyTuple(**parsed_data)
            return text

    def is_ok(self) -> bool:
        """HTTP 상태 코드로 성공 판단"""
        return 200 <= self._status_code < 300
        
    def get_body(self):
        return self._body

    def get_status_code(self):
        return self._status_code
        
    def get_error_message(self):
        return self._response.text

class GeneralAPIResponseError(GeneralAPIResponse):
    """에러를 래핑할 때 사용"""
    def __init__(self, status_code: int, error_text: str):
        self._status_code = status_code
        self.error_text = error_text
        self._body = None

    def is_ok(self) -> bool:
        return False
        
    def get_error_message(self):
        return self.error_text

class GeneralHttpClient:
    """KIS API가 아닌 일반 웹 API를 위한 범용 HTTP 클라이언트"""
    
    def __init__(self, debug: bool = False):
        self.debug = debug
        
    def fetch(
        self,
        api_url: str,
        api_id: str,
        header_json: dict = None,
        params: Dict[str, Any] = None,
        additional_headers: Dict[str, str] = None,
        method: str = "GET",
        use_hash: bool = False  # 무시됨
    ):
        if params is None:
            params = {}
            
        headers = header_json or {}
        if additional_headers:
            headers.update(additional_headers)
            
        try:
            if method.upper() == "GET":
                response = requests.get(api_url, params=params, headers=headers)
            elif method.upper() == "POST":
                # JSON인지 XML인지 판단 혹은 dict 그대로 전송
                content_type = headers.get('Content-Type', '').lower()
                
                if 'application/xml' in content_type:
                    # 일반 XML 요청의 경우 params가 문자열이면 그대로 보내고, 아니면 기본 처리
                    data = params if isinstance(params, str) else params
                    response = requests.post(api_url, data=data, headers=headers)
                elif 'application/json' in content_type:
                    response = requests.post(api_url, json=params, headers=headers)
                else:
                    # 기본 urlencoded 폼 데이터
                    response = requests.post(api_url, data=params, headers=headers)
            else:
                response = requests.request(method.upper(), api_url, params=params, headers=headers)
                
            return GeneralAPIResponse(response)
            
        except requests.exceptions.RequestException as e:
            logging.error(f"[General HTTP Error] {api_url}: {str(e)}")
            return GeneralAPIResponseError(500, str(e))
