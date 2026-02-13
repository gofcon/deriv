# -*- coding: utf-8 -*-
"""
kis_auth.py - KIS API 인증 관리
- 토큰 발급 및 관리
- 토큰 저장/로드
- 자동 재인증
"""

import os
import json
import logging
from datetime import datetime
from typing import Optional

import requests
import yaml

from . import kis_config


class KISAuthManager:
    """KIS API 인증 관리 클래스"""
    
    
    def __init__(self, config):
        """
        Args:
            config: KISConfig 인스턴스
        """
        self.config = config
        self.token_file = os.path.join(
            self.config.config_root,
            f"KIS{datetime.today().strftime('%Y%m%d')}"
        )
        
        # 토큰 파일 생성 (없으면)
        if not os.path.exists(self.token_file):
            try:
                with open(self.token_file, "w+") as f:
                    pass
            except Exception as e:
                logging.warning(f"Failed to create token file: {e}")
        
        # 마지막 인증 시간
        self.last_auth_time = datetime.now()
    
    def save_token(self, token: str, expired: str) -> None:
        """
        토큰 저장
        
        Args:
            token: 액세스 토큰
            expired: 만료 시간 (YYYY-MM-DD HH:MM:SS)
        """
        valid_date = datetime.strptime(expired, "%Y-%m-%d %H:%M:%S")
        
        try:
            with open(self.token_file, "w", encoding="utf-8") as f:
                f.write(f"token: {token}\n")
                f.write(f"valid-date: {valid_date}\n")
            
            logging.info(f"토큰 저장 완료: {valid_date}")
        except Exception as e:
            logging.error(f"Failed to save token: {e}")
    
    def read_token(self) -> Optional[str]:
        """
        저장된 토큰 읽기
        
        Returns:
            유효한 토큰 또는 None
        """
        try:
            if not os.path.exists(self.token_file):
                return None
                
            with open(self.token_file, encoding="UTF-8") as f:
                token_data = yaml.load(f, Loader=yaml.FullLoader)
            
            if not token_data:
                return None

            # 만료 시간 확인
            expired = datetime.strftime(token_data["valid-date"], "%Y-%m-%d %H:%M:%S")
            now = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            
            if expired > now:
                logging.info(f"기존 토큰 사용 (만료: {expired})")
                return token_data["token"]
            else:
                logging.info(f"토큰 만료: {expired}")
                return None
        
        except Exception as e:
            logging.warning(f"토큰 읽기 실패: {e}")
            return None
    
    def authenticate(
        self,
        server: str = "prod",
        product: str = None,
        force_new: bool = False
    ) -> str:
        """
        인증 토큰 발급
        
        Args:
            server: "prod" 또는 "vps"
            product: 상품 코드
            force_new: 강제 재발급 여부
        
        Returns:
            액세스 토큰
        """
        # 설정
        cfg = self.config.config
        if product is None:
            product = cfg["my_prod"]
        
        # 앱키/시크릿 선택
        if server == "prod":
            app_key = cfg["my_app"]
            app_secret = cfg["my_sec"]
        elif server == "vps":
            app_key = cfg["paper_app"]
            app_secret = cfg["paper_sec"]
        else:
            raise ValueError(f"Invalid server: {server}")
        
        # 기존 토큰 확인
        if not force_new:
            saved_token = self.read_token()
            if saved_token:
                # 환경 설정
                self.config.setup_environment(saved_token, server, product)
                self.last_auth_time = datetime.now()
                return saved_token
        
        # 새 토큰 발급
        logging.info(f"새 토큰 발급 중... (server={server})")
        
        url = f"{cfg[server]}/oauth2/tokenP"
        headers = self.config.get_base_headers()
        params = {
            "grant_type": "client_credentials",
            "appkey": app_key,
            "appsecret": app_secret
        }
        
        response = requests.post(url, data=json.dumps(params), headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            token = data["access_token"]
            expired = data["access_token_token_expired"]
            
            # 토큰 저장
            self.save_token(token, expired)
            
            # 환경 설정
            self.config.setup_environment(token, server, product)
            
            # 시간 기록
            self.last_auth_time = datetime.now()
            
            logging.info("✓ 토큰 발급 성공")
            return token
        
        else:
            error_msg = f"토큰 발급 실패: {response.status_code} - {response.text}"
            logging.error(error_msg)
            raise Exception(error_msg)
    
    def re_authenticate(self, server: str = "prod", product: str = None) -> None:
        """
        토큰 재발급 (24시간 경과 시)
        
        Args:
            server: "prod" 또는 "vps"
            product: 상품 코드
        """
        elapsed = (datetime.now() - self.last_auth_time).seconds
        
        if elapsed >= 86400:  # 24시간
            logging.info(f"토큰 재발급 (경과 시간: {elapsed}초)")
            self.authenticate(server, product, force_new=True)
    
    def get_auth_headers(self) -> dict:
        """
        인증 헤더 반환
        
        Returns:
            인증 정보가 포함된 헤더
        """
        env = self.config.get_env()
        headers = self.config.get_base_headers()
        
        headers["authorization"] = f"Bearer {env.my_token}"
        headers["appkey"] = env.my_app
        headers["appsecret"] = env.my_sec
        
        return headers



