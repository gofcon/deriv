"""
config.py - Application configuration
"""

import os
from urllib.parse import quote_plus
import json
from dotenv import load_dotenv

# Load .env from project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

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


def get_engine_kwargs() -> dict:
    """
    create_engine()에 전달할 키워드 인자 반환.
    Oracle ADB의 경우 creator 패턴을 사용하여 wallet 파라미터를 전달.
    """
    if DB_TYPE == "oracle":
        import oracledb
        
        def oracle_creator():
            return oracledb.connect(
                user=ORACLE_USER,
                password=ORACLE_PASSWORD,
                dsn=ORACLE_DSN,
                config_dir=TNS_ADMIN,
                wallet_location=TNS_ADMIN,
                wallet_password=WALLET_PASSWORD
            )
        
        return {
            "url": "oracle+oracledb://",
            "creator": oracle_creator,
            "echo": False,
            "pool_pre_ping": True,
        }
    else:
        return {
            "url": f"sqlite:///{DB_PATH}",
            "echo": False,
        }
