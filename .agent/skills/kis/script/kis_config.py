# -*- coding: utf-8 -*-
"""
kis_config.py - KIS API 설정 및 환경 관리
- 설정 파일 로드
- 환경 변수 관리
- 계좌 정보 관리
"""

import os
from collections import namedtuple
from datetime import datetime
import yaml


class KISConfig:
    """KIS API 설정 관리 클래스"""
    
    def __init__(self, config_dir: str = None):
        """
        Args:
            config_dir: 설정 파일 디렉토리 (기본: ~/KIS/config)
        """
        if config_dir is None:
            self.config_root = os.path.join(os.path.expanduser("~"), "KIS", "config")
        else:
            self.config_root = config_dir
        
        # 설정 파일 로드
        config_file = os.path.join(self.config_root, "kis_devlp.yaml")
        with open(config_file, encoding="UTF-8") as f:
            self._cfg = yaml.load(f, Loader=yaml.FullLoader)
        
        # 환경 변수
        self._env = None
        self._is_paper = False
        self._smart_sleep = 0.1
    
    @property
    def config(self):
        """설정 딕셔너리"""
        return self._cfg
    
    @property
    def is_paper_trading(self):
        """모의투자 여부"""
        return self._is_paper
    
    @property
    def smart_sleep_time(self):
        """Rate limit 대기 시간"""
        return self._smart_sleep
    
    def get_env(self):
        """현재 환경 정보 반환"""
        return self._env
    
    def set_env(
        self,
        app_key: str,
        app_secret: str,
        account: str,
        product: str,
        hts_id: str,
        token: str,
        url: str,
        url_ws: str
    ):
        """
        환경 설정
        
        Args:
            app_key: 앱 키
            app_secret: 앱 시크릿
            account: 계좌번호 (8자리)
            product: 상품코드 (2자리)
            hts_id: HTS ID
            token: 인증 토큰
            url: REST API URL
            url_ws: WebSocket URL
        """
        KISEnv = namedtuple(
            "KISEnv",
            ["my_app", "my_sec", "my_acct", "my_prod", "my_htsid", 
             "my_token", "my_url", "my_url_ws"]
        )
        
        self._env = KISEnv(
            my_app=app_key,
            my_sec=app_secret,
            my_acct=account,
            my_prod=product,
            my_htsid=hts_id,
            my_token=token,
            my_url=url,
            my_url_ws=url_ws
        )
    
    def setup_environment(
        self,
        token: str = None,
        server: str = "prod",
        product: str = None
    ):
        """
        환경 설정 (간편 버전)
        
        Args:
            token: 인증 토큰
            server: 서버 종류 ("prod" 또는 "vps")
            product: 상품 코드 (기본값: 설정 파일에서 가져옴)
        """
        if product is None:
            product = self._cfg["my_prod"]
        
        # 서버별 설정
        if server == "prod":  # 실전투자
            app_key = self._cfg["my_app"]
            app_secret = self._cfg["my_sec"]
            self._is_paper = False
            self._smart_sleep = 0.05
        elif server == "vps":  # 모의투자
            app_key = self._cfg["paper_app"]
            app_secret = self._cfg["paper_sec"]
            self._is_paper = True
            self._smart_sleep = 0.5
        else:
            raise ValueError(f"Invalid server: {server} (must be 'prod' or 'vps')")
        
        # 상품별 계좌번호 선택
        account = self._get_account(server, product)
        
        # HTS ID
        hts_id = self._cfg["my_htsid"]
        
        # URL
        url = self._cfg[server]
        url_ws = self._cfg["ops" if server == "prod" else "vops"]
        
        # 환경 설정
        self.set_env(
            app_key=app_key,
            app_secret=app_secret,
            account=account,
            product=product,
            hts_id=hts_id,
            token=token or "",
            url=url,
            url_ws=url_ws
        )
    
    def _get_account(self, server: str, product: str) -> str:
        """
        서버와 상품 코드에 따른 계좌번호 반환
        
        Args:
            server: "prod" 또는 "vps"
            product: 상품 코드 ("01", "03", "08", "22", "29")
        
        Returns:
            계좌번호 (8자리)
        """
        if server == "prod":
            if product == "01":  # 주식투자
                return self._cfg["my_acct_stock"]
            elif product in ("03", "08"):  # 선물옵션, 해외선물옵션
                return self._cfg["my_acct_future"]
            elif product in ("22", "29"):  # 연금저축, 퇴직연금
                return self._cfg["my_acct_stock"]
            else:
                raise ValueError(f"Unknown product: {product}")
        
        elif server == "vps":
            if product == "01":  # 주식투자
                return self._cfg["my_paper_stock"]
            elif product == "03":  # 선물옵션
                return self._cfg["my_paper_future"]
            else:
                raise ValueError(f"Unknown product for vps: {product}")
        
        else:
            raise ValueError(f"Unknown server: {server}")
    
    def get_base_headers(self) -> dict:
        """기본 HTTP 헤더 반환"""
        return {
            "Content-Type": "application/json",
            "Accept": "text/plain",
            "charset": "UTF-8",
            "User-Agent": self._cfg["my_agent"],
        }


# 전역 설정 인스턴스 (하위 호환성)
_global_config = None


def get_global_config() -> KISConfig:
    """전역 설정 인스턴스 반환"""
    global _global_config
    if _global_config is None:
        _global_config = KISConfig()
    return _global_config


# 하위 호환성을 위한 함수들
def getEnv():
    """환경 정보 반환 (하위 호환)"""
    return get_global_config().config


def getTREnv():
    """거래 환경 정보 반환 (하위 호환)"""
    return get_global_config().get_env()


def isPaperTrading():
    """모의투자 여부 반환 (하위 호환)"""
    return get_global_config().is_paper_trading
