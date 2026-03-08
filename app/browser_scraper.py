import os
import sys
import json
import logging
from typing import Dict, Any, Optional

from playwright.sync_api import sync_playwright

# DB Models
from app.models_gofcon import BrowserMst, BrowserJobMst
from app.database import DatabaseManager

class BrowserScraper:
    """
    Playwright 기반 브라우저 스크래퍼
    BrowserMst의 정의를 바탕으로 페이지를 로드하고, 
    BrowserJobMst의 파라미터를 활용하여 동적 스크래핑을 수행합니다.
    """
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        
    def execute_job(self, job: BrowserJobMst) -> Optional[Dict[str, Any]]:
        """작업 1건 실행 (단일 쓰레드 동기 방식)"""
        logging.info(f"▶ Browser 작업 시작: {job.job_id} (Target BrowserMst: {job.browser_id})")
        
        browser_mst = self.db.get_browser_mst(job.browser_id)
        if not browser_mst:
            logging.error(f"✕ Browser 정의를 찾을 수 없습니다: {job.browser_id}")
            return None
            
        params = job.params_json or {}
        
        try:
            with sync_playwright() as p:
                # 1. 브라우저 런칭
                browser_args = []
                # TODO: human_like 옵션 구성 (Stealth 등)
                
                browser = p.chromium.launch(
                    headless=True,
                    args=browser_args
                )
                
                context = browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                )
                
                page = context.new_page()
                
                # 2. URL 처리 (템플릿 변환)
                target_url = browser_mst.target_url
                for key, value in params.items():
                    target_url = target_url.replace(f"{{{key}}}", str(value))
                    
                logging.info(f"  - 페이지 이동: {target_url}")
                page.goto(target_url, wait_until="networkidle")
                
                # 3. Behavior JSON 실행 (클릭, 타이핑 등)
                behaviors = browser_mst.behavior_json or []
                self._execute_behaviors(page, behaviors, params)
                
                # 4. 데이터 추출 및 페이지네이션
                pagination = browser_mst.pagination_json or {}
                extracted_all = []
                
                page_count = 1
                
                # 최대 페이지 수 동적 계산
                max_pages = 1 # 기본값
                if "max_pages" in pagination:
                    max_pages = int(pagination.get("max_pages", 1))
                elif pagination.get("total_items_selector") and pagination.get("items_per_page"):
                    try:
                        total_text = page.inner_text(pagination.get("total_items_selector"))
                        import re
                        total_items = int(re.sub(r'[^0-9]', '', total_text))
                        items_per_page = int(pagination.get("items_per_page"))
                        
                        import math
                        max_pages = math.ceil(total_items / items_per_page)
                        logging.info(f"    동적 페이지 계산: 총 {total_items}건 / {items_per_page}건씩 = {max_pages} 페이지")
                    except Exception as e:
                        logging.warning(f"    동적 최대 페이지 수 계산 실패: {e}")
                elif pagination.get("type") == "click_next" and "max_pages" not in pagination:
                    # 다음 버튼이 명시되어 있고 max_pages가 명시적으로 없으면 무한 루프(다음 버튼 없을때까지)
                    max_pages = 9999
                
                while page_count <= max_pages:
                    logging.info(f"    [Page {page_count}] 데이터 추출 중...")
                    page_data = self._extract_data(page, browser_mst.selector_json)
                    extracted_all.append(page_data)
                    
                    if page_count >= max_pages:
                        break
                        
                    # 다음 페이지 이동
                    pagination_type = pagination.get("type")
                    if pagination_type == "click_next":
                        next_selector = pagination.get("next_selector")
                        if not next_selector:
                            break
                        
                        try:
                            # Verify if the next button actually exists (and isn't disabled or unclickable in some UIs)
                            next_btn = page.query_selector(next_selector)
                            if not next_btn:
                                logging.info("    더 이상 다음 페이지 버튼이 없습니다.")
                                break
                                
                            next_btn.click()
                            wait_time = int(pagination.get("wait_after", 2000))
                            page.wait_for_timeout(wait_time)
                            page_count += 1
                        except Exception as e:
                            logging.warning(f"    페이지네이션 클릭 실패: {e}")
                            break
                    else:
                        break

                # 병합: [{"A": [1,2]}, {"A": [3,4]}] -> {"A": [1,2,3,4]}
                result_data = {}
                if extracted_all:
                    keys = extracted_all[0].keys()
                    for k in keys:
                        result_data[k] = []
                        for section in extracted_all:
                            val = section.get(k)
                            if isinstance(val, list):
                                result_data[k].extend(val)
                            else:
                                result_data[k].append(val)
                
                browser.close()
                
                logging.info(f"✓ 스크래핑 완료: {len(result_data)} 항목 추출")
                return result_data
                
        except Exception as e:
            logging.error(f"✕ Browser 스크래핑 오류: {e}")
            return None
            
    def _execute_behaviors(self, page, behaviors: list, params: dict):
        """정의된 행동 순서대로 실행"""
        for behavior in behaviors:
            action = behavior.get("action")
            selector = behavior.get("selector")
            
            if not action:
                continue
                
            try:
                if action == "click" and selector:
                    page.click(selector)
                elif action == "input" and selector:
                    value = str(behavior.get("value", ""))
                    # 파라미터 치환
                    for k, v in params.items():
                        value = value.replace(f"{{{k}}}", str(v))
                    page.fill(selector, value)
                elif action == "wait":
                    wait_time = behavior.get("value", 1000)
                    page.wait_for_timeout(int(wait_time))
                elif action == "wait_for_selector" and selector:
                    page.wait_for_selector(selector)
            except Exception as e:
                logging.warning(f"행동 실행 오류 ({action} on {selector}): {e}")

    def _extract_data(self, page, selectors: dict) -> Dict[str, Any]:
        """정의된 CSS Selector를 사용해 페이지에서 데이터 추출"""
        extracted_data = {}
        if not selectors:
            return extracted_data
            
        for key, selector_def in selectors.items():
            try:
                selector = selector_def.get("selector")
                attr = selector_def.get("attribute", "text")
                is_list = selector_def.get("is_list", False)
                
                if is_list:
                    elements = page.query_selector_all(selector)
                    values = []
                    for el in elements:
                        if attr == "text":
                            values.append(el.inner_text().strip())
                        else:
                            values.append(el.get_attribute(attr))
                    extracted_data[key] = values
                else:
                    el = page.query_selector(selector)
                    if el:
                        if attr == "text":
                            extracted_data[key] = el.inner_text().strip()
                        else:
                            extracted_data[key] = el.get_attribute(attr)
                    else:
                        extracted_data[key] = None
            except Exception as e:
                logging.warning(f"데이터 추출 오류 ({key}): {e}")
                extracted_data[key] = None
                
        return extracted_data
