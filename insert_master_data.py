"""
insert_master_data.py - 마스터 데이터 다운로드 및 삽입 스크립트

KIS API에서 16가지 마스터 데이터를 다운로드하고 데이터베이스에 삽입합니다.
"""

import os
import sys
import ssl
import zipfile
import urllib.request
import pandas as pd
import logging
from pathlib import Path
from typing import List, Dict, Any

from app.db_mst import MasterDatabaseManager
from app.config import DB_PATH
from sqlmodel import SQLModel
from logs.log_setup import setup_logging

# SSL 인증서 검증 비활성화
ssl._create_default_https_context = ssl._create_unverified_context


def download_and_extract_zip(url: str, filename: str, base_dir: str, extracted_filename: str = None) -> str:
    """ZIP 파일 다운로드 및 압축 해제"""
    zip_path = os.path.join(base_dir, filename)
    
    logging.info(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, zip_path)
    except Exception as e:
        logging.error(f"Download failed: {url} - {e}")
        return ""
    
    logging.info(f"Extracting {filename}...")
    try:
        with zipfile.ZipFile(zip_path) as zip_file:
            zip_file.extractall(base_dir)
            
            # If extracted_filename is not provided, try to guess
            if not extracted_filename:
                if len(zip_file.namelist()) == 1:
                    extracted_filename = zip_file.namelist()[0]
                else:
                    extracted_filename = filename.replace('.zip', '')
                    
    except Exception as e:
        logging.error(f"Extraction failed: {filename} - {e}")
        return ""
        
    if not extracted_filename:
        logging.error(f"Could not determine extracted filename for {filename}")
        return ""

    full_path = os.path.join(base_dir, extracted_filename)
    if not os.path.exists(full_path):
        logging.warning(f"Extracted file not found at expected path: {full_path}")
        search_name = filename.replace('.zip', '')
        for f in os.listdir(base_dir):
            if (f.endswith(".mst") or f.endswith(".cod")) and search_name in f:
                return os.path.join(base_dir, f)
        return ""

    return full_path


# =============================================================================
# 1. 국내 지수선물옵션 (DomFutureMst)
# =============================================================================
def insert_domestic_index_future_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import DomFutureMst
    url = "https://new.real.download.dws.co.kr/common/master/fo_idx_code_mts.mst.zip"
    mst_file = download_and_extract_zip(url, "fo_idx_code_mts.mst.zip", base_dir)
    if not mst_file: return

    columns = ['product_type', 'short_code', 'standard_code', 'kor_name', 'atm_division',
               'strike_price', 'month_code', 'underlying_short_code', 'underlying_name']
    
    df = pd.read_table(mst_file, sep='|', encoding='cp949', header=None, names=columns)
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    db.insert_data(DomFutureMst, df.to_dict('records'))


# =============================================================================
# 2. 해외선물옵션 (OverFutureMst)
# =============================================================================
def insert_overseas_future_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import OverFutureMst
    url = "https://new.real.download.dws.co.kr/common/master/ffcode.mst.zip"
    mst_file = download_and_extract_zip(url, "ffcode.mst.zip", base_dir)
    if not mst_file: return
    
    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
            data_list.append({
                'symbol_code': row[:32].strip(),
                'auto_order_yn': row[32:33].strip(),
                'twap_order_yn': row[33:34].strip(),
                'econ_order_yn': row[34:35].strip(),
                'filler': row[35:82].strip(),
                'kor_name': row[82:107].strip(),
                'exchange_code': row[-92:-82].strip(),
                'item_code': row[-82:-72].strip(),
                'item_type': row[-72:-69].strip(),
                'display_decimal': row[-69:-64].strip(),
                'calc_decimal': row[-64:-59].strip(),
                'tick_size': row[-59:-45].strip(),
                'tick_value': row[-45:-31].strip(),
                'contract_size': row[-31:-21].strip(),
                'price_notation': row[-21:-17].strip(),
                'conversion_multiplier': row[-17:-7].strip(),
                'most_active_yn': row[-7:-6].strip(),
                'nearest_month_yn': row[-6:-5].strip(),
                'spread_yn': row[-5:-4].strip(),
                'spread_leg1_yn': row[-4:-3].strip(),
                'sub_exchange_code': row[-3:].strip()
            })
            
    db.insert_data(OverFutureMst, data_list)


# =============================================================================
# 3. 국내 주식선물옵션 (DomStockFutureMst)
# =============================================================================
def insert_domestic_stock_future_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import DomStockFutureMst
    url = "https://new.real.download.dws.co.kr/common/master/fo_stk_code_mts.mst.zip"
    mst_file = download_and_extract_zip(url, "fo_stk_code_mts.mst.zip", base_dir)
    if not mst_file: return

    columns = ['product_type', 'short_code', 'standard_code', 'kor_name', 'atm_division',
               'strike_price', 'month_code', 'underlying_short_code', 'underlying_name']
    
    df = pd.read_table(mst_file, sep='|', encoding='cp949', header=None, names=columns)
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    db.insert_data(DomStockFutureMst, df.to_dict('records'))


# =============================================================================
# 4. 해외주식 (OverStockMst)
# =============================================================================
def insert_overseas_stock_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import OverStockMst
    market_codes = ['nas', 'nys', 'ams', 'shs', 'shi', 'szs', 'szi', 'tse', 'hks', 'hnx', 'hsx']
    columns = ['national_code', 'exchange_id', 'exchange_code', 'exchange_name', 'symbol',
               'realtime_symbol', 'korea_name', 'english_name', 'security_type', 'currency',
               'float_position', 'data_type', 'base_price', 'bid_order_size', 'ask_order_size',
               'market_start_time', 'market_end_time', 'dr_yn', 'dr_country_code', 'industry_code',
               'index_constituent_yn', 'tick_size_type', 'division_code', 'tick_size_type_detail']
    
    all_data = []
    for market in market_codes:
        url = f"https://new.real.download.dws.co.kr/common/master/{market}mst.cod.zip"
        cod_file = download_and_extract_zip(url, f"{market}mst.cod.zip", base_dir)
        if not cod_file: continue
        
        try:
            df = pd.read_table(cod_file, sep='\t', encoding='cp949', header=None, names=columns)
            df = df.fillna("")
            all_data.extend(df.to_dict('records'))
        except Exception as e:
            logging.error(f"Failed to parse {market}: {e}")

    db.insert_data(OverStockMst, all_data, batch_size=2000)


# =============================================================================
# 5. 국내 채권 (DomBondMst)
# =============================================================================
def insert_domestic_bond_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import DomBondMst
    url = "https://new.real.download.dws.co.kr/common/master/bond_code.mst.zip"
    mst_file = download_and_extract_zip(url, "bond_code.zip", base_dir)
    if not mst_file: return
    
    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f.readlines():
            row = row.strip()
            if len(row) < 30: continue
            data_list.append({
                'bond_type': row[0:2].strip(),
                'bond_cls_code': row[2:4].strip(),
                'standard_code': row[4:16].strip(),
                'redemption_date': row[-8:].strip(),
                'public_date': row[-16:-8].strip(),
                'listed_date': row[-24:-16].strip(),
                'bond_int_cls_code': row[-26:-24].strip(),
                'kor_name': row[16:-26].rstrip()
            })
            
    db.insert_data(DomBondMst, data_list)


# =============================================================================
# 6. CME연계 야간선물 (DomCmeFutureMst)
# =============================================================================
def insert_domestic_cme_future_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import DomCmeFutureMst
    url = "https://new.real.download.dws.co.kr/common/master/fo_cme_code.mst.zip"
    mst_file = download_and_extract_zip(url, "fo_cme_code.mst.zip", base_dir)
    if not mst_file: return

    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
             data_list.append({
                'product_type': row[0:1].strip(),
                'short_code': row[1:10].strip(),
                'standard_code': row[10:22].strip(),
                'kor_name': row[22:63].strip(),
                'strike_price': row[63:72].strip(),
                'underlying_short_code': row[72:81].strip(),
                'underlying_name': row[81:].strip()
            })
            
    db.insert_data(DomCmeFutureMst, data_list)


# =============================================================================
# 7. 상품선물옵션 (DomComFutureMst)
# =============================================================================
def insert_domestic_commodity_future_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import DomComFutureMst
    url = "https://new.real.download.dws.co.kr/common/master/fo_com_code.mst.zip"
    mst_file = download_and_extract_zip(url, "fo_com_code.mst.zip", base_dir)
    if not mst_file: return

    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
            data_list.append({
                'product_class': row[0:1].strip(),
                'product_type': row[1:2].strip(),
                'short_code': row[2:11].strip(),
                'standard_code': row[11:23].strip(),
                'kor_name': row[23:55].strip(),
                'month_code': row[63:64].strip(),
                'underlying_short_code': row[64:67].strip(),
                'underlying_name': row[67:].strip()
            })
            
    db.insert_data(DomComFutureMst, data_list)


# =============================================================================
# 8. 국내 ELW (DomElwMst)
# =============================================================================
def insert_domestic_elw_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import DomElwMst
    url = "https://new.real.download.dws.co.kr/common/master/elw_code.mst.zip"
    mst_file = download_and_extract_zip(url, "elw_code.zip", base_dir)
    if not mst_file: return
    
    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
            crow = row[50:]
            data_list.append({
                'short_code': row[0:9].strip(),
                'standard_code': row[9:21].strip(),
                'kor_name': row[21:50].strip(),
                'elw_right_type': crow[:1].strip(),
                'elw_early_end_price': crow[1:14].strip(),
                'basket_yn': crow[14:15].strip(),
                'underlying_code1': crow[15:24].strip(),
                'underlying_code2': crow[24:33].strip(),
                'underlying_code3': crow[33:42].strip(),
                'underlying_code4': crow[42:51].strip(),
                'underlying_code5': crow[51:60].strip(),
                'issuer_name': row[-110:-11].strip() if len(row) > 110 else "",
                'issuer_code': row[-110:-105].strip(),
                'strike_price': row[-105:-96].strip(),
                'last_trade_date': row[-96:-88].strip(),
                'remain_days': row[-88:-84].strip(),
                'right_type_code': row[-84:-83].strip(),
                'payment_date': row[-83:-75].strip(),
                'prev_market_cap': row[-75:-66].strip(),
                'listed_shares': row[-66:-51].strip(),
            })
    
    db.insert_data(DomElwMst, data_list)


# =============================================================================
# 9. EUREX연계 야간옵션 (DomEurexOptionMst)
# =============================================================================
def insert_domestic_eurex_option_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import DomEurexOptionMst
    url = "https://new.real.download.dws.co.kr/common/master/fo_eurex_code.mst.zip"
    mst_file = download_and_extract_zip(url, "fo_eurex_code.mst.zip", base_dir)
    if not mst_file: return
    
    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
            data_list.append({
                'product_type': row[0:1].strip(),
                'short_code': row[1:10].strip(),
                'standard_code': row[10:22].strip(),
                'kor_name': row[22:59].strip(),
                'atm_division': row[59:60].strip(),
                'strike_price': row[60:68].strip(),
                'underlying_short_code': row[68:76].strip(),
                'underlying_name': row[76:].strip()
            })
            
    db.insert_data(DomEurexOptionMst, data_list)


# =============================================================================
# 10. 코넥스 (DomKonexMst)
# =============================================================================
def insert_domestic_konex_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import DomKonexMst
    url = "https://new.real.download.dws.co.kr/common/master/konex_code.mst.zip"
    mst_file = download_and_extract_zip(url, "konex_code.zip", base_dir)
    if not mst_file: return
    
    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
            row = row.strip()
            if not row: continue
            data_list.append({
                'short_code': row[0:9].strip(),
                'standard_code': row[9:21].strip(),
                'kor_name': row[21:-184].strip(),
                'group_code': row[-184:-182].strip(),
                'base_price': row[-182:-173].strip(),
                'listed_date': row[-118:-110].strip(),
                'listed_shares': row[-110:-95].strip(),
                'capital': row[-95:-74].strip(),
                'face_value': row[-130:-118].strip()
            })

    db.insert_data(DomKonexMst, data_list)


# =============================================================================
# 11. 코스닥 (DomKosdaqMst)
# =============================================================================
def insert_domestic_kosdaq_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import DomKosdaqMst
    url = "https://new.real.download.dws.co.kr/common/master/kosdaq_code.mst.zip"
    mst_file = download_and_extract_zip(url, "kosdaq_code.zip", base_dir)
    if not mst_file: return
    
    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
            rf1 = row[0:len(row) - 222]
            rf2 = row[-222:]
            
            data_list.append({
                'short_code': rf1[0:9].rstrip(),
                'standard_code': rf1[9:21].rstrip(),
                'kor_name': rf1[21:].strip(),
                'group_code': rf2[0:2].strip(),
                'market_cap_scale': rf2[2:3].strip(),
                'industry_code_l': rf2[3:7].strip(),
                'industry_code_m': rf2[7:11].strip(),
                'industry_code_s': rf2[11:15].strip(),
                'base_price': rf2[57:66].strip(),
            })

    db.insert_data(DomKosdaqMst, data_list)


# =============================================================================
# 12. 코스피 (DomKospiMst)
# =============================================================================
def insert_domestic_kospi_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import DomKospiMst
    url = "https://new.real.download.dws.co.kr/common/master/kospi_code.mst.zip"
    mst_file = download_and_extract_zip(url, "kospi_code.zip", base_dir)
    if not mst_file: return
    
    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
            rf1 = row[0:len(row) - 228]
            rf2 = row[-228:]
            
            data_list.append({
                'short_code': rf1[0:9].rstrip(),
                'standard_code': rf1[9:21].rstrip(),
                'kor_name': rf1[21:].strip(),
                'group_code': rf2[0:2].strip(),
                'market_cap_scale': rf2[2:3].strip(),
                'industry_code_l': rf2[3:7].strip(),
                'industry_code_m': rf2[7:11].strip(),
                'industry_code_s': rf2[11:15].strip(),
                'base_price': rf2[57:66].strip(),
            })

    db.insert_data(DomKospiMst, data_list)


# =============================================================================
# 13. 회원사 코드 (MemberCodeMst)
# =============================================================================
def insert_member_code_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import MemberCodeMst
    url = "https://new.real.download.dws.co.kr/common/master/memcode.mst"
    mst_file = os.path.join(base_dir, "memcode.mst")
    try:
        urllib.request.urlretrieve(url, mst_file)
    except:
        return

    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f.readlines():
            if row.strip():
                data_list.append({
                    'member_code': row[:5].strip(),
                    'member_name': row[5:-2].strip(),
                    'region_code': row[-2:].strip()
                })
                
    db.insert_data(MemberCodeMst, data_list)


# =============================================================================
# 14. 해외주식 지수 (OverIndexMst)
# =============================================================================
def insert_overseas_index_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import OverIndexMst
    url = "https://new.real.download.dws.co.kr/common/master/frgn_code.mst.zip"
    mst_file = download_and_extract_zip(url, "frgn_code.mst.zip", base_dir)
    if not mst_file: return
    
    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
            rf1 = row[0:len(row) - 14]
            rf2 = row[-15:]
            
            data_list.append({
                'division_code': rf1[0:1],
                'symbol': rf1[1:11].strip(),
                'eng_name': rf1[11:40].replace(",","").strip(),
                'kor_name': rf1[40:].strip() if len(rf1) > 40 else "" 
            })

    db.insert_data(OverIndexMst, data_list)


# =============================================================================
# 15. 업종 코드 (SectorMst)
# =============================================================================
def insert_sector_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import SectorMst
    url = "https://new.real.download.dws.co.kr/common/master/idxcode.mst.zip"
    mst_file = download_and_extract_zip(url, "idxcode.zip", base_dir)
    if not mst_file: return
    
    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
             data_list.append({
                'sector_code': row[1:5].strip(),
                'sector_name': row[3:43].rstrip()
            })
            
    db.insert_data(SectorMst, data_list)


# =============================================================================
# 16. 테마 코드 (ThemeMst)
# =============================================================================
def insert_theme_master(db: MasterDatabaseManager, base_dir: str):
    from app.models import ThemeMst
    url = "https://new.real.download.dws.co.kr/common/master/theme_code.mst.zip"
    mst_file = download_and_extract_zip(url, "theme_code.zip", base_dir)
    if not mst_file: return
    
    data_list = []
    with open(mst_file, mode="r", encoding="cp949") as f:
        for row in f:
            data_list.append({
                'theme_code': row[0:3].strip(),
                'theme_name': row[3:-10].rstrip(),
                'stock_code': row[-10:].rstrip()
            })
            
    db.insert_data(ThemeMst, data_list)


def main():
    logging.info("=" * 60)
    logging.info("마스터 데이터 다운로드 및 삽입 시작 (16 Types)")
    logging.info("=" * 60)
    
    base_dir = "temp_master_data_full"
    os.makedirs(base_dir, exist_ok=True)
    
    db = MasterDatabaseManager(DB_PATH)
    
    # Create all tables (or just master tables)
    db.init_master_tables()
    
    try:
        insert_domestic_index_future_master(db, base_dir)      # 1
        insert_overseas_future_master(db, base_dir)            # 2
        insert_domestic_stock_future_master(db, base_dir)      # 3
        insert_overseas_stock_master(db, base_dir)             # 4
        insert_domestic_bond_master(db, base_dir)              # 5
        insert_domestic_cme_future_master(db, base_dir)        # 6
        insert_domestic_commodity_future_master(db, base_dir)  # 7
        insert_domestic_elw_master(db, base_dir)               # 8
        insert_domestic_eurex_option_master(db, base_dir)      # 9
        insert_domestic_konex_master(db, base_dir)             # 10
        insert_domestic_kosdaq_master(db, base_dir)            # 11
        insert_domestic_kospi_master(db, base_dir)             # 12
        insert_member_code_master(db, base_dir)                # 13
        insert_overseas_index_master(db, base_dir)             # 14
        insert_sector_master(db, base_dir)                     # 15
        insert_theme_master(db, base_dir)                      # 16
        
        logging.info("=" * 60)
        
        # 메타데이터 업데이트 실행
        db.update_metadata_tables()
        
        logging.info("✓ 모든 마스터 데이터 처리 완료")
    except Exception as e:
        logging.error(f"Critical Error: {e}")
        import traceback
        logging.error(traceback.format_exc())
    import shutil
    try:
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
            logging.info(f"Removed temporary directory: {base_dir}")
    except Exception as e:
        logging.error(f"Failed to remove temporary directory: {e}")


if __name__ == "__main__":
    setup_logging()
    main()
