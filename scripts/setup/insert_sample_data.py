"""
insert_sample_data.py - 샘플 데이터 적재
"""

import os
import logging
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.database import DatabaseManager
from app.config import DB_PATH, DB_TYPE
from scripts.log_setup import setup_logging

setup_logging()

def insert_data():
    """샘플 데이터 적재"""
    
    # Absolute path to DB
    db_path = DB_PATH
    
    if DB_TYPE == "sqlite" and not os.path.exists(db_path):
        print(f"DB 파일이 존재하지 않습니다: {db_path}")
        print("먼저 init_database.py를 실행하여 테이블을 생성하세요.")
        return

    db = DatabaseManager()
    
    print("="*80)
    print("샘플 데이터 적재")
    print("="*80)
    
    # 1. stock_price
    print("\n[1] stock_price")
    try:
        db.add_api_mst(
            api_id="FHKST01010100",
            api_name="stock_price",
            api_type="HTTP",
            api_url="/uapi/domestic-stock/v1/quotations/inquire-price",
            header_json={"tr_id": "FHKST01010100"},
            description="주식 현재가 시세",
            output_table_name="stock_price"
            
        )
        
        db.add_api_param(
            api_id="FHKST01010100",
            param_name="FID_COND_MRKT_DIV_CODE",
            is_required=True,
            allowed_values="J,K",
            description="시장 분류 (J:주식, K:ETF)"
        )
        
        db.add_api_param(
            api_id="FHKST01010100",
            param_name="FID_INPUT_ISCD",
            is_required=True,
            min_length=6,
            max_length=6,
            description="종목 코드 (6자리)"
        )
        
        db.add_api_job_mst(
            job_id="job_stock_price_01",
            api_id="FHKST01010100",
            params={
                "FID_COND_MRKT_DIV_CODE": "J",
                "FID_INPUT_ISCD": "005930"
            },
            description="삼성전자",
            is_active=True,
            save_mode="overwrite"
        )
    except Exception as e:
        print(f"⚠ stock_price 데이터 적재 중 오류 (이미 존재할 수 있음): {e}")
    
    # 2. daily_price
    print("\n[2] daily_price")
    try:
        db.add_api_mst(
            api_id="FHKST01010400",
            api_name="daily_price",
            api_type="HTTP",
            api_url="/uapi/domestic-stock/v1/quotations/inquire-daily-price",
            header_json={"tr_id": "FHKST01010400"},
            description="주식 일별 시세",
            output_table_name="daily_price",
            
        )
        
        db.add_api_param(
            api_id="FHKST01010400",
            param_name="FID_COND_MRKT_DIV_CODE",
            is_required=True,
            allowed_values="J,K",
            description="시장 분류"
        )
        
        db.add_api_param(
            api_id="FHKST01010400",
            param_name="FID_INPUT_ISCD",
            is_required=True,
            min_length=6,
            max_length=6,
            description="종목 코드"
        )
        
        db.add_api_param(
            api_id="FHKST01010400",
            param_name="FID_PERIOD_DIV_CODE",
            is_required=False,
            default_value="D",
            allowed_values="D,W,M",
            description="기간 (D:일, W:주, M:월)"
        )
        
        db.add_api_param(
            api_id="FHKST01010400",
            param_name="FID_ORG_ADJ_PRC",
            is_required=False,
            default_value="0",
            allowed_values="0,1",
            description="수정주가 (0:미수정, 1:수정)"
        )
        
        db.add_api_job_mst(
            job_id="job_daily_price_01",
            api_id="FHKST01010400",
            params={
                "FID_COND_MRKT_DIV_CODE": "J",
                "FID_INPUT_ISCD": "000660",
                "FID_PERIOD_DIV_CODE": "D",
                "FID_ORG_ADJ_PRC": "0"
            },
            description="SK하이닉스 일봉",
            is_active=True,
            save_mode="overwrite"
        )
    except Exception as e:
        print(f"⚠ daily_price 데이터 적재 중 오류: {e}")

    # 3. display_board_top
    print("\n[3] display_board_top")
    try:
        db.add_api_mst(
            api_id="FHPIF05030000",
            api_name="display_board_top",
            api_type="HTTP",
            api_url="/uapi/domestic-futureoption/v1/quotations/display-board-top",
            header_json={"tr_id": "FHPIF05030000"},
            description="국내선물옵션_상단바시세",
            output_table_name="display_board_top",
            
        )
        
        db.add_api_param(
            api_id="FHPIF05030000",
            param_name="FID_COND_MRKT_DIV_CODE",
            is_required=True,
            description="조건 시장 분류 코드 (ex. F)"
        )

        db.add_api_param(
            api_id="FHPIF05030000",
            param_name="FID_INPUT_ISCD",
            is_required=True,
            description="입력 종목코드 (ex. 101V06)"
        )

        db.add_api_job_mst(
            job_id="job_display_board_top_01",
            api_id="FHPIF05030000",
            params={
                "FID_COND_MRKT_DIV_CODE": "F",
                "FID_INPUT_ISCD": "A01603",
            },
            description="선물 기초자산",
            is_active=True,
            save_mode="overwrite"
        )
    except Exception as e:
        print(f"⚠ display_board_top 데이터 적재 중 오류: {e}")

    
    print("\n" + "="*80)
    print("✓ 데이터 적재 완료")
    print("="*80)


if __name__ == "__main__":
    insert_data()
