"""
Query display_board_top definition from DB
"""
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import DatabaseManager
from app.models import APIDefinition, ParameterDefinition
from sqlmodel import select

# Absolute path to DB
db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "kis_api.db")
db = DatabaseManager(db_path)

with db.get_session() as session:
    # Get API definition
    statement = select(APIDefinition).where(APIDefinition.program_name == "display_board_top")
    api_def = session.exec(statement).first()
    
    if api_def:
        print(f"Program: {api_def.program_name}")
        print(f"URL: {api_def.api_url}")
        print(f"TR_ID: {api_def.tr_id}")
        
        # Get parameters
        params = session.exec(select(ParameterDefinition).where(ParameterDefinition.api_id == api_def.id)).all()
        for p in params:
            print(f"Param: {p.param_name}, Required: {p.is_required}, Default: {p.default_value}")
    else:
        print("display_board_top definition not found in DB")
