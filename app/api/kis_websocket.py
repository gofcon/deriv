# -*- coding: utf-8 -*-
"""
kis_websocket.py - KIS API WebSocket 처리
- WebSocket 인증
- 실시간 데이터 수신
- 암호화 처리
- 구독 관리
"""

import asyncio
import json
import logging
import copy
from base64 import b64decode
from collections import namedtuple
from collections.abc import Callable
from datetime import datetime
from io import StringIO
from typing import Dict, List, Optional

import pandas as pd
import requests
import websockets
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from .kis_config import get_global_config, getTREnv


class KISWebSocketAuth:
    """WebSocket 인증 관리"""
    
    def __init__(self):
        self.config = get_global_config()
        self.approval_key = None
        self.last_auth_time = None
        self._base_headers = {"content-type": "utf-8"}
    
    def authenticate(self, server: str = "prod", product: str = None) -> str:
        """
        WebSocket 인증
        
        Args:
            server: "prod" 또는 "vps"
            product: 상품 코드
        
        Returns:
            Approval key
        """
        cfg = self.config.config
        
        if product is None:
            product = cfg["my_prod"]
        
        # 앱키/시크릿
        if server == "prod":
            app_key = cfg["my_app"]
            app_secret = cfg["my_sec"]
        elif server == "vps":
            app_key = cfg["paper_app"]
            app_secret = cfg["paper_sec"]
        else:
            raise ValueError(f"Invalid server: {server}")
        
        # 인증 요청
        url = f"{cfg[server]}/oauth2/Approval"
        params = {
            "grant_type": "client_credentials",
            "appkey": app_key,
            "secretkey": app_secret  # WebSocket은 secretkey 사용
        }
        
        headers = self.config.get_base_headers()
        response = requests.post(url, data=json.dumps(params), headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            self.approval_key = data["approval_key"]
            self._base_headers["approval_key"] = self.approval_key
            self.last_auth_time = datetime.now()
            
            # 환경 설정
            self.config.setup_environment(None, server, product)
            
            logging.info("✓ WebSocket 인증 성공")
            return self.approval_key
        
        else:
            error_msg = f"WebSocket 인증 실패: {response.status_code}"
            logging.error(error_msg)
            raise Exception(error_msg)
    
    def re_authenticate(self, server: str = "prod", product: str = None) -> None:
        """재인증 (24시간 경과 시)"""
        if self.last_auth_time is None:
            self.authenticate(server, product)
            return
        
        elapsed = (datetime.now() - self.last_auth_time).seconds
        if elapsed >= 86400:
            logging.info(f"WebSocket 재인증 (경과: {elapsed}초)")
            self.authenticate(server, product)
    
    def get_headers(self) -> dict:
        """인증 헤더 반환"""
        return copy.deepcopy(self._base_headers)


def aes_cbc_base64_decrypt(key: str, iv: str, cipher_text: str) -> str:
    """
    AES CBC 복호화
    
    Args:
        key: 암호화 키
        iv: 초기화 벡터
        cipher_text: Base64 암호문
    
    Returns:
        복호화된 텍스트
    """
    if key is None or iv is None:
        raise ValueError("Key and IV cannot be None")
    
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    decrypted = unpad(cipher.decrypt(b64decode(cipher_text)), AES.block_size)
    
    return decrypted.decode("utf-8")


def parse_system_response(data: str) -> namedtuple:
    """
    시스템 응답 파싱
    
    Args:
        data: JSON 문자열
    
    Returns:
        시스템 메시지 namedtuple
    """
    json_data = json.loads(data)
    
    is_ping_pong = False
    is_unsub = False
    is_ok = False
    tr_msg = None
    tr_key = None
    encrypt = None
    iv = None
    ekey = None
    
    api_id = json_data["header"]["tr_id"]
    
    if api_id != "PINGPONG":
        tr_key = json_data["header"]["tr_key"]
        encrypt = json_data["header"]["encrypt"]
    
    if json_data.get("body") is not None:
        is_ok = json_data["body"]["rt_cd"] == "0"
        tr_msg = json_data["body"]["msg1"]
        
        # 복호화 키 추출
        if "output" in json_data["body"]:
            iv = json_data["body"]["output"]["iv"]
            ekey = json_data["body"]["output"]["key"]
        
        is_unsub = tr_msg[:5] == "UNSUB" if tr_msg else False
    else:
        is_ping_pong = api_id == "PINGPONG"
    
    SystemMessage = namedtuple(
        "SystemMessage",
        ["is_ok", "api_id", "tr_key", "is_unsub", "is_ping_pong",
         "tr_msg", "iv", "ekey", "encrypt"]
    )
    
    return SystemMessage(
        is_ok=is_ok,
        api_id=api_id,
        tr_key=tr_key,
        is_unsub=is_unsub,
        is_ping_pong=is_ping_pong,
        tr_msg=tr_msg,
        iv=iv,
        ekey=ekey,
        encrypt=encrypt
    )


class KISWebSocket:
    """KIS WebSocket 클라이언트"""
    
    def __init__(self, api_url: str, max_retries: int = 3):
        """
        Args:
            api_url: WebSocket API 경로
            max_retries: 최대 재시도 횟수
        """
        self.api_url = api_url
        self.max_retries = max_retries
        self.retry_count = 0
        
        self.on_result = None
        self.result_all_data = False
        
        # 구독 관리
        self.subscriptions: Dict[str, dict] = {}
        
        # 데이터 매핑
        self.data_map: Dict[str, dict] = {}
    
    def add_subscription(
        self,
        name: str,
        request_func: Callable,
        data: str | List[str],
        kwargs: dict = None
    ) -> None:
        """
        구독 추가
        
        Args:
            name: 구독 이름
            request_func: 요청 생성 함수
            data: 구독 데이터
            kwargs: 추가 인자
        """
        if name not in self.subscriptions:
            self.subscriptions[name] = {
                "func": request_func,
                "items": [],
                "kwargs": kwargs
            }
        
        if isinstance(data, list):
            self.subscriptions[name]["items"].extend(data)
        elif isinstance(data, str):
            self.subscriptions[name]["items"].append(data)
    
    def add_data_mapping(
        self,
        api_id: str,
        columns: List[str] = None,
        encrypt: str = None,
        key: str = None,
        iv: str = None
    ) -> None:
        """
        데이터 매핑 추가
        
        Args:
            api_id: 거래 ID
            columns: 컬럼 리스트
            encrypt: 암호화 여부
            key: 암호화 키
            iv: 초기화 벡터
        """
        if api_id not in self.data_map:
            self.data_map[api_id] = {
                "columns": [],
                "encrypt": False,
                "key": None,
                "iv": None
            }
        
        if columns is not None:
            self.data_map[api_id]["columns"] = columns
        if encrypt is not None:
            self.data_map[api_id]["encrypt"] = encrypt
        if key is not None:
            self.data_map[api_id]["key"] = key
        if iv is not None:
            self.data_map[api_id]["iv"] = iv
    
    async def _subscriber(self, ws: websockets.ClientConnection):
        """메시지 수신 처리"""
        async for raw_message in ws:
            logging.info(f"Received message: {raw_message}")
            
            show_result = False
            df = pd.DataFrame()
            api_id = None
            
            # 데이터 메시지 (0 또는 1로 시작)
            if raw_message[0] in ["0", "1"]:
                parts = raw_message.split("|")
                
                if len(parts) < 4:
                    raise ValueError("Invalid data message format")
                
                api_id = parts[1]
                data_mapping = self.data_map.get(api_id, {})
                data = parts[3]
                
                # 복호화
                if data_mapping.get("encrypt") == "Y":
                    data = aes_cbc_base64_decrypt(
                        data_mapping["key"],
                        data_mapping["iv"],
                        data
                    )
                
                # DataFrame 변환
                df = pd.read_csv(
                    StringIO(data),
                    header=None,
                    sep="^",
                    names=data_mapping.get("columns", []),
                    dtype=object
                )
                
                show_result = True
            
            # 시스템 메시지
            else:
                sys_msg = parse_system_response(raw_message)
                api_id = sys_msg.api_id
                
                # 데이터 매핑 업데이트
                self.add_data_mapping(
                    api_id=sys_msg.api_id,
                    encrypt=sys_msg.encrypt,
                    key=sys_msg.ekey,
                    iv=sys_msg.iv
                )
                
                # PINGPONG 처리
                if sys_msg.is_ping_pong:
                    print(f"### RECV [PINGPONG] [{raw_message}]")
                    await ws.pong(raw_message)
                    print(f"### SEND [PINGPONG] [{raw_message}]")
                
                if self.result_all_data:
                    show_result = True
            
            # 결과 콜백
            if show_result and self.on_result is not None:
                self.on_result(ws, api_id, df, self.data_map.get(api_id, {}))
    
    async def _runner(self):
        """WebSocket 연결 및 실행"""
        if len(self.subscriptions) > 40:
            raise ValueError("Maximum 40 subscriptions allowed")
        
        url = f"{getTREnv().my_url_ws}{self.api_url}"
        
        while self.retry_count < self.max_retries:
            try:
                async with websockets.connect(url) as ws:
                    # 구독 요청
                    for name, sub in self.subscriptions.items():
                        await self.send_multiple(
                            ws,
                            sub["func"],
                            "1",  # 구독
                            sub["items"],
                            sub["kwargs"]
                        )
                    
                    # 메시지 수신
                    await asyncio.gather(self._subscriber(ws))
            
            except Exception as e:
                logging.error(f"Connection exception: {e}")
                self.retry_count += 1
                await asyncio.sleep(1)
    
    @classmethod
    async def send(
        cls,
        ws: websockets.ClientConnection,
        request_func: Callable,
        tr_type: str,
        data: str,
        kwargs: dict = None
    ):
        """
        메시지 전송
        
        Args:
            ws: WebSocket 연결
            request_func: 요청 생성 함수
            tr_type: 거래 타입 ("1": 구독, "2": 구독 해제)
            data: 데이터
            kwargs: 추가 인자
        """
        k = kwargs or {}
        message, columns = request_func(tr_type, data, **k)
        
        # 데이터 매핑 추가 (전역 방식)
        global data_map
        add_data_map(api_id=message["body"]["input"]["tr_id"], columns=columns)
        
        logging.info(f"Send message: {json.dumps(message)}")
        await ws.send(json.dumps(message))
    
    async def send_multiple(
        self,
        ws: websockets.ClientConnection,
        request_func: Callable,
        tr_type: str,
        data: str | List[str],
        kwargs: dict = None
    ):
        """다중 메시지 전송"""
        if isinstance(data, str):
            await self.send(ws, request_func, tr_type, data, kwargs)
        elif isinstance(data, list):
            for item in data:
                await self.send(ws, request_func, tr_type, item, kwargs)
        else:
            raise ValueError("Data must be str or list")
    
    def start(
        self,
        on_result: Callable,
        result_all_data: bool = False
    ):
        """
        WebSocket 시작
        
        Args:
            on_result: 결과 콜백 함수
            result_all_data: 모든 데이터 결과 전달 여부
        """
        self.on_result = on_result
        self.result_all_data = result_all_data
        
        try:
            asyncio.run(self._runner())
        except KeyboardInterrupt:
            print("Closing by KeyboardInterrupt")


# 전역 변수 (하위 호환)
open_map: dict = {}
data_map: dict = {}


def add_open_map(
    name: str,
    request: Callable,
    data: str | List[str],
    kwargs: dict = None
):
    """구독 추가 (하위 호환)"""
    global open_map
    
    if name not in open_map:
        open_map[name] = {
            "func": request,
            "items": [],
            "kwargs": kwargs
        }
    
    if isinstance(data, list):
        open_map[name]["items"].extend(data)
    elif isinstance(data, str):
        open_map[name]["items"].append(data)


def add_data_map(
    api_id: str,
    columns: List[str] = None,
    encrypt: str = None,
    key: str = None,
    iv: str = None
):
    """데이터 매핑 추가 (하위 호환)"""
    global data_map
    
    if api_id not in data_map:
        data_map[api_id] = {
            "columns": [],
            "encrypt": False,
            "key": None,
            "iv": None
        }
    
    if columns is not None:
        data_map[api_id]["columns"] = columns
    if encrypt is not None:
        data_map[api_id]["encrypt"] = encrypt
    if key is not None:
        data_map[api_id]["key"] = key
    if iv is not None:
        data_map[api_id]["iv"] = iv


# 하위 호환 함수들
def auth_ws(svr="prod", product=None):
    """WebSocket 인증 (하위 호환)"""
    auth_manager = KISWebSocketAuth()
    return auth_manager.authenticate(svr, product)


def reAuth_ws(svr="prod", product=None):
    """WebSocket 재인증 (하위 호환)"""
    auth_manager = KISWebSocketAuth()
    auth_manager.re_authenticate(svr, product)


def system_resp(data: str):
    """시스템 응답 파싱 (하위 호환)"""
    return parse_system_response(data)


def aes_cbc_base64_dec(key: str, iv: str, cipher_text: str):
    """AES 복호화 (하위 호환)"""
    return aes_cbc_base64_decrypt(key, iv, cipher_text)


def data_fetch(api_id: str, tr_type: str, params: dict, appendHeaders: dict = None) -> dict:
    """WebSocket 데이터 요청 생성 (하위 호환)"""
    auth_manager = KISWebSocketAuth()
    headers = auth_manager.get_headers()
    
    headers["tr_type"] = tr_type
    headers["custtype"] = "P"
    
    if appendHeaders:
        headers.update(appendHeaders)
    
    inp = {"tr_id": api_id}
    inp.update(params)
    
    return {
        "header": headers,
        "body": {"input": inp}
    }
