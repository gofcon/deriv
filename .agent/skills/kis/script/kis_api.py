# -*- coding: utf-8 -*-
"""
kis_api.py - KIS API 통합 모듈
기존 kis_auth.py와 동일한 인터페이스 제공 (하위 호환)
"""

# 설정 관리
from kis_config import (
    KISConfig,
    get_global_config,
    getEnv,
    getTREnv,
    isPaperTrading
)

# 인증 관리
from kis_auth_new import (
    KISAuthManager,
    get_global_auth_manager,
    auth,
    reAuth,
    save_token,
    read_token
)

# HTTP 요청/응답
from kis_http import (
    APIResponse,
    APIResponseError,
    KISHttpClient,
    get_global_http_client,
    _url_fetch,
    smart_sleep,
    # 별칭
    APIResp,
    APIRespError
)

# WebSocket
from kis_websocket import (
    KISWebSocket,
    KISWebSocketAuth,
    aes_cbc_base64_decrypt,
    parse_system_response,
    add_open_map,
    add_data_map,
    # 하위 호환
    auth_ws,
    reAuth_ws,
    system_resp,
    aes_cbc_base64_dec,
    data_fetch,
    open_map,
    data_map
)


__all__ = [
    # 설정
    "KISConfig",
    "get_global_config",
    "getEnv",
    "getTREnv",
    "isPaperTrading",
    
    # 인증
    "KISAuthManager",
    "get_global_auth_manager",
    "auth",
    "reAuth",
    "save_token",
    "read_token",
    
    # HTTP
    "APIResponse",
    "APIResponseError",
    "KISHttpClient",
    "get_global_http_client",
    "_url_fetch",
    "smart_sleep",
    "APIResp",
    "APIRespError",
    
    # WebSocket
    "KISWebSocket",
    "KISWebSocketAuth",
    "aes_cbc_base64_decrypt",
    "parse_system_response",
    "add_open_map",
    "add_data_map",
    "auth_ws",
    "reAuth_ws",
    "system_resp",
    "aes_cbc_base64_dec",
    "data_fetch",
    "open_map",
    "data_map",
]


def initialize(server="prod", product=None, debug=False):
    """
    초기화 (편의 함수)
    
    Args:
        server: "prod" 또는 "vps"
        product: 상품 코드
        debug: 디버그 모드
    
    Returns:
        인증 토큰
    """
    # HTTP 클라이언트 디버그 설정
    client = get_global_http_client()
    client.debug = debug
    
    # 인증
    token = auth(server, product)
    
    return token


def get_client(debug=False) -> KISHttpClient:
    """
    HTTP 클라이언트 가져오기
    
    Args:
        debug: 디버그 모드
    
    Returns:
        KISHttpClient 인스턴스
    """
    client = get_global_http_client()
    client.debug = debug
    return client


def get_websocket(api_url: str, max_retries=3) -> KISWebSocket:
    """
    WebSocket 클라이언트 생성
    
    Args:
        api_url: WebSocket API 경로
        max_retries: 최대 재시도 횟수
    
    Returns:
        KISWebSocket 인스턴스
    """
    return KISWebSocket(api_url, max_retries)


# 버전 정보
__version__ = "2.0.0"
__author__ = "KIS API Team"
__description__ = "Korea Investment & Securities API Client (Refactored)"
