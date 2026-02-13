"""
update_param_names.py - 기존 파라미터 이름을 대문자로 업데이트
"""

import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import DatabaseManager
from sqlmodel import select
from app.models import ParameterDefinition

# Absolute path to DB
db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "kis_api.db")
db = DatabaseManager(db_path)

with db.get_session() as session:
    # 모든 파라미터 정의 조회
    statement = select(ParameterDefinition)
    params = session.exec(statement).all()
    
    updated_count = 0
    for param in params:
        old_name = param.param_name
        new_name = old_name.upper()
        
        if old_name != new_name:
            param.param_name = new_name
            updated_count += 1
            print(f"Updated: {old_name} -> {new_name}")
    
    session.commit()
    print(f"\n총 {updated_count}개 파라미터 이름이 대문자로 업데이트되었습니다.")
