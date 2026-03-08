"""
KRX ISIN 사이트에서 전체 데이터를 스크래핑하는 스크립트
페이지네이션 처리 포함
(Refactored for Scheduler Integration & Human-like Features)
"""

from playwright.sync_api import sync_playwright
import datetime
from dateutil.relativedelta import relativedelta
import time
import pandas as pd
import argparse
import os
import csv
import json
import random

def scrape_krx_isin_logic(page, search_keyword, start_date, end_date, output_path, human_like=False):
    """
    Core scraping logic adapted from original script.
    """
    print(f"검색 키워드: {search_keyword}")
    print(f"기간: {start_date} ~ {end_date}")
    print(f"저장 경로: {output_path}")

    # 페이지 이동
    page.goto('https://isin.krx.co.kr/srch/srch.do?method=srchList')
    time.sleep(2)
    
    if human_like:
        time.sleep(random.uniform(1, 2))
        try:
             page.mouse.move(random.randint(100, 500), random.randint(100, 500))
        except: pass

    # 한글종목명 입력
    page.fill('input[name="isur_nm1"]', search_keyword)

    # 조회시작일자 ~ 종료일자 입력
    if human_like: time.sleep(random.uniform(0.5, 1))
    page.fill('input[name="std_cd_grnt_start_dd"]', start_date)

    if human_like: time.sleep(random.uniform(0.5, 1))
    page.fill('input[name="std_cd_grnt_end_dd"]', end_date)



    # 검색 버튼 클릭
    if human_like: time.sleep(random.uniform(0.5, 1))
    page.get_by_role("link", name="조회", exact=True).first.click()
    time.sleep(3)
    
    all_data = []
    
    print("페이지 1 수집 중...")
    rows = page.query_selector_all('#dataTb > tbody > tr')
    print(f"첫 페이지 행 수: {len(rows)}")
    
    for row in rows:
        cells = row.query_selector_all('td')
        if len(cells) > 1: # Ignore 'No data' rows which usually have colspan
            row_data = [cell.inner_text().strip() for cell in cells]
            all_data.append(row_data)

    # 페이지 정보 확인
    try:
        # 총 페이지 수나 총 건수 확인
        page_info = page.query_selector('.page-info, .total-count, .paging')
        if page_info:
            print(f"페이지 정보: {page_info.inner_text()}")
    except:
        pass

    # 페이지네이션 처리
    try:
            # Ensure element exists before getting inner_text
            tot_page_el = page.query_selector('#totPage1')
            if tot_page_el:
                total_page_num = int(tot_page_el.inner_text().split('/')[1].split(')')[0])
            else:
                total_page_num = 0
            print(f"total_page_num: {total_page_num}")
    except Exception as e:
            print(f"Error parsing total pages: {e}")
            total_page_num = 0

    page_num = 2

    while total_page_num > 1 and page_num < total_page_num + 1:
        try:
            # 다음 페이지 버튼 찾기 (여러 가능한 셀렉터 시도)
            next_button = None
            if not next_button:
                # 방법 2: 다음 버튼
                next_button = page.query_selector('a:has(img[src="/img/btn/btn-next.gif"])')
            if not next_button:
                print("더 이상 페이지가 없습니다.")
                break
            
            if human_like: time.sleep(random.uniform(1, 2))

            # 다음 페이지로 이동
            print(f"button next_button: {next_button}")
            print(f"페이지 {page_num} 수집 중...")
            next_button.click()
            time.sleep(2)

            # 현재 페이지 데이터 수집
            rows = page.query_selector_all('#dataTb > tbody > tr')
            print(f"페이지 {page_num} 행 수: {len(rows)}")

            if len(rows) == 0:
                break

            for row in rows:
                cells = row.query_selector_all('td')
                if len(cells) > 1:
                    row_data = [cell.inner_text().strip() for cell in cells]
                    all_data.append(row_data)

            page_num += 1

        except Exception as e:
            print(f"페이지네이션 중 오류: {e}")
            break

    # 데이터프레임 생성
    if all_data:
        # 헤더 추출 (다시 페이지 방문 using same page)
        page.goto('https://isin.krx.co.kr/srch/srch.do?method=srchList')
        time.sleep(2)
        
        headers = []
        header_cells = page.query_selector_all('#dataTb > #theadF > tr')
        for cell in header_cells:
            headers.append(cell.inner_text().strip())

        if headers and len(headers) == 1 and '\t' in headers[0]:
            headers = headers[0].split('\t')

        print(f"cell headers: {headers}")

        df = pd.DataFrame(all_data, columns=headers if headers else None)
        print(f"\n총 수집된 데이터: {len(df)} 건")
        print(df.head(10))

        # CSV로 저장
        # Ensure output directory exists (handled by caller logic usually, but here path is built)
        out_dir = os.path.dirname(output_path)
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir)

        df.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"\n데이터가 '{output_path}'에 저장되었습니다.")

        return df
    else:
        print("수집된 데이터가 없습니다.")
        return None
            

def main():
    parser = argparse.ArgumentParser(description='KRX Scraper (Simple)')
    parser.add_argument('input_file', nargs='?', default='input/krx_scraper_input.csv', help='Path to input CSV')
    
    today = datetime.datetime.now()
    default_end = today.strftime('%Y-%m-%d')
    default_start = (today - relativedelta(months=1)).strftime('%Y-%m-%d')

    args = parser.parse_args()
    input_file = args.input_file

    if not os.path.exists(input_file):
        print(f"Input file {input_file} not found.")
        return

    print(f"Running krx_scraper.py with {input_file}")

    with open(input_file, mode='r', encoding='utf-8') as f:
        reader = list(csv.DictReader(f)) 
    
    # Open browser ONCE
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for row in reader:

            search_keyword = row.get('search_keyword', 'KR1')
            start_date = row.get('start_date', '').strip()
            if not start_date:
                start_date = default_start

            end_date = row.get('end_date', '').strip()
            if not end_date:
                end_date = default_end

            # Get human_like from row, default False
            human_like_str = row.get('human_like', 'False')
            human_like = human_like_str.lower() in ('true', '1', 'yes')


            output_file_raw = row.get('output_file', 'krx_data.csv')
            if output_file_raw.endswith('.json'):
                    output_file_raw = output_file_raw.replace('.json', '.csv')

            # Append end_date to filename
            file_root, file_ext = os.path.splitext(output_file_raw)
            output_file_name = f"{file_root}_{end_date}{file_ext}"
            
            if not os.path.isabs(output_file_name):
                output_file = os.path.join('output', output_file_name)
            else:
                output_file = output_file_name

            scrape_krx_isin_logic(page, search_keyword, start_date, end_date, output_file, human_like=human_like)
        
        browser.close()

if __name__ == "__main__":
    main()

