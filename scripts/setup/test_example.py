"""
config.py - Application configuration
"""

import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Load .env from project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# print(os.path.abspath(__file__))
# print(BASE_DIR)
# print(os.getcwd())

# 현재 파일 위치 기준 상위 폴더(root)
# from pathlib import Path
# root_dir = Path(__file__).resolve().parent
# print(root_dir)


# Database type: 'sqlite' or 'oracle'
DB_TYPE = os.getenv("DB_TYPE", "sqlite")

# SQLite settings (fallback)
DB_PATH = os.path.join(BASE_DIR, "data", "kis_api.db")

# Oracle ADB settings
ORACLE_USER = os.getenv("ORACLE_USER", "")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD", "")
ORACLE_DSN = os.getenv("ORACLE_DSN", "")
TNS_ADMIN = os.getenv("TNS_ADMIN", "")
WALLET_PASSWORD = os.getenv("WALLET_PASSWORD", "")

# Log directory
LOG_DIR = os.path.join(BASE_DIR, "logs")

