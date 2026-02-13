"""
Query output tables to verify data insertion
"""
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import DatabaseManager
from app.models import StockPrice, DailyPrice, DisplayBoardTop
from sqlmodel import select

# Absolute path to DB
db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "kis_api.db")
db = DatabaseManager(db_path)

with db.get_session() as session:
    # 1. StockPrice
    print("\n[1] StockPrice")
    results = session.exec(select(StockPrice)).all()
    print(f"Count: {len(results)}")
    if results:
        print(f"Sample (stck_prpr): {results[0].stck_prpr}")
        print(f"Created At: {results[0].created_at}")

    # 2. DailyPrice
    print("\n[2] DailyPrice")
    results = session.exec(select(DailyPrice)).all()
    print(f"Count: {len(results)}")
    if results:
        print(f"Sample (stck_clpr): {results[0].stck_clpr}")

    # 3. DisplayBoardTop
    print("\n[3] DisplayBoardTop")
    results = session.exec(select(DisplayBoardTop)).all()
    print(f"Count: {len(results)}")
    if results:
        # DisplayBoardTop fields might be empty if API response is empty/error
        # But main.py only inserts on success.
        print(f"Sample (unas_prpr): {results[0].unas_prpr}")
