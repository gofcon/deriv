# -*- coding: utf-8 -*-
"""
kis_http.py - KIS API HTTP 요청/응답 처리
- REST API 호출
- 응답 래퍼 클래스
- Hash key 관리
- Rate limiting
"""

import time
import json
import logging
import copy
from collections import namedtuple
from typing import Dict, Any, Optional

import requests




class APIResponse:
    """API 응답 래퍼 클래스"""
    
    def __init__(self, response: requests.Response):
        """
        Args:
            response: requests.Response 객체
        """
        self._response = response
        self._status_code = response.status_code
        self._header = self._parse_header()
        self._body = self._parse_body()
        self._error_code = getattr(self._body, 'msg_cd', None)
        self._error_message = getattr(self._body, 'msg1', None)
    
    def _parse_header(self):
        """응답 헤더 파싱"""
        fields = {}
        for key in self._response.headers.keys():
            if key.islower():
                fields[key] = self._response.headers.get(key)
        
        if not fields:
            return None
        
        HeaderTuple = namedtuple("Header", fields.keys())
        return HeaderTuple(**fields)
    
    def _parse_body(self):
        """응답 바디 파싱"""
        try:
            json_data = self._response.json()
            BodyTuple = namedtuple("Body", json_data.keys())
            return BodyTuple(**json_data)
        except Exception:
            return None
    
    def get_status_code(self) -> int:
        """HTTP 상태 코드 반환"""
        return self._status_code
    
    def get_header(self):
        """응답 헤더 반환"""
        return self._header
    
    def get_body(self):
        """응답 바디 반환"""
        return self._body
    
    def get_response(self) -> requests.Response:
        """원본 Response 객체 반환"""
        return self._response
    
    def is_ok(self) -> bool:
        """성공 여부 확인"""
        try:
            return self.get_body().rt_cd == "0"
        except Exception:
            return False
    def print_all(self) -> None:
        """전체 응답 출력"""
        print("<Header>")
        if self._header:
            for field in self._header._fields:
                print(f"\t-{field}: {getattr(self._header, field)}")
        
        print("<Body>")
        if self._body:
            for field in self._body._fields:
                print(f"\t-{field}: {getattr(self._body, field)}")
    
   
    def print_error(self, url: str = "") -> None:
        """에러 정보 출력"""
        print("-" * 60)
        print(f"Error in response: {self._status_code}")
        if url:
            print(f"URL: {url}")
        
        if self._body:
            print(f"rt_cd: {getattr(self._body, 'rt_cd', 'N/A')}")
            print(f"msg_cd: {self._error_code}")
            print(f"msg1: {self._error_message}")
        
        print("-" * 60)
    
class APIResponseError(APIResponse):
    """에러 응답 래퍼 클래스"""
    
    def __init__(self, status_code: int, error_text: str):
        """
        Args:
            status_code: HTTP 상태 코드
            error_text: 에러 메시지
        """
        self.status_code = status_code
        self.error_text = error_text
        self._error_code = str(status_code)
        self._error_message = error_text
    
    def is_ok(self) -> bool:
        """항상 False"""
        return False
    
    def get_error_code(self) -> str:
        return self._error_code
    
    def get_error_message(self) -> str:
        return self._error_message
    
    def get_body(self):
        """빈 Body 객체 반환"""
        class EmptyBody:
            def __getattr__(self, name):
                return None
        return EmptyBody()
    
    def get_header(self):
        """빈 Header 객체 반환"""
        class EmptyHeader:
            tr_cont = ""
            def __getattr__(self, name):
                return ""
        return EmptyHeader()
    
    def print_all(self) -> None:
        print("=== ERROR RESPONSE ===")
        print(f"Status Code: {self.status_code}")
        print(f"Error Message: {self.error_text}")
        print("=" * 22)
    
    def print_error(self, url: str = "") -> None:
        print(f"Error Code: {self.status_code} | {self.error_text}")
        if url:
            print(f"URL: {url}")


class KISHttpClient:
    """KIS API HTTP 클라이언트"""
    
    
    def __init__(self, config, debug: bool = False, smart_sleep: float = 0.1):
        """
        Args:
            config: KISConfig 인스턴스
            debug: 디버그 모드
            smart_sleep: Rate limit 대기 시간
        """
        self.config = config
        self.debug = debug
        self.smart_sleep_time = smart_sleep
    
    def get_base_headers(self) -> dict:
        """기본 헤더 반환 (토큰 포함)"""
        env = self.config.get_env()
        headers = self.config.get_base_headers()
        
        if env and env.my_token:
            headers["authorization"] = f"Bearer {env.my_token}"
            headers["appkey"] = env.my_app
            headers["appsecret"] = env.my_sec
        
        return copy.deepcopy(headers)
    
    def set_hash_key(self, headers: dict, params: dict) -> None:
        """
        주문 Hash key 설정
        
        Args:
            headers: HTTP 헤더
            params: POST 파라미터
        """
        url = f"{self.config.get_env().my_url}/uapi/hashkey"
        
        response = requests.post(
            url,
            data=json.dumps(params),
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            headers["hashkey"] = data["HASH"]
        else:
            logging.error(f"Hash key 발급 실패: {response.status_code}")
    
    def smart_sleep(self) -> None:
        """Rate limit 대기"""
        if self.debug:
            logging.info(f"[RateLimit] Sleeping {self.smart_sleep_time}s")
        
        time.sleep(self.smart_sleep_time)
    
    def fetch(
        self,
        api_url: str,
        api_id: str,
        header_json: dict = None,
        params: Dict[str, Any] = None,
        additional_headers: Dict[str, str] = None,
        method: str = "GET",
        use_hash: bool = False
    ) -> APIResponse:
        """
        API 호출
        
        Args:
            api_url: API 엔드포인트
            api_id: 거래 ID
            header_json: API 전용 헤더 매핑
            params: 요청 파라미터
            additional_headers: 추가 헤더
            method: HTTP 메서드 ("GET" 또는 "POST")
            use_hash: Hash key 사용 여부
        
        Returns:
            APIResponse 객체
        """
        if params is None:
            params = {}
        
        # URL 생성
        # URL 생성
        url = f"{self.config.get_env().my_url}{api_url}"
        
        # 헤더 생성
        headers = self.get_base_headers()
        
        # 매핑된 헤더들을 병합 (tr_id, tr_cont 등)
        if header_json:
            for k, v in header_json.items():
                headers[k.lower()] = str(v)
            
            # TR ID 변환 (모의투자) - 만약 header_json에서 tr_id가 주어졌을 때
            if "tr_id" in headers and headers["tr_id"][0] in ("T", "J", "C") and self.config.is_paper_trading:
                headers["tr_id"] = "V" + headers["tr_id"][1:]
        
        # 추가 헤더
        if additional_headers:
            headers.update(additional_headers)
        
        # 디버그 출력
        if self.debug:
            print("< Sending Request >")
            print(f"URL: {url}")
            print(f"API_ID: {api_id}")
            print(f"Headers: {headers}")
            print(f"Params: {params}")
        
        # 요청 실행
        try:
            if method.upper() == "POST":
                if use_hash:
                    self.set_hash_key(headers, params)
                
                response = requests.post(
                    url,
                    headers=headers,
                    data=json.dumps(params)
                )
            else:  # GET
                response = requests.get(
                    url,
                    headers=headers,
                    params=params
                )
            
            # 응답 처리
            if response.status_code == 200:
                api_response = APIResponse(response)
                
                if self.debug:
                    api_response.print_all()
                
                return api_response
            
            else:
                error_msg = f"Error Code: {response.status_code} | {response.text}"
                logging.error(error_msg)
                return APIResponseError(response.status_code, response.text)
        
        except Exception as e:
            error_msg = f"Request failed: {e}"
            logging.error(error_msg)
            return APIResponseError(500, error_msg)



