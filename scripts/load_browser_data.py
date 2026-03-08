import os
import sys
import logging

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import DatabaseManager
from scripts.log_setup import setup_logging

setup_logging()

def load_sample_browser_data():
    """
    브라우저 스크래핑을 위한 샘플 BrowserMst 및 BrowserJobMst 데이터 생성
    """
    db = DatabaseManager()
    
    # 1. BrowserMst: KIS 국내선물옵션 마스터정보 스크래핑 템플릿 예시
    browser_mst_1 = db.add_browser_mst(
        browser_id="browser_kis_dom_future",
        browser_name="KIS 국내선물옵션 마스터 브라우저 스크래퍼",
        target_url="https://some-example-kis-site.com/futures/{product_code}", # 예시 URL
        output_table_name="KIS_DOM_FUTURE_MST",
        selector_json={
            "prod_name": {"selector": "#product-name", "attribute": "text"},
            "price": {"selector": ".current-price", "attribute": "text"},
        },
        behavior_json=[
            {"action": "wait_for_selector", "selector": "#product-name"},
        ],
        human_like=True,
        description="KIS 국내 선물/옵션 종목 정보 스크래핑 (브라우저 방식)"
    )
    
    # 2. BrowserJobMst: 실제 실행을 위한 작업 인스턴스 (선물 종목)
    db.add_browser_job_mst(
        job_id="job_browser_kis_future_01",
        browser_id="browser_kis_dom_future",
        description="코스피200 선물 최근월물 브라우저 스크래핑",
        params={
            "product_code": "101V3000" # KOSPI200 F 202403 예시
        },
        is_active=True,
        save_mode="append",
        execution_cycle="daily"
    )

    # 3. BrowserMst: KRX ISIN 검색 스크래핑 템플릿 예시
    browser_mst_krx = db.add_browser_mst(
        browser_id="browser_krx_isin",
        browser_name="KRX ISIN 검색 브라우저 스크래퍼",
        target_url="https://isin.krx.co.kr/srch/srch.do?method=srchList",
        output_table_name="BROWSER_RST",
        selector_json={
            "isin_code": {"selector": "#dataTb > tbody > tr > td:nth-child(2)", "attribute": "text", "is_list": True},
            "item_name": {"selector": "#dataTb > tbody > tr > td:nth-child(3)", "attribute": "text", "is_list": True}
        },
        behavior_json=[
            {"action": "wait", "value": 2000},
            {"action": "input", "selector": "input[name='isur_nm1']", "value": "{search_keyword}"},
            {"action": "input", "selector": "input[name='std_cd_grnt_start_dd']", "value": "{start_date}"},
            {"action": "input", "selector": "input[name='std_cd_grnt_end_dd']", "value": "{end_date}"},
            {"action": "click", "selector": "a.btn-sprite.type-02.vmiddle:nth-child(2)"}, 
            {"action": "wait", "value": 3000}
        ],
        pagination_json={
            "type": "click_next",
            "next_selector": 'a:has(img[src="/img/btn/btn-next.gif"])',
            "wait_after": 2000,
            "max_pages": 5
        },
        human_like=True,
        description="KRX ISIN 종목 정보 스크래핑"
    )

    # 4. BrowserJobMst: KRX ISIN 실제 실행을 위한 작업 인스턴스
    db.add_browser_job_mst(
        job_id="job_browser_krx_isin_01",
        browser_id="browser_krx_isin",
        description="KRX ISIN 검색 (국고채, 최근 1년)",
        params={
            "search_keyword": "KR1",
            "start_date": "2025-01-01",
            "end_date": "2026-02-01"
        },
        is_active=True,
        save_mode="append",
        execution_cycle="daily"
    )

    logging.info("==========================================")
    logging.info("✓ 브라우저 샘플 데이터 적재 완료")
    logging.info("==========================================")

if __name__ == "__main__":
    load_sample_browser_data()
