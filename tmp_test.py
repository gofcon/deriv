from playwright.sync_api import sync_playwright
import time
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        page.goto("https://isin.krx.co.kr/srch/srch.do?method=srchList", wait_until="networkidle")
        
        # fill
        page.fill("input[name='isur_nm1']", "삼성전자")
        
        # click search
        print("Clicking search ...")
        page.get_by_role("link", name="조회", exact=True).first.click()
        page.wait_for_timeout(4000)
        
        try:
            # count rows
            rows = page.query_selector_all("#dataTb > tbody > tr")
            print(f"Found {len(rows)} elements in table")
            
            paginator = page.query_selector("div.paging, #pageNavi, .page-navi, div.pagination")
            if paginator:
                pag_html = paginator.inner_html()
                print("Paginator found!")
                with open("tmp_paginator.html", "w", encoding="utf-8") as f:
                    f.write(pag_html)
            else:
                print("No paginator found!")
        except Exception as e:
            print(f"Error: {e}")
                
        browser.close()

if __name__ == "__main__":
    run()
