"""Test Oracle ADB connection via SQLAlchemy creator pattern (config.py)"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import get_engine_kwargs, DB_TYPE
from sqlmodel import create_engine, text

print(f"DB_TYPE: {DB_TYPE}")

kwargs = get_engine_kwargs()
url = kwargs.pop("url")
print(f"URL: {url}")

engine = create_engine(url, **kwargs)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT SYSDATE FROM DUAL"))
        row = result.fetchone()
        print(f"Connection successful! DB time: {row[0]}")
except Exception as e:
    print(f"Connection failed: {e}")
