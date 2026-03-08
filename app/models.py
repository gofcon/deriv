"""
models.py - SQLModel 기반 데이터베이스 모델 정의
"""

import json
from typing import Optional, List, Dict, Any
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship

import app.oracle_mapping  # noqa: F401


# Core modeling logic moved to models_gofcon.py


# ===== Output Table Models =====
# Auto-generated from COLUMN_MAPPING in temp_repo

class StockPrice(SQLModel, table=True):
    """Output table for stock_price"""
    __tablename__ = "kis_stock_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    iscd_stat_cls_code: Optional[str] = None  # 종목 상태 구분 코드
    marg_rate: Optional[str] = None  # 증거금 비율
    rprs_mrkt_kor_name: Optional[str] = None  # 대표 시장 한글 명
    new_hgpr_lwpr_cls_code: Optional[str] = None  # 신 고가 저가 구분 코드
    bstp_kor_isnm: Optional[str] = None  # 업종 한글 종목명
    temp_stop_yn: Optional[str] = None  # 임시 정지 여부
    oprc_rang_cont_yn: Optional[str] = None  # 시가 범위 연장 여부
    clpr_rang_cont_yn: Optional[str] = None  # 종가 범위 연장 여부
    crdt_able_yn: Optional[str] = None  # 신용 가능 여부
    grmn_rate_cls_code: Optional[str] = None  # 보증금 비율 구분 코드
    elw_pblc_yn: Optional[str] = None  # ELW 발행 여부
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    acml_vol: Optional[str] = None  # 누적 거래량
    prdy_vrss_vol_rate: Optional[str] = None  # 전일 대비 거래량 비율
    stck_oprc: Optional[str] = None  # 주식 시가2
    stck_hgpr: Optional[str] = None  # 주식 최고가
    stck_lwpr: Optional[str] = None  # 주식 최저가
    stck_mxpr: Optional[str] = None  # 주식 상한가
    stck_llam: Optional[str] = None  # 주식 하한가
    stck_sdpr: Optional[str] = None  # 주식 기준가
    wghn_avrg_stck_prc: Optional[str] = None  # 가중 평균 주식 가격
    hts_frgn_ehrt: Optional[str] = None  # HTS 외국인 소진율
    frgn_ntby_qty: Optional[str] = None  # 외국인 순매수 수량
    pgtr_ntby_qty: Optional[str] = None  # 프로그램매매 순매수 수량
    pvt_scnd_dmrs_prc: Optional[str] = None  # 피벗 2차 디저항 가격
    pvt_frst_dmrs_prc: Optional[str] = None  # 피벗 1차 디저항 가격
    pvt_pont_val: Optional[str] = None  # 피벗 포인트 값
    pvt_frst_dmsp_prc: Optional[str] = None  # 피벗 1차 디지지 가격
    pvt_scnd_dmsp_prc: Optional[str] = None  # 피벗 2차 디지지 가격
    dmrs_val: Optional[str] = None  # 디저항 값
    dmsp_val: Optional[str] = None  # 디지지 값
    cpfn: Optional[str] = None  # 자본금
    rstc_wdth_prc: Optional[str] = None  # 제한 폭 가격
    stck_fcam: Optional[str] = None  # 주식 액면가
    stck_sspr: Optional[str] = None  # 주식 대용가
    aspr_unit: Optional[str] = None  # 호가단위
    hts_deal_qty_unit_val: Optional[str] = None  # HTS 매매 수량 단위 값
    lstn_stcn: Optional[str] = None  # 상장 주수
    hts_avls: Optional[str] = None  # HTS 시가총액
    per: Optional[str] = None  # PER
    pbr: Optional[str] = None  # PBR
    stac_month: Optional[str] = None  # 결산 월
    vol_tnrt: Optional[str] = None  # 거래량 회전율
    eps: Optional[str] = None  # EPS
    bps: Optional[str] = None  # BPS
    d250_hgpr: Optional[str] = None  # 250일 최고가
    d250_hgpr_date: Optional[str] = None  # 250일 최고가 일자
    d250_hgpr_vrss_prpr_rate: Optional[str] = None  # 250일 최고가 대비 현재가 비율
    d250_lwpr: Optional[str] = None  # 250일 최저가
    d250_lwpr_date: Optional[str] = None  # 250일 최저가 일자
    d250_lwpr_vrss_prpr_rate: Optional[str] = None  # 250일 최저가 대비 현재가 비율
    stck_dryy_hgpr: Optional[str] = None  # 주식 연중 최고가
    dryy_hgpr_vrss_prpr_rate: Optional[str] = None  # 연중 최고가 대비 현재가 비율
    dryy_hgpr_date: Optional[str] = None  # 연중 최고가 일자
    stck_dryy_lwpr: Optional[str] = None  # 주식 연중 최저가
    dryy_lwpr_vrss_prpr_rate: Optional[str] = None  # 연중 최저가 대비 현재가 비율
    dryy_lwpr_date: Optional[str] = None  # 연중 최저가 일자
    w52_hgpr: Optional[str] = None  # 52주일 최고가
    w52_hgpr_vrss_prpr_ctrt: Optional[str] = None  # 52주일 최고가 대비 현재가 대비
    w52_hgpr_date: Optional[str] = None  # 52주일 최고가 일자
    w52_lwpr: Optional[str] = None  # 52주일 최저가
    w52_lwpr_vrss_prpr_ctrt: Optional[str] = None  # 52주일 최저가 대비 현재가 대비
    w52_lwpr_date: Optional[str] = None  # 52주일 최저가 일자
    whol_loan_rmnd_rate: Optional[str] = None  # 전체 융자 잔고 비율
    ssts_yn: Optional[str] = None  # 공매도가능여부
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    fcam_cnnm: Optional[str] = None  # 액면가 통화명
    cpfn_cnnm: Optional[str] = None  # 자본금 통화명
    apprch_rate: Optional[str] = None  # 접근도
    frgn_hldn_qty: Optional[str] = None  # 외국인 보유 수량
    vi_cls_code: Optional[str] = None  # VI적용구분코드
    ovtm_vi_cls_code: Optional[str] = None  # 시간외단일가VI적용구분코드
    last_ssts_cntg_qty: Optional[str] = None  # 최종 공매도 체결 수량
    invt_caful_yn: Optional[str] = None  # 투자유의여부
    mrkt_warn_cls_code: Optional[str] = None  # 시장경고코드
    short_over_yn: Optional[str] = None  # 단기과열여부
    sltr_yn: Optional[str] = None  # 정리매매여부
    mang_issu_cls_code: Optional[str] = None  # 관리종목여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DailyPrice(SQLModel, table=True):
    """Output table for daily_price"""
    __tablename__ = "kis_daily_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_oprc: Optional[str] = None  # 주식 시가2
    stck_hgpr: Optional[str] = None  # 주식 최고가
    stck_lwpr: Optional[str] = None  # 주식 최저가
    stck_clpr: Optional[str] = None  # 주식 종가
    acml_vol: Optional[str] = None  # 누적 거래량
    prdy_vrss_vol_rate: Optional[str] = None  # 전일 대비 거래량 비율
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    hts_frgn_ehrt: Optional[str] = None  # HTS 외국인 소진율
    frgn_ntby_qty: Optional[str] = None  # 외국인 순매수 수량
    flng_cls_code: Optional[str] = None  # 락 구분 코드
    acml_prtt_rate: Optional[str] = None  # 누적 분할 비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DisplayBoardTop(SQLModel, table=True):
    """Output table for display_board_top"""
    __tablename__ = "kis_display_board_top"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    unas_prpr: Optional[str] = None  # 기초자산 현재가
    unas_prdy_vrss: Optional[str] = None  # 기초자산 전일 대비
    unas_prdy_vrss_sign: Optional[str] = None  # 기초자산 전일 대비 부호
    unas_prdy_ctrt: Optional[str] = None  # 기초자산 전일 대비율
    unas_acml_vol: Optional[str] = None  # 기초자산 누적 거래량
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    futs_prpr: Optional[str] = None  # 선물 현재가
    futs_prdy_vrss: Optional[str] = None  # 선물 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    futs_prdy_ctrt: Optional[str] = None  # 선물 전일 대비율
    hts_rmnn_dynu: Optional[str] = None  # HTS 잔존 일수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)




class AvgUnit(SQLModel, table=True):
    """Output table for avg_unit"""
    __tablename__ = "kis_avg_unit"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    evlu_dt: Optional[str] = None  # 평가일자
    pdno: Optional[str] = None  # 상품번호
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    kis_unpr: Optional[str] = None  # 한국신용평가단가
    kbp_unpr: Optional[str] = None  # 한국채권평가단가
    nice_evlu_unpr: Optional[str] = None  # 한국신용정보평가단가
    fnp_unpr: Optional[str] = None  # 에프앤자산평가단가
    avg_evlu_unpr: Optional[str] = None  # 평균평가단가
    kis_crdt_grad_text: Optional[str] = None  # 한국신용평가신용등급내용
    kbp_crdt_grad_text: Optional[str] = None  # 한국채권평가신용등급내용
    nice_crdt_grad_text: Optional[str] = None  # 한국신용정보신용등급내용
    fnp_crdt_grad_text: Optional[str] = None  # 에프앤자산평가신용등급내용
    chng_yn: Optional[str] = None  # 변경여부
    kis_erng_rt: Optional[str] = None  # 한국신용평가수익율
    kbp_erng_rt: Optional[str] = None  # 한국채권평가수익율
    nice_evlu_erng_rt: Optional[str] = None  # 한국신용정보평가수익율
    fnp_erng_rt: Optional[str] = None  # 에프앤자산평가수익율
    avg_evlu_erng_rt: Optional[str] = None  # 평균평가수익율
    kis_rf_unpr: Optional[str] = None  # 한국신용평가RF단가
    kbp_rf_unpr: Optional[str] = None  # 한국채권평가RF단가
    nice_evlu_rf_unpr: Optional[str] = None  # 한국신용정보평가RF단가
    avg_evlu_rf_unpr: Optional[str] = None  # 평균평가RF단가
    kis_evlu_amt: Optional[str] = None  # 한국신용평가평가금액
    kbp_evlu_amt: Optional[str] = None  # 한국채권평가평가금액
    nice_evlu_amt: Optional[str] = None  # 한국신용정보평가금액
    fnp_evlu_amt: Optional[str] = None  # 에프앤자산평가평가금액
    avg_evlu_amt: Optional[str] = None  # 평균평가금액
    output3: Optional[str] = None  # 응답상세
    kis_crcy_cd: Optional[str] = None  # 한국신용평가통화코드
    kis_evlu_unit_pric: Optional[str] = None  # 한국신용평가평가단위가격
    kis_evlu_pric: Optional[str] = None  # 한국신용평가평가가격
    kbp_crcy_cd: Optional[str] = None  # 한국채권평가통화코드
    kbp_evlu_unit_pric: Optional[str] = None  # 한국채권평가평가단위가격
    kbp_evlu_pric: Optional[str] = None  # 한국채권평가평가가격
    nice_crcy_cd: Optional[str] = None  # 한국신용정보통화코드
    nice_evlu_unit_pric: Optional[str] = None  # 한국신용정보평가단위가격
    nice_evlu_pric: Optional[str] = None  # 한국신용정보평가가격
    avg_evlu_unit_pric: Optional[str] = None  # 평균평가단위가격
    avg_evlu_pric: Optional[str] = None  # 평균평가가격
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class BondAskingPrice(SQLModel, table=True):
    """Output table for bond_asking_price"""
    __tablename__ = "kis_bond_asking_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stnd_iscd: Optional[str] = None  # 표준종목코드
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    askp_ert1: Optional[str] = None  # 매도호가수익률1
    bidp_ert1: Optional[str] = None  # 매수호가수익률1
    askp1: Optional[str] = None  # 매도호가1
    bidp1: Optional[str] = None  # 매수호가1
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    askp_ert2: Optional[str] = None  # 매도호가수익률2
    bidp_ert2: Optional[str] = None  # 매수호가수익률2
    askp2: Optional[str] = None  # 매도호가2
    bidp2: Optional[str] = None  # 매수호가2
    askp_rsqn2: Optional[str] = None  # 매도호가잔량2
    bidp_rsqn2: Optional[str] = None  # 매수호가잔량2
    askp_ert3: Optional[str] = None  # 매도호가수익률3
    bidp_ert3: Optional[str] = None  # 매수호가수익률3
    askp3: Optional[str] = None  # 매도호가3
    bidp3: Optional[str] = None  # 매수호가3
    askp_rsqn3: Optional[str] = None  # 매도호가잔량3
    bidp_rsqn3: Optional[str] = None  # 매수호가잔량3
    askp_ert4: Optional[str] = None  # 매도호가수익률4
    bidp_ert4: Optional[str] = None  # 매수호가수익률4
    askp4: Optional[str] = None  # 매도호가4
    bidp4: Optional[str] = None  # 매수호가4
    askp_rsqn4: Optional[str] = None  # 매도호가잔량4
    bidp_rsqn4: Optional[str] = None  # 매수호가잔량4
    askp_ert5: Optional[str] = None  # 매도호가수익률5
    bidp_ert5: Optional[str] = None  # 매수호가수익률5
    askp5: Optional[str] = None  # 매도호가5
    bidp5: Optional[str] = None  # 매수호가5
    askp_rsqn52: Optional[str] = None  # 매도호가잔량5
    bidp_rsqn53: Optional[str] = None  # 매수호가잔량5
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class BondCcnl(SQLModel, table=True):
    """Output table for bond_ccnl"""
    __tablename__ = "kis_bond_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stnd_iscd: Optional[str] = None  # 표준종목코드
    bond_isnm: Optional[str] = None  # 채권종목명
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    stck_prpr: Optional[str] = None  # 현재가
    cntg_vol: Optional[str] = None  # 체결거래량
    stck_oprc: Optional[str] = None  # 시가
    stck_hgpr: Optional[str] = None  # 고가
    stck_lwpr: Optional[str] = None  # 저가
    stck_prdy_clpr: Optional[str] = None  # 전일종가
    bond_cntg_ert: Optional[str] = None  # 현재수익률
    oprc_ert: Optional[str] = None  # 시가수익률
    hgpr_ert: Optional[str] = None  # 고가수익률
    lwpr_ert: Optional[str] = None  # 저가수익률
    acml_vol: Optional[str] = None  # 누적거래량
    prdy_vol: Optional[str] = None  # 전일거래량
    cntg_type_cls_code: Optional[str] = None  # 체결유형코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class BondIndexCcnl(SQLModel, table=True):
    """Output table for bond_index_ccnl"""
    __tablename__ = "kis_bond_index_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    nmix_id: Optional[str] = None  # 지수ID
    stnd_date1: Optional[str] = None  # 기준일자1
    trnm_hour: Optional[str] = None  # 전송시간
    totl_ernn_nmix_oprc: Optional[str] = None  # 총수익지수시가지수
    totl_ernn_nmix_hgpr: Optional[str] = None  # 총수익지수최고가
    totl_ernn_nmix_lwpr: Optional[str] = None  # 총수익지수최저가
    totl_ernn_nmix: Optional[str] = None  # 총수익지수
    prdy_totl_ernn_nmix: Optional[str] = None  # 전일총수익지수
    totl_ernn_nmix_prdy_vrss: Optional[str] = None  # 총수익지수전일대비
    totl_ernn_nmix_prdy_vrss_sign: Optional[str] = None  # 총수익지수전일대비부호
    totl_ernn_nmix_prdy_ctrt: Optional[str] = None  # 총수익지수전일대비율
    clen_prc_nmix: Optional[str] = None  # 순가격지수
    mrkt_prc_nmix: Optional[str] = None  # 시장가격지수
    bond_call_rnvs_nmix: Optional[str] = None  # Call재투자지수
    bond_zero_rnvs_nmix: Optional[str] = None  # Zero재투자지수
    bond_futs_thpr: Optional[str] = None  # 선물이론가격
    bond_avrg_drtn_val: Optional[str] = None  # 평균듀레이션
    bond_avrg_cnvx_val: Optional[str] = None  # 평균컨벡서티
    bond_avrg_ytm_val: Optional[str] = None  # 평균YTM
    bond_avrg_frdl_ytm_val: Optional[str] = None  # 평균선도YTM
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Buy(SQLModel, table=True):
    """Output table for buy"""
    __tablename__ = "kis_buy"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    KRX_FWDG_ORD_ORGNO: Optional[str] = None  # 한국거래소전송주문조직번호
    ODNO: Optional[str] = None  # 주문번호
    ORD_TMD: Optional[str] = None  # 주문시각
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireAskingPrice(SQLModel, table=True):
    """Output table for inquire_asking_price"""
    __tablename__ = "kis_inquire_asking_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    rsym: Optional[str] = None  # 실시간조회종목코드
    zdiv: Optional[str] = None  # 소수점자리수
    curr: Optional[str] = None  # 통화
    base: Optional[str] = None  # 전일종가
    open: Optional[str] = None  # 시가
    high: Optional[str] = None  # 고가
    low: Optional[str] = None  # 저가
    last: Optional[str] = None  # 현재가
    dymd: Optional[str] = None  # 호가일자
    dhms: Optional[str] = None  # 호가시간
    bvol: Optional[str] = None  # 매수호가총잔량
    avol: Optional[str] = None  # 매도호가총잔량
    bdvl: Optional[str] = None  # 매수호가총잔량대비
    advl: Optional[str] = None  # 매도호가총잔량대비
    code: Optional[str] = None  # 종목코드
    ropen: Optional[str] = None  # 시가율
    rhigh: Optional[str] = None  # 고가율
    rlow: Optional[str] = None  # 저가율
    rclose: Optional[str] = None  # 현재가율
    pbid1: Optional[str] = None  # 매수호가가격1
    pask1: Optional[str] = None  # 매도호가가격1
    vbid1: Optional[str] = None  # 매수호가잔량1
    vask1: Optional[str] = None  # 매도호가잔량1
    dbid1: Optional[str] = None  # 매수호가대비1
    dask1: Optional[str] = None  # 매도호가대비1
    vstm: Optional[str] = None  # VCMStart시간
    vetm: Optional[str] = None  # VCMEnd시간
    csbp: Optional[str] = None  # CAS/VCM기준가
    cshi: Optional[str] = None  # CAS/VCMHighprice
    cslo: Optional[str] = None  # CAS/VCMLowprice
    iep: Optional[str] = None  # IEP
    iev: Optional[str] = None  # IEV
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireBalance(SQLModel, table=True):
    """Output table for inquire_balance"""
    __tablename__ = "kis_inquire_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cano: Optional[str] = None  # 종합계좌번호
    acnt_prdt_cd: Optional[str] = None  # 계좌상품코드
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    ovrs_pdno: Optional[str] = None  # 해외상품번호
    frcr_evlu_pfls_amt: Optional[str] = None  # 외화평가손익금액
    evlu_pfls_rt: Optional[str] = None  # 평가손익율
    pchs_avg_pric: Optional[str] = None  # 매입평균가격
    ovrs_cblc_qty: Optional[str] = None  # 해외잔고수량
    ord_psbl_qty: Optional[str] = None  # 주문가능수량
    frcr_pchs_amt1: Optional[str] = None  # 외화매입금액1
    ovrs_stck_evlu_amt: Optional[str] = None  # 해외주식평가금액
    now_pric2: Optional[str] = None  # 현재가격2
    tr_crcy_cd: Optional[str] = None  # 거래통화코드
    ovrs_excg_cd: Optional[str] = None  # 해외거래소코드
    loan_type_cd: Optional[str] = None  # 대출유형코드
    loan_dt: Optional[str] = None  # 대출일자
    expd_dt: Optional[str] = None  # 만기일자
    ovrs_rlzt_pfls_amt: Optional[str] = None  # 해외실현손익금액
    ovrs_tot_pfls: Optional[str] = None  # 해외총손익
    rlzt_erng_rt: Optional[str] = None  # 실현수익율
    tot_evlu_pfls_amt: Optional[str] = None  # 총평가손익금액
    tot_pftrt: Optional[str] = None  # 총수익률
    frcr_buy_amt_smtl1: Optional[str] = None  # 외화매수금액합계1
    ovrs_rlzt_pfls_amt2: Optional[str] = None  # 해외실현손익금액2
    frcr_buy_amt_smtl2: Optional[str] = None  # 외화매수금액합계2
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireCcnl(SQLModel, table=True):
    """Output table for inquire_ccnl"""
    __tablename__ = "kis_inquire_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ord_dt: Optional[str] = None  # 주문일자
    ord_gno_brno: Optional[str] = None  # 주문채번지점번호
    odno: Optional[str] = None  # 주문번호
    orgn_odno: Optional[str] = None  # 원주문번호
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    sll_buy_dvsn_cd_name: Optional[str] = None  # 매도매수구분코드명
    rvse_cncl_dvsn: Optional[str] = None  # 정정취소구분
    rvse_cncl_dvsn_name: Optional[str] = None  # 정정취소구분명
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    ft_ord_qty: Optional[str] = None  # FT주문수량
    ft_ord_unpr3: Optional[str] = None  # FT주문단가3
    ft_ccld_qty: Optional[str] = None  # FT체결수량
    ft_ccld_unpr3: Optional[str] = None  # FT체결단가3
    ft_ccld_amt3: Optional[str] = None  # FT체결금액3
    nccs_qty: Optional[str] = None  # 미체결수량
    prcs_stat_name: Optional[str] = None  # 처리상태명
    rjct_rson: Optional[str] = None  # 거부사유
    rjct_rson_name: Optional[str] = None  # 거부사유명
    ord_tmd: Optional[str] = None  # 주문시각
    tr_mket_name: Optional[str] = None  # 거래시장명
    tr_crcy_cd: Optional[str] = None  # 거래통화코드
    tr_natn: Optional[str] = None  # 거래국가
    ovrs_excg_cd: Optional[str] = None  # 해외거래소코드
    tr_natn_name: Optional[str] = None  # 거래국가명
    dmst_ord_dt: Optional[str] = None  # 국내주문일자
    thco_ord_tmd: Optional[str] = None  # 당사주문시각
    loan_type_cd: Optional[str] = None  # 대출유형코드
    loan_dt: Optional[str] = None  # 대출일자
    mdia_dvsn_name: Optional[str] = None  # 매체구분명
    usa_amk_exts_rqst_yn: Optional[str] = None  # 미국애프터마켓연장신청여부
    splt_buy_attr_name: Optional[str] = None  # 분할매수/매도속성명
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDailyCcld(SQLModel, table=True):
    """Output table for inquire_daily_ccld"""
    __tablename__ = "kis_inquire_daily_ccld"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    fm_tot_ccld_qty: Optional[str] = None  # FM총체결수량
    fm_tot_futr_agrm_amt: Optional[str] = None  # FM총선물약정금액
    fm_tot_opt_agrm_amt: Optional[str] = None  # FM총옵션약정금액
    fm_fee_smtl: Optional[str] = None  # FM수수료합계
    dt: Optional[str] = None  # 일자
    ccno: Optional[str] = None  # 체결번호
    ovrs_futr_fx_pdno: Optional[str] = None  # 해외선물FX상품번호
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    fm_ccld_qty: Optional[str] = None  # FM체결수량
    fm_ccld_amt: Optional[str] = None  # FM체결금액
    fm_futr_ccld_amt: Optional[str] = None  # FM선물체결금액
    fm_opt_ccld_amt: Optional[str] = None  # FM옵션체결금액
    crcy_cd: Optional[str] = None  # 통화코드
    fm_fee: Optional[str] = None  # FM수수료
    fm_futr_pure_agrm_amt: Optional[str] = None  # FM선물순약정금액
    fm_opt_pure_agrm_amt: Optional[str] = None  # FM옵션순약정금액
    ccld_dtl_dtime: Optional[str] = None  # 체결상세일시
    ord_dt: Optional[str] = None  # 주문일자
    odno: Optional[str] = None  # 주문번호
    ord_mdia_dvsn_name: Optional[str] = None  # 주문매체구분명
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDailyItemchartprice(SQLModel, table=True):
    """Output table for inquire_daily_itemchartprice"""
    __tablename__ = "kis_inquire_daily_itemchartprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    stck_prdy_clpr: Optional[str] = None  # 주식 전일 종가
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    prdy_vol: Optional[str] = None  # 전일 거래량
    stck_mxpr: Optional[str] = None  # 주식 상한가
    stck_llam: Optional[str] = None  # 주식 하한가
    stck_oprc: Optional[str] = None  # 주식 시가2
    stck_hgpr: Optional[str] = None  # 주식 최고가
    stck_lwpr: Optional[str] = None  # 주식 최저가
    stck_prdy_oprc: Optional[str] = None  # 주식 전일 시가
    stck_prdy_hgpr: Optional[str] = None  # 주식 전일 최고가
    stck_prdy_lwpr: Optional[str] = None  # 주식 전일 최저가
    askp: Optional[str] = None  # 매도호가
    bidp: Optional[str] = None  # 매수호가
    prdy_vrss_vol: Optional[str] = None  # 전일 대비 거래량
    vol_tnrt: Optional[str] = None  # 거래량 회전율
    stck_fcam: Optional[str] = None  # 주식 액면가
    lstn_stcn: Optional[str] = None  # 상장 주수
    cpfn: Optional[str] = None  # 자본금
    hts_avls: Optional[str] = None  # HTS 시가총액
    per: Optional[str] = None  # PER
    eps: Optional[str] = None  # EPS
    pbr: Optional[str] = None  # PBR
    itewhol_loan_rmnd_ratem: Optional[str] = None  # 전체 융자 잔고 비율
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_clpr: Optional[str] = None  # 주식 종가
    flng_cls_code: Optional[str] = None  # 락 구분 코드
    prtt_rate: Optional[str] = None  # 분할 비율
    mod_yn: Optional[str] = None  # 변경 여부
    revl_issu_reas: Optional[str] = None  # 재평가사유코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDailyPrice(SQLModel, table=True):
    """Output table for inquire_daily_price"""
    __tablename__ = "kis_inquire_daily_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_oprc: Optional[str] = None  # 주식 시가2
    stck_hgpr: Optional[str] = None  # 주식 최고가
    stck_lwpr: Optional[str] = None  # 주식 최저가
    stck_clpr: Optional[str] = None  # 주식 종가
    acml_vol: Optional[str] = None  # 누적 거래량
    prdy_vrss_vol_rate: Optional[str] = None  # 전일 대비 거래량 비율
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    hts_frgn_ehrt: Optional[str] = None  # HTS 외국인 소진율
    frgn_ntby_qty: Optional[str] = None  # 외국인 순매수 수량
    flng_cls_code: Optional[str] = None  # 락 구분 코드
    acml_prtt_rate: Optional[str] = None  # 누적 분할 비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePrice(SQLModel, table=True):
    """Output table for inquire_price"""
    __tablename__ = "kis_inquire_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    proc_date: Optional[str] = None  # 최종처리일자
    high_price: Optional[str] = None  # 고가
    proc_time: Optional[str] = None  # 최종처리시각
    open_price: Optional[str] = None  # 시가
    trst_mgn: Optional[str] = None  # 증거금
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 현재가
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    bid_qntt: Optional[str] = None  # 매수1수량
    bid_price: Optional[str] = None  # 매수1호가
    ask_qntt: Optional[str] = None  # 매도1수량
    ask_price: Optional[str] = None  # 매도1호가
    prev_price: Optional[str] = None  # 전일종가
    exch_cd: Optional[str] = None  # 거래소코드
    crc_cd: Optional[str] = None  # 거래통화
    trd_fr_date: Optional[str] = None  # 상장일
    expr_date: Optional[str] = None  # 만기일
    trd_to_date: Optional[str] = None  # 최종거래일
    remn_cnt: Optional[str] = None  # 잔존일수
    last_qntt: Optional[str] = None  # 체결량
    tot_ask_qntt: Optional[str] = None  # 총매도잔량
    tot_bid_qntt: Optional[str] = None  # 총매수잔량
    tick_size: Optional[str] = None  # 틱사이즈
    open_date: Optional[str] = None  # 장개시일자
    open_time: Optional[str] = None  # 장개시시각
    close_date: Optional[str] = None  # 장종료일자
    close_time: Optional[str] = None  # 장종료시각
    sbsnsdate: Optional[str] = None  # 영업일자
    sttl_price: Optional[str] = None  # 정산가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePsblOrder(SQLModel, table=True):
    """Output table for inquire_psbl_order"""
    __tablename__ = "kis_inquire_psbl_order"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ord_psbl_cash: Optional[str] = None  # 주문가능현금
    ord_psbl_sbst: Optional[str] = None  # 주문가능대용
    ruse_psbl_amt: Optional[str] = None  # 재사용가능금액
    fund_rpch_chgs: Optional[str] = None  # 펀드환매대금
    psbl_qty_calc_unpr: Optional[str] = None  # 가능수량계산단가
    nrcvb_buy_amt: Optional[str] = None  # 미수없는매수금액
    nrcvb_buy_qty: Optional[str] = None  # 미수없는매수수량
    max_buy_amt: Optional[str] = None  # 최대매수금액
    max_buy_qty: Optional[str] = None  # 최대매수수량
    cma_evlu_amt: Optional[str] = None  # CMA평가금액
    ovrs_re_use_amt_wcrc: Optional[str] = None  # 해외재사용금액원화
    ord_psbl_frcr_amt_wcrc: Optional[str] = None  # 주문가능외화금액원화
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePsblRvsecncl(SQLModel, table=True):
    """Output table for inquire_psbl_rvsecncl"""
    __tablename__ = "kis_inquire_psbl_rvsecncl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ord_gno_brno: Optional[str] = None  # 주문채번지점번호
    odno: Optional[str] = None  # 주문번호
    orgn_odno: Optional[str] = None  # 원주문번호
    ord_dvsn_name: Optional[str] = None  # 주문구분명
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    rvse_cncl_dvsn_name: Optional[str] = None  # 정정취소구분명
    ord_qty: Optional[str] = None  # 주문수량
    ord_unpr: Optional[str] = None  # 주문단가
    ord_tmd: Optional[str] = None  # 주문시각
    tot_ccld_qty: Optional[str] = None  # 총체결수량
    tot_ccld_amt: Optional[str] = None  # 총체결금액
    psbl_qty: Optional[str] = None  # 가능수량
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    ord_dvsn_cd: Optional[str] = None  # 주문구분코드
    mgco_aptm_odno: Optional[str] = None  # 운용사지정주문번호
    excg_dvsn_cd: Optional[str] = None  # 거래소구분코드
    excg_id_dvsn_cd: Optional[str] = None  # 거래소ID구분코드
    excg_id_dvsn_name: Optional[str] = None  # 거래소ID구분명
    stpm_cndt_pric: Optional[str] = None  # 스톱지정가조건가격
    stpm_efct_occr_yn: Optional[str] = None  # 스톱지정가효력발생여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IssueInfo(SQLModel, table=True):
    """Output table for issue_info"""
    __tablename__ = "kis_issue_info"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pdno: Optional[str] = None  # 상품번호
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    prdt_name: Optional[str] = None  # 상품명
    prdt_eng_name: Optional[str] = None  # 상품영문명
    ivst_heed_prdt_yn: Optional[str] = None  # 투자유의상품여부
    exts_yn: Optional[str] = None  # 연장여부
    bond_clsf_cd: Optional[str] = None  # 채권분류코드
    bond_clsf_kor_name: Optional[str] = None  # 채권분류한글명
    papr: Optional[str] = None  # 액면가
    int_mned_dvsn_cd: Optional[str] = None  # 이자월말구분코드
    rvnu_shap_cd: Optional[str] = None  # 매출형태코드
    issu_amt: Optional[str] = None  # 발행금액
    lstg_rmnd: Optional[str] = None  # 상장잔액
    int_dfrm_mcnt: Optional[str] = None  # 이자지급개월수
    bond_int_dfrm_mthd_cd: Optional[str] = None  # 채권이자지급방법코드
    splt_rdpt_rcnt: Optional[str] = None  # 분할상환횟수
    prca_dfmt_term_mcnt: Optional[str] = None  # 원금거치기간개월수
    int_anap_dvsn_cd: Optional[str] = None  # 이자선후급구분코드
    bond_rght_dvsn_cd: Optional[str] = None  # 채권권리구분코드
    prdt_pclc_text: Optional[str] = None  # 상품특성내용
    prdt_abrv_name: Optional[str] = None  # 상품약어명
    prdt_eng_abrv_name: Optional[str] = None  # 상품영문약어명
    sprx_psbl_yn: Optional[str] = None  # 분리과세가능여부
    pbff_pplc_ofrg_mthd_cd: Optional[str] = None  # 공모사모모집방법코드
    cmco_cd: Optional[str] = None  # 주간사코드
    issu_istt_cd: Optional[str] = None  # 발행기관코드
    issu_istt_name: Optional[str] = None  # 발행기관명
    pnia_dfrm_agcy_istt_cd: Optional[str] = None  # 원리금지급대행기관코드
    dsct_ec_rt: Optional[str] = None  # 할인할증율
    srfc_inrt: Optional[str] = None  # 표면이율
    expd_rdpt_rt: Optional[str] = None  # 만기상환율
    expd_asrc_erng_rt: Optional[str] = None  # 만기보장수익율
    bond_grte_istt_name: Optional[str] = None  # 채권보증기관명
    int_dfrm_day_type_cd: Optional[str] = None  # 이자지급일유형코드
    ksd_int_calc_unit_cd: Optional[str] = None  # 증권예탁결제원이자계산단위코드
    int_wunt_uder_prcs_dvsn_cd: Optional[str] = None  # 이자원화단위미만처리구분코드
    rvnu_dt: Optional[str] = None  # 매출일자
    issu_dt: Optional[str] = None  # 발행일자
    lstg_dt: Optional[str] = None  # 상장일자
    expd_dt: Optional[str] = None  # 만기일자
    rdpt_dt: Optional[str] = None  # 상환일자
    sbst_pric: Optional[str] = None  # 대용가격
    rgbf_int_dfrm_dt: Optional[str] = None  # 직전이자지급일자
    nxtm_int_dfrm_dt: Optional[str] = None  # 차기이자지급일자
    frst_int_dfrm_dt: Optional[str] = None  # 최초이자지급일자
    ecis_pric: Optional[str] = None  # 행사가격
    rght_stck_std_pdno: Optional[str] = None  # 권리주식표준상품번호
    ecis_opng_dt: Optional[str] = None  # 행사개시일자
    ecis_end_dt: Optional[str] = None  # 행사종료일자
    bond_rvnu_mthd_cd: Optional[str] = None  # 채권매출방법코드
    oprt_stfno: Optional[str] = None  # 조작직원번호
    oprt_stff_name: Optional[str] = None  # 조작직원명
    rgbf_int_dfrm_wday: Optional[str] = None  # 직전이자지급요일
    nxtm_int_dfrm_wday: Optional[str] = None  # 차기이자지급요일
    kis_crdt_grad_text: Optional[str] = None  # 한국신용평가신용등급내용
    kbp_crdt_grad_text: Optional[str] = None  # 한국채권평가신용등급내용
    nice_crdt_grad_text: Optional[str] = None  # 한국신용정보신용등급내용
    fnp_crdt_grad_text: Optional[str] = None  # 에프앤자산평가신용등급내용
    dpsi_psbl_yn: Optional[str] = None  # 예탁가능여부
    pnia_int_calc_unpr: Optional[str] = None  # 원리금이자계산단가
    prcm_idx_bond_yn: Optional[str] = None  # 물가지수채권여부
    expd_exts_srdp_rcnt: Optional[str] = None  # 만기연장분할상환횟수
    expd_exts_srdp_rt: Optional[str] = None  # 만기연장분할상환율
    loan_psbl_yn: Optional[str] = None  # 대출가능여부
    grte_dvsn_cd: Optional[str] = None  # 보증구분코드
    fnrr_rank_dvsn_cd: Optional[str] = None  # 선후순위구분코드
    krx_lstg_abol_dvsn_cd: Optional[str] = None  # 한국거래소상장폐지구분코드
    asst_rqdi_dvsn_cd: Optional[str] = None  # 자산유동화구분코드
    opcb_dvsn_cd: Optional[str] = None  # 옵션부사채구분코드
    crfd_item_yn: Optional[str] = None  # 크라우드펀딩종목여부
    crfd_item_rstc_cclc_dt: Optional[str] = None  # 크라우드펀딩종목제한해지일자
    bond_nmpr_unit_pric: Optional[str] = None  # 채권호가단위가격
    ivst_heed_bond_dvsn_name: Optional[str] = None  # 투자유의채권구분명
    add_erng_rt: Optional[str] = None  # 추가수익율
    add_erng_rt_aply_dt: Optional[str] = None  # 추가수익율적용일자
    bond_tr_stop_dvsn_cd: Optional[str] = None  # 채권거래정지구분코드
    ivst_heed_bond_dvsn_cd: Optional[str] = None  # 투자유의채권구분코드
    pclr_cndt_text: Optional[str] = None  # 특이조건내용
    hbbd_yn: Optional[str] = None  # 하이브리드채권여부
    cdtl_cptl_scty_type_cd: Optional[str] = None  # 조건부자본증권유형코드
    elec_scty_yn: Optional[str] = None  # 전자증권여부
    sq1_clop_ecis_opng_dt: Optional[str] = None  # 1차콜옵션행사개시일자
    frst_erlm_stfno: Optional[str] = None  # 최초등록직원번호
    frst_erlm_dt: Optional[str] = None  # 최초등록일자
    frst_erlm_tmd: Optional[str] = None  # 최초등록시각
    tlg_rcvg_dtl_dtime: Optional[str] = None  # 전문수신상세일시
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OrderRvsecncl(SQLModel, table=True):
    """Output table for order_rvsecncl"""
    __tablename__ = "kis_order_rvsecncl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    KRX_FWDG_ORD_ORGNO: Optional[str] = None  # 한국거래소전송주문조직번호
    ODNO: Optional[str] = None  # 주문번호
    ORD_TMD: Optional[str] = None  # 주문시각
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SearchBondInfo(SQLModel, table=True):
    """Output table for search_bond_info"""
    __tablename__ = "kis_search_bond_info"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pdno: Optional[str] = None  # 상품번호
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    ksd_bond_item_name: Optional[str] = None  # 증권예탁결제원채권종목명
    ksd_bond_item_eng_name: Optional[str] = None  # 증권예탁결제원채권종목영문명
    ksd_bond_lstg_type_cd: Optional[str] = None  # 증권예탁결제원채권상장유형코드
    ksd_ofrg_dvsn_cd: Optional[str] = None  # 증권예탁결제원모집구분코드
    ksd_bond_int_dfrm_dvsn_cd: Optional[str] = None  # 증권예탁결제원채권이자지급구분
    issu_dt: Optional[str] = None  # 발행일자
    rdpt_dt: Optional[str] = None  # 상환일자
    rvnu_dt: Optional[str] = None  # 매출일자
    iso_crcy_cd: Optional[str] = None  # 통화코드
    mdwy_rdpt_dt: Optional[str] = None  # 중도상환일자
    ksd_rcvg_bond_dsct_rt: Optional[str] = None  # 증권예탁결제원수신채권할인율
    ksd_rcvg_bond_srfc_inrt: Optional[str] = None  # 증권예탁결제원수신채권표면이율
    bond_expd_rdpt_rt: Optional[str] = None  # 채권만기상환율
    ksd_prca_rdpt_mthd_cd: Optional[str] = None  # 증권예탁결제원원금상환방법코드
    int_caltm_mcnt: Optional[str] = None  # 이자계산기간개월수
    ksd_int_calc_unit_cd: Optional[str] = None  # 증권예탁결제원이자계산단위코드
    uval_cut_dvsn_cd: Optional[str] = None  # 절상절사구분코드
    uval_cut_dcpt_dgit: Optional[str] = None  # 절상절사소수점자릿수
    ksd_dydv_caltm_aply_dvsn_cd: Optional[str] = None  # 증권예탁결제원일할계산기간적용
    dydv_calc_dcnt: Optional[str] = None  # 일할계산일수
    bond_expd_asrc_erng_rt: Optional[str] = None  # 채권만기보장수익율
    padf_plac_hdof_name: Optional[str] = None  # 원리금지급장소본점명
    lstg_dt: Optional[str] = None  # 상장일자
    lstg_abol_dt: Optional[str] = None  # 상장폐지일자
    ksd_bond_issu_mthd_cd: Optional[str] = None  # 증권예탁결제원채권발행방법코드
    laps_indf_yn: Optional[str] = None  # 경과이자지급여부
    ksd_lhdy_pnia_dfrm_mthd_cd: Optional[str] = None  # 증권예탁결제원공휴일원리금지급
    frst_int_dfrm_dt: Optional[str] = None  # 최초이자지급일자
    ksd_prcm_lnkg_gvbd_yn: Optional[str] = None  # 증권예탁결제원물가연동국고채여
    dpsi_end_dt: Optional[str] = None  # 예탁종료일자
    dpsi_strt_dt: Optional[str] = None  # 예탁시작일자
    dpsi_psbl_yn: Optional[str] = None  # 예탁가능여부
    atyp_rdpt_bond_erlm_yn: Optional[str] = None  # 비정형상환채권등록여부
    dshn_occr_yn: Optional[str] = None  # 부도발생여부
    expd_exts_yn: Optional[str] = None  # 만기연장여부
    pclr_ptcr_text: Optional[str] = None  # 특이사항내용
    dpsi_psbl_excp_stat_cd: Optional[str] = None  # 예탁가능예외상태코드
    expd_exts_srdp_rcnt: Optional[str] = None  # 만기연장분할상환횟수
    expd_exts_srdp_rt: Optional[str] = None  # 만기연장분할상환율
    expd_rdpt_rt: Optional[str] = None  # 만기상환율
    expd_asrc_erng_rt: Optional[str] = None  # 만기보장수익율
    bond_int_dfrm_mthd_cd: Optional[str] = None  # 채권이자지급방법코드
    int_dfrm_day_type_cd: Optional[str] = None  # 이자지급일유형코드
    prca_dfmt_term_mcnt: Optional[str] = None  # 원금거치기간개월수
    splt_rdpt_rcnt: Optional[str] = None  # 분할상환횟수
    rgbf_int_dfrm_dt: Optional[str] = None  # 직전이자지급일자
    nxtm_int_dfrm_dt: Optional[str] = None  # 차기이자지급일자
    sprx_psbl_yn: Optional[str] = None  # 분리과세가능여부
    ictx_rt_dvsn_cd: Optional[str] = None  # 소득세율구분코드
    bond_clsf_cd: Optional[str] = None  # 채권분류코드
    bond_clsf_kor_name: Optional[str] = None  # 채권분류한글명
    int_mned_dvsn_cd: Optional[str] = None  # 이자월말구분코드
    pnia_int_calc_unpr: Optional[str] = None  # 원리금이자계산단가
    frn_intr: Optional[str] = None  # FRN금리
    aply_day_prcm_idx_lnkg_cefc: Optional[str] = None  # 적용일물가지수연동계수
    ksd_expd_dydv_calc_bass_cd: Optional[str] = None  # 증권예탁결제원만기일할계산기준
    expd_dydv_calc_dcnt: Optional[str] = None  # 만기일할계산일수
    ksd_cbbw_dvsn_cd: Optional[str] = None  # 증권예탁결제원신종사채구분코드
    crfd_item_yn: Optional[str] = None  # 크라우드펀딩종목여부
    pnia_bank_ofdy_dfrm_mthd_cd: Optional[str] = None  # 원리금은행휴무일지급방법코드
    qib_yn: Optional[str] = None  # QIB여부
    qib_cclc_dt: Optional[str] = None  # QIB해지일자
    csbd_yn: Optional[str] = None  # 영구채여부
    csbd_cclc_dt: Optional[str] = None  # 영구채해지일자
    ksd_opcb_yn: Optional[str] = None  # 증권예탁결제원옵션부사채여부
    ksd_sodn_yn: Optional[str] = None  # 증권예탁결제원후순위채권여부
    ksd_rqdi_scty_yn: Optional[str] = None  # 증권예탁결제원유동화증권여부
    elec_scty_yn: Optional[str] = None  # 전자증권여부
    rght_ecis_mbdy_dvsn_cd: Optional[str] = None  # 권리행사주체구분코드
    int_rkng_mthd_dvsn_cd: Optional[str] = None  # 이자산정방법구분코드
    ofrg_dvsn_cd: Optional[str] = None  # 모집구분코드
    ksd_tot_issu_amt: Optional[str] = None  # 증권예탁결제원총발행금액
    next_indf_chk_ecls_yn: Optional[str] = None  # 다음이자지급체크제외여부
    ksd_bond_intr_dvsn_cd: Optional[str] = None  # 증권예탁결제원채권금리구분코드
    ksd_inrt_aply_dvsn_cd: Optional[str] = None  # 증권예탁결제원이율적용구분코드
    krx_issu_istt_cd: Optional[str] = None  # KRX발행기관코드
    ksd_indf_frqc_uder_calc_cd: Optional[str] = None  # 증권예탁결제원이자지급주기미만
    ksd_indf_frqc_uder_calc_dcnt: Optional[str] = None  # 증권예탁결제원이자지급주기미만
    tlg_rcvg_dtl_dtime: Optional[str] = None  # 전문수신상세일시
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Sell(SQLModel, table=True):
    """Output table for sell"""
    __tablename__ = "kis_sell"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    KRX_FWDG_ORD_ORGNO: Optional[str] = None  # 한국거래소전송주문조직번호
    ODNO: Optional[str] = None  # 주문번호
    ORD_TMD: Optional[str] = None  # 주문시각
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CommodityFuturesRealtimeConclusion(SQLModel, table=True):
    """Output table for commodity_futures_realtime_conclusion"""
    __tablename__ = "kis_commodity_futures_realtime_conclusion"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_shrn_iscd: Optional[str] = None  # 선물 단축 종목코드
    bsop_hour: Optional[str] = None  # 영업 시간
    futs_prdy_vrss: Optional[str] = None  # 선물 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    futs_prdy_ctrt: Optional[str] = None  # 선물 전일 대비율
    futs_prpr: Optional[str] = None  # 선물 현재가
    futs_oprc: Optional[str] = None  # 선물 시가2
    futs_hgpr: Optional[str] = None  # 선물 최고가
    futs_lwpr: Optional[str] = None  # 선물 최저가
    last_cnqn: Optional[str] = None  # 최종 거래량
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    hts_thpr: Optional[str] = None  # HTS 이론가
    mrkt_basis: Optional[str] = None  # 시장 베이시스
    dprt: Optional[str] = None  # 괴리율
    nmsc_fctn_stpl_prc: Optional[str] = None  # 근월물 약정가
    fmsc_fctn_stpl_prc: Optional[str] = None  # 원월물 약정가
    spead_prc: Optional[str] = None  # 스프레드1
    hts_otst_stpl_qty: Optional[str] = None  # HTS 미결제 약정 수량
    otst_stpl_qty_icdc: Optional[str] = None  # 미결제 약정 수량 증감
    oprc_hour: Optional[str] = None  # 시가 시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2 대비 현재가 부호
    oprc_vrss_nmix_prpr: Optional[str] = None  # 시가 대비 지수 현재가
    hgpr_hour: Optional[str] = None  # 최고가 시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가 대비 현재가 부호
    hgpr_vrss_nmix_prpr: Optional[str] = None  # 최고가 대비 지수 현재가
    lwpr_hour: Optional[str] = None  # 최저가 시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가 대비 현재가 부호
    lwpr_vrss_nmix_prpr: Optional[str] = None  # 최저가 대비 지수 현재가
    shnu_rate: Optional[str] = None  # 매수2 비율
    cttr: Optional[str] = None  # 체결강도
    esdg: Optional[str] = None  # 괴리도
    otst_stpl_rgbf_qty_icdc: Optional[str] = None  # 미결제 약정 직전 수량 증감
    thpr_basis: Optional[str] = None  # 이론 베이시스
    futs_askp1: Optional[str] = None  # 선물 매도호가1
    futs_bidp1: Optional[str] = None  # 선물 매수호가1
    askp_rsqn1: Optional[str] = None  # 매도호가 잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가 잔량1
    seln_cntg_csnu: Optional[str] = None  # 매도 체결 건수
    shnu_cntg_csnu: Optional[str] = None  # 매수 체결 건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수 체결 건수
    seln_cntg_smtn: Optional[str] = None  # 총 매도 수량
    shnu_cntg_smtn: Optional[str] = None  # 총 매수 수량
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일 거래량 대비 등락율
    dscs_bltr_acml_qty: Optional[str] = None  # 협의 대량 거래량
    dynm_mxpr: Optional[str] = None  # 실시간상한가
    dynm_llam: Optional[str] = None  # 실시간하한가
    dynm_prc_limt_yn: Optional[str] = None  # 실시간가격제한구분
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CommodityFuturesRealtimeQuote(SQLModel, table=True):
    """Output table for commodity_futures_realtime_quote"""
    __tablename__ = "kis_commodity_futures_realtime_quote"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_shrn_iscd: Optional[str] = None  # 선물 단축 종목코드
    bsop_hour: Optional[str] = None  # 영업 시간
    futs_askp1: Optional[str] = None  # 선물 매도호가1
    futs_askp2: Optional[str] = None  # 선물 매도호가2
    futs_askp3: Optional[str] = None  # 선물 매도호가3
    futs_askp4: Optional[str] = None  # 선물 매도호가4
    futs_askp5: Optional[str] = None  # 선물 매도호가5
    futs_bidp1: Optional[str] = None  # 선물 매수호가1
    futs_bidp2: Optional[str] = None  # 선물 매수호가2
    futs_bidp3: Optional[str] = None  # 선물 매수호가3
    futs_bidp4: Optional[str] = None  # 선물 매수호가4
    futs_bidp5: Optional[str] = None  # 선물 매수호가5
    askp_csnu1: Optional[str] = None  # 매도호가 건수1
    askp_csnu2: Optional[str] = None  # 매도호가 건수2
    askp_csnu3: Optional[str] = None  # 매도호가 건수3
    askp_csnu4: Optional[str] = None  # 매도호가 건수4
    askp_csnu5: Optional[str] = None  # 매도호가 건수5
    bidp_csnu1: Optional[str] = None  # 매수호가 건수1
    bidp_csnu2: Optional[str] = None  # 매수호가 건수2
    bidp_csnu3: Optional[str] = None  # 매수호가 건수3
    bidp_csnu4: Optional[str] = None  # 매수호가 건수4
    bidp_csnu5: Optional[str] = None  # 매수호가 건수5
    askp_rsqn1: Optional[str] = None  # 매도호가 잔량1
    askp_rsqn2: Optional[str] = None  # 매도호가 잔량2
    askp_rsqn3: Optional[str] = None  # 매도호가 잔량3
    askp_rsqn4: Optional[str] = None  # 매도호가 잔량4
    askp_rsqn5: Optional[str] = None  # 매도호가 잔량5
    bidp_rsqn1: Optional[str] = None  # 매수호가 잔량1
    bidp_rsqn2: Optional[str] = None  # 매수호가 잔량2
    bidp_rsqn3: Optional[str] = None  # 매수호가 잔량3
    bidp_rsqn4: Optional[str] = None  # 매수호가 잔량4
    bidp_rsqn5: Optional[str] = None  # 매수호가 잔량5
    total_askp_csnu: Optional[str] = None  # 총 매도호가 건수
    total_bidp_csnu: Optional[str] = None  # 총 매수호가 건수
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    total_askp_rsqn_icdc: Optional[str] = None  # 총 매도호가 잔량 증감
    total_bidp_rsqn_icdc: Optional[str] = None  # 총 매수호가 잔량 증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DisplayBoardCallput(SQLModel, table=True):
    """Output table for display_board_callput"""
    __tablename__ = "kis_display_board_callput"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    acpr: Optional[str] = None  # 행사가
    unch_prpr: Optional[str] = None  # 환산 현재가
    optn_shrn_iscd: Optional[str] = None  # 옵션 단축 종목코드
    optn_prpr: Optional[str] = None  # 옵션 현재가
    optn_prdy_vrss: Optional[str] = None  # 옵션 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    optn_prdy_ctrt: Optional[str] = None  # 옵션 전일 대비율
    optn_bidp: Optional[str] = None  # 옵션 매수호가
    optn_askp: Optional[str] = None  # 옵션 매도호가
    tmvl_val: Optional[str] = None  # 시간가치 값
    nmix_sdpr: Optional[str] = None  # 지수 기준가
    acml_vol: Optional[str] = None  # 누적 거래량
    seln_rsqn: Optional[str] = None  # 매도 잔량
    shnu_rsqn: Optional[str] = None  # 매수2 잔량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    hts_otst_stpl_qty: Optional[str] = None  # HTS 미결제 약정 수량
    otst_stpl_qty_icdc: Optional[str] = None  # 미결제 약정 수량 증감
    delta_val: Optional[str] = None  # 델타 값
    gama: Optional[str] = None  # 감마
    vega: Optional[str] = None  # 베가
    theta: Optional[str] = None  # 세타
    rho: Optional[str] = None  # 로우
    hts_ints_vltl: Optional[str] = None  # HTS 내재 변동성
    invl_val: Optional[str] = None  # 내재가치 값
    esdg: Optional[str] = None  # 괴리도
    dprt: Optional[str] = None  # 괴리율
    hist_vltl: Optional[str] = None  # 역사적 변동성
    hts_thpr: Optional[str] = None  # HTS 이론가
    optn_oprc: Optional[str] = None  # 옵션 시가2
    optn_hgpr: Optional[str] = None  # 옵션 최고가
    optn_lwpr: Optional[str] = None  # 옵션 최저가
    optn_mxpr: Optional[str] = None  # 옵션 상한가
    optn_llam: Optional[str] = None  # 옵션 하한가
    atm_cls_name: Optional[str] = None  # ATM 구분 명
    rgbf_vrss_icdc: Optional[str] = None  # 직전 대비 증감
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    futs_antc_cnpr: Optional[str] = None  # 선물예상체결가
    futs_antc_cntg_vrss: Optional[str] = None  # 선물예상체결대비
    antc_cntg_vrss_sign: Optional[str] = None  # 예상 체결 대비 부호
    antc_cntg_prdy_ctrt: Optional[str] = None  # 예상 체결 전일 대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DisplayBoardFutures(SQLModel, table=True):
    """Output table for display_board_futures"""
    __tablename__ = "kis_display_board_futures"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_shrn_iscd: Optional[str] = None  # 선물 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    futs_prpr: Optional[str] = None  # 선물 현재가
    futs_prdy_vrss: Optional[str] = None  # 선물 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    futs_prdy_ctrt: Optional[str] = None  # 선물 전일 대비율
    hts_thpr: Optional[str] = None  # HTS 이론가
    acml_vol: Optional[str] = None  # 누적 거래량
    futs_askp: Optional[str] = None  # 선물 매도호가
    futs_bidp: Optional[str] = None  # 선물 매수호가
    hts_otst_stpl_qty: Optional[str] = None  # HTS 미결제 약정 수량
    futs_hgpr: Optional[str] = None  # 선물 최고가
    futs_lwpr: Optional[str] = None  # 선물 최저가
    hts_rmnn_dynu: Optional[str] = None  # HTS 잔존 일수
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    futs_antc_cnpr: Optional[str] = None  # 선물예상체결가
    futs_antc_cntg_vrss: Optional[str] = None  # 선물예상체결대비
    antc_cntg_vrss_sign: Optional[str] = None  # 예상 체결 대비 부호
    antc_cntg_prdy_ctrt: Optional[str] = None  # 예상 체결 전일 대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DisplayBoardOptionList(SQLModel, table=True):
    """Output table for display_board_option_list"""
    __tablename__ = "kis_display_board_option_list"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mtrt_yymm_code: Optional[str] = None  # 만기 년월 코드
    mtrt_yymm: Optional[str] = None  # 만기 년월
    
    created_at: datetime = Field(default_factory=datetime.utcnow)





class ExpPriceTrend(SQLModel, table=True):
    """Output table for exp_price_trend"""
    __tablename__ = "kis_exp_price_trend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    rprs_mrkt_kor_name: Optional[str] = None  # 대표 시장 한글 명
    antc_cnpr: Optional[str] = None  # 예상 체결가
    antc_cntg_vrss_sign: Optional[str] = None  # 예상 체결 대비 부호
    antc_cntg_vrss: Optional[str] = None  # 예상 체결 대비
    antc_cntg_prdy_ctrt: Optional[str] = None  # 예상 체결 전일 대비율
    antc_vol: Optional[str] = None  # 예상 거래량
    antc_tr_pbmn: Optional[str] = None  # 예상 거래대금
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FuoptCcnlNotice(SQLModel, table=True):
    """Output table for fuopt_ccnl_notice"""
    __tablename__ = "kis_fuopt_ccnl_notice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cust_id: Optional[str] = None  # 고객 ID
    acnt_no: Optional[str] = None  # 계좌번호
    oder_no: Optional[str] = None  # 주문번호
    ooder_no: Optional[str] = None  # 원주문번호
    seln_byov_cls: Optional[str] = None  # 매도매수구분
    rctf_cls: Optional[str] = None  # 정정구분
    oder_kind2: Optional[str] = None  # 주문종류2
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    cntg_qty: Optional[str] = None  # 체결 수량
    cntg_unpr: Optional[str] = None  # 체결단가
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    rfus_yn: Optional[str] = None  # 거부여부
    cntg_yn: Optional[str] = None  # 체결여부
    acpt_yn: Optional[str] = None  # 접수여부
    brnc_no: Optional[str] = None  # 지점번호
    oder_qty: Optional[str] = None  # 주문수량
    acnt_name: Optional[str] = None  # 계좌명
    cntg_isnm: Optional[str] = None  # 체결종목명
    oder_cond: Optional[str] = None  # 주문조건
    ord_grp: Optional[str] = None  # 주문그룹ID
    ord_grpseq: Optional[str] = None  # 주문그룹SEQ
    order_prc: Optional[str] = None  # 주문가격
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FuturesExpCcnl(SQLModel, table=True):
    """Output table for futures_exp_ccnl"""
    __tablename__ = "kis_futures_exp_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_shrn_iscd: Optional[str] = None  # 선물단축종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    antc_cnpr: Optional[str] = None  # 예상체결가
    antc_cntg_vrss: Optional[str] = None  # 예상체결대비
    antc_cntg_vrss_sign: Optional[str] = None  # 예상체결대비부호
    antc_cntg_prdy_ctrt: Optional[str] = None  # 예상체결전일대비율
    antc_mkop_cls_code: Optional[str] = None  # 예상장운영구분코드
    antc_cnqn: Optional[str] = None  # 예상체결수량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndexFuturesRealtimeConclusion(SQLModel, table=True):
    """Output table for index_futures_realtime_conclusion"""
    __tablename__ = "kis_index_futures_realtime_conclusion"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_shrn_iscd: Optional[str] = None  # 선물 단축 종목코드
    bsop_hour: Optional[str] = None  # 영업 시간
    futs_prdy_vrss: Optional[str] = None  # 선물 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    futs_prdy_ctrt: Optional[str] = None  # 선물 전일 대비율
    futs_prpr: Optional[str] = None  # 선물 현재가
    futs_oprc: Optional[str] = None  # 선물 시가2
    futs_hgpr: Optional[str] = None  # 선물 최고가
    futs_lwpr: Optional[str] = None  # 선물 최저가
    last_cnqn: Optional[str] = None  # 최종 거래량
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    hts_thpr: Optional[str] = None  # HTS 이론가
    mrkt_basis: Optional[str] = None  # 시장 베이시스
    dprt: Optional[str] = None  # 괴리율
    nmsc_fctn_stpl_prc: Optional[str] = None  # 근월물 약정가
    fmsc_fctn_stpl_prc: Optional[str] = None  # 원월물 약정가
    spead_prc: Optional[str] = None  # 스프레드1
    hts_otst_stpl_qty: Optional[str] = None  # HTS 미결제 약정 수량
    otst_stpl_qty_icdc: Optional[str] = None  # 미결제 약정 수량 증감
    oprc_hour: Optional[str] = None  # 시가 시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2 대비 현재가 부호
    oprc_vrss_nmix_prpr: Optional[str] = None  # 시가 대비 지수 현재가
    hgpr_hour: Optional[str] = None  # 최고가 시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가 대비 현재가 부호
    hgpr_vrss_nmix_prpr: Optional[str] = None  # 최고가 대비 지수 현재가
    lwpr_hour: Optional[str] = None  # 최저가 시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가 대비 현재가 부호
    lwpr_vrss_nmix_prpr: Optional[str] = None  # 최저가 대비 지수 현재가
    shnu_rate: Optional[str] = None  # 매수2 비율
    cttr: Optional[str] = None  # 체결강도
    esdg: Optional[str] = None  # 괴리도
    otst_stpl_rgbf_qty_icdc: Optional[str] = None  # 미결제 약정 직전 수량 증감
    thpr_basis: Optional[str] = None  # 이론 베이시스
    futs_askp1: Optional[str] = None  # 선물 매도호가1
    futs_bidp1: Optional[str] = None  # 선물 매수호가1
    askp_rsqn1: Optional[str] = None  # 매도호가 잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가 잔량1
    seln_cntg_csnu: Optional[str] = None  # 매도 체결 건수
    shnu_cntg_csnu: Optional[str] = None  # 매수 체결 건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수 체결 건수
    seln_cntg_smtn: Optional[str] = None  # 총 매도 수량
    shnu_cntg_smtn: Optional[str] = None  # 총 매수 수량
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일 거래량 대비 등락율
    dscs_bltr_acml_qty: Optional[str] = None  # 협의 대량 거래량
    dynm_mxpr: Optional[str] = None  # 실시간상한가
    dynm_llam: Optional[str] = None  # 실시간하한가
    dynm_prc_limt_yn: Optional[str] = None  # 실시간가격제한구분
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndexFuturesRealtimeQuote(SQLModel, table=True):
    """Output table for index_futures_realtime_quote"""
    __tablename__ = "kis_index_futures_realtime_quote"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_shrn_iscd: Optional[str] = None  # 선물 단축 종목코드
    bsop_hour: Optional[str] = None  # 영업 시간
    futs_askp1: Optional[str] = None  # 선물 매도호가1
    futs_askp2: Optional[str] = None  # 선물 매도호가2
    futs_askp3: Optional[str] = None  # 선물 매도호가3
    futs_askp4: Optional[str] = None  # 선물 매도호가4
    futs_askp5: Optional[str] = None  # 선물 매도호가5
    futs_bidp1: Optional[str] = None  # 선물 매수호가1
    futs_bidp2: Optional[str] = None  # 선물 매수호가2
    futs_bidp3: Optional[str] = None  # 선물 매수호가3
    futs_bidp4: Optional[str] = None  # 선물 매수호가4
    futs_bidp5: Optional[str] = None  # 선물 매수호가5
    askp_csnu1: Optional[str] = None  # 매도호가 건수1
    askp_csnu2: Optional[str] = None  # 매도호가 건수2
    askp_csnu3: Optional[str] = None  # 매도호가 건수3
    askp_csnu4: Optional[str] = None  # 매도호가 건수4
    askp_csnu5: Optional[str] = None  # 매도호가 건수5
    bidp_csnu1: Optional[str] = None  # 매수호가 건수1
    bidp_csnu2: Optional[str] = None  # 매수호가 건수2
    bidp_csnu3: Optional[str] = None  # 매수호가 건수3
    bidp_csnu4: Optional[str] = None  # 매수호가 건수4
    bidp_csnu5: Optional[str] = None  # 매수호가 건수5
    askp_rsqn1: Optional[str] = None  # 매도호가 잔량1
    askp_rsqn2: Optional[str] = None  # 매도호가 잔량2
    askp_rsqn3: Optional[str] = None  # 매도호가 잔량3
    askp_rsqn4: Optional[str] = None  # 매도호가 잔량4
    askp_rsqn5: Optional[str] = None  # 매도호가 잔량5
    bidp_rsqn1: Optional[str] = None  # 매수호가 잔량1
    bidp_rsqn2: Optional[str] = None  # 매수호가 잔량2
    bidp_rsqn3: Optional[str] = None  # 매수호가 잔량3
    bidp_rsqn4: Optional[str] = None  # 매수호가 잔량4
    bidp_rsqn5: Optional[str] = None  # 매수호가 잔량5
    total_askp_csnu: Optional[str] = None  # 총 매도호가 건수
    total_bidp_csnu: Optional[str] = None  # 총 매수호가 건수
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    total_askp_rsqn_icdc: Optional[str] = None  # 총 매도호가 잔량 증감
    total_bidp_rsqn_icdc: Optional[str] = None  # 총 매수호가 잔량 증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndexOptionRealtimeConclusion(SQLModel, table=True):
    """Output table for index_option_realtime_conclusion"""
    __tablename__ = "kis_index_option_realtime_conclusion"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    optn_shrn_iscd: Optional[str] = None  # 옵션 단축 종목코드
    bsop_hour: Optional[str] = None  # 영업 시간
    optn_prpr: Optional[str] = None  # 옵션 현재가
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    optn_prdy_vrss: Optional[str] = None  # 옵션 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    optn_oprc: Optional[str] = None  # 옵션 시가2
    optn_hgpr: Optional[str] = None  # 옵션 최고가
    optn_lwpr: Optional[str] = None  # 옵션 최저가
    last_cnqn: Optional[str] = None  # 최종 거래량
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    hts_thpr: Optional[str] = None  # HTS 이론가
    hts_otst_stpl_qty: Optional[str] = None  # HTS 미결제 약정 수량
    otst_stpl_qty_icdc: Optional[str] = None  # 미결제 약정 수량 증감
    oprc_hour: Optional[str] = None  # 시가 시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2 대비 현재가 부호
    oprc_vrss_nmix_prpr: Optional[str] = None  # 시가 대비 지수 현재가
    hgpr_hour: Optional[str] = None  # 최고가 시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가 대비 현재가 부호
    hgpr_vrss_nmix_prpr: Optional[str] = None  # 최고가 대비 지수 현재가
    lwpr_hour: Optional[str] = None  # 최저가 시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가 대비 현재가 부호
    lwpr_vrss_nmix_prpr: Optional[str] = None  # 최저가 대비 지수 현재가
    shnu_rate: Optional[str] = None  # 매수2 비율
    prmm_val: Optional[str] = None  # 프리미엄 값
    invl_val: Optional[str] = None  # 내재가치 값
    tmvl_val: Optional[str] = None  # 시간가치 값
    delta: Optional[str] = None  # 델타
    gama: Optional[str] = None  # 감마
    vega: Optional[str] = None  # 베가
    theta: Optional[str] = None  # 세타
    rho: Optional[str] = None  # 로우
    hts_ints_vltl: Optional[str] = None  # HTS 내재 변동성
    esdg: Optional[str] = None  # 괴리도
    otst_stpl_rgbf_qty_icdc: Optional[str] = None  # 미결제 약정 직전 수량 증감
    thpr_basis: Optional[str] = None  # 이론 베이시스
    unas_hist_vltl: Optional[str] = None  # 역사적변동성
    cttr: Optional[str] = None  # 체결강도
    dprt: Optional[str] = None  # 괴리율
    mrkt_basis: Optional[str] = None  # 시장 베이시스
    optn_askp1: Optional[str] = None  # 옵션 매도호가1
    optn_bidp1: Optional[str] = None  # 옵션 매수호가1
    askp_rsqn1: Optional[str] = None  # 매도호가 잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가 잔량1
    seln_cntg_csnu: Optional[str] = None  # 매도 체결 건수
    shnu_cntg_csnu: Optional[str] = None  # 매수 체결 건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수 체결 건수
    seln_cntg_smtn: Optional[str] = None  # 총 매도 수량
    shnu_cntg_smtn: Optional[str] = None  # 총 매수 수량
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일 거래량 대비 등락율
    avrg_vltl: Optional[str] = None  # 평균 변동성
    dscs_lrqn_vol: Optional[str] = None  # 협의대량누적 거래량
    dynm_mxpr: Optional[str] = None  # 실시간상한가
    dynm_llam: Optional[str] = None  # 실시간하한가
    dynm_prc_limt_yn: Optional[str] = None  # 실시간가격제한구분
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndexOptionRealtimeQuote(SQLModel, table=True):
    """Output table for index_option_realtime_quote"""
    __tablename__ = "kis_index_option_realtime_quote"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    optn_shrn_iscd: Optional[str] = None  # 옵션 단축 종목코드
    bsop_hour: Optional[str] = None  # 영업 시간
    optn_askp1: Optional[str] = None  # 옵션 매도호가1
    optn_askp2: Optional[str] = None  # 옵션 매도호가2
    optn_askp3: Optional[str] = None  # 옵션 매도호가3
    optn_askp4: Optional[str] = None  # 옵션 매도호가4
    optn_askp5: Optional[str] = None  # 옵션 매도호가5
    optn_bidp1: Optional[str] = None  # 옵션 매수호가1
    optn_bidp2: Optional[str] = None  # 옵션 매수호가2
    optn_bidp3: Optional[str] = None  # 옵션 매수호가3
    optn_bidp4: Optional[str] = None  # 옵션 매수호가4
    optn_bidp5: Optional[str] = None  # 옵션 매수호가5
    askp_csnu1: Optional[str] = None  # 매도호가 건수1
    askp_csnu2: Optional[str] = None  # 매도호가 건수2
    askp_csnu3: Optional[str] = None  # 매도호가 건수3
    askp_csnu4: Optional[str] = None  # 매도호가 건수4
    askp_csnu5: Optional[str] = None  # 매도호가 건수5
    bidp_csnu1: Optional[str] = None  # 매수호가 건수1
    bidp_csnu2: Optional[str] = None  # 매수호가 건수2
    bidp_csnu3: Optional[str] = None  # 매수호가 건수3
    bidp_csnu4: Optional[str] = None  # 매수호가 건수4
    bidp_csnu5: Optional[str] = None  # 매수호가 건수5
    askp_rsqn1: Optional[str] = None  # 매도호가 잔량1
    askp_rsqn2: Optional[str] = None  # 매도호가 잔량2
    askp_rsqn3: Optional[str] = None  # 매도호가 잔량3
    askp_rsqn4: Optional[str] = None  # 매도호가 잔량4
    askp_rsqn5: Optional[str] = None  # 매도호가 잔량5
    bidp_rsqn1: Optional[str] = None  # 매수호가 잔량1
    bidp_rsqn2: Optional[str] = None  # 매수호가 잔량2
    bidp_rsqn3: Optional[str] = None  # 매수호가 잔량3
    bidp_rsqn4: Optional[str] = None  # 매수호가 잔량4
    bidp_rsqn5: Optional[str] = None  # 매수호가 잔량5
    total_askp_csnu: Optional[str] = None  # 총 매도호가 건수
    total_bidp_csnu: Optional[str] = None  # 총 매수호가 건수
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    total_askp_rsqn_icdc: Optional[str] = None  # 총 매도호가 잔량 증감
    total_bidp_rsqn_icdc: Optional[str] = None  # 총 매수호가 잔량 증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireBalanceSettlementPl(SQLModel, table=True):
    """Output table for inquire_balance_settlement_pl"""
    __tablename__ = "kis_inquire_balance_settlement_pl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    trad_dvsn_name: Optional[str] = None  # 매매구분명
    bfdy_cblc_qty: Optional[str] = None  # 전일잔고수량
    new_qty: Optional[str] = None  # 신규수량
    mnpl_rpch_qty: Optional[str] = None  # 전매환매수량
    cblc_qty: Optional[str] = None  # 잔고수량
    cblc_amt: Optional[str] = None  # 잔고금액
    trad_pfls_amt: Optional[str] = None  # 매매손익금액
    evlu_amt: Optional[str] = None  # 평가금액
    evlu_pfls_amt: Optional[str] = None  # 평가손익금액
    nxdy_dnca: Optional[str] = None  # 익일예수금
    mmga_cash: Optional[str] = None  # 유지증거금현금
    brkg_mgna_cash: Optional[str] = None  # 위탁증거금현금
    opt_buy_chgs: Optional[str] = None  # 옵션매수대금
    opt_lqd_evlu_amt: Optional[str] = None  # 옵션청산평가금액
    dnca_sbst: Optional[str] = None  # 예수금대용
    mmga_tota: Optional[str] = None  # 유지증거금총액
    brkg_mgna_tota: Optional[str] = None  # 위탁증거금총액
    opt_sll_chgs: Optional[str] = None  # 옵션매도대금
    fee: Optional[str] = None  # 수수료
    thdt_dfpa: Optional[str] = None  # 당일차금
    rnwl_dfpa: Optional[str] = None  # 갱신차금
    dnca_cash: Optional[str] = None  # 예수금현금
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireBalanceValuationPl(SQLModel, table=True):
    """Output table for inquire_balance_valuation_pl"""
    __tablename__ = "kis_inquire_balance_valuation_pl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cano: Optional[str] = None  # 종합계좌번호
    acnt_prdt_cd: Optional[str] = None  # 계좌상품코드
    pdno: Optional[str] = None  # 상품번호
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    shtn_pdno: Optional[str] = None  # 단축상품번호
    prdt_name: Optional[str] = None  # 상품명
    sll_buy_dvsn_name: Optional[str] = None  # 매도매수구분명
    cblc_qty1: Optional[str] = None  # 잔고수량1
    excc_unpr: Optional[str] = None  # 정산단가
    ccld_avg_unpr1: Optional[str] = None  # 체결평균단가1
    idx_clpr: Optional[str] = None  # 지수종가
    pchs_amt: Optional[str] = None  # 매입금액
    evlu_amt: Optional[str] = None  # 평가금액
    evlu_pfls_amt: Optional[str] = None  # 평가손익금액
    trad_pfls_amt: Optional[str] = None  # 매매손익금액
    lqd_psbl_qty: Optional[str] = None  # 청산가능수량
    dnca_cash: Optional[str] = None  # 예수금현금
    frcr_dncl_amt: Optional[str] = None  # 외화예수금액
    dnca_sbst: Optional[str] = None  # 예수금대용
    tot_dncl_amt: Optional[str] = None  # 총예수금액
    tot_ccld_amt: Optional[str] = None  # 총체결금액
    cash_mgna: Optional[str] = None  # 현금증거금
    sbst_mgna: Optional[str] = None  # 대용증거금
    mgna_tota: Optional[str] = None  # 증거금총액
    opt_dfpa: Optional[str] = None  # 옵션차금
    thdt_dfpa: Optional[str] = None  # 당일차금
    rnwl_dfpa: Optional[str] = None  # 갱신차금
    fee: Optional[str] = None  # 수수료
    nxdy_dnca: Optional[str] = None  # 익일예수금
    nxdy_dncl_amt: Optional[str] = None  # 익일예수금액
    prsm_dpast: Optional[str] = None  # 추정예탁자산
    prsm_dpast_amt: Optional[str] = None  # 추정예탁자산금액
    pprt_ord_psbl_cash: Optional[str] = None  # 적정주문가능현금
    add_mgna_cash: Optional[str] = None  # 추가증거금현금
    add_mgna_tota: Optional[str] = None  # 추가증거금총액
    futr_trad_pfls_amt: Optional[str] = None  # 선물매매손익금액
    opt_trad_pfls_amt: Optional[str] = None  # 옵션매매손익금액
    futr_evlu_pfls_amt: Optional[str] = None  # 선물평가손익금액
    opt_evlu_pfls_amt: Optional[str] = None  # 옵션평가손익금액
    trad_pfls_amt_smtl: Optional[str] = None  # 매매손익금액합계
    evlu_pfls_amt_smtl: Optional[str] = None  # 평가손익금액합계
    wdrw_psbl_tot_amt: Optional[str] = None  # 인출가능총금액
    ord_psbl_cash: Optional[str] = None  # 주문가능현금
    ord_psbl_sbst: Optional[str] = None  # 주문가능대용
    ord_psbl_tota: Optional[str] = None  # 주문가능총액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireCcnlBstime(SQLModel, table=True):
    """Output table for inquire_ccnl_bstime"""
    __tablename__ = "kis_inquire_ccnl_bstime"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    odno: Optional[str] = None  # 주문번호
    tr_type_name: Optional[str] = None  # 거래유형명
    last_sttldt: Optional[str] = None  # 최종결제일
    ccld_idx: Optional[str] = None  # 체결지수
    ccld_qty: Optional[str] = None  # 체결량
    trad_amt: Optional[str] = None  # 매매금액
    fee: Optional[str] = None  # 수수료
    ccld_btwn: Optional[str] = None  # 체결시간
    tot_ccld_qty_smtl: Optional[str] = None  # 총체결수량합계
    tot_ccld_amt_smtl: Optional[str] = None  # 총체결금액합계
    fee_adjt: Optional[str] = None  # 수수료조정
    fee_smtl: Optional[str] = None  # 수수료합계
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDailyAmountFee(SQLModel, table=True):
    """Output table for inquire_daily_amount_fee"""
    __tablename__ = "kis_inquire_daily_amount_fee"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ord_dt: Optional[str] = None  # 주문일자
    pdno: Optional[str] = None  # 상품번호
    item_name: Optional[str] = None  # 종목명
    sll_agrm_amt: Optional[str] = None  # 매도약정금액
    sll_fee: Optional[str] = None  # 매도수수료
    buy_agrm_amt: Optional[str] = None  # 매수약정금액
    buy_fee: Optional[str] = None  # 매수수수료
    tot_fee_smtl: Optional[str] = None  # 총수수료합계
    trad_pfls: Optional[str] = None  # 매매손익
    futr_agrm: Optional[str] = None  # 선물약정
    futr_agrm_amt: Optional[str] = None  # 선물약정금액
    futr_agrm_amt_smtl: Optional[str] = None  # 선물약정금액합계
    futr_sll_fee_smtl: Optional[str] = None  # 선물매도수수료합계
    futr_buy_fee_smtl: Optional[str] = None  # 선물매수수수료합계
    futr_fee_smtl: Optional[str] = None  # 선물수수료합계
    opt_agrm: Optional[str] = None  # 옵션약정
    opt_agrm_amt: Optional[str] = None  # 옵션약정금액
    opt_agrm_amt_smtl: Optional[str] = None  # 옵션약정금액합계
    opt_sll_fee_smtl: Optional[str] = None  # 옵션매도수수료합계
    opt_buy_fee_smtl: Optional[str] = None  # 옵션매수수수료합계
    opt_fee_smtl: Optional[str] = None  # 옵션수수료합계
    prdt_futr_agrm: Optional[str] = None  # 상품선물약정
    prdt_fuop: Optional[str] = None  # 상품선물옵션
    prdt_futr_evlu_amt: Optional[str] = None  # 상품선물평가금액
    futr_fee: Optional[str] = None  # 선물수수료
    opt_fee: Optional[str] = None  # 옵션수수료
    fee: Optional[str] = None  # 수수료
    agrm_amt_smtl: Optional[str] = None  # 약정금액합계
    fee_smtl: Optional[str] = None  # 수수료합계
    trad_pfls_smtl: Optional[str] = None  # 매매손익합계
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDailyFuopchartprice(SQLModel, table=True):
    """Output table for inquire_daily_fuopchartprice"""
    __tablename__ = "kis_inquire_daily_fuopchartprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    futs_prdy_ctrt: Optional[str] = None  # 선물 전일 대비율
    futs_prdy_clpr: Optional[str] = None  # 선물 전일 종가
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    futs_prpr: Optional[str] = None  # 현재가
    futs_shrn_iscd: Optional[str] = None  # 단축 종목코드
    prdy_vol: Optional[str] = None  # 전일 거래량
    futs_mxpr: Optional[str] = None  # 상한가
    futs_llam: Optional[str] = None  # 하한가
    futs_oprc: Optional[str] = None  # 시가
    futs_hgpr: Optional[str] = None  # 최고가
    futs_lwpr: Optional[str] = None  # 최저가
    futs_prdy_oprc: Optional[str] = None  # 전일 시가
    futs_prdy_hgpr: Optional[str] = None  # 전일 최고가
    futs_prdy_lwpr: Optional[str] = None  # 전일 최저가
    futs_askp: Optional[str] = None  # 매도호가
    futs_bidp: Optional[str] = None  # 매수호가
    basis: Optional[str] = None  # 베이시스
    kospi200_nmix: Optional[str] = None  # KOSPI200 지수
    kospi200_prdy_vrss: Optional[str] = None  # KOSPI200 전일 대비
    kospi200_prdy_ctrt: Optional[str] = None  # KOSPI200 전일 대비율
    kospi200_prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    hts_otst_stpl_qty: Optional[str] = None  # HTS 미결제 약정 수량
    otst_stpl_qty_icdc: Optional[str] = None  # 미결제 약정 수량 증감
    tday_rltv: Optional[str] = None  # 당일 체결강도
    hts_thpr: Optional[str] = None  # HTS 이론가
    dprt: Optional[str] = None  # 괴리율
    stck_bsop_date: Optional[str] = None  # 영업 일자
    mod_yn: Optional[str] = None  # 변경 여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDeposit(SQLModel, table=True):
    """Output table for inquire_deposit"""
    __tablename__ = "kis_inquire_deposit"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    fm_nxdy_dncl_amt: Optional[str] = None  # FM익일예수금액
    fm_tot_asst_evlu_amt: Optional[str] = None  # FM총자산평가금액
    cano: Optional[str] = None  # 종합계좌번호
    acnt_prdt_cd: Optional[str] = None  # 계좌상품코드
    crcy_cd: Optional[str] = None  # 통화코드
    resp_dt: Optional[str] = None  # 응답일자
    fm_dnca_rmnd: Optional[str] = None  # FM예수금잔액
    fm_lqd_pfls_amt: Optional[str] = None  # FM청산손익금액
    fm_fee: Optional[str] = None  # FM수수료
    fm_fuop_evlu_pfls_amt: Optional[str] = None  # FM선물옵션평가손익금액
    fm_rcvb_amt: Optional[str] = None  # FM미수금액
    fm_brkg_mgn_amt: Optional[str] = None  # FM위탁증거금액
    fm_mntn_mgn_amt: Optional[str] = None  # FM유지증거금액
    fm_add_mgn_amt: Optional[str] = None  # FM추가증거금액
    fm_risk_rt: Optional[str] = None  # FM위험율
    fm_ord_psbl_amt: Optional[str] = None  # FM주문가능금액
    fm_drwg_psbl_amt: Optional[str] = None  # FM출금가능금액
    fm_echm_rqrm_amt: Optional[str] = None  # FM환전요청금액
    fm_drwg_prar_amt: Optional[str] = None  # FM출금예정금액
    fm_opt_tr_chgs: Optional[str] = None  # FM옵션거래대금
    fm_opt_icld_asst_evlu_amt: Optional[str] = None  # FM옵션포함자산평가금액
    fm_opt_evlu_amt: Optional[str] = None  # FM옵션평가금액
    fm_crcy_sbst_amt: Optional[str] = None  # FM통화대용금액
    fm_crcy_sbst_use_amt: Optional[str] = None  # FM통화대용사용금액
    fm_crcy_sbst_stup_amt: Optional[str] = None  # FM통화대용설정금액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireNgtBalance(SQLModel, table=True):
    """Output table for inquire_ngt_balance"""
    __tablename__ = "kis_inquire_ngt_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cano: Optional[str] = None  # 종합계좌번호
    acnt_prdt_cd: Optional[str] = None  # 계좌상품코드
    pdno: Optional[str] = None  # 상품번호
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    shtn_pdno: Optional[str] = None  # 단축상품번호
    prdt_name: Optional[str] = None  # 상품명
    sll_buy_dvsn_name: Optional[str] = None  # 매도매수구분명
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    trad_dvsn_name: Optional[str] = None  # 매매구분명
    cblc_qty: Optional[str] = None  # 잔고수량
    excc_unpr: Optional[str] = None  # 정산단가
    ccld_avg_unpr1: Optional[str] = None  # 체결평균단가1
    idx_clpr: Optional[str] = None  # 지수종가
    pchs_amt: Optional[str] = None  # 매입금액
    evlu_amt: Optional[str] = None  # 평가금액
    evlu_pfls_amt: Optional[str] = None  # 평가손익금액
    trad_pfls_amt: Optional[str] = None  # 매매손익금액
    lqd_psbl_qty: Optional[str] = None  # 청산가능수량
    dnca_cash: Optional[str] = None  # 예수금현금
    frcr_dncl_amt: Optional[str] = None  # 외화예수금액
    dnca_sbst: Optional[str] = None  # 예수금대용
    tot_dncl_amt: Optional[str] = None  # 총예수금액
    cash_mgna: Optional[str] = None  # 현금증거금
    sbst_mgna: Optional[str] = None  # 대용증거금
    mgna_tota: Optional[str] = None  # 증거금총액
    opt_dfpa: Optional[str] = None  # 옵션차금
    thdt_dfpa: Optional[str] = None  # 당일차금
    rnwl_dfpa: Optional[str] = None  # 갱신차금
    fee: Optional[str] = None  # 수수료
    nxdy_dnca: Optional[str] = None  # 익일예수금
    nxdy_dncl_amt: Optional[str] = None  # 익일예수금액
    prsm_dpast: Optional[str] = None  # 추정예탁자산
    pprt_ord_psbl_cash: Optional[str] = None  # 적정주문가능현금
    add_mgna_cash: Optional[str] = None  # 추가증거금현금
    add_mgna_tota: Optional[str] = None  # 추가증거금총액
    futr_trad_pfls_amt: Optional[str] = None  # 선물매매손익금액
    opt_trad_pfls_amt: Optional[str] = None  # 옵션매매손익금액
    futr_evlu_pfls_amt: Optional[str] = None  # 선물평가손익금액
    opt_evlu_pfls_amt: Optional[str] = None  # 옵션평가손익금액
    trad_pfls_amt_smtl: Optional[str] = None  # 매매손익금액합계
    evlu_pfls_amt_smtl: Optional[str] = None  # 평가손익금액합계
    wdrw_psbl_tot_amt: Optional[str] = None  # 인출가능총금액
    ord_psbl_cash: Optional[str] = None  # 주문가능현금
    ord_psbl_sbst: Optional[str] = None  # 주문가능대용
    ord_psbl_tota: Optional[str] = None  # 주문가능총액
    mmga_tot_amt: Optional[str] = None  # 유지증거금총금액
    mmga_cash_amt: Optional[str] = None  # 유지증거금현금금액
    mtnc_rt: Optional[str] = None  # 유지비율
    isfc_amt: Optional[str] = None  # 부족금액
    pchs_amt_smtl: Optional[str] = None  # 매입금액합계
    evlu_amt_smtl: Optional[str] = None  # 평가금액합계
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireNgtCcnl(SQLModel, table=True):
    """Output table for inquire_ngt_ccnl"""
    __tablename__ = "kis_inquire_ngt_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ord_gno_brno: Optional[str] = None  # 주문채번지점번호
    cano: Optional[str] = None  # 종합계좌번호
    csac_name: Optional[str] = None  # 종합계좌명
    acnt_prdt_cd: Optional[str] = None  # 계좌상품코드
    ord_dt: Optional[str] = None  # 주문일자
    odno: Optional[str] = None  # 주문번호
    orgn_odno: Optional[str] = None  # 원주문번호
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    trad_dvsn_name: Optional[str] = None  # 매매구분명
    nmpr_type_name: Optional[str] = None  # 호가유형명
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    ord_qty: Optional[str] = None  # 주문수량
    ord_idx4: Optional[str] = None  # 주문지수
    qty: Optional[str] = None  # 잔량
    ord_tmd: Optional[str] = None  # 주문시각
    tot_ccld_qty: Optional[str] = None  # 총체결수량
    avg_idx: Optional[str] = None  # 평균지수
    tot_ccld_amt: Optional[str] = None  # 총체결금액
    rjct_qty: Optional[str] = None  # 거부수량
    ingr_trad_rjct_rson_cd: Optional[str] = None  # 장내매매거부사유코드
    ingr_trad_rjct_rson_name: Optional[str] = None  # 장내매매거부사유명
    ord_stfno: Optional[str] = None  # 주문직원번호
    sprd_item_yn: Optional[str] = None  # 스프레드종목여부
    ord_ip_addr: Optional[str] = None  # 주문IP주소
    tot_ord_qty: Optional[str] = None  # 총주문수량
    tot_ccld_qty_SMTL: Optional[str] = None  # 총체결수량
    tot_ccld_amt_SMTL: Optional[str] = None  # 총체결금액
    fee: Optional[str] = None  # 수수료
    ctac_tlno: Optional[str] = None  # 연락전화번호
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePsblNgtOrder(SQLModel, table=True):
    """Output table for inquire_psbl_ngt_order"""
    __tablename__ = "kis_inquire_psbl_ngt_order"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    max_ord_psbl_qty: Optional[str] = None  # 최대주문가능수량
    tot_psbl_qty: Optional[str] = None  # 최대주문가능수량
    lqd_psbl_qty: Optional[str] = None  # 청산가능수량
    lqd_psbl_qty_1: Optional[str] = None  # 청산가능수량
    ord_psbl_qty: Optional[str] = None  # 주문가능수량
    bass_idx: Optional[str] = None  # 기준지수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireTimeFuopchartprice(SQLModel, table=True):
    """Output table for inquire_time_fuopchartprice"""
    __tablename__ = "kis_inquire_time_fuopchartprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_prdy_vrss: Optional[str] = None  # 선물 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    futs_prdy_ctrt: Optional[str] = None  # 선물 전일 대비율
    futs_prdy_clpr: Optional[str] = None  # 선물 전일 종가
    prdy_nmix: Optional[str] = None  # 전일 지수
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    futs_prpr: Optional[str] = None  # 선물 현재가
    futs_shrn_iscd: Optional[str] = None  # 선물 단축 종목코드
    prdy_vol: Optional[str] = None  # 전일 거래량
    futs_mxpr: Optional[str] = None  # 선물 상한가
    futs_llam: Optional[str] = None  # 선물 하한가
    futs_oprc: Optional[str] = None  # 선물 시가2
    futs_hgpr: Optional[str] = None  # 선물 최고가
    futs_lwpr: Optional[str] = None  # 선물 최저가
    futs_prdy_oprc: Optional[str] = None  # 선물 전일 시가
    futs_prdy_hgpr: Optional[str] = None  # 선물 전일 최고가
    futs_prdy_lwpr: Optional[str] = None  # 선물 전일 최저가
    futs_askp: Optional[str] = None  # 선물 매도호가
    futs_bidp: Optional[str] = None  # 선물 매수호가
    basis: Optional[str] = None  # 베이시스
    kospi200_nmix: Optional[str] = None  # KOSPI200 지수
    kospi200_prdy_vrss: Optional[str] = None  # KOSPI200 전일 대비
    kospi200_prdy_ctrt: Optional[str] = None  # KOSPI200 전일 대비율
    kospi200_prdy_vrss_sign: Optional[str] = None  # KOSPI200 전일 대비 부호
    hts_otst_stpl_qty: Optional[str] = None  # HTS 미결제 약정 수량
    otst_stpl_qty_icdc: Optional[str] = None  # 미결제 약정 수량 증감
    tday_rltv: Optional[str] = None  # 당일 체결강도
    hts_thpr: Optional[str] = None  # HTS 이론가
    dprt: Optional[str] = None  # 괴리율
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    cntg_vol: Optional[str] = None  # 체결 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KrxNgtFuturesAskingPrice(SQLModel, table=True):
    """Output table for krx_ngt_futures_asking_price"""
    __tablename__ = "kis_krx_ngt_futures_asking_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_shrn_iscd: Optional[str] = None  # 선물 단축 종목코드
    bsop_hour: Optional[str] = None  # 영업 시간
    futs_askp1: Optional[str] = None  # 선물 매도호가1
    futs_askp2: Optional[str] = None  # 선물 매도호가2
    futs_askp3: Optional[str] = None  # 선물 매도호가3
    futs_askp4: Optional[str] = None  # 선물 매도호가4
    futs_askp5: Optional[str] = None  # 선물 매도호가5
    futs_bidp1: Optional[str] = None  # 선물 매수호가1
    futs_bidp2: Optional[str] = None  # 선물 매수호가2
    futs_bidp3: Optional[str] = None  # 선물 매수호가3
    futs_bidp4: Optional[str] = None  # 선물 매수호가4
    futs_bidp5: Optional[str] = None  # 선물 매수호가5
    askp_csnu1: Optional[str] = None  # 매도호가 건수1
    askp_csnu2: Optional[str] = None  # 매도호가 건수2
    askp_csnu3: Optional[str] = None  # 매도호가 건수3
    askp_csnu4: Optional[str] = None  # 매도호가 건수4
    askp_csnu5: Optional[str] = None  # 매도호가 건수5
    bidp_csnu1: Optional[str] = None  # 매수호가 건수1
    bidp_csnu2: Optional[str] = None  # 매수호가 건수2
    bidp_csnu3: Optional[str] = None  # 매수호가 건수3
    bidp_csnu4: Optional[str] = None  # 매수호가 건수4
    bidp_csnu5: Optional[str] = None  # 매수호가 건수5
    askp_rsqn1: Optional[str] = None  # 매도호가 잔량1
    askp_rsqn2: Optional[str] = None  # 매도호가 잔량2
    askp_rsqn3: Optional[str] = None  # 매도호가 잔량3
    askp_rsqn4: Optional[str] = None  # 매도호가 잔량4
    askp_rsqn5: Optional[str] = None  # 매도호가 잔량5
    bidp_rsqn1: Optional[str] = None  # 매수호가 잔량1
    bidp_rsqn2: Optional[str] = None  # 매수호가 잔량2
    bidp_rsqn3: Optional[str] = None  # 매수호가 잔량3
    bidp_rsqn4: Optional[str] = None  # 매수호가 잔량4
    bidp_rsqn5: Optional[str] = None  # 매수호가 잔량5
    total_askp_csnu: Optional[str] = None  # 총 매도호가 건수
    total_bidp_csnu: Optional[str] = None  # 총 매수호가 건수
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    total_askp_rsqn_icdc: Optional[str] = None  # 총 매도호가 잔량 증감
    total_bidp_rsqn_icdc: Optional[str] = None  # 총 매수호가 잔량 증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KrxNgtFuturesCcnl(SQLModel, table=True):
    """Output table for krx_ngt_futures_ccnl"""
    __tablename__ = "kis_krx_ngt_futures_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_shrn_iscd: Optional[str] = None  # 선물 단축 종목코드
    bsop_hour: Optional[str] = None  # 영업 시간
    futs_prdy_vrss: Optional[str] = None  # 선물 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    futs_prdy_ctrt: Optional[str] = None  # 선물 전일 대비율
    futs_prpr: Optional[str] = None  # 선물 현재가
    futs_oprc: Optional[str] = None  # 선물 시가2
    futs_hgpr: Optional[str] = None  # 선물 최고가
    futs_lwpr: Optional[str] = None  # 선물 최저가
    last_cnqn: Optional[str] = None  # 최종 거래량
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    hts_thpr: Optional[str] = None  # HTS 이론가
    mrkt_basis: Optional[str] = None  # 시장 베이시스
    dprt: Optional[str] = None  # 괴리율
    nmsc_fctn_stpl_prc: Optional[str] = None  # 근월물 약정가
    fmsc_fctn_stpl_prc: Optional[str] = None  # 원월물 약정가
    spead_prc: Optional[str] = None  # 스프레드1
    hts_otst_stpl_qty: Optional[str] = None  # HTS 미결제 약정 수량
    otst_stpl_qty_icdc: Optional[str] = None  # 미결제 약정 수량 증감
    oprc_hour: Optional[str] = None  # 시가 시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2 대비 현재가 부호
    oprc_vrss_nmix_prpr: Optional[str] = None  # 시가 대비 지수 현재가
    hgpr_hour: Optional[str] = None  # 최고가 시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가 대비 현재가 부호
    hgpr_vrss_nmix_prpr: Optional[str] = None  # 최고가 대비 지수 현재가
    lwpr_hour: Optional[str] = None  # 최저가 시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가 대비 현재가 부호
    lwpr_vrss_nmix_prpr: Optional[str] = None  # 최저가 대비 지수 현재가
    shnu_rate: Optional[str] = None  # 매수2 비율
    cttr: Optional[str] = None  # 체결강도
    esdg: Optional[str] = None  # 괴리도
    otst_stpl_rgbf_qty_icdc: Optional[str] = None  # 미결제 약정 직전 수량 증감
    thpr_basis: Optional[str] = None  # 이론 베이시스
    futs_askp1: Optional[str] = None  # 선물 매도호가1
    futs_bidp1: Optional[str] = None  # 선물 매수호가1
    askp_rsqn1: Optional[str] = None  # 매도호가 잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가 잔량1
    seln_cntg_csnu: Optional[str] = None  # 매도 체결 건수
    shnu_cntg_csnu: Optional[str] = None  # 매수 체결 건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수 체결 건수
    seln_cntg_smtn: Optional[str] = None  # 총 매도 수량
    shnu_cntg_smtn: Optional[str] = None  # 총 매수 수량
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일 거래량 대비 등락율
    dynm_mxpr: Optional[str] = None  # 실시간상한가
    dynm_llam: Optional[str] = None  # 실시간하한가
    dynm_prc_limt_yn: Optional[str] = None  # 실시간가격제한구분
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KrxNgtFuturesCcnlNotice(SQLModel, table=True):
    """Output table for krx_ngt_futures_ccnl_notice"""
    __tablename__ = "kis_krx_ngt_futures_ccnl_notice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cust_id: Optional[str] = None  # 고객 ID
    acnt_no: Optional[str] = None  # 계좌번호
    oder_no: Optional[str] = None  # 주문번호
    ooder_no: Optional[str] = None  # 원주문번호
    seln_byov_cls: Optional[str] = None  # 매도매수구분
    rctf_cls: Optional[str] = None  # 정정구분
    oder_kind2: Optional[str] = None  # 주문종류2
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    cntg_qty: Optional[str] = None  # 체결 수량
    cntg_unpr: Optional[str] = None  # 체결단가
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    rfus_yn: Optional[str] = None  # 거부여부
    cntg_yn: Optional[str] = None  # 체결여부
    acpt_yn: Optional[str] = None  # 접수여부
    brnc_no: Optional[str] = None  # 지점번호
    oder_qty: Optional[str] = None  # 주문수량
    acnt_name: Optional[str] = None  # 계좌명
    cntg_isnm: Optional[str] = None  # 체결종목명
    oder_cond: Optional[str] = None  # 주문조건
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KrxNgtOptionAskingPrice(SQLModel, table=True):
    """Output table for krx_ngt_option_asking_price"""
    __tablename__ = "kis_krx_ngt_option_asking_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    optn_shrn_iscd: Optional[str] = None  # 옵션단축종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    optn_askp1: Optional[str] = None  # 옵션매도호가1
    optn_askp2: Optional[str] = None  # 옵션매도호가2
    optn_askp3: Optional[str] = None  # 옵션매도호가3
    optn_askp4: Optional[str] = None  # 옵션매도호가4
    optn_askp5: Optional[str] = None  # 옵션매도호가5
    optn_bidp1: Optional[str] = None  # 옵션매수호가1
    optn_bidp2: Optional[str] = None  # 옵션매수호가2
    optn_bidp3: Optional[str] = None  # 옵션매수호가3
    optn_bidp4: Optional[str] = None  # 옵션매수호가4
    optn_bidp5: Optional[str] = None  # 옵션매수호가5
    askp_csnu1: Optional[str] = None  # 매도호가건수1
    askp_csnu2: Optional[str] = None  # 매도호가건수2
    askp_csnu3: Optional[str] = None  # 매도호가건수3
    askp_csnu4: Optional[str] = None  # 매도호가건수4
    askp_csnu5: Optional[str] = None  # 매도호가건수5
    bidp_csnu1: Optional[str] = None  # 매수호가건수1
    bidp_csnu2: Optional[str] = None  # 매수호가건수2
    bidp_csnu3: Optional[str] = None  # 매수호가건수3
    bidp_csnu4: Optional[str] = None  # 매수호가건수4
    bidp_csnu5: Optional[str] = None  # 매수호가건수5
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    askp_rsqn2: Optional[str] = None  # 매도호가잔량2
    askp_rsqn3: Optional[str] = None  # 매도호가잔량3
    askp_rsqn4: Optional[str] = None  # 매도호가잔량4
    askp_rsqn5: Optional[str] = None  # 매도호가잔량5
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    bidp_rsqn2: Optional[str] = None  # 매수호가잔량2
    bidp_rsqn3: Optional[str] = None  # 매수호가잔량3
    bidp_rsqn4: Optional[str] = None  # 매수호가잔량4
    bidp_rsqn5: Optional[str] = None  # 매수호가잔량5
    total_askp_csnu: Optional[str] = None  # 총매도호가건수
    total_bidp_csnu: Optional[str] = None  # 총매수호가건수
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    total_askp_rsqn_icdc: Optional[str] = None  # 총매도호가잔량증감
    total_bidp_rsqn_icdc: Optional[str] = None  # 총매수호가잔량증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KrxNgtOptionCcnl(SQLModel, table=True):
    """Output table for krx_ngt_option_ccnl"""
    __tablename__ = "kis_krx_ngt_option_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    optn_shrn_iscd: Optional[str] = None  # 옵션단축종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    optn_prpr: Optional[str] = None  # 옵션현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    optn_prdy_vrss: Optional[str] = None  # 옵션전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    optn_oprc: Optional[str] = None  # 옵션시가2
    optn_hgpr: Optional[str] = None  # 옵션최고가
    optn_lwpr: Optional[str] = None  # 옵션최저가
    last_cnqn: Optional[str] = None  # 최종거래량
    acml_vol: Optional[str] = None  # 누적거래량
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    hts_thpr: Optional[str] = None  # HTS이론가
    hts_otst_stpl_qty: Optional[str] = None  # HTS미결제약정수량
    otst_stpl_qty_icdc: Optional[str] = None  # 미결제약정수량증감
    oprc_hour: Optional[str] = None  # 시가시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2대비현재가부호
    oprc_vrss_nmix_prpr: Optional[str] = None  # 시가대비지수현재가
    hgpr_hour: Optional[str] = None  # 최고가시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가대비현재가부호
    hgpr_vrss_nmix_prpr: Optional[str] = None  # 최고가대비지수현재가
    lwpr_hour: Optional[str] = None  # 최저가시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가대비현재가부호
    lwpr_vrss_nmix_prpr: Optional[str] = None  # 최저가대비지수현재가
    shnu_rate: Optional[str] = None  # 매수2비율
    prmm_val: Optional[str] = None  # 프리미엄값
    invl_val: Optional[str] = None  # 내재가치값
    tmvl_val: Optional[str] = None  # 시간가치값
    delta: Optional[str] = None  # 델타
    gama: Optional[str] = None  # 감마
    vega: Optional[str] = None  # 베가
    theta: Optional[str] = None  # 세타
    rho: Optional[str] = None  # 로우
    hts_ints_vltl: Optional[str] = None  # HTS내재변동성
    esdg: Optional[str] = None  # 괴리도
    otst_stpl_rgbf_qty_icdc: Optional[str] = None  # 미결제약정직전수량증감
    thpr_basis: Optional[str] = None  # 이론베이시스
    unas_hist_vltl: Optional[str] = None  # 역사적변동성
    cttr: Optional[str] = None  # 체결강도
    dprt: Optional[str] = None  # 괴리율
    mrkt_basis: Optional[str] = None  # 시장베이시스
    optn_askp1: Optional[str] = None  # 옵션매도호가1
    optn_bidp1: Optional[str] = None  # 옵션매수호가1
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    seln_cntg_csnu: Optional[str] = None  # 매도체결건수
    shnu_cntg_csnu: Optional[str] = None  # 매수체결건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수체결건수
    seln_cntg_smtn: Optional[str] = None  # 총매도수량
    shnu_cntg_smtn: Optional[str] = None  # 총매수수량
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일거래량대비등락율
    dynm_mxpr: Optional[str] = None  # 실시간상한가
    dynm_prc_limt_yn: Optional[str] = None  # 실시간가격제한구분
    dynm_llam: Optional[str] = None  # 실시간하한가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KrxNgtOptionExpCcnl(SQLModel, table=True):
    """Output table for krx_ngt_option_exp_ccnl"""
    __tablename__ = "kis_krx_ngt_option_exp_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    optn_shrn_iscd: Optional[str] = None  # 옵션단축종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    antc_cnpr: Optional[str] = None  # 예상체결가
    antc_cntg_vrss: Optional[str] = None  # 예상체결대비
    antc_cntg_vrss_sign: Optional[str] = None  # 예상체결대비부호
    antc_cntg_prdy_ctrt: Optional[str] = None  # 예상체결전일대비율
    antc_mkop_cls_code: Optional[str] = None  # 예상장운영구분코드
    antc_cnqn: Optional[str] = None  # 예상체결수량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KrxNgtOptionNotice(SQLModel, table=True):
    """Output table for krx_ngt_option_notice"""
    __tablename__ = "kis_krx_ngt_option_notice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cust_id: Optional[str] = None  # 고객 ID
    acnt_no: Optional[str] = None  # 계좌번호
    oder_no: Optional[str] = None  # 주문번호
    ooder_no: Optional[str] = None  # 원주문번호
    seln_byov_cls: Optional[str] = None  # 매도매수구분
    rctf_cls: Optional[str] = None  # 정정구분
    oder_kind2: Optional[str] = None  # 주문종류2
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    cntg_qty: Optional[str] = None  # 체결 수량
    cntg_unpr: Optional[str] = None  # 체결단가
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    rfus_yn: Optional[str] = None  # 거부여부
    cntg_yn: Optional[str] = None  # 체결여부
    acpt_yn: Optional[str] = None  # 접수여부
    brnc_no: Optional[str] = None  # 지점번호
    oder_qty: Optional[str] = None  # 주문수량
    acnt_name: Optional[str] = None  # 계좌명
    cntg_isnm: Optional[str] = None  # 체결종목명
    oder_cond: Optional[str] = None  # 주문조건
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NgtMarginDetail(SQLModel, table=True):
    """Output table for ngt_margin_detail"""
    __tablename__ = "kis_ngt_margin_detail"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futr_new_mgn_amt: Optional[str] = None  # 선물신규증거금액
    futr_sprd_ord_mgna: Optional[str] = None  # 선물스프레드주문증거금
    opt_sll_new_mgn_amt: Optional[str] = None  # 옵션매도신규증거금액
    opt_buy_new_mgn_amt: Optional[str] = None  # 옵션매수신규증거금액
    new_mgn_amt: Optional[str] = None  # 신규증거금액
    opt_pric_mgna: Optional[str] = None  # 옵션가격증거금
    fuop_pric_altr_mgna: Optional[str] = None  # 선물옵션가격변동증거금
    futr_sprd_mgna: Optional[str] = None  # 선물스프레드증거금
    uwdl_mgna: Optional[str] = None  # 인수도증거금
    ctrt_per_min_mgna: Optional[str] = None  # 계약당최소증거금
    tot_risk_mgna: Optional[str] = None  # 총위험증거금
    netrisk_brkg_mgna: Optional[str] = None  # 순위험위탁증거금
    opt_sll_chgs: Optional[str] = None  # 옵션매도대금
    opt_buy_chgs: Optional[str] = None  # 옵션매수대금
    futr_loss_amt: Optional[str] = None  # 선물손실금액
    futr_prft_amt: Optional[str] = None  # 선물이익금액
    thdt_ccld_net_loss_amt: Optional[str] = None  # 당일체결순손실금액
    brkg_mgna: Optional[str] = None  # 위탁증거금
    dnca_cash: Optional[str] = None  # 예수금현금
    dnca_sbst: Optional[str] = None  # 예수금대용
    dnca_tota: Optional[str] = None  # 예수금총액
    wdrw_psbl_cash_amt: Optional[str] = None  # 인출가능현금금액
    wdrw_psbl_sbsa: Optional[str] = None  # 인출가능대용금액
    wdrw_psbl_tot_amt: Optional[str] = None  # 인출가능총금액
    ord_psbl_cash_amt: Optional[str] = None  # 주문가능현금금액
    ord_psbl_sbsa: Optional[str] = None  # 주문가능대용금액
    ord_psbl_tot_amt: Optional[str] = None  # 주문가능총금액
    brkg_mgna_cash_amt: Optional[str] = None  # 위탁증거금현금금액
    brkg_mgna_sbst: Optional[str] = None  # 위탁증거금대용
    brkg_mgna_tot_amt: Optional[str] = None  # 위탁증거금총금액
    add_mgna_cash_amt: Optional[str] = None  # 추가증거금현금금액
    add_mgna_sbsa: Optional[str] = None  # 추가증거금대용금액
    add_mgna_tot_amt: Optional[str] = None  # 추가증거금총금액
    bfdy_sbst_sll_sbst_amt: Optional[str] = None  # 전일대용매도대용금액
    thdt_sbst_sll_sbst_amt: Optional[str] = None  # 당일대용매도대용금액
    bfdy_sbst_sll_ccld_amt: Optional[str] = None  # 전일대용매도체결금액
    thdt_sbst_sll_ccld_amt: Optional[str] = None  # 당일대용매도체결금액
    opt_dfpa: Optional[str] = None  # 옵션차금
    excc_dfpa: Optional[str] = None  # 정산차금
    fee_amt: Optional[str] = None  # 수수료금액
    nxdy_dncl_amt: Optional[str] = None  # 익일예수금액
    prsm_dpast_amt: Optional[str] = None  # 추정예탁자산금액
    opt_buy_exus_acnt_yn: Optional[str] = None  # 옵션매수전용계좌여부
    base_dpsa_gdat_grad_cd: Optional[str] = None  # 기본예탁금차등등급코드
    opt_base_dpsa_gdat_grad_cd: Optional[str] = None  # 옵션기본예탁금차등등급코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OptionExpCcnl(SQLModel, table=True):
    """Output table for option_exp_ccnl"""
    __tablename__ = "kis_option_exp_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    optn_shrn_iscd: Optional[str] = None  # 옵션단축종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    antc_cnpr: Optional[str] = None  # 예상체결가
    antc_cntg_vrss: Optional[str] = None  # 예상체결대비
    antc_cntg_vrss_sign: Optional[str] = None  # 예상체결대비부호
    antc_cntg_prdy_ctrt: Optional[str] = None  # 예상체결전일대비율
    antc_mkop_cls_code: Optional[str] = None  # 예상장운영구분코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Order(SQLModel, table=True):
    """Output table for order"""
    __tablename__ = "kis_order"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    KRX_FWDG_ORD_ORGNO: Optional[str] = None  # 한국거래소전송주문조직번호
    ODNO: Optional[str] = None  # 주문번호
    ORD_TMD: Optional[str] = None  # 주문시각
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class StockFuturesRealtimeConclusion(SQLModel, table=True):
    """Output table for stock_futures_realtime_conclusion"""
    __tablename__ = "kis_stock_futures_realtime_conclusion"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_shrn_iscd: Optional[str] = None  # 선물단축종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_vrss: Optional[str] = None  # 전일대비
    futs_prdy_ctrt: Optional[str] = None  # 선물전일대비율
    stck_oprc: Optional[str] = None  # 주식시가2
    stck_hgpr: Optional[str] = None  # 주식최고가
    stck_lwpr: Optional[str] = None  # 주식최저가
    last_cnqn: Optional[str] = None  # 최종거래량
    acml_vol: Optional[str] = None  # 누적거래량
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    hts_thpr: Optional[str] = None  # HTS이론가
    mrkt_basis: Optional[str] = None  # 시장베이시스
    dprt: Optional[str] = None  # 괴리율
    nmsc_fctn_stpl_prc: Optional[str] = None  # 근월물약정가
    fmsc_fctn_stpl_prc: Optional[str] = None  # 원월물약정가
    spead_prc: Optional[str] = None  # 스프레드1
    hts_otst_stpl_qty: Optional[str] = None  # HTS미결제약정수량
    otst_stpl_qty_icdc: Optional[str] = None  # 미결제약정수량증감
    oprc_hour: Optional[str] = None  # 시가시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2대비현재가부호
    oprc_vrss_prpr: Optional[str] = None  # 시가2대비현재가
    hgpr_hour: Optional[str] = None  # 최고가시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가대비현재가부호
    hgpr_vrss_prpr: Optional[str] = None  # 최고가대비현재가
    lwpr_hour: Optional[str] = None  # 최저가시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가대비현재가부호
    lwpr_vrss_prpr: Optional[str] = None  # 최저가대비현재가
    shnu_rate: Optional[str] = None  # 매수2비율
    cttr: Optional[str] = None  # 체결강도
    esdg: Optional[str] = None  # 괴리도
    otst_stpl_rgbf_qty_icdc: Optional[str] = None  # 미결제약정직전수량증감
    thpr_basis: Optional[str] = None  # 이론베이시스
    askp1: Optional[str] = None  # 매도호가1
    bidp1: Optional[str] = None  # 매수호가1
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    seln_cntg_csnu: Optional[str] = None  # 매도체결건수
    shnu_cntg_csnu: Optional[str] = None  # 매수체결건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수체결건수
    seln_cntg_smtn: Optional[str] = None  # 총매도수량
    shnu_cntg_smtn: Optional[str] = None  # 총매수수량
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일거래량대비등락율
    dynm_mxpr: Optional[str] = None  # 실시간상한가
    dynm_llam: Optional[str] = None  # 실시간하한가
    dynm_prc_limt_yn: Optional[str] = None  # 실시간가격제한구분
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class StockFuturesRealtimeQuote(SQLModel, table=True):
    """Output table for stock_futures_realtime_quote"""
    __tablename__ = "kis_stock_futures_realtime_quote"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    futs_shrn_iscd: Optional[str] = None  # 선물단축종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    askp1: Optional[str] = None  # 매도호가1
    askp2: Optional[str] = None  # 매도호가2
    askp3: Optional[str] = None  # 매도호가3
    askp4: Optional[str] = None  # 매도호가4
    askp5: Optional[str] = None  # 매도호가5
    askp6: Optional[str] = None  # 매도호가6
    askp7: Optional[str] = None  # 매도호가7
    askp8: Optional[str] = None  # 매도호가8
    askp9: Optional[str] = None  # 매도호가9
    askp10: Optional[str] = None  # 매도호가10
    bidp1: Optional[str] = None  # 매수호가1
    bidp2: Optional[str] = None  # 매수호가2
    bidp3: Optional[str] = None  # 매수호가3
    bidp4: Optional[str] = None  # 매수호가4
    bidp5: Optional[str] = None  # 매수호가5
    bidp6: Optional[str] = None  # 매수호가6
    bidp7: Optional[str] = None  # 매수호가7
    bidp8: Optional[str] = None  # 매수호가8
    bidp9: Optional[str] = None  # 매수호가9
    bidp10: Optional[str] = None  # 매수호가10
    askp_csnu1: Optional[str] = None  # 매도호가건수1
    askp_csnu2: Optional[str] = None  # 매도호가건수2
    askp_csnu3: Optional[str] = None  # 매도호가건수3
    askp_csnu4: Optional[str] = None  # 매도호가건수4
    askp_csnu5: Optional[str] = None  # 매도호가건수5
    askp_csnu6: Optional[str] = None  # 매도호가건수6
    askp_csnu7: Optional[str] = None  # 매도호가건수7
    askp_csnu8: Optional[str] = None  # 매도호가건수8
    askp_csnu9: Optional[str] = None  # 매도호가건수9
    askp_csnu10: Optional[str] = None  # 매도호가건수10
    bidp_csnu1: Optional[str] = None  # 매수호가건수1
    bidp_csnu2: Optional[str] = None  # 매수호가건수2
    bidp_csnu3: Optional[str] = None  # 매수호가건수3
    bidp_csnu4: Optional[str] = None  # 매수호가건수4
    bidp_csnu5: Optional[str] = None  # 매수호가건수5
    bidp_csnu6: Optional[str] = None  # 매수호가건수6
    bidp_csnu7: Optional[str] = None  # 매수호가건수7
    bidp_csnu8: Optional[str] = None  # 매수호가건수8
    bidp_csnu9: Optional[str] = None  # 매수호가건수9
    bidp_csnu10: Optional[str] = None  # 매수호가건수10
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    askp_rsqn2: Optional[str] = None  # 매도호가잔량2
    askp_rsqn3: Optional[str] = None  # 매도호가잔량3
    askp_rsqn4: Optional[str] = None  # 매도호가잔량4
    askp_rsqn5: Optional[str] = None  # 매도호가잔량5
    askp_rsqn6: Optional[str] = None  # 매도호가잔량6
    askp_rsqn7: Optional[str] = None  # 매도호가잔량7
    askp_rsqn8: Optional[str] = None  # 매도호가잔량8
    askp_rsqn9: Optional[str] = None  # 매도호가잔량9
    askp_rsqn10: Optional[str] = None  # 매도호가잔량10
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    bidp_rsqn2: Optional[str] = None  # 매수호가잔량2
    bidp_rsqn3: Optional[str] = None  # 매수호가잔량3
    bidp_rsqn4: Optional[str] = None  # 매수호가잔량4
    bidp_rsqn5: Optional[str] = None  # 매수호가잔량5
    bidp_rsqn6: Optional[str] = None  # 매수호가잔량6
    bidp_rsqn7: Optional[str] = None  # 매수호가잔량7
    bidp_rsqn8: Optional[str] = None  # 매수호가잔량8
    bidp_rsqn9: Optional[str] = None  # 매수호가잔량9
    bidp_rsqn10: Optional[str] = None  # 매수호가잔량10
    total_askp_csnu: Optional[str] = None  # 총매도호가건수
    total_bidp_csnu: Optional[str] = None  # 총매수호가건수
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    total_askp_rsqn_icdc: Optional[str] = None  # 총매도호가잔량증감
    total_bidp_rsqn_icdc: Optional[str] = None  # 총매수호가잔량증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class StockOptionAskingPrice(SQLModel, table=True):
    """Output table for stock_option_asking_price"""
    __tablename__ = "kis_stock_option_asking_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    optn_shrn_iscd: Optional[str] = None  # 종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    optn_askp1: Optional[str] = None  # 옵션매도호가1
    optn_askp2: Optional[str] = None  # 옵션매도호가2
    optn_askp3: Optional[str] = None  # 옵션매도호가3
    optn_askp4: Optional[str] = None  # 옵션매도호가4
    optn_askp5: Optional[str] = None  # 옵션매도호가5
    optn_bidp1: Optional[str] = None  # 옵션매수호가1
    optn_bidp2: Optional[str] = None  # 옵션매수호가2
    optn_bidp3: Optional[str] = None  # 옵션매수호가3
    optn_bidp4: Optional[str] = None  # 옵션매수호가4
    optn_bidp5: Optional[str] = None  # 옵션매수호가5
    askp_csnu1: Optional[str] = None  # 매도호가건수1
    askp_csnu2: Optional[str] = None  # 매도호가건수2
    askp_csnu3: Optional[str] = None  # 매도호가건수3
    askp_csnu4: Optional[str] = None  # 매도호가건수4
    askp_csnu5: Optional[str] = None  # 매도호가건수5
    bidp_csnu1: Optional[str] = None  # 매수호가건수1
    bidp_csnu2: Optional[str] = None  # 매수호가건수2
    bidp_csnu3: Optional[str] = None  # 매수호가건수3
    bidp_csnu4: Optional[str] = None  # 매수호가건수4
    bidp_csnu5: Optional[str] = None  # 매수호가건수5
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    askp_rsqn2: Optional[str] = None  # 매도호가잔량2
    askp_rsqn3: Optional[str] = None  # 매도호가잔량3
    askp_rsqn4: Optional[str] = None  # 매도호가잔량4
    askp_rsqn5: Optional[str] = None  # 매도호가잔량5
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    bidp_rsqn2: Optional[str] = None  # 매수호가잔량2
    bidp_rsqn3: Optional[str] = None  # 매수호가잔량3
    bidp_rsqn4: Optional[str] = None  # 매수호가잔량4
    bidp_rsqn5: Optional[str] = None  # 매수호가잔량5
    total_askp_csnu: Optional[str] = None  # 총매도호가건수
    total_bidp_csnu: Optional[str] = None  # 총매수호가건수
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    total_askp_rsqn_icdc: Optional[str] = None  # 총매도호가잔량증감
    total_bidp_rsqn_icdc: Optional[str] = None  # 총매수호가잔량증감
    optn_askp6: Optional[str] = None  # 옵션매도호가6
    optn_askp7: Optional[str] = None  # 옵션매도호가7
    optn_askp8: Optional[str] = None  # 옵션매도호가8
    optn_askp9: Optional[str] = None  # 옵션매도호가9
    optn_askp10: Optional[str] = None  # 옵션매도호가10
    optn_bidp6: Optional[str] = None  # 옵션매수호가6
    optn_bidp7: Optional[str] = None  # 옵션매수호가7
    optn_bidp8: Optional[str] = None  # 옵션매수호가8
    optn_bidp9: Optional[str] = None  # 옵션매수호가9
    optn_bidp10: Optional[str] = None  # 옵션매수호가10
    askp_csnu6: Optional[str] = None  # 매도호가건수6
    askp_csnu7: Optional[str] = None  # 매도호가건수7
    askp_csnu8: Optional[str] = None  # 매도호가건수8
    askp_csnu9: Optional[str] = None  # 매도호가건수9
    askp_csnu10: Optional[str] = None  # 매도호가건수10
    bidp_csnu6: Optional[str] = None  # 매수호가건수6
    bidp_csnu7: Optional[str] = None  # 매수호가건수7
    bidp_csnu8: Optional[str] = None  # 매수호가건수8
    bidp_csnu9: Optional[str] = None  # 매수호가건수9
    bidp_csnu10: Optional[str] = None  # 매수호가건수10
    askp_rsqn6: Optional[str] = None  # 매도호가잔량6
    askp_rsqn7: Optional[str] = None  # 매도호가잔량7
    askp_rsqn8: Optional[str] = None  # 매도호가잔량8
    askp_rsqn9: Optional[str] = None  # 매도호가잔량9
    askp_rsqn10: Optional[str] = None  # 매도호가잔량10
    bidp_rsqn6: Optional[str] = None  # 매수호가잔량6
    bidp_rsqn7: Optional[str] = None  # 매수호가잔량7
    bidp_rsqn8: Optional[str] = None  # 매수호가잔량8
    bidp_rsqn9: Optional[str] = None  # 매수호가잔량9
    bidp_rsqn10: Optional[str] = None  # 매수호가잔량10
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class StockOptionCcnl(SQLModel, table=True):
    """Output table for stock_option_ccnl"""
    __tablename__ = "kis_stock_option_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    optn_shrn_iscd: Optional[str] = None  # 종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    optn_prpr: Optional[str] = None  # 옵션현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    optn_prdy_vrss: Optional[str] = None  # 옵션전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    optn_oprc: Optional[str] = None  # 옵션시가2
    optn_hgpr: Optional[str] = None  # 옵션최고가
    optn_lwpr: Optional[str] = None  # 옵션최저가
    last_cnqn: Optional[str] = None  # 최종거래량
    acml_vol: Optional[str] = None  # 누적거래량
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    hts_thpr: Optional[str] = None  # HTS이론가
    hts_otst_stpl_qty: Optional[str] = None  # HTS미결제약정수량
    otst_stpl_qty_icdc: Optional[str] = None  # 미결제약정수량증감
    oprc_hour: Optional[str] = None  # 시가시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2대비현재가부호
    oprc_vrss_nmix_prpr: Optional[str] = None  # 시가대비지수현재가
    hgpr_hour: Optional[str] = None  # 최고가시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가대비현재가부호
    hgpr_vrss_nmix_prpr: Optional[str] = None  # 최고가대비지수현재가
    lwpr_hour: Optional[str] = None  # 최저가시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가대비현재가부호
    lwpr_vrss_nmix_prpr: Optional[str] = None  # 최저가대비지수현재가
    shnu_rate: Optional[str] = None  # 매수2비율
    prmm_val: Optional[str] = None  # 프리미엄값
    invl_val: Optional[str] = None  # 내재가치값
    tmvl_val: Optional[str] = None  # 시간가치값
    delta: Optional[str] = None  # 델타
    gama: Optional[str] = None  # 감마
    vega: Optional[str] = None  # 베가
    theta: Optional[str] = None  # 세타
    rho: Optional[str] = None  # 로우
    hts_ints_vltl: Optional[str] = None  # HTS내재변동성
    esdg: Optional[str] = None  # 괴리도
    otst_stpl_rgbf_qty_icdc: Optional[str] = None  # 미결제약정직전수량증감
    thpr_basis: Optional[str] = None  # 이론베이시스
    unas_hist_vltl: Optional[str] = None  # 역사적변동성
    cttr: Optional[str] = None  # 체결강도
    dprt: Optional[str] = None  # 괴리율
    mrkt_basis: Optional[str] = None  # 시장베이시스
    optn_askp1: Optional[str] = None  # 옵션매도호가1
    optn_bidp1: Optional[str] = None  # 옵션매수호가1
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    seln_cntg_csnu: Optional[str] = None  # 매도체결건수
    shnu_cntg_csnu: Optional[str] = None  # 매수체결건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수체결건수
    seln_cntg_smtn: Optional[str] = None  # 총매도수량
    shnu_cntg_smtn: Optional[str] = None  # 총매수수량
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일거래량대비등락율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class AfterHourBalance(SQLModel, table=True):
    """Output table for after_hour_balance"""
    __tablename__ = "kis_after_hour_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    data_rank: Optional[str] = None  # 데이터 순위
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    ovtm_total_askp_rsqn: Optional[str] = None  # 시간외 총 매도호가 잔량
    ovtm_total_bidp_rsqn: Optional[str] = None  # 시간외 총 매수호가 잔량
    mkob_otcp_vol: Optional[str] = None  # 장개시전 시간외종가 거래량
    mkfa_otcp_vol: Optional[str] = None  # 장종료후 시간외종가 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class AskingPriceKrx(SQLModel, table=True):
    """Output table for asking_price_krx"""
    __tablename__ = "kis_asking_price_krx"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권 단축 종목코드
    BSOP_HOUR: Optional[str] = None  # 영업 시간
    HOUR_CLS_CODE: Optional[str] = None  # 시간 구분 코드
    ASKP1: Optional[str] = None  # 매도호가1
    ASKP2: Optional[str] = None  # 매도호가2
    ASKP3: Optional[str] = None  # 매도호가3
    ASKP4: Optional[str] = None  # 매도호가4
    ASKP5: Optional[str] = None  # 매도호가5
    ASKP6: Optional[str] = None  # 매도호가6
    ASKP7: Optional[str] = None  # 매도호가7
    ASKP8: Optional[str] = None  # 매도호가8
    ASKP9: Optional[str] = None  # 매도호가9
    ASKP10: Optional[str] = None  # 매도호가10
    BIDP1: Optional[str] = None  # 매수호가1
    BIDP2: Optional[str] = None  # 매수호가2
    BIDP3: Optional[str] = None  # 매수호가3
    BIDP4: Optional[str] = None  # 매수호가4
    BIDP5: Optional[str] = None  # 매수호가5
    BIDP6: Optional[str] = None  # 매수호가6
    BIDP7: Optional[str] = None  # 매수호가7
    BIDP8: Optional[str] = None  # 매수호가8
    BIDP9: Optional[str] = None  # 매수호가9
    BIDP10: Optional[str] = None  # 매수호가10
    ASKP_RSQN1: Optional[str] = None  # 매도호가 잔량1
    ASKP_RSQN2: Optional[str] = None  # 매도호가 잔량2
    ASKP_RSQN3: Optional[str] = None  # 매도호가 잔량3
    ASKP_RSQN4: Optional[str] = None  # 매도호가 잔량4
    ASKP_RSQN5: Optional[str] = None  # 매도호가 잔량5
    ASKP_RSQN6: Optional[str] = None  # 매도호가 잔량6
    ASKP_RSQN7: Optional[str] = None  # 매도호가 잔량7
    ASKP_RSQN8: Optional[str] = None  # 매도호가 잔량8
    ASKP_RSQN9: Optional[str] = None  # 매도호가 잔량9
    ASKP_RSQN10: Optional[str] = None  # 매도호가 잔량10
    BIDP_RSQN1: Optional[str] = None  # 매수호가 잔량1
    BIDP_RSQN2: Optional[str] = None  # 매수호가 잔량2
    BIDP_RSQN3: Optional[str] = None  # 매수호가 잔량3
    BIDP_RSQN4: Optional[str] = None  # 매수호가 잔량4
    BIDP_RSQN5: Optional[str] = None  # 매수호가 잔량5
    BIDP_RSQN6: Optional[str] = None  # 매수호가 잔량6
    BIDP_RSQN7: Optional[str] = None  # 매수호가 잔량7
    BIDP_RSQN8: Optional[str] = None  # 매수호가 잔량8
    BIDP_RSQN9: Optional[str] = None  # 매수호가 잔량9
    BIDP_RSQN10: Optional[str] = None  # 매수호가 잔량10
    TOTAL_ASKP_RSQN: Optional[str] = None  # 총 매도호가 잔량
    TOTAL_BIDP_RSQN: Optional[str] = None  # 총 매수호가 잔량
    OVTM_TOTAL_ASKP_RSQN: Optional[str] = None  # 시간외 총 매도호가 잔량
    OVTM_TOTAL_BIDP_RSQN: Optional[str] = None  # 시간외 총 매수호가 잔량
    ANTC_CNPR: Optional[str] = None  # 예상 체결가
    ANTC_CNQN: Optional[str] = None  # 예상 체결량
    ANTC_VOL: Optional[str] = None  # 예상 거래량
    ANTC_CNTG_VRSS: Optional[str] = None  # 예상 체결 대비
    ANTC_CNTG_VRSS_SIGN: Optional[str] = None  # 예상 체결 대비 부호
    ANTC_CNTG_PRDY_CTRT: Optional[str] = None  # 예상 체결 전일 대비율
    ACML_VOL: Optional[str] = None  # 누적 거래량
    TOTAL_ASKP_RSQN_ICDC: Optional[str] = None  # 총 매도호가 잔량 증감
    TOTAL_BIDP_RSQN_ICDC: Optional[str] = None  # 총 매수호가 잔량 증감
    OVTM_TOTAL_ASKP_ICDC: Optional[str] = None  # 시간외 총 매도호가 증감
    OVTM_TOTAL_BIDP_ICDC: Optional[str] = None  # 시간외 총 매수호가 증감
    STCK_DEAL_CLS_CODE: Optional[str] = None  # 주식 매매 구분 코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class AskingPriceNxt(SQLModel, table=True):
    """Output table for asking_price_nxt"""
    __tablename__ = "kis_asking_price_nxt"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권 단축 종목코드
    BSOP_HOUR: Optional[str] = None  # 영업 시간
    HOUR_CLS_CODE: Optional[str] = None  # 시간 구분 코드
    ASKP1: Optional[str] = None  # 매도호가1
    ASKP2: Optional[str] = None  # 매도호가2
    ASKP3: Optional[str] = None  # 매도호가3
    ASKP4: Optional[str] = None  # 매도호가4
    ASKP5: Optional[str] = None  # 매도호가5
    ASKP6: Optional[str] = None  # 매도호가6
    ASKP7: Optional[str] = None  # 매도호가7
    ASKP8: Optional[str] = None  # 매도호가8
    ASKP9: Optional[str] = None  # 매도호가9
    ASKP10: Optional[str] = None  # 매도호가10
    BIDP1: Optional[str] = None  # 매수호가1
    BIDP2: Optional[str] = None  # 매수호가2
    BIDP3: Optional[str] = None  # 매수호가3
    BIDP4: Optional[str] = None  # 매수호가4
    BIDP5: Optional[str] = None  # 매수호가5
    BIDP6: Optional[str] = None  # 매수호가6
    BIDP7: Optional[str] = None  # 매수호가7
    BIDP8: Optional[str] = None  # 매수호가8
    BIDP9: Optional[str] = None  # 매수호가9
    BIDP10: Optional[str] = None  # 매수호가10
    ASKP_RSQN1: Optional[str] = None  # 매도호가 잔량1
    ASKP_RSQN2: Optional[str] = None  # 매도호가 잔량2
    ASKP_RSQN3: Optional[str] = None  # 매도호가 잔량3
    ASKP_RSQN4: Optional[str] = None  # 매도호가 잔량4
    ASKP_RSQN5: Optional[str] = None  # 매도호가 잔량5
    ASKP_RSQN6: Optional[str] = None  # 매도호가 잔량6
    ASKP_RSQN7: Optional[str] = None  # 매도호가 잔량7
    ASKP_RSQN8: Optional[str] = None  # 매도호가 잔량8
    ASKP_RSQN9: Optional[str] = None  # 매도호가 잔량9
    ASKP_RSQN10: Optional[str] = None  # 매도호가 잔량10
    BIDP_RSQN1: Optional[str] = None  # 매수호가 잔량1
    BIDP_RSQN2: Optional[str] = None  # 매수호가 잔량2
    BIDP_RSQN3: Optional[str] = None  # 매수호가 잔량3
    BIDP_RSQN4: Optional[str] = None  # 매수호가 잔량4
    BIDP_RSQN5: Optional[str] = None  # 매수호가 잔량5
    BIDP_RSQN6: Optional[str] = None  # 매수호가 잔량6
    BIDP_RSQN7: Optional[str] = None  # 매수호가 잔량7
    BIDP_RSQN8: Optional[str] = None  # 매수호가 잔량8
    BIDP_RSQN9: Optional[str] = None  # 매수호가 잔량9
    BIDP_RSQN10: Optional[str] = None  # 매수호가 잔량10
    TOTAL_ASKP_RSQN: Optional[str] = None  # 총 매도호가 잔량
    TOTAL_BIDP_RSQN: Optional[str] = None  # 총 매수호가 잔량
    OVTM_TOTAL_ASKP_RSQN: Optional[str] = None  # 시간외 총 매도호가 잔량
    OVTM_TOTAL_BIDP_RSQN: Optional[str] = None  # 시간외 총 매수호가 잔량
    ANTC_CNPR: Optional[str] = None  # 예상 체결가
    ANTC_CNQN: Optional[str] = None  # 예상 체결량
    ANTC_VOL: Optional[str] = None  # 예상 거래량
    ANTC_CNTG_VRSS: Optional[str] = None  # 예상 체결 대비
    ANTC_CNTG_VRSS_SIGN: Optional[str] = None  # 예상 체결 대비 부호
    ANTC_CNTG_PRDY_CTRT: Optional[str] = None  # 예상 체결 전일 대비율
    ACML_VOL: Optional[str] = None  # 누적 거래량
    TOTAL_ASKP_RSQN_ICDC: Optional[str] = None  # 총 매도호가 잔량 증감
    TOTAL_BIDP_RSQN_ICDC: Optional[str] = None  # 총 매수호가 잔량 증감
    OVTM_TOTAL_ASKP_ICDC: Optional[str] = None  # 시간외 총 매도호가 증감
    OVTM_TOTAL_BIDP_ICDC: Optional[str] = None  # 시간외 총 매수호가 증감
    STCK_DEAL_CLS_CODE: Optional[str] = None  # 주식 매매 구분 코드
    KMID_PRC: Optional[str] = None  # KRX 중간가
    KMID_TOTAL_RSQN: Optional[str] = None  # KRX 중간가잔량합계수량
    KMID_CLS_CODE: Optional[str] = None  # KRX 중간가 매수매도 구분
    NMID_PRC: Optional[str] = None  # NXT 중간가
    NMID_TOTAL_RSQN: Optional[str] = None  # NXT 중간가잔량합계수량
    NMID_CLS_CODE: Optional[str] = None  # NXT 중간가 매수매도 구분
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class AskingPriceTotal(SQLModel, table=True):
    """Output table for asking_price_total"""
    __tablename__ = "kis_asking_price_total"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권 단축 종목코드
    BSOP_HOUR: Optional[str] = None  # 영업 시간
    HOUR_CLS_CODE: Optional[str] = None  # 시간 구분 코드
    ASKP1: Optional[str] = None  # 매도호가1
    ASKP2: Optional[str] = None  # 매도호가2
    ASKP3: Optional[str] = None  # 매도호가3
    ASKP4: Optional[str] = None  # 매도호가4
    ASKP5: Optional[str] = None  # 매도호가5
    ASKP6: Optional[str] = None  # 매도호가6
    ASKP7: Optional[str] = None  # 매도호가7
    ASKP8: Optional[str] = None  # 매도호가8
    ASKP9: Optional[str] = None  # 매도호가9
    ASKP10: Optional[str] = None  # 매도호가10
    BIDP1: Optional[str] = None  # 매수호가1
    BIDP2: Optional[str] = None  # 매수호가2
    BIDP3: Optional[str] = None  # 매수호가3
    BIDP4: Optional[str] = None  # 매수호가4
    BIDP5: Optional[str] = None  # 매수호가5
    BIDP6: Optional[str] = None  # 매수호가6
    BIDP7: Optional[str] = None  # 매수호가7
    BIDP8: Optional[str] = None  # 매수호가8
    BIDP9: Optional[str] = None  # 매수호가9
    BIDP10: Optional[str] = None  # 매수호가10
    ASKP_RSQN1: Optional[str] = None  # 매도호가 잔량1
    ASKP_RSQN2: Optional[str] = None  # 매도호가 잔량2
    ASKP_RSQN3: Optional[str] = None  # 매도호가 잔량3
    ASKP_RSQN4: Optional[str] = None  # 매도호가 잔량4
    ASKP_RSQN5: Optional[str] = None  # 매도호가 잔량5
    ASKP_RSQN6: Optional[str] = None  # 매도호가 잔량6
    ASKP_RSQN7: Optional[str] = None  # 매도호가 잔량7
    ASKP_RSQN8: Optional[str] = None  # 매도호가 잔량8
    ASKP_RSQN9: Optional[str] = None  # 매도호가 잔량9
    ASKP_RSQN10: Optional[str] = None  # 매도호가 잔량10
    BIDP_RSQN1: Optional[str] = None  # 매수호가 잔량1
    BIDP_RSQN2: Optional[str] = None  # 매수호가 잔량2
    BIDP_RSQN3: Optional[str] = None  # 매수호가 잔량3
    BIDP_RSQN4: Optional[str] = None  # 매수호가 잔량4
    BIDP_RSQN5: Optional[str] = None  # 매수호가 잔량5
    BIDP_RSQN6: Optional[str] = None  # 매수호가 잔량6
    BIDP_RSQN7: Optional[str] = None  # 매수호가 잔량7
    BIDP_RSQN8: Optional[str] = None  # 매수호가 잔량8
    BIDP_RSQN9: Optional[str] = None  # 매수호가 잔량9
    BIDP_RSQN10: Optional[str] = None  # 매수호가 잔량10
    TOTAL_ASKP_RSQN: Optional[str] = None  # 총 매도호가 잔량
    TOTAL_BIDP_RSQN: Optional[str] = None  # 총 매수호가 잔량
    OVTM_TOTAL_ASKP_RSQN: Optional[str] = None  # 시간외 총 매도호가 잔량
    OVTM_TOTAL_BIDP_RSQN: Optional[str] = None  # 시간외 총 매수호가 잔량
    ANTC_CNPR: Optional[str] = None  # 예상 체결가
    ANTC_CNQN: Optional[str] = None  # 예상 체결량
    ANTC_VOL: Optional[str] = None  # 예상 거래량
    ANTC_CNTG_VRSS: Optional[str] = None  # 예상 체결 대비
    ANTC_CNTG_VRSS_SIGN: Optional[str] = None  # 예상 체결 대비 부호
    ANTC_CNTG_PRDY_CTRT: Optional[str] = None  # 예상 체결 전일 대비율
    ACML_VOL: Optional[str] = None  # 누적 거래량
    TOTAL_ASKP_RSQN_ICDC: Optional[str] = None  # 총 매도호가 잔량 증감
    TOTAL_BIDP_RSQN_ICDC: Optional[str] = None  # 총 매수호가 잔량 증감
    OVTM_TOTAL_ASKP_ICDC: Optional[str] = None  # 시간외 총 매도호가 증감
    OVTM_TOTAL_BIDP_ICDC: Optional[str] = None  # 시간외 총 매수호가 증감
    STCK_DEAL_CLS_CODE: Optional[str] = None  # 주식 매매 구분 코드
    KMID_PRC: Optional[str] = None  # KRX 중간가
    KMID_TOTAL_RSQN: Optional[str] = None  # KRX 중간가잔량합계수량
    KMID_CLS_CODE: Optional[str] = None  # KRX 중간가 매수매도 구분
    NMID_PRC: Optional[str] = None  # NXT 중간가
    NMID_TOTAL_RSQN: Optional[str] = None  # NXT 중간가잔량합계수량
    NMID_CLS_CODE: Optional[str] = None  # NXT 중간가 매수매도 구분
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class BulkTransNum(SQLModel, table=True):
    """Output table for bulk_trans_num"""
    __tablename__ = "kis_bulk_trans_num"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    data_rank: Optional[str] = None  # 데이터 순위
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    shnu_cntg_csnu: Optional[str] = None  # 매수2 체결 건수
    seln_cntg_csnu: Optional[str] = None  # 매도 체결 건수
    ntby_cnqn: Optional[str] = None  # 순매수 체결량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CaptureUplowprice(SQLModel, table=True):
    """Output table for capture_uplowprice"""
    __tablename__ = "kis_capture_uplowprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    hts_kor_isnm: Optional[str] = None  # HTS한글종목명
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    prdy_vol: Optional[str] = None  # 전일거래량
    seln_cnqn: Optional[str] = None  # 매도체결량
    shnu_cnqn: Optional[str] = None  # 매수2체결량
    stck_llam: Optional[str] = None  # 주식하한가
    stck_mxpr: Optional[str] = None  # 주식상한가
    prdy_vrss_vol_rate: Optional[str] = None  # 전일대비거래량비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CcnlKrx(SQLModel, table=True):
    """Output table for ccnl_krx"""
    __tablename__ = "kis_ccnl_krx"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권 단축 종목코드
    STCK_CNTG_HOUR: Optional[str] = None  # 주식 체결 시간
    STCK_PRPR: Optional[str] = None  # 주식 현재가
    PRDY_VRSS_SIGN: Optional[str] = None  # 전일 대비 부호
    PRDY_VRSS: Optional[str] = None  # 전일 대비
    PRDY_CTRT: Optional[str] = None  # 전일 대비율
    WGHN_AVRG_STCK_PRC: Optional[str] = None  # 가중 평균 주식 가격
    STCK_OPRC: Optional[str] = None  # 주식 시가
    STCK_HGPR: Optional[str] = None  # 주식 최고가
    STCK_LWPR: Optional[str] = None  # 주식 최저가
    ASKP1: Optional[str] = None  # 매도호가1
    BIDP1: Optional[str] = None  # 매수호가1
    CNTG_VOL: Optional[str] = None  # 체결 거래량
    ACML_VOL: Optional[str] = None  # 누적 거래량
    ACML_TR_PBMN: Optional[str] = None  # 누적 거래 대금
    SELN_CNTG_CSNU: Optional[str] = None  # 매도 체결 건수
    SHNU_CNTG_CSNU: Optional[str] = None  # 매수 체결 건수
    NTBY_CNTG_CSNU: Optional[str] = None  # 순매수 체결 건수
    CTTR: Optional[str] = None  # 체결강도
    SELN_CNTG_SMTN: Optional[str] = None  # 총 매도 수량
    SHNU_CNTG_SMTN: Optional[str] = None  # 총 매수 수량
    CCLD_DVSN: Optional[str] = None  # 체결구분
    SHNU_RATE: Optional[str] = None  # 매수비율
    PRDY_VOL_VRSS_ACML_VOL_RATE: Optional[str] = None  # 전일 거래량 대비 등락율
    OPRC_HOUR: Optional[str] = None  # 시가 시간
    OPRC_VRSS_PRPR_SIGN: Optional[str] = None  # 시가대비구분
    OPRC_VRSS_PRPR: Optional[str] = None  # 시가대비
    HGPR_HOUR: Optional[str] = None  # 최고가 시간
    HGPR_VRSS_PRPR_SIGN: Optional[str] = None  # 고가대비구분
    HGPR_VRSS_PRPR: Optional[str] = None  # 고가대비
    LWPR_HOUR: Optional[str] = None  # 최저가 시간
    LWPR_VRSS_PRPR_SIGN: Optional[str] = None  # 저가대비구분
    LWPR_VRSS_PRPR: Optional[str] = None  # 저가대비
    BSOP_DATE: Optional[str] = None  # 영업 일자
    NEW_MKOP_CLS_CODE: Optional[str] = None  # 신 장운영 구분 코드
    TRHT_YN: Optional[str] = None  # 거래정지 여부
    ASKP_RSQN1: Optional[str] = None  # 매도호가 잔량1
    BIDP_RSQN1: Optional[str] = None  # 매수호가 잔량1
    TOTAL_ASKP_RSQN: Optional[str] = None  # 총 매도호가 잔량
    TOTAL_BIDP_RSQN: Optional[str] = None  # 총 매수호가 잔량
    VOL_TNRT: Optional[str] = None  # 거래량 회전율
    PRDY_SMNS_HOUR_ACML_VOL: Optional[str] = None  # 전일 동시간 누적 거래량
    PRDY_SMNS_HOUR_ACML_VOL_RATE: Optional[str] = None  # 전일 동시간 누적 거래량 비율
    HOUR_CLS_CODE: Optional[str] = None  # 시간 구분 코드
    MRKT_TRTM_CLS_CODE: Optional[str] = None  # 임의종료구분코드
    VI_STND_PRC: Optional[str] = None  # 정적VI발동기준가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CcnlNotice(SQLModel, table=True):
    """Output table for ccnl_notice"""
    __tablename__ = "kis_ccnl_notice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    CUST_ID: Optional[str] = None  # 고객 ID
    ACNT_NO: Optional[str] = None  # 계좌번호
    ODER_NO: Optional[str] = None  # 주문번호
    OODER_NO: Optional[str] = None  # 원주문번호
    SELN_BYOV_CLS: Optional[str] = None  # 매도매수구분
    RCTF_CLS: Optional[str] = None  # 정정구분
    ODER_KIND2: Optional[str] = None  # 주문종류2
    STCK_SHRN_ISCD: Optional[str] = None  # 주식 단축 종목코드
    CNTG_QTY: Optional[str] = None  # 체결수량
    CNTG_UNPR: Optional[str] = None  # 체결단가12
    STCK_CNTG_HOUR: Optional[str] = None  # 주식 체결 시간
    RFUS_YN: Optional[str] = None  # 거부여부
    CNTG_YN: Optional[str] = None  # 체결여부
    ACPT_YN: Optional[str] = None  # 접수여부
    BRNC_NO: Optional[str] = None  # 지점번호
    ODER_QTY: Optional[str] = None  # 주문 수량
    ACNT_NAME: Optional[str] = None  # 계좌명
    CNTG_ISNM: Optional[str] = None  # 체결종목명
    ODER_COND: Optional[str] = None  # 해외종목구분
    DEBT_GB: Optional[str] = None  # 담보유형코드
    DEBT_DATE: Optional[str] = None  # 담보대출일자
    START_TM: Optional[str] = None  # 분할매수/매도 시작시간
    END_TM: Optional[str] = None  # 분할매수/매도 종료시간
    TM_DIV_TP: Optional[str] = None  # 시간분할타입유형
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CcnlNxt(SQLModel, table=True):
    """Output table for ccnl_nxt"""
    __tablename__ = "kis_ccnl_nxt"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권 단축 종목코드
    STCK_CNTG_HOUR: Optional[str] = None  # 주식 체결 시간
    STCK_PRPR: Optional[str] = None  # 주식 현재가
    PRDY_VRSS_SIGN: Optional[str] = None  # 전일 대비 부호
    PRDY_VRSS: Optional[str] = None  # 전일 대비
    PRDY_CTRT: Optional[str] = None  # 전일 대비율
    WGHN_AVRG_STCK_PRC: Optional[str] = None  # 가중 평균 주식 가격
    STCK_OPRC: Optional[str] = None  # 주식 시가
    STCK_HGPR: Optional[str] = None  # 주식 최고가
    STCK_LWPR: Optional[str] = None  # 주식 최저가
    ASKP1: Optional[str] = None  # 매도호가1
    BIDP1: Optional[str] = None  # 매수호가1
    CNTG_VOL: Optional[str] = None  # 체결 거래량
    ACML_VOL: Optional[str] = None  # 누적 거래량
    ACML_TR_PBMN: Optional[str] = None  # 누적 거래 대금
    SELN_CNTG_CSNU: Optional[str] = None  # 매도 체결 건수
    SHNU_CNTG_CSNU: Optional[str] = None  # 매수 체결 건수
    NTBY_CNTG_CSNU: Optional[str] = None  # 순매수 체결 건수
    CTTR: Optional[str] = None  # 체결강도
    SELN_CNTG_SMTN: Optional[str] = None  # 총 매도 수량
    SHNU_CNTG_SMTN: Optional[str] = None  # 총 매수 수량
    CNTG_CLS_CODE: Optional[str] = None  # 체결구분
    SHNU_RATE: Optional[str] = None  # 매수비율
    PRDY_VOL_VRSS_ACML_VOL_RATE: Optional[str] = None  # 전일 거래량 대비 등락율
    OPRC_HOUR: Optional[str] = None  # 시가 시간
    OPRC_VRSS_PRPR_SIGN: Optional[str] = None  # 시가대비구분
    OPRC_VRSS_PRPR: Optional[str] = None  # 시가대비
    HGPR_HOUR: Optional[str] = None  # 최고가 시간
    HGPR_VRSS_PRPR_SIGN: Optional[str] = None  # 고가대비구분
    HGPR_VRSS_PRPR: Optional[str] = None  # 고가대비
    LWPR_HOUR: Optional[str] = None  # 최저가 시간
    LWPR_VRSS_PRPR_SIGN: Optional[str] = None  # 저가대비구분
    LWPR_VRSS_PRPR: Optional[str] = None  # 저가대비
    BSOP_DATE: Optional[str] = None  # 영업 일자
    NEW_MKOP_CLS_CODE: Optional[str] = None  # 신 장운영 구분 코드
    TRHT_YN: Optional[str] = None  # 거래정지 여부
    ASKP_RSQN1: Optional[str] = None  # 매도호가 잔량1
    BIDP_RSQN1: Optional[str] = None  # 매수호가 잔량1
    TOTAL_ASKP_RSQN: Optional[str] = None  # 총 매도호가 잔량
    TOTAL_BIDP_RSQN: Optional[str] = None  # 총 매수호가 잔량
    VOL_TNRT: Optional[str] = None  # 거래량 회전율
    PRDY_SMNS_HOUR_ACML_VOL: Optional[str] = None  # 전일 동시간 누적 거래량
    PRDY_SMNS_HOUR_ACML_VOL_RATE: Optional[str] = None  # 전일 동시간 누적 거래량 비율
    HOUR_CLS_CODE: Optional[str] = None  # 시간 구분 코드
    MRKT_TRTM_CLS_CODE: Optional[str] = None  # 임의종료구분코드
    VI_STND_PRC: Optional[str] = None  # 정적VI발동기준가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CcnlTotal(SQLModel, table=True):
    """Output table for ccnl_total"""
    __tablename__ = "kis_ccnl_total"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권 단축 종목코드
    STCK_CNTG_HOUR: Optional[str] = None  # 주식 체결 시간
    STCK_PRPR: Optional[str] = None  # 주식 현재가
    PRDY_VRSS_SIGN: Optional[str] = None  # 전일 대비 부호
    PRDY_VRSS: Optional[str] = None  # 전일 대비
    PRDY_CTRT: Optional[str] = None  # 전일 대비율
    WGHN_AVRG_STCK_PRC: Optional[str] = None  # 가중 평균 주식 가격
    STCK_OPRC: Optional[str] = None  # 주식 시가
    STCK_HGPR: Optional[str] = None  # 주식 최고가
    STCK_LWPR: Optional[str] = None  # 주식 최저가
    ASKP1: Optional[str] = None  # 매도호가1
    BIDP1: Optional[str] = None  # 매수호가1
    CNTG_VOL: Optional[str] = None  # 체결 거래량
    ACML_VOL: Optional[str] = None  # 누적 거래량
    ACML_TR_PBMN: Optional[str] = None  # 누적 거래 대금
    SELN_CNTG_CSNU: Optional[str] = None  # 매도 체결 건수
    SHNU_CNTG_CSNU: Optional[str] = None  # 매수 체결 건수
    NTBY_CNTG_CSNU: Optional[str] = None  # 순매수 체결 건수
    CTTR: Optional[str] = None  # 체결강도
    SELN_CNTG_SMTN: Optional[str] = None  # 총 매도 수량
    SHNU_CNTG_SMTN: Optional[str] = None  # 총 매수 수량
    CNTG_CLS_CODE: Optional[str] = None  # 체결구분
    SHNU_RATE: Optional[str] = None  # 매수비율
    PRDY_VOL_VRSS_ACML_VOL_RATE: Optional[str] = None  # 전일 거래량 대비 등락율
    OPRC_HOUR: Optional[str] = None  # 시가 시간
    OPRC_VRSS_PRPR_SIGN: Optional[str] = None  # 시가대비구분
    OPRC_VRSS_PRPR: Optional[str] = None  # 시가대비
    HGPR_HOUR: Optional[str] = None  # 최고가 시간
    HGPR_VRSS_PRPR_SIGN: Optional[str] = None  # 고가대비구분
    HGPR_VRSS_PRPR: Optional[str] = None  # 고가대비
    LWPR_HOUR: Optional[str] = None  # 최저가 시간
    LWPR_VRSS_PRPR_SIGN: Optional[str] = None  # 저가대비구분
    LWPR_VRSS_PRPR: Optional[str] = None  # 저가대비
    BSOP_DATE: Optional[str] = None  # 영업 일자
    NEW_MKOP_CLS_CODE: Optional[str] = None  # 신 장운영 구분 코드
    TRHT_YN: Optional[str] = None  # 거래정지 여부
    ASKP_RSQN1: Optional[str] = None  # 매도호가 잔량1
    BIDP_RSQN1: Optional[str] = None  # 매수호가 잔량1
    TOTAL_ASKP_RSQN: Optional[str] = None  # 총 매도호가 잔량
    TOTAL_BIDP_RSQN: Optional[str] = None  # 총 매수호가 잔량
    VOL_TNRT: Optional[str] = None  # 거래량 회전율
    PRDY_SMNS_HOUR_ACML_VOL: Optional[str] = None  # 전일 동시간 누적 거래량
    PRDY_SMNS_HOUR_ACML_VOL_RATE: Optional[str] = None  # 전일 동시간 누적 거래량 비율
    HOUR_CLS_CODE: Optional[str] = None  # 시간 구분 코드
    MRKT_TRTM_CLS_CODE: Optional[str] = None  # 임의종료구분코드
    VI_STND_PRC: Optional[str] = None  # 정적VI발동기준가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ChkHoliday(SQLModel, table=True):
    """Output table for chk_holiday"""
    __tablename__ = "kis_chk_holiday"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bass_dt: Optional[str] = None  # 기준일자
    wday_dvsn_cd: Optional[str] = None  # 요일구분코드
    bzdy_yn: Optional[str] = None  # 영업일여부
    tr_day_yn: Optional[str] = None  # 거래일여부
    opnd_yn: Optional[str] = None  # 개장일여부
    sttl_day_yn: Optional[str] = None  # 결제일여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CompInterest(SQLModel, table=True):
    """Output table for comp_interest"""
    __tablename__ = "kis_comp_interest"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bcdt_code: Optional[str] = None  # 자료코드
    hts_kor_isnm: Optional[str] = None  # HTS한글종목명
    bond_mnrt_prpr: Optional[str] = None  # 채권금리현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    bond_mnrt_prdy_vrss: Optional[str] = None  # 채권금리전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    stck_bsop_date: Optional[str] = None  # 주식영업일자
    bstp_nmix_prdy_ctrt: Optional[str] = None  # 업종지수전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CompProgramTradeDaily(SQLModel, table=True):
    """Output table for comp_program_trade_daily"""
    __tablename__ = "kis_comp_program_trade_daily"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    nabt_entm_seln_tr_pbmn: Optional[str] = None  # 비차익 위탁 매도 거래 대금
    nabt_onsl_seln_vol: Optional[str] = None  # 비차익 자기 매도 거래량
    whol_onsl_seln_tr_pbmn: Optional[str] = None  # 전체 자기 매도 거래 대금
    arbt_smtn_shnu_vol: Optional[str] = None  # 차익 합계 매수2 거래량
    nabt_smtn_shnu_tr_pbmn: Optional[str] = None  # 비차익 합계 매수2 거래 대금
    arbt_entm_ntby_qty: Optional[str] = None  # 차익 위탁 순매수 수량
    nabt_entm_ntby_tr_pbmn: Optional[str] = None  # 비차익 위탁 순매수 거래 대금
    arbt_entm_seln_vol: Optional[str] = None  # 차익 위탁 매도 거래량
    nabt_entm_seln_vol_rate: Optional[str] = None  # 비차익 위탁 매도 거래량 비율
    nabt_onsl_seln_vol_rate: Optional[str] = None  # 전체 자기 매도 거래량 비율
    whol_onsl_seln_tr_pbmn_rate: Optional[str] = None  # 전체 자기 매도 거래 대금 비율
    arbt_smtm_shun_vol_rate: Optional[str] = None  # 차익 합계 매수 거래량 비율
    nabt_smtm_shun_tr_pbmn_rate: Optional[str] = None  # 비차익 합계 매수 거래대금 비율
    arbt_entm_ntby_qty_rate: Optional[str] = None  # 차익 위탁 순매수 수량 비율
    nabt_entm_ntby_tr_pbmn_rate: Optional[str] = None  # 비차익 위탁 순매수 거래 대금
    arbt_entm_seln_vol_rate: Optional[str] = None  # 차익 위탁 매도 거래량 비율
    nabt_entm_seln_tr_pbmn_rate: Optional[str] = None  # 비차익 위탁 매도 거래 대금 비
    nabt_onsl_seln_tr_pbmn: Optional[str] = None  # 비차익 자기 매도 거래 대금
    whol_smtn_seln_vol: Optional[str] = None  # 전체 합계 매도 거래량
    arbt_smtn_shnu_tr_pbmn: Optional[str] = None  # 차익 합계 매수2 거래 대금
    whol_entm_shnu_vol: Optional[str] = None  # 전체 위탁 매수2 거래량
    arbt_entm_ntby_tr_pbmn: Optional[str] = None  # 차익 위탁 순매수 거래 대금
    nabt_onsl_ntby_qty: Optional[str] = None  # 비차익 자기 순매수 수량
    arbt_entm_seln_tr_pbmn: Optional[str] = None  # 차익 위탁 매도 거래 대금
    whol_seln_vol_rate: Optional[str] = None  # 전체 매도 거래량 비율
    whol_entm_shnu_vol_rate: Optional[str] = None  # 전체 위탁 매수 거래량 비율
    whol_entm_seln_tr_pbmn: Optional[str] = None  # 전체 위탁 매도 거래 대금
    nabt_smtm_seln_vol: Optional[str] = None  # 비차익 합계 매도 거래량
    arbt_entm_shnu_vol: Optional[str] = None  # 차익 위탁 매수2 거래량
    nabt_entm_shnu_tr_pbmn: Optional[str] = None  # 비차익 위탁 매수2 거래 대금
    whol_onsl_shnu_vol: Optional[str] = None  # 전체 자기 매수2 거래량
    arbt_onsl_ntby_tr_pbmn: Optional[str] = None  # 차익 자기 순매수 거래 대금
    nabt_smtn_ntby_qty: Optional[str] = None  # 비차익 합계 순매수 수량
    arbt_onsl_seln_vol: Optional[str] = None  # 차익 자기 매도 거래량
    whol_entm_ntby_qty: Optional[str] = None  # 전체 위탁 순매수 수량
    nabt_onsl_ntby_tr_pbmn: Optional[str] = None  # 비차익 자기 순매수 거래 대금
    arbt_onsl_seln_tr_pbmn: Optional[str] = None  # 차익 자기 매도 거래 대금
    nabt_smtm_seln_tr_pbmn_rate: Optional[str] = None  # 비차익 합계 매도 거래대금 비율
    arbt_entm_shnu_vol_rate: Optional[str] = None  # 차익 위탁 매수 거래량 비율
    nabt_entm_shnu_tr_pbmn_rate: Optional[str] = None  # 비차익 위탁 매수 거래 대금 비
    whol_onsl_shnu_tr_pbmn: Optional[str] = None  # 전체 자기 매수2 거래 대금
    arbt_onsl_ntby_tr_pbmn_rate: Optional[str] = None  # 차익 자기 순매수 거래 대금 비
    nabt_smtm_ntby_qty_rate: Optional[str] = None  # 비차익 합계 순매수 수량 비율
    arbt_onsl_seln_vol_rate: Optional[str] = None  # 차익 자기 매도 거래량 비율
    whol_entm_seln_vol: Optional[str] = None  # 전체 위탁 매도 거래량
    arbt_entm_shnu_tr_pbmn: Optional[str] = None  # 차익 위탁 매수2 거래 대금
    nabt_onsl_shnu_vol: Optional[str] = None  # 비차익 자기 매수2 거래량
    whol_smtn_shnu_vol: Optional[str] = None  # 전체 합계 매수2 거래량
    arbt_smtn_ntby_tr_pbmn: Optional[str] = None  # 차익 합계 순매수 거래 대금
    arbt_smtn_seln_vol: Optional[str] = None  # 차익 합계 매도 거래량
    whol_entm_seln_tr_pbmn_rate: Optional[str] = None  # 전체 위탁 매도 거래 대금 비율
    arbt_onsl_shnu_vol_rate: Optional[str] = None  # 차익 자기 매수 거래량 비율
    nabt_smtm_shun_vol_rate: Optional[str] = None  # 비차익 합계 매수 거래량 비율
    whol_shun_tr_pbmn_rate: Optional[str] = None  # 전체 매수 거래대금 비율
    nabt_entm_ntby_qty_rate: Optional[str] = None  # 비차익 위탁 순매수 수량 비율
    arbt_smtm_seln_tr_pbmn_rate: Optional[str] = None  # 차익 합계 매도 거래대금 비율
    arbt_onsl_shnu_vol: Optional[str] = None  # 차익 자기 매수2 거래량
    nabt_onsl_shnu_tr_pbmn: Optional[str] = None  # 비차익 자기 매수2 거래 대금
    nabt_smtn_shnu_vol: Optional[str] = None  # 비차익 합계 매수2 거래량
    whol_smtn_shnu_tr_pbmn: Optional[str] = None  # 전체 합계 매수2 거래 대금
    arbt_smtm_ntby_qty: Optional[str] = None  # 차익 합계 순매수 수량
    nabt_smtn_ntby_tr_pbmn: Optional[str] = None  # 비차익 합계 순매수 거래 대금
    arbt_smtn_seln_tr_pbmn: Optional[str] = None  # 차익 합계 매도 거래 대금
    arbt_onsl_shnu_tr_pbmn_rate: Optional[str] = None  # 차익 자기 매수 거래 대금 비율
    whol_shun_vol_rate: Optional[str] = None  # 전체 매수 거래량 비율
    arbt_smtm_ntby_tr_pbmn_rate: Optional[str] = None  # 차익 합계 순매수 거래대금 비율
    whol_entm_ntby_qty_rate: Optional[str] = None  # 전체 위탁 순매수 수량 비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CompProgramTradeToday(SQLModel, table=True):
    """Output table for comp_program_trade_today"""
    __tablename__ = "kis_comp_program_trade_today"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식영업일자
    stck_clpr: Optional[str] = None  # 주식종가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    whol_smtn_seln_vol: Optional[str] = None  # 전체합계매도거래량
    whol_smtn_shnu_vol: Optional[str] = None  # 전체합계매수2
    whol_smtn_ntby_qty: Optional[str] = None  # 전체합계순매수수량
    whol_smtn_seln_tr_pbmn: Optional[str] = None  # 전체합계매도거래대금
    whol_smtn_shnu_tr_pbmn: Optional[str] = None  # 전체합계매수2거래대금
    whol_smtn_ntby_tr_pbmn: Optional[str] = None  # 전체합계순매수거래대금
    whol_ntby_vol_icdc: Optional[str] = None  # 전체순매수거래량증감
    whol_ntby_tr_pbmn_icdc2: Optional[str] = None  # 전체순매수거래대금증감2
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CreditBalance(SQLModel, table=True):
    """Output table for credit_balance"""
    __tablename__ = "kis_credit_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bstp_cls_code: Optional[str] = None  # 업종 구분 코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stnd_date1: Optional[str] = None  # 기준 일자1
    stnd_date2: Optional[str] = None  # 기준 일자2
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    whol_loan_rmnd_stcn: Optional[str] = None  # 전체 융자 잔고 주수
    whol_loan_rmnd_amt: Optional[str] = None  # 전체 융자 잔고 금액
    whol_loan_rmnd_rate: Optional[str] = None  # 전체 융자 잔고 비율
    whol_stln_rmnd_stcn: Optional[str] = None  # 전체 대주 잔고 주수
    whol_stln_rmnd_amt: Optional[str] = None  # 전체 대주 잔고 금액
    whol_stln_rmnd_rate: Optional[str] = None  # 전체 대주 잔고 비율
    nday_vrss_loan_rmnd_inrt: Optional[str] = None  # N일 대비 융자 잔고 증가율
    nday_vrss_stln_rmnd_inrt: Optional[str] = None  # N일 대비 대주 잔고 증가율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CreditByCompany(SQLModel, table=True):
    """Output table for credit_by_company"""
    __tablename__ = "kis_credit_by_company"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    crdt_rate: Optional[str] = None  # 신용 비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DailyCreditBalance(SQLModel, table=True):
    """Output table for daily_credit_balance"""
    __tablename__ = "kis_daily_credit_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    deal_date: Optional[str] = None  # 매매 일자
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    stlm_date: Optional[str] = None  # 결제 일자
    whol_loan_new_stcn: Optional[str] = None  # 전체 융자 신규 주수
    whol_loan_rdmp_stcn: Optional[str] = None  # 전체 융자 상환 주수
    whol_loan_rmnd_stcn: Optional[str] = None  # 전체 융자 잔고 주수
    whol_loan_new_amt: Optional[str] = None  # 전체 융자 신규 금액
    whol_loan_rdmp_amt: Optional[str] = None  # 전체 융자 상환 금액
    whol_loan_rmnd_amt: Optional[str] = None  # 전체 융자 잔고 금액
    whol_loan_rmnd_rate: Optional[str] = None  # 전체 융자 잔고 비율
    whol_loan_gvrt: Optional[str] = None  # 전체 융자 공여율
    whol_stln_new_stcn: Optional[str] = None  # 전체 대주 신규 주수
    whol_stln_rdmp_stcn: Optional[str] = None  # 전체 대주 상환 주수
    whol_stln_rmnd_stcn: Optional[str] = None  # 전체 대주 잔고 주수
    whol_stln_new_amt: Optional[str] = None  # 전체 대주 신규 금액
    whol_stln_rdmp_amt: Optional[str] = None  # 전체 대주 상환 금액
    whol_stln_rmnd_amt: Optional[str] = None  # 전체 대주 잔고 금액
    whol_stln_rmnd_rate: Optional[str] = None  # 전체 대주 잔고 비율
    whol_stln_gvrt: Optional[str] = None  # 전체 대주 공여율
    stck_oprc: Optional[str] = None  # 주식 시가2
    stck_hgpr: Optional[str] = None  # 주식 최고가
    stck_lwpr: Optional[str] = None  # 주식 최저가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DailyLoanTrans(SQLModel, table=True):
    """Output table for daily_loan_trans"""
    __tablename__ = "kis_daily_loan_trans"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bsop_date: Optional[str] = None  # 일자
    stck_prpr: Optional[str] = None  # 주식 종가
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    new_stcn: Optional[str] = None  # 당일 증가 주수 (체결)
    rdmp_stcn: Optional[str] = None  # 당일 감소 주수 (상환)
    prdy_rmnd_vrss: Optional[str] = None  # 대차거래 증감
    rmnd_stcn: Optional[str] = None  # 당일 잔고 주수
    rmnd_amt: Optional[str] = None  # 당일 잔고 금액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DailyShortSale(SQLModel, table=True):
    """Output table for daily_short_sale"""
    __tablename__ = "kis_daily_short_sale"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    prdy_vol: Optional[str] = None  # 전일 거래량
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_clpr: Optional[str] = None  # 주식 종가
    stnd_vol_smtn: Optional[str] = None  # 기준 거래량 합계
    ssts_cntg_qty: Optional[str] = None  # 공매도 체결 수량
    ssts_vol_rlim: Optional[str] = None  # 공매도 거래량 비중
    acml_ssts_cntg_qty: Optional[str] = None  # 누적 공매도 체결 수량
    acml_ssts_cntg_qty_rlim: Optional[str] = None  # 누적 공매도 체결 수량 비중
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    stnd_tr_pbmn_smtn: Optional[str] = None  # 기준 거래대금 합계
    ssts_tr_pbmn: Optional[str] = None  # 공매도 거래 대금
    ssts_tr_pbmn_rlim: Optional[str] = None  # 공매도 거래대금 비중
    acml_ssts_tr_pbmn: Optional[str] = None  # 누적 공매도 거래 대금
    acml_ssts_tr_pbmn_rlim: Optional[str] = None  # 누적 공매도 거래 대금 비중
    stck_oprc: Optional[str] = None  # 주식 시가2
    stck_hgpr: Optional[str] = None  # 주식 최고가
    stck_lwpr: Optional[str] = None  # 주식 최저가
    avrg_prc: Optional[str] = None  # 평균가격
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Disparity(SQLModel, table=True):
    """Output table for disparity"""
    __tablename__ = "kis_disparity"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    data_rank: Optional[str] = None  # 데이터 순위
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    acml_vol: Optional[str] = None  # 누적 거래량
    d5_dsrt: Optional[str] = None  # 5일 이격도
    d10_dsrt: Optional[str] = None  # 10일 이격도
    d20_dsrt: Optional[str] = None  # 20일 이격도
    d60_dsrt: Optional[str] = None  # 60일 이격도
    d120_dsrt: Optional[str] = None  # 120일 이격도
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DividendRate(SQLModel, table=True):
    """Output table for dividend_rate"""
    __tablename__ = "kis_dividend_rate"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    rank: Optional[str] = None  # 순위
    sht_cd: Optional[str] = None  # 종목코드
    record_date: Optional[str] = None  # 기준일
    per_sto_divi_amt: Optional[str] = None  # 현금/주식배당금
    divi_rate: Optional[str] = None  # 현금/주식배당률(%)
    divi_kind: Optional[str] = None  # 배당종류
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class EstimatePerform(SQLModel, table=True):
    """Output table for estimate_perform"""
    __tablename__ = "kis_estimate_perform"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    sht_cd: Optional[str] = None  # ELW단축종목코드
    item_kor_nm: Optional[str] = None  # HTS한글종목명
    estdate: Optional[str] = None  # 전일대비부호
    capital: Optional[str] = None  # 누적거래량
    forn_item_lmtrt: Optional[str] = None  # 행사가
    data1: Optional[str] = None  # DATA1
    data2: Optional[str] = None  # DATA2
    data3: Optional[str] = None  # DATA3
    data4: Optional[str] = None  # DATA4
    data5: Optional[str] = None  # DATA5
    output3: Optional[str] = None  # 응답상세
    output4: Optional[str] = None  # 응답상세
    dt: Optional[str] = None  # 결산년월
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ExpCcnlKrx(SQLModel, table=True):
    """Output table for exp_ccnl_krx"""
    __tablename__ = "kis_exp_ccnl_krx"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비구분
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 등락율
    wghn_avrg_stck_prc: Optional[str] = None  # 가중평균주식가격
    stck_oprc: Optional[str] = None  # 시가
    stck_hgpr: Optional[str] = None  # 고가
    stck_lwpr: Optional[str] = None  # 저가
    askp1: Optional[str] = None  # 매도호가
    bidp1: Optional[str] = None  # 매수호가
    cntg_vol: Optional[str] = None  # 거래량
    acml_vol: Optional[str] = None  # 누적거래량
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    seln_cntg_csnu: Optional[str] = None  # 매도체결건수
    shnu_cntg_csnu: Optional[str] = None  # 매수체결건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수체결건수
    cttr: Optional[str] = None  # 체결강도
    seln_cntg_smtn: Optional[str] = None  # 총매도수량
    shnu_cntg_smtn: Optional[str] = None  # 총매수수량
    cntg_cls_code: Optional[str] = None  # 체결구분
    shnu_rate: Optional[str] = None  # 매수비율
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일거래량대비등락율
    oprc_hour: Optional[str] = None  # 시가시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가대비구분
    oprc_vrss_prpr: Optional[str] = None  # 시가대비
    hgpr_hour: Optional[str] = None  # 최고가시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 고가대비구분
    hgpr_vrss_prpr: Optional[str] = None  # 고가대비
    lwpr_hour: Optional[str] = None  # 최저가시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 저가대비구분
    lwpr_vrss_prpr: Optional[str] = None  # 저가대비
    bsop_date: Optional[str] = None  # 영업일자
    new_mkop_cls_code: Optional[str] = None  # 신장운영구분코드
    trht_yn: Optional[str] = None  # 거래정지여부
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    vol_tnrt: Optional[str] = None  # 거래량회전율
    prdy_smns_hour_acml_vol: Optional[str] = None  # 전일동시간누적거래량
    prdy_smns_hour_acml_vol_rate: Optional[str] = None  # 전일동시간누적거래량비율
    hour_cls_code: Optional[str] = None  # 시간구분코드
    mrkt_trtm_cls_code: Optional[str] = None  # 임의종료구분코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ExpCcnlNxt(SQLModel, table=True):
    """Output table for exp_ccnl_nxt"""
    __tablename__ = "kis_exp_ccnl_nxt"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권단축종목코드
    STCK_CNTG_HOUR: Optional[str] = None  # 주식체결시간
    STCK_PRPR: Optional[str] = None  # 주식현재가
    PRDY_VRSS_SIGN: Optional[str] = None  # 전일대비구분
    PRDY_VRSS: Optional[str] = None  # 전일대비
    PRDY_CTRT: Optional[str] = None  # 등락율
    WGHN_AVRG_STCK_PRC: Optional[str] = None  # 가중평균주식가격
    STCK_OPRC: Optional[str] = None  # 시가
    STCK_HGPR: Optional[str] = None  # 고가
    STCK_LWPR: Optional[str] = None  # 저가
    ASKP1: Optional[str] = None  # 매도호가
    BIDP1: Optional[str] = None  # 매수호가
    CNTG_VOL: Optional[str] = None  # 거래량
    ACML_VOL: Optional[str] = None  # 누적거래량
    ACML_TR_PBMN: Optional[str] = None  # 누적거래대금
    SELN_CNTG_CSNU: Optional[str] = None  # 매도체결건수
    SHNU_CNTG_CSNU: Optional[str] = None  # 매수체결건수
    NTBY_CNTG_CSNU: Optional[str] = None  # 순매수체결건수
    CTTR: Optional[str] = None  # 체결강도
    SELN_CNTG_SMTN: Optional[str] = None  # 총매도수량
    SHNU_CNTG_SMTN: Optional[str] = None  # 총매수수량
    CNTG_CLS_CODE: Optional[str] = None  # 체결구분
    SHNU_RATE: Optional[str] = None  # 매수비율
    PRDY_VOL_VRSS_ACML_VOL_RATE: Optional[str] = None  # 전일거래량대비등락율
    OPRC_HOUR: Optional[str] = None  # 시가시간
    OPRC_VRSS_PRPR_SIGN: Optional[str] = None  # 시가대비구분
    OPRC_VRSS_PRPR: Optional[str] = None  # 시가대비
    HGPR_HOUR: Optional[str] = None  # 최고가시간
    HGPR_VRSS_PRPR_SIGN: Optional[str] = None  # 고가대비구분
    HGPR_VRSS_PRPR: Optional[str] = None  # 고가대비
    LWPR_HOUR: Optional[str] = None  # 최저가시간
    LWPR_VRSS_PRPR_SIGN: Optional[str] = None  # 저가대비구분
    LWPR_VRSS_PRPR: Optional[str] = None  # 저가대비
    BSOP_DATE: Optional[str] = None  # 영업일자
    NEW_MKOP_CLS_CODE: Optional[str] = None  # 신장운영구분코드
    TRHT_YN: Optional[str] = None  # 거래정지여부
    ASKP_RSQN1: Optional[str] = None  # 매도호가잔량1
    BIDP_RSQN1: Optional[str] = None  # 매수호가잔량1
    TOTAL_ASKP_RSQN: Optional[str] = None  # 총매도호가잔량
    TOTAL_BIDP_RSQN: Optional[str] = None  # 총매수호가잔량
    VOL_TNRT: Optional[str] = None  # 거래량회전율
    PRDY_SMNS_HOUR_ACML_VOL: Optional[str] = None  # 전일동시간누적거래량
    PRDY_SMNS_HOUR_ACML_VOL_RATE: Optional[str] = None  # 전일동시간누적거래량비율
    HOUR_CLS_CODE: Optional[str] = None  # 시간구분코드
    MRKT_TRTM_CLS_CODE: Optional[str] = None  # 임의종료구분코드
    VI_STND_PRC: Optional[str] = None  # VI 상태값
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ExpCcnlTotal(SQLModel, table=True):
    """Output table for exp_ccnl_total"""
    __tablename__ = "kis_exp_ccnl_total"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권단축종목코드
    STCK_CNTG_HOUR: Optional[str] = None  # 주식체결시간
    STCK_PRPR: Optional[str] = None  # 주식현재가
    PRDY_VRSS_SIGN: Optional[str] = None  # 전일대비구분
    PRDY_VRSS: Optional[str] = None  # 전일대비
    PRDY_CTRT: Optional[str] = None  # 등락율
    WGHN_AVRG_STCK_PRC: Optional[str] = None  # 가중평균주식가격
    STCK_OPRC: Optional[str] = None  # 시가
    STCK_HGPR: Optional[str] = None  # 고가
    STCK_LWPR: Optional[str] = None  # 저가
    ASKP1: Optional[str] = None  # 매도호가
    BIDP1: Optional[str] = None  # 매수호가
    CNTG_VOL: Optional[str] = None  # 거래량
    ACML_VOL: Optional[str] = None  # 누적거래량
    ACML_TR_PBMN: Optional[str] = None  # 누적거래대금
    SELN_CNTG_CSNU: Optional[str] = None  # 매도체결건수
    SHNU_CNTG_CSNU: Optional[str] = None  # 매수체결건수
    NTBY_CNTG_CSNU: Optional[str] = None  # 순매수체결건수
    CTTR: Optional[str] = None  # 체결강도
    SELN_CNTG_SMTN: Optional[str] = None  # 총매도수량
    SHNU_CNTG_SMTN: Optional[str] = None  # 총매수수량
    CNTG_CLS_CODE: Optional[str] = None  # 체결구분
    SHNU_RATE: Optional[str] = None  # 매수비율
    PRDY_VOL_VRSS_ACML_VOL_RATE: Optional[str] = None  # 전일거래량대비등락율
    OPRC_HOUR: Optional[str] = None  # 시가시간
    OPRC_VRSS_PRPR_SIGN: Optional[str] = None  # 시가대비구분
    OPRC_VRSS_PRPR: Optional[str] = None  # 시가대비
    HGPR_HOUR: Optional[str] = None  # 최고가시간
    HGPR_VRSS_PRPR_SIGN: Optional[str] = None  # 고가대비구분
    HGPR_VRSS_PRPR: Optional[str] = None  # 고가대비
    LWPR_HOUR: Optional[str] = None  # 최저가시간
    LWPR_VRSS_PRPR_SIGN: Optional[str] = None  # 저가대비구분
    LWPR_VRSS_PRPR: Optional[str] = None  # 저가대비
    BSOP_DATE: Optional[str] = None  # 영업일자
    NEW_MKOP_CLS_CODE: Optional[str] = None  # 신장운영구분코드
    TRHT_YN: Optional[str] = None  # 거래정지여부
    ASKP_RSQN1: Optional[str] = None  # 매도호가잔량1
    BIDP_RSQN1: Optional[str] = None  # 매수호가잔량1
    TOTAL_ASKP_RSQN: Optional[str] = None  # 총매도호가잔량
    TOTAL_BIDP_RSQN: Optional[str] = None  # 총매수호가잔량
    VOL_TNRT: Optional[str] = None  # 거래량회전율
    PRDY_SMNS_HOUR_ACML_VOL: Optional[str] = None  # 전일동시간누적거래량
    PRDY_SMNS_HOUR_ACML_VOL_RATE: Optional[str] = None  # 전일동시간누적거래량비율
    HOUR_CLS_CODE: Optional[str] = None  # 시간구분코드
    MRKT_TRTM_CLS_CODE: Optional[str] = None  # 임의종료구분코드
    VI_STND_PRC: Optional[str] = None  # VI 상태값
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ExpClosingPrice(SQLModel, table=True):
    """Output table for exp_closing_price"""
    __tablename__ = "kis_exp_closing_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    sdpr_vrss_prpr: Optional[str] = None  # 기준가 대비 현재가
    sdpr_vrss_prpr_rate: Optional[str] = None  # 기준가 대비 현재가 비율
    cntg_vol: Optional[str] = None  # 체결 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ExpIndexTrend(SQLModel, table=True):
    """Output table for exp_index_trend"""
    __tablename__ = "kis_exp_index_trend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_cntg_hour: Optional[str] = None  # 주식 단축 종목코드
    bstp_nmix_prpr: Optional[str] = None  # HTS 한글 종목명
    prdy_vrss_sign: Optional[str] = None  # 주식 현재가
    bstp_nmix_prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비 부호
    acml_vol: Optional[str] = None  # 전일 대비율
    acml_tr_pbmn: Optional[str] = None  # 기준가 대비 현재가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ExpTotalIndex(SQLModel, table=True):
    """Output table for exp_total_index"""
    __tablename__ = "kis_exp_total_index"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bstp_nmix_prpr: Optional[str] = None  # 업종 지수 현재가
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종 지수 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    ascn_issu_cnt: Optional[str] = None  # 상승 종목 수
    down_issu_cnt: Optional[str] = None  # 하락 종목 수
    stnr_issu_cnt: Optional[str] = None  # 보합 종목 수
    bstp_cls_code: Optional[str] = None  # 업종 구분 코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    bstp_nmix_prdy_ctrt: Optional[str] = None  # 업종 지수 전일 대비율
    nmix_sdpr: Optional[str] = None  # 지수 기준가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ExpTransUpdown(SQLModel, table=True):
    """Output table for exp_trans_updown"""
    __tablename__ = "kis_exp_trans_updown"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    stck_sdpr: Optional[str] = None  # 주식 기준가
    seln_rsqn: Optional[str] = None  # 매도 잔량
    askp: Optional[str] = None  # 매도호가
    bidp: Optional[str] = None  # 매수호가
    shnu_rsqn: Optional[str] = None  # 매수2 잔량
    cntg_vol: Optional[str] = None  # 체결 거래량
    antc_tr_pbmn: Optional[str] = None  # 체결 거래대금
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FinanceBalanceSheet(SQLModel, table=True):
    """Output table for finance_balance_sheet"""
    __tablename__ = "kis_finance_balance_sheet"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stac_yymm: Optional[str] = None  # 결산 년월
    cras: Optional[str] = None  # 유동자산
    fxas: Optional[str] = None  # 고정자산
    total_aset: Optional[str] = None  # 자산총계
    flow_lblt: Optional[str] = None  # 유동부채
    fix_lblt: Optional[str] = None  # 고정부채
    total_lblt: Optional[str] = None  # 부채총계
    cpfn: Optional[str] = None  # 자본금
    cfp_surp: Optional[str] = None  # 자본 잉여금
    prfi_surp: Optional[str] = None  # 이익 잉여금
    total_cptl: Optional[str] = None  # 자본총계
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FinanceFinancialRatio(SQLModel, table=True):
    """Output table for finance_financial_ratio"""
    __tablename__ = "kis_finance_financial_ratio"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stac_yymm: Optional[str] = None  # 결산 년월
    grs: Optional[str] = None  # 매출액 증가율
    bsop_prfi_inrt: Optional[str] = None  # 영업 이익 증가율
    ntin_inrt: Optional[str] = None  # 순이익 증가율
    roe_val: Optional[str] = None  # ROE 값
    eps: Optional[str] = None  # EPS
    sps: Optional[str] = None  # 주당매출액
    bps: Optional[str] = None  # BPS
    rsrv_rate: Optional[str] = None  # 유보 비율
    lblt_rate: Optional[str] = None  # 부채 비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FinanceGrowthRatio(SQLModel, table=True):
    """Output table for finance_growth_ratio"""
    __tablename__ = "kis_finance_growth_ratio"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stac_yymm: Optional[str] = None  # 결산 년월
    grs: Optional[str] = None  # 매출액 증가율
    bsop_prfi_inrt: Optional[str] = None  # 영업 이익 증가율
    equt_inrt: Optional[str] = None  # 자기자본 증가율
    totl_aset_inrt: Optional[str] = None  # 총자산 증가율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FinanceIncomeStatement(SQLModel, table=True):
    """Output table for finance_income_statement"""
    __tablename__ = "kis_finance_income_statement"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stac_yymm: Optional[str] = None  # 결산 년월
    sale_account: Optional[str] = None  # 매출액
    sale_cost: Optional[str] = None  # 매출 원가
    sale_totl_prfi: Optional[str] = None  # 매출 총 이익
    depr_cost: Optional[str] = None  # 감가상각비
    sell_mang: Optional[str] = None  # 판매 및 관리비
    bsop_prti: Optional[str] = None  # 영업 이익
    bsop_non_ernn: Optional[str] = None  # 영업 외 수익
    bsop_non_expn: Optional[str] = None  # 영업 외 비용
    op_prfi: Optional[str] = None  # 경상 이익
    spec_prfi: Optional[str] = None  # 특별 이익
    spec_loss: Optional[str] = None  # 특별 손실
    thtr_ntin: Optional[str] = None  # 당기순이익
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FinanceOtherMajorRatios(SQLModel, table=True):
    """Output table for finance_other_major_ratios"""
    __tablename__ = "kis_finance_other_major_ratios"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stac_yymm: Optional[str] = None  # 결산 년월
    payout_rate: Optional[str] = None  # 배당 성향
    eva: Optional[str] = None  # EVA
    ebitda: Optional[str] = None  # EBITDA
    ev_ebitda: Optional[str] = None  # EV_EBITDA
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FinanceProfitRatio(SQLModel, table=True):
    """Output table for finance_profit_ratio"""
    __tablename__ = "kis_finance_profit_ratio"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stac_yymm: Optional[str] = None  # 결산 년월
    cptl_ntin_rate: Optional[str] = None  # 총자본 순이익율
    self_cptl_ntin_inrt: Optional[str] = None  # 자기자본 순이익율
    sale_ntin_rate: Optional[str] = None  # 매출액 순이익율
    sale_totl_rate: Optional[str] = None  # 매출액 총이익율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FinanceRatio(SQLModel, table=True):
    """Output table for finance_ratio"""
    __tablename__ = "kis_finance_ratio"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    data_rank: Optional[str] = None  # 데이터 순위
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    cptl_op_prfi: Optional[str] = None  # 총자본경상이익율
    cptl_ntin_rate: Optional[str] = None  # 총자본 순이익율
    sale_totl_rate: Optional[str] = None  # 매출액 총이익율
    sale_ntin_rate: Optional[str] = None  # 매출액 순이익율
    bis: Optional[str] = None  # 자기자본비율
    lblt_rate: Optional[str] = None  # 부채 비율
    bram_depn: Optional[str] = None  # 차입금 의존도
    rsrv_rate: Optional[str] = None  # 유보 비율
    grs: Optional[str] = None  # 매출액 증가율
    op_prfi_inrt: Optional[str] = None  # 경상 이익 증가율
    bsop_prfi_inrt: Optional[str] = None  # 영업 이익 증가율
    ntin_inrt: Optional[str] = None  # 순이익 증가율
    equt_inrt: Optional[str] = None  # 자기자본 증가율
    cptl_tnrt: Optional[str] = None  # 총자본회전율
    sale_bond_tnrt: Optional[str] = None  # 매출 채권 회전율
    totl_aset_inrt: Optional[str] = None  # 총자산 증가율
    stac_month: Optional[str] = None  # 결산 월
    stac_month_cls_code: Optional[str] = None  # 결산 월 구분 코드
    iqry_csnu: Optional[str] = None  # 조회 건수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FinanceStabilityRatio(SQLModel, table=True):
    """Output table for finance_stability_ratio"""
    __tablename__ = "kis_finance_stability_ratio"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stac_yymm: Optional[str] = None  # 결산 년월
    lblt_rate: Optional[str] = None  # 부채 비율
    bram_depn: Optional[str] = None  # 차입금 의존도
    crnt_rate: Optional[str] = None  # 유동 비율
    quck_rate: Optional[str] = None  # 당좌 비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Fluctuation(SQLModel, table=True):
    """Output table for fluctuation"""
    __tablename__ = "kis_fluctuation"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    data_rank: Optional[str] = None  # 데이터 순위
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    stck_hgpr: Optional[str] = None  # 주식 최고가
    hgpr_hour: Optional[str] = None  # 최고가 시간
    acml_hgpr_date: Optional[str] = None  # 누적 최고가 일자
    stck_lwpr: Optional[str] = None  # 주식 최저가
    lwpr_hour: Optional[str] = None  # 최저가 시간
    acml_lwpr_date: Optional[str] = None  # 누적 최저가 일자
    lwpr_vrss_prpr_rate: Optional[str] = None  # 저가 대비 현재가 비율
    dsgt_date_clpr_vrss_prpr_rate: Optional[str] = None  # 영업 일수 대비 현재가 비율
    cnnt_ascn_dynu: Optional[str] = None  # 연속 상승 일수
    hgpr_vrss_prpr_rate: Optional[str] = None  # 고가 대비 현재가 비율
    cnnt_down_dynu: Optional[str] = None  # 연속 하락 일수
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가 대비 부호
    oprc_vrss_prpr: Optional[str] = None  # 시가 대비
    oprc_vrss_prpr_rate: Optional[str] = None  # 시가 대비 현재가 비율
    prd_rsfl: Optional[str] = None  # 기간 등락
    prd_rsfl_rate: Optional[str] = None  # 기간 등락 비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ForeignInstitutionTotal(SQLModel, table=True):
    """Output table for foreign_institution_total"""
    __tablename__ = "kis_foreign_institution_total"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    ntby_qty: Optional[str] = None  # 순매수 수량
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    frgn_ntby_qty: Optional[str] = None  # 외국인 순매수 수량
    orgn_ntby_qty: Optional[str] = None  # 기관계 순매수 수량
    ivtr_ntby_qty: Optional[str] = None  # 투자신탁 순매수 수량
    bank_ntby_qty: Optional[str] = None  # 은행 순매수 수량
    insu_ntby_qty: Optional[str] = None  # 보험 순매수 수량
    mrbn_ntby_qty: Optional[str] = None  # 종금 순매수 수량
    fund_ntby_qty: Optional[str] = None  # 기금 순매수 수량
    etc_orgt_ntby_vol: Optional[str] = None  # 기타 단체 순매수 거래량
    etc_corp_ntby_vol: Optional[str] = None  # 기타 법인 순매수 거래량
    frgn_ntby_tr_pbmn: Optional[str] = None  # 외국인 순매수 거래 대금
    orgn_ntby_tr_pbmn: Optional[str] = None  # 기관계 순매수 거래 대금
    ivtr_ntby_tr_pbmn: Optional[str] = None  # 투자신탁 순매수 거래 대금
    bank_ntby_tr_pbmn: Optional[str] = None  # 은행 순매수 거래 대금
    insu_ntby_tr_pbmn: Optional[str] = None  # 보험 순매수 거래 대금
    mrbn_ntby_tr_pbmn: Optional[str] = None  # 종금 순매수 거래 대금
    fund_ntby_tr_pbmn: Optional[str] = None  # 기금 순매수 거래 대금
    etc_orgt_ntby_tr_pbmn: Optional[str] = None  # 기타 단체 순매수 거래 대금
    etc_corp_ntby_tr_pbmn: Optional[str] = None  # 기타 법인 순매수 거래 대금
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FrgnmemPchsTrend(SQLModel, table=True):
    """Output table for frgnmem_pchs_trend"""
    __tablename__ = "kis_frgnmem_pchs_trend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bsop_hour: Optional[str] = None  # 영업시간
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    frgn_seln_vol: Optional[str] = None  # 외국인매도거래량
    frgn_shnu_vol: Optional[str] = None  # 외국인매수2거래량
    glob_ntby_qty: Optional[str] = None  # 외국계순매수수량
    frgn_ntby_qty_icdc: Optional[str] = None  # 외국인순매수수량증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FrgnmemTradeEstimate(SQLModel, table=True):
    """Output table for frgnmem_trade_estimate"""
    __tablename__ = "kis_frgnmem_trade_estimate"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_shrn_iscd: Optional[str] = None  # 주식단축종목코드
    hts_kor_isnm: Optional[str] = None  # HTS한글종목명
    glob_ntsl_qty: Optional[str] = None  # 외국계순매도수량
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    glob_total_seln_qty: Optional[str] = None  # 외국계총매도수량
    glob_total_shnu_qty: Optional[str] = None  # 외국계총매수2수량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FrgnmemTradeTrend(SQLModel, table=True):
    """Output table for frgnmem_trade_trend"""
    __tablename__ = "kis_frgnmem_trade_trend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    total_seln_qty: Optional[str] = None  # 총매도수량
    total_shnu_qty: Optional[str] = None  # 총매수2수량
    bsop_hour: Optional[str] = None  # 영업시간
    hts_kor_isnm: Optional[str] = None  # HTS한글종목명
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    cntg_vol: Optional[str] = None  # 체결거래량
    acml_ntby_qty: Optional[str] = None  # 누적순매수수량
    glob_ntby_qty: Optional[str] = None  # 외국계순매수수량
    frgn_ntby_qty_icdc: Optional[str] = None  # 외국인순매수수량증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class HtsTopView(SQLModel, table=True):
    """Output table for hts_top_view"""
    __tablename__ = "kis_hts_top_view"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    output1: Optional[str] = None  # 응답상세
    mrkt_div_cls_code: Optional[str] = None  # 시장구분
    mksc_shrn_iscd: Optional[str] = None  # 종목코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndexCcnl(SQLModel, table=True):
    """Output table for index_ccnl"""
    __tablename__ = "kis_index_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bstp_cls_code: Optional[str] = None  # 업종 구분 코드
    bsop_hour: Optional[str] = None  # 영업 시간
    prpr_nmix: Optional[str] = None  # 현재가 지수
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종 지수 전일 대비
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    pcas_vol: Optional[str] = None  # 건별 거래량
    pcas_tr_pbmn: Optional[str] = None  # 건별 거래 대금
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    oprc_nmix: Optional[str] = None  # 시가 지수
    nmix_hgpr: Optional[str] = None  # 지수 최고가
    nmix_lwpr: Optional[str] = None  # 지수 최저가
    oprc_vrss_nmix_prpr: Optional[str] = None  # 시가 대비 지수 현재가
    oprc_vrss_nmix_sign: Optional[str] = None  # 시가 대비 지수 부호
    hgpr_vrss_nmix_prpr: Optional[str] = None  # 최고가 대비 지수 현재가
    hgpr_vrss_nmix_sign: Optional[str] = None  # 최고가 대비 지수 부호
    lwpr_vrss_nmix_prpr: Optional[str] = None  # 최저가 대비 지수 현재가
    lwpr_vrss_nmix_sign: Optional[str] = None  # 최저가 대비 지수 부호
    prdy_clpr_vrss_oprc_rate: Optional[str] = None  # 전일 종가 대비 시가2 비율
    prdy_clpr_vrss_hgpr_rate: Optional[str] = None  # 전일 종가 대비 최고가 비율
    prdy_clpr_vrss_lwpr_rate: Optional[str] = None  # 전일 종가 대비 최저가 비율
    uplm_issu_cnt: Optional[str] = None  # 상한 종목 수
    ascn_issu_cnt: Optional[str] = None  # 상승 종목 수
    stnr_issu_cnt: Optional[str] = None  # 보합 종목 수
    down_issu_cnt: Optional[str] = None  # 하락 종목 수
    lslm_issu_cnt: Optional[str] = None  # 하한 종목 수
    qtqt_ascn_issu_cnt: Optional[str] = None  # 기세 상승 종목수
    qtqt_down_issu_cnt: Optional[str] = None  # 기세 하락 종목수
    tick_vrss: Optional[str] = None  # TICK대비
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndexExpCcnl(SQLModel, table=True):
    """Output table for index_exp_ccnl"""
    __tablename__ = "kis_index_exp_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bstp_cls_code: Optional[str] = None  # 업종 구분 코드
    bsop_hour: Optional[str] = None  # 영업 시간
    prpr_nmix: Optional[str] = None  # 현재가 지수
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종 지수 전일 대비
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    pcas_vol: Optional[str] = None  # 건별 거래량
    pcas_tr_pbmn: Optional[str] = None  # 건별 거래 대금
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    oprc_nmix: Optional[str] = None  # 시가 지수
    nmix_hgpr: Optional[str] = None  # 지수 최고가
    nmix_lwpr: Optional[str] = None  # 지수 최저가
    oprc_vrss_nmix_prpr: Optional[str] = None  # 시가 대비 지수 현재가
    oprc_vrss_nmix_sign: Optional[str] = None  # 시가 대비 지수 부호
    hgpr_vrss_nmix_prpr: Optional[str] = None  # 최고가 대비 지수 현재가
    hgpr_vrss_nmix_sign: Optional[str] = None  # 최고가 대비 지수 부호
    lwpr_vrss_nmix_prpr: Optional[str] = None  # 최저가 대비 지수 현재가
    lwpr_vrss_nmix_sign: Optional[str] = None  # 최저가 대비 지수 부호
    prdy_clpr_vrss_oprc_rate: Optional[str] = None  # 전일 종가 대비 시가2 비율
    prdy_clpr_vrss_hgpr_rate: Optional[str] = None  # 전일 종가 대비 최고가 비율
    prdy_clpr_vrss_lwpr_rate: Optional[str] = None  # 전일 종가 대비 최저가 비율
    uplm_issu_cnt: Optional[str] = None  # 상한 종목 수
    ascn_issu_cnt: Optional[str] = None  # 상승 종목 수
    stnr_issu_cnt: Optional[str] = None  # 보합 종목 수
    down_issu_cnt: Optional[str] = None  # 하락 종목 수
    lslm_issu_cnt: Optional[str] = None  # 하한 종목 수
    qtqt_ascn_issu_cnt: Optional[str] = None  # 기세 상승 종목수
    qtqt_down_issu_cnt: Optional[str] = None  # 기세 하락 종목수
    tick_vrss: Optional[str] = None  # TICK대비
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndexProgramTrade(SQLModel, table=True):
    """Output table for index_program_trade"""
    __tablename__ = "kis_index_program_trade"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bstp_cls_code: Optional[str] = None  # 업종 구분 코드
    bsop_hour: Optional[str] = None  # 영업 시간
    arbt_seln_entm_cnqn: Optional[str] = None  # 차익 매도 위탁 체결량
    arbt_seln_onsl_cnqn: Optional[str] = None  # 차익 매도 자기 체결량
    arbt_shnu_entm_cnqn: Optional[str] = None  # 차익 매수2 위탁 체결량
    arbt_shnu_onsl_cnqn: Optional[str] = None  # 차익 매수2 자기 체결량
    nabt_seln_entm_cnqn: Optional[str] = None  # 비차익 매도 위탁 체결량
    nabt_seln_onsl_cnqn: Optional[str] = None  # 비차익 매도 자기 체결량
    nabt_shnu_entm_cnqn: Optional[str] = None  # 비차익 매수2 위탁 체결량
    nabt_shnu_onsl_cnqn: Optional[str] = None  # 비차익 매수2 자기 체결량
    arbt_seln_entm_cntg_amt: Optional[str] = None  # 차익 매도 위탁 체결 금액
    arbt_seln_onsl_cntg_amt: Optional[str] = None  # 차익 매도 자기 체결 금액
    arbt_shnu_entm_cntg_amt: Optional[str] = None  # 차익 매수2 위탁 체결 금액
    arbt_shnu_onsl_cntg_amt: Optional[str] = None  # 차익 매수2 자기 체결 금액
    nabt_seln_entm_cntg_amt: Optional[str] = None  # 비차익 매도 위탁 체결 금액
    nabt_seln_onsl_cntg_amt: Optional[str] = None  # 비차익 매도 자기 체결 금액
    nabt_shnu_entm_cntg_amt: Optional[str] = None  # 비차익 매수2 위탁 체결 금액
    nabt_shnu_onsl_cntg_amt: Optional[str] = None  # 비차익 매수2 자기 체결 금액
    arbt_smtn_seln_vol: Optional[str] = None  # 차익 합계 매도 거래량
    arbt_smtm_seln_vol_rate: Optional[str] = None  # 차익 합계 매도 거래량 비율
    arbt_smtn_seln_tr_pbmn: Optional[str] = None  # 차익 합계 매도 거래 대금
    arbt_smtm_seln_tr_pbmn_rate: Optional[str] = None  # 차익 합계 매도 거래대금 비율
    arbt_smtn_shnu_vol: Optional[str] = None  # 차익 합계 매수2 거래량
    arbt_smtm_shnu_vol_rate: Optional[str] = None  # 차익 합계 매수 거래량 비율
    arbt_smtn_shnu_tr_pbmn: Optional[str] = None  # 차익 합계 매수2 거래 대금
    arbt_smtm_shnu_tr_pbmn_rate: Optional[str] = None  # 차익 합계 매수 거래대금 비율
    arbt_smtn_ntby_qty: Optional[str] = None  # 차익 합계 순매수 수량
    arbt_smtm_ntby_qty_rate: Optional[str] = None  # 차익 합계 순매수 수량 비율
    arbt_smtn_ntby_tr_pbmn: Optional[str] = None  # 차익 합계 순매수 거래 대금
    arbt_smtm_ntby_tr_pbmn_rate: Optional[str] = None  # 차익 합계 순매수 거래대금 비율
    nabt_smtn_seln_vol: Optional[str] = None  # 비차익 합계 매도 거래량
    nabt_smtm_seln_vol_rate: Optional[str] = None  # 비차익 합계 매도 거래량 비율
    nabt_smtn_seln_tr_pbmn: Optional[str] = None  # 비차익 합계 매도 거래 대금
    nabt_smtm_seln_tr_pbmn_rate: Optional[str] = None  # 비차익 합계 매도 거래대금 비율
    nabt_smtn_shnu_vol: Optional[str] = None  # 비차익 합계 매수2 거래량
    nabt_smtm_shnu_vol_rate: Optional[str] = None  # 비차익 합계 매수 거래량 비율
    nabt_smtn_shnu_tr_pbmn: Optional[str] = None  # 비차익 합계 매수2 거래 대금
    nabt_smtm_shnu_tr_pbmn_rate: Optional[str] = None  # 비차익 합계 매수 거래대금 비율
    nabt_smtn_ntby_qty: Optional[str] = None  # 비차익 합계 순매수 수량
    nabt_smtm_ntby_qty_rate: Optional[str] = None  # 비차익 합계 순매수 수량 비율
    nabt_smtn_ntby_tr_pbmn: Optional[str] = None  # 비차익 합계 순매수 거래 대금
    nabt_smtm_ntby_tr_pbmn_rate: Optional[str] = None  # 비차익 합계 순매수 거래대금 비율
    whol_entm_seln_vol: Optional[str] = None  # 전체 위탁 매도 거래량
    entm_seln_vol_rate: Optional[str] = None  # 위탁 매도 거래량 비율
    whol_entm_seln_tr_pbmn: Optional[str] = None  # 전체 위탁 매도 거래 대금
    entm_seln_tr_pbmn_rate: Optional[str] = None  # 위탁 매도 거래대금 비율
    whol_entm_shnu_vol: Optional[str] = None  # 전체 위탁 매수2 거래량
    entm_shnu_vol_rate: Optional[str] = None  # 위탁 매수 거래량 비율
    whol_entm_shnu_tr_pbmn: Optional[str] = None  # 전체 위탁 매수2 거래 대금
    entm_shnu_tr_pbmn_rate: Optional[str] = None  # 위탁 매수 거래대금 비율
    whol_entm_ntby_qt: Optional[str] = None  # 전체 위탁 순매수 수량
    entm_ntby_qty_rat: Optional[str] = None  # 위탁 순매수 수량 비율
    whol_entm_ntby_tr_pbmn: Optional[str] = None  # 전체 위탁 순매수 거래 대금
    entm_ntby_tr_pbmn_rate: Optional[str] = None  # 위탁 순매수 금액 비율
    whol_onsl_seln_vol: Optional[str] = None  # 전체 자기 매도 거래량
    onsl_seln_vol_rate: Optional[str] = None  # 자기 매도 거래량 비율
    whol_onsl_seln_tr_pbmn: Optional[str] = None  # 전체 자기 매도 거래 대금
    onsl_seln_tr_pbmn_rate: Optional[str] = None  # 자기 매도 거래대금 비율
    whol_onsl_shnu_vol: Optional[str] = None  # 전체 자기 매수2 거래량
    onsl_shnu_vol_rate: Optional[str] = None  # 자기 매수 거래량 비율
    whol_onsl_shnu_tr_pbmn: Optional[str] = None  # 전체 자기 매수2 거래 대금
    onsl_shnu_tr_pbmn_rate: Optional[str] = None  # 자기 매수 거래대금 비율
    whol_onsl_ntby_qty: Optional[str] = None  # 전체 자기 순매수 수량
    onsl_ntby_qty_rate: Optional[str] = None  # 자기 순매수량 비율
    whol_onsl_ntby_tr_pbmn: Optional[str] = None  # 전체 자기 순매수 거래 대금
    onsl_ntby_tr_pbmn_rate: Optional[str] = None  # 자기 순매수 대금 비율
    total_seln_qty: Optional[str] = None  # 총 매도 수량
    whol_seln_vol_rate: Optional[str] = None  # 전체 매도 거래량 비율
    total_seln_tr_pbmn: Optional[str] = None  # 총 매도 거래 대금
    whol_seln_tr_pbmn_rate: Optional[str] = None  # 전체 매도 거래대금 비율
    shnu_cntg_smtn: Optional[str] = None  # 총 매수 수량
    whol_shun_vol_rate: Optional[str] = None  # 전체 매수 거래량 비율
    total_shnu_tr_pbmn: Optional[str] = None  # 총 매수2 거래 대금
    whol_shun_tr_pbmn_rate: Optional[str] = None  # 전체 매수 거래대금 비율
    whol_ntby_qty: Optional[str] = None  # 전체 순매수 수량
    whol_smtm_ntby_qty_rate: Optional[str] = None  # 전체 합계 순매수 수량 비율
    whol_ntby_tr_pbmn: Optional[str] = None  # 전체 순매수 거래 대금
    whol_ntby_tr_pbmn_rate: Optional[str] = None  # 전체 순매수 거래대금 비율
    arbt_entm_ntby_qty: Optional[str] = None  # 차익 위탁 순매수 수량
    arbt_entm_ntby_tr_pbmn: Optional[str] = None  # 차익 위탁 순매수 거래 대금
    arbt_onsl_ntby_qty: Optional[str] = None  # 차익 자기 순매수 수량
    arbt_onsl_ntby_tr_pbmn: Optional[str] = None  # 차익 자기 순매수 거래 대금
    nabt_entm_ntby_qty: Optional[str] = None  # 비차익 위탁 순매수 수량
    nabt_entm_ntby_tr_pbmn: Optional[str] = None  # 비차익 위탁 순매수 거래 대금
    nabt_onsl_ntby_qty: Optional[str] = None  # 비차익 자기 순매수 수량
    nabt_onsl_ntby_tr_pbmn: Optional[str] = None  # 비차익 자기 순매수 거래 대금
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireAccountBalance(SQLModel, table=True):
    """Output table for inquire_account_balance"""
    __tablename__ = "kis_inquire_account_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pchs_amt: Optional[str] = None  # 매입금액
    evlu_amt: Optional[str] = None  # 평가금액
    evlu_pfls_amt: Optional[str] = None  # 평가손익금액
    crdt_lnd_amt: Optional[str] = None  # 신용대출금액
    real_nass_amt: Optional[str] = None  # 실제순자산금액
    whol_weit_rt: Optional[str] = None  # 전체비중율
    pchs_amt_smtl: Optional[str] = None  # 매입금액합계
    nass_tot_amt: Optional[str] = None  # 순자산총금액
    loan_amt_smtl: Optional[str] = None  # 대출금액합계
    evlu_pfls_amt_smtl: Optional[str] = None  # 평가손익금액합계
    evlu_amt_smtl: Optional[str] = None  # 평가금액합계
    tot_asst_amt: Optional[str] = None  # 총자산금액
    tot_lnda_tot_ulst_lnda: Optional[str] = None  # 총대출금액총융자대출금액
    cma_auto_loan_amt: Optional[str] = None  # CMA자동대출금액
    tot_mgln_amt: Optional[str] = None  # 총담보대출금액
    stln_evlu_amt: Optional[str] = None  # 대주평가금액
    crdt_fncg_amt: Optional[str] = None  # 신용융자금액
    ocl_apl_loan_amt: Optional[str] = None  # OCL_APL대출금액
    pldg_stup_amt: Optional[str] = None  # 질권설정금액
    frcr_evlu_tota: Optional[str] = None  # 외화평가총액
    tot_dncl_amt: Optional[str] = None  # 총예수금액
    cma_evlu_amt: Optional[str] = None  # CMA평가금액
    dncl_amt: Optional[str] = None  # 예수금액
    tot_sbst_amt: Optional[str] = None  # 총대용금액
    thdt_rcvb_amt: Optional[str] = None  # 당일미수금액
    ovrs_stck_evlu_amt1: Optional[str] = None  # 해외주식평가금액1
    ovrs_bond_evlu_amt: Optional[str] = None  # 해외채권평가금액
    mmf_cma_mgge_loan_amt: Optional[str] = None  # MMFCMA담보대출금액
    sbsc_dncl_amt: Optional[str] = None  # 청약예수금액
    pbst_sbsc_fnds_loan_use_amt: Optional[str] = None  # 공모주청약자금대출사용금액
    etpr_crdt_grnt_loan_amt: Optional[str] = None  # 기업신용공여대출금액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireAskingPriceExpCcn(SQLModel, table=True):
    """Output table for inquire_asking_price_exp_ccn"""
    __tablename__ = "kis_inquire_asking_price_exp_ccn"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    aspr_acpt_hour: Optional[str] = None  # 호가 접수 시간
    askp1: Optional[str] = None  # 매도호가1
    askp2: Optional[str] = None  # 매도호가2
    askp3: Optional[str] = None  # 매도호가3
    askp4: Optional[str] = None  # 매도호가4
    askp5: Optional[str] = None  # 매도호가5
    askp6: Optional[str] = None  # 매도호가6
    askp7: Optional[str] = None  # 매도호가7
    askp8: Optional[str] = None  # 매도호가8
    askp9: Optional[str] = None  # 매도호가9
    askp10: Optional[str] = None  # 매도호가10
    bidp1: Optional[str] = None  # 매수호가1
    bidp2: Optional[str] = None  # 매수호가2
    bidp3: Optional[str] = None  # 매수호가3
    bidp4: Optional[str] = None  # 매수호가4
    bidp5: Optional[str] = None  # 매수호가5
    bidp6: Optional[str] = None  # 매수호가6
    bidp7: Optional[str] = None  # 매수호가7
    bidp8: Optional[str] = None  # 매수호가8
    bidp9: Optional[str] = None  # 매수호가9
    bidp10: Optional[str] = None  # 매수호가10
    askp_rsqn1: Optional[str] = None  # 매도호가 잔량1
    askp_rsqn2: Optional[str] = None  # 매도호가 잔량2
    askp_rsqn3: Optional[str] = None  # 매도호가 잔량3
    askp_rsqn4: Optional[str] = None  # 매도호가 잔량4
    askp_rsqn5: Optional[str] = None  # 매도호가 잔량5
    askp_rsqn6: Optional[str] = None  # 매도호가 잔량6
    askp_rsqn7: Optional[str] = None  # 매도호가 잔량7
    askp_rsqn8: Optional[str] = None  # 매도호가 잔량8
    askp_rsqn9: Optional[str] = None  # 매도호가 잔량9
    askp_rsqn10: Optional[str] = None  # 매도호가 잔량10
    bidp_rsqn1: Optional[str] = None  # 매수호가 잔량1
    bidp_rsqn2: Optional[str] = None  # 매수호가 잔량2
    bidp_rsqn3: Optional[str] = None  # 매수호가 잔량3
    bidp_rsqn4: Optional[str] = None  # 매수호가 잔량4
    bidp_rsqn5: Optional[str] = None  # 매수호가 잔량5
    bidp_rsqn6: Optional[str] = None  # 매수호가 잔량6
    bidp_rsqn7: Optional[str] = None  # 매수호가 잔량7
    bidp_rsqn8: Optional[str] = None  # 매수호가 잔량8
    bidp_rsqn9: Optional[str] = None  # 매수호가 잔량9
    bidp_rsqn10: Optional[str] = None  # 매수호가 잔량10
    askp_rsqn_icdc1: Optional[str] = None  # 매도호가 잔량 증감1
    askp_rsqn_icdc2: Optional[str] = None  # 매도호가 잔량 증감2
    askp_rsqn_icdc3: Optional[str] = None  # 매도호가 잔량 증감3
    askp_rsqn_icdc4: Optional[str] = None  # 매도호가 잔량 증감4
    askp_rsqn_icdc5: Optional[str] = None  # 매도호가 잔량 증감5
    askp_rsqn_icdc6: Optional[str] = None  # 매도호가 잔량 증감6
    askp_rsqn_icdc7: Optional[str] = None  # 매도호가 잔량 증감7
    askp_rsqn_icdc8: Optional[str] = None  # 매도호가 잔량 증감8
    askp_rsqn_icdc9: Optional[str] = None  # 매도호가 잔량 증감9
    askp_rsqn_icdc10: Optional[str] = None  # 매도호가 잔량 증감10
    bidp_rsqn_icdc1: Optional[str] = None  # 매수호가 잔량 증감1
    bidp_rsqn_icdc2: Optional[str] = None  # 매수호가 잔량 증감2
    bidp_rsqn_icdc3: Optional[str] = None  # 매수호가 잔량 증감3
    bidp_rsqn_icdc4: Optional[str] = None  # 매수호가 잔량 증감4
    bidp_rsqn_icdc5: Optional[str] = None  # 매수호가 잔량 증감5
    bidp_rsqn_icdc6: Optional[str] = None  # 매수호가 잔량 증감6
    bidp_rsqn_icdc7: Optional[str] = None  # 매수호가 잔량 증감7
    bidp_rsqn_icdc8: Optional[str] = None  # 매수호가 잔량 증감8
    bidp_rsqn_icdc9: Optional[str] = None  # 매수호가 잔량 증감9
    bidp_rsqn_icdc10: Optional[str] = None  # 매수호가 잔량 증감10
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    total_askp_rsqn_icdc: Optional[str] = None  # 총 매도호가 잔량 증감
    total_bidp_rsqn_icdc: Optional[str] = None  # 총 매수호가 잔량 증감
    ovtm_total_askp_icdc: Optional[str] = None  # 시간외 총 매도호가 증감
    ovtm_total_bidp_icdc: Optional[str] = None  # 시간외 총 매수호가 증감
    ovtm_total_askp_rsqn: Optional[str] = None  # 시간외 총 매도호가 잔량
    ovtm_total_bidp_rsqn: Optional[str] = None  # 시간외 총 매수호가 잔량
    ntby_aspr_rsqn: Optional[str] = None  # 순매수 호가 잔량
    new_mkop_cls_code: Optional[str] = None  # 신 장운영 구분 코드
    antc_mkop_cls_code: Optional[str] = None  # 예상 장운영 구분 코드
    stck_prpr: Optional[str] = None  # 주식 현재가
    stck_oprc: Optional[str] = None  # 주식 시가2
    stck_hgpr: Optional[str] = None  # 주식 최고가
    stck_lwpr: Optional[str] = None  # 주식 최저가
    stck_sdpr: Optional[str] = None  # 주식 기준가
    antc_cnpr: Optional[str] = None  # 예상 체결가
    antc_cntg_vrss_sign: Optional[str] = None  # 예상 체결 대비 부호
    antc_cntg_vrss: Optional[str] = None  # 예상 체결 대비
    antc_cntg_prdy_ctrt: Optional[str] = None  # 예상 체결 전일 대비율
    antc_vol: Optional[str] = None  # 예상 거래량
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    vi_cls_code: Optional[str] = None  # VI적용구분코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireBalanceRlzPl(SQLModel, table=True):
    """Output table for inquire_balance_rlz_pl"""
    __tablename__ = "kis_inquire_balance_rlz_pl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    trad_dvsn_name: Optional[str] = None  # 매매구분명
    bfdy_buy_qty: Optional[str] = None  # 전일매수수량
    bfdy_sll_qty: Optional[str] = None  # 전일매도수량
    thdt_buyqty: Optional[str] = None  # 금일매수수량
    thdt_sll_qty: Optional[str] = None  # 금일매도수량
    hldg_qty: Optional[str] = None  # 보유수량
    ord_psbl_qty: Optional[str] = None  # 주문가능수량
    pchs_avg_pric: Optional[str] = None  # 매입평균가격
    pchs_amt: Optional[str] = None  # 매입금액
    prpr: Optional[str] = None  # 현재가
    evlu_amt: Optional[str] = None  # 평가금액
    evlu_pfls_amt: Optional[str] = None  # 평가손익금액
    evlu_pfls_rt: Optional[str] = None  # 평가손익율
    evlu_erng_rt: Optional[str] = None  # 평가수익율
    loan_dt: Optional[str] = None  # 대출일자
    loan_amt: Optional[str] = None  # 대출금액
    stln_slng_chgs: Optional[str] = None  # 대주매각대금
    expd_dt: Optional[str] = None  # 만기일자
    stck_loan_unpr: Optional[str] = None  # 주식대출단가
    bfdy_cprs_icdc: Optional[str] = None  # 전일대비증감
    fltt_rt: Optional[str] = None  # 등락율
    dnca_tot_amt: Optional[str] = None  # 예수금총금액
    nxdy_excc_amt: Optional[str] = None  # 익일정산금액
    prvs_rcdl_excc_amt: Optional[str] = None  # 가수도정산금액
    cma_evlu_amt: Optional[str] = None  # CMA평가금액
    bfdy_buy_amt: Optional[str] = None  # 전일매수금액
    thdt_buy_amt: Optional[str] = None  # 금일매수금액
    nxdy_auto_rdpt_amt: Optional[str] = None  # 익일자동상환금액
    bfdy_sll_amt: Optional[str] = None  # 전일매도금액
    thdt_sll_amt: Optional[str] = None  # 금일매도금액
    d2_auto_rdpt_amt: Optional[str] = None  # D+2자동상환금액
    bfdy_tlex_amt: Optional[str] = None  # 전일제비용금액
    thdt_tlex_amt: Optional[str] = None  # 금일제비용금액
    tot_loan_amt: Optional[str] = None  # 총대출금액
    scts_evlu_amt: Optional[str] = None  # 유가평가금액
    tot_evlu_amt: Optional[str] = None  # 총평가금액
    nass_amt: Optional[str] = None  # 순자산금액
    fncg_gld_auto_rdpt_yn: Optional[str] = None  # 융자금자동상환여부
    pchs_amt_smtl_amt: Optional[str] = None  # 매입금액합계금액
    evlu_amt_smtl_amt: Optional[str] = None  # 평가금액합계금액
    evlu_pfls_smtl_amt: Optional[str] = None  # 평가손익합계금액
    tot_stln_slng_chgs: Optional[str] = None  # 총대주매각대금
    bfdy_tot_asst_evlu_amt: Optional[str] = None  # 전일총자산평가금액
    asst_icdc_amt: Optional[str] = None  # 자산증감액
    asst_icdc_erng_rt: Optional[str] = None  # 자산증감수익율
    rlzt_pfls: Optional[str] = None  # 실현손익
    rlzt_erng_rt: Optional[str] = None  # 실현수익율
    real_evlu_pfls: Optional[str] = None  # 실평가손익
    real_evlu_pfls_erng_rt: Optional[str] = None  # 실평가손익수익율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireCreditPsamount(SQLModel, table=True):
    """Output table for inquire_credit_psamount"""
    __tablename__ = "kis_inquire_credit_psamount"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ord_psbl_cash: Optional[str] = None  # 주문가능현금
    ord_psbl_sbst: Optional[str] = None  # 주문가능대용
    ruse_psbl_amt: Optional[str] = None  # 재사용가능금액
    fund_rpch_chgs: Optional[str] = None  # 펀드환매대금
    psbl_qty_calc_unpr: Optional[str] = None  # 가능수량계산단가
    nrcvb_buy_amt: Optional[str] = None  # 미수없는매수금액
    nrcvb_buy_qty: Optional[str] = None  # 미수없는매수수량
    max_buy_amt: Optional[str] = None  # 최대매수금액
    max_buy_qty: Optional[str] = None  # 최대매수수량
    cma_evlu_amt: Optional[str] = None  # CMA평가금액
    ovrs_re_use_amt_wcrc: Optional[str] = None  # 해외재사용금액원화
    ord_psbl_frcr_amt_wcrc: Optional[str] = None  # 주문가능외화금액원화
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDailyIndexchartprice(SQLModel, table=True):
    """Output table for inquire_daily_indexchartprice"""
    __tablename__ = "kis_inquire_daily_indexchartprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종 지수 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    bstp_nmix_prdy_ctrt: Optional[str] = None  # 업종 지수 전일 대비율
    prdy_nmix: Optional[str] = None  # 전일 지수
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    bstp_nmix_prpr: Optional[str] = None  # 업종 지수 현재가
    bstp_cls_code: Optional[str] = None  # 업종 구분 코드
    prdy_vol: Optional[str] = None  # 전일 거래량
    bstp_nmix_oprc: Optional[str] = None  # 업종 지수 시가
    bstp_nmix_hgpr: Optional[str] = None  # 업종 지수 최고가
    bstp_nmix_lwpr: Optional[str] = None  # 업종 지수 최저가
    futs_prdy_oprc: Optional[str] = None  # 업종 전일 시가
    futs_prdy_hgpr: Optional[str] = None  # 업종 전일 최고가
    futs_prdy_lwpr: Optional[str] = None  # 업종 전일 최저가
    stck_bsop_date: Optional[str] = None  # 영업 일자
    mod_yn: Optional[str] = None  # 변경 여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDailyOvertimeprice(SQLModel, table=True):
    """Output table for inquire_daily_overtimeprice"""
    __tablename__ = "kis_inquire_daily_overtimeprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ovtm_untp_prpr: Optional[str] = None  # 시간외 단일가 현재가
    ovtm_untp_prdy_vrss: Optional[str] = None  # 시간외 단일가 전일 대비
    ovtm_untp_prdy_vrss_sign: Optional[str] = None  # 시간외 단일가 전일 대비 부호
    ovtm_untp_prdy_ctrt: Optional[str] = None  # 시간외 단일가 전일 대비율
    ovtm_untp_vol: Optional[str] = None  # 시간외 단일가 거래량
    ovtm_untp_tr_pbmn: Optional[str] = None  # 시간외 단일가 거래대금
    ovtm_untp_mxpr: Optional[str] = None  # 시간외 단일가 상한가
    ovtm_untp_llam: Optional[str] = None  # 시간외 단일가 하한가
    ovtm_untp_oprc: Optional[str] = None  # 시간외 단일가 시가2
    ovtm_untp_hgpr: Optional[str] = None  # 시간외 단일가 최고가
    ovtm_untp_lwpr: Optional[str] = None  # 시간외 단일가 최저가
    ovtm_untp_antc_cnpr: Optional[str] = None  # 시간외 단일가 예상 체결가
    ovtm_untp_antc_cntg_vrss: Optional[str] = None  # 시간외 단일가 예상 체결 대비
    ovtm_untp_antc_cntg_vrss_sign: Optional[str] = None  # 시간외 단일가 예상 체결 대비
    ovtm_untp_antc_cntg_ctrt: Optional[str] = None  # 시간외 단일가 예상 체결 대비율
    ovtm_untp_antc_vol: Optional[str] = None  # 시간외 단일가 예상 거래량
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_clpr: Optional[str] = None  # 주식 종가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDailyTradeVolume(SQLModel, table=True):
    """Output table for inquire_daily_trade_volume"""
    __tablename__ = "kis_inquire_daily_trade_volume"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    shnu_cnqn_smtn: Optional[str] = None  # 매수 체결량 합계
    seln_cnqn_smtn: Optional[str] = None  # 매도 체결량 합계
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    total_seln_qty: Optional[str] = None  # 총 매도 수량
    total_shnu_qty: Optional[str] = None  # 총 매수 수량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireElwPrice(SQLModel, table=True):
    """Output table for inquire_elw_price"""
    __tablename__ = "kis_inquire_elw_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    elw_shrn_iscd: Optional[str] = None  # ELW 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    elw_prpr: Optional[str] = None  # ELW 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    prdy_vrss_vol_rate: Optional[str] = None  # 전일 대비 거래량 비율
    unas_shrn_iscd: Optional[str] = None  # 기초자산 단축 종목코드
    unas_isnm: Optional[str] = None  # 기초자산 종목명
    unas_prpr: Optional[str] = None  # 기초자산 현재가
    unas_prdy_vrss: Optional[str] = None  # 기초자산 전일 대비
    unas_prdy_vrss_sign: Optional[str] = None  # 기초자산 전일 대비 부호
    unas_prdy_ctrt: Optional[str] = None  # 기초자산 전일 대비율
    bidp: Optional[str] = None  # 매수호가
    askp: Optional[str] = None  # 매도호가
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    vol_tnrt: Optional[str] = None  # 거래량 회전율
    elw_oprc: Optional[str] = None  # ELW 시가2
    elw_hgpr: Optional[str] = None  # ELW 최고가
    elw_lwpr: Optional[str] = None  # ELW 최저가
    stck_prdy_clpr: Optional[str] = None  # 주식 전일 종가
    hts_thpr: Optional[str] = None  # HTS 이론가
    dprt: Optional[str] = None  # 괴리율
    atm_cls_name: Optional[str] = None  # ATM구분명
    hts_ints_vltl: Optional[str] = None  # HTS 내재 변동성
    acpr: Optional[str] = None  # 행사가
    pvt_scnd_dmrs_prc: Optional[str] = None  # 피벗 2차 디저항 가격
    pvt_frst_dmrs_prc: Optional[str] = None  # 피벗 1차 디저항 가격
    pvt_pont_val: Optional[str] = None  # 피벗 포인트 값
    pvt_frst_dmsp_prc: Optional[str] = None  # 피벗 1차 디지지 가격
    pvt_scnd_dmsp_prc: Optional[str] = None  # 피벗 2차 디지지 가격
    dmsp_val: Optional[str] = None  # 디지지 값
    dmrs_val: Optional[str] = None  # 디저항 값
    elw_sdpr: Optional[str] = None  # ELW 기준가
    apprch_rate: Optional[str] = None  # 접근도
    tick_conv_prc: Optional[str] = None  # 틱환산가
    invt_epmd_cntt: Optional[str] = None  # 투자 유의 내용
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireIndexCategoryPrice(SQLModel, table=True):
    """Output table for inquire_index_category_price"""
    __tablename__ = "kis_inquire_index_category_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bstp_nmix_prpr: Optional[str] = None  # 업종 지수 현재가
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종 지수 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    bstp_nmix_prdy_ctrt: Optional[str] = None  # 업종 지수 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    bstp_nmix_oprc: Optional[str] = None  # 업종 지수 시가2
    bstp_nmix_hgpr: Optional[str] = None  # 업종 지수 최고가
    bstp_nmix_lwpr: Optional[str] = None  # 업종 지수 최저가
    prdy_vol: Optional[str] = None  # 전일 거래량
    ascn_issu_cnt: Optional[str] = None  # 상승 종목 수
    down_issu_cnt: Optional[str] = None  # 하락 종목 수
    stnr_issu_cnt: Optional[str] = None  # 보합 종목 수
    uplm_issu_cnt: Optional[str] = None  # 상한 종목 수
    lslm_issu_cnt: Optional[str] = None  # 하한 종목 수
    prdy_tr_pbmn: Optional[str] = None  # 전일 거래 대금
    dryy_bstp_nmix_hgpr_date: Optional[str] = None  # 연중업종지수최고가일자
    dryy_bstp_nmix_hgpr: Optional[str] = None  # 연중업종지수최고가
    dryy_bstp_nmix_lwpr: Optional[str] = None  # 연중업종지수최저가
    dryy_bstp_nmix_lwpr_date: Optional[str] = None  # 연중업종지수최저가일자
    bstp_cls_code: Optional[str] = None  # 업종 구분 코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    acml_vol_rlim: Optional[str] = None  # 누적 거래량 비중
    acml_tr_pbmn_rlim: Optional[str] = None  # 누적 거래 대금 비중
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireIndexDailyPrice(SQLModel, table=True):
    """Output table for inquire_index_daily_price"""
    __tablename__ = "kis_inquire_index_daily_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bstp_nmix_prpr: Optional[str] = None  # 업종 지수 현재가
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종 지수 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    bstp_nmix_prdy_ctrt: Optional[str] = None  # 업종 지수 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    bstp_nmix_oprc: Optional[str] = None  # 업종 지수 시가2
    bstp_nmix_hgpr: Optional[str] = None  # 업종 지수 최고가
    bstp_nmix_lwpr: Optional[str] = None  # 업종 지수 최저가
    prdy_vol: Optional[str] = None  # 전일 거래량
    ascn_issu_cnt: Optional[str] = None  # 상승 종목 수
    down_issu_cnt: Optional[str] = None  # 하락 종목 수
    stnr_issu_cnt: Optional[str] = None  # 보합 종목 수
    uplm_issu_cnt: Optional[str] = None  # 상한 종목 수
    lslm_issu_cnt: Optional[str] = None  # 하한 종목 수
    prdy_tr_pbmn: Optional[str] = None  # 전일 거래 대금
    dryy_bstp_nmix_hgpr_date: Optional[str] = None  # 연중업종지수최고가일자
    dryy_bstp_nmix_hgpr: Optional[str] = None  # 연중업종지수최고가
    dryy_bstp_nmix_lwpr: Optional[str] = None  # 연중업종지수최저가
    dryy_bstp_nmix_lwpr_date: Optional[str] = None  # 연중업종지수최저가일자
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    acml_vol_rlim: Optional[str] = None  # 누적 거래량 비중
    invt_new_psdg: Optional[str] = None  # 투자 신 심리도
    d20_dsrt: Optional[str] = None  # 20일 이격도
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireIndexPrice(SQLModel, table=True):
    """Output table for inquire_index_price"""
    __tablename__ = "kis_inquire_index_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bstp_nmix_prpr: Optional[str] = None  # 업종 지수 현재가
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종 지수 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    bstp_nmix_prdy_ctrt: Optional[str] = None  # 업종 지수 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    prdy_vol: Optional[str] = None  # 전일 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    prdy_tr_pbmn: Optional[str] = None  # 전일 거래 대금
    bstp_nmix_oprc: Optional[str] = None  # 업종 지수 시가2
    prdy_nmix_vrss_nmix_oprc: Optional[str] = None  # 전일 지수 대비 지수 시가2
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2 대비 현재가 부호
    bstp_nmix_oprc_prdy_ctrt: Optional[str] = None  # 업종 지수 시가2 전일 대비율
    bstp_nmix_hgpr: Optional[str] = None  # 업종 지수 최고가
    prdy_nmix_vrss_nmix_hgpr: Optional[str] = None  # 전일 지수 대비 지수 최고가
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가 대비 현재가 부호
    bstp_nmix_hgpr_prdy_ctrt: Optional[str] = None  # 업종 지수 최고가 전일 대비율
    bstp_nmix_lwpr: Optional[str] = None  # 업종 지수 최저가
    prdy_clpr_vrss_lwpr: Optional[str] = None  # 전일 종가 대비 최저가
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가 대비 현재가 부호
    prdy_clpr_vrss_lwpr_rate: Optional[str] = None  # 전일 종가 대비 최저가 비율
    ascn_issu_cnt: Optional[str] = None  # 상승 종목 수
    uplm_issu_cnt: Optional[str] = None  # 상한 종목 수
    stnr_issu_cnt: Optional[str] = None  # 보합 종목 수
    down_issu_cnt: Optional[str] = None  # 하락 종목 수
    lslm_issu_cnt: Optional[str] = None  # 하한 종목 수
    dryy_bstp_nmix_hgpr: Optional[str] = None  # 연중업종지수최고가
    dryy_hgpr_vrss_prpr_rate: Optional[str] = None  # 연중 최고가 대비 현재가 비율
    dryy_bstp_nmix_hgpr_date: Optional[str] = None  # 연중업종지수최고가일자
    dryy_bstp_nmix_lwpr: Optional[str] = None  # 연중업종지수최저가
    dryy_lwpr_vrss_prpr_rate: Optional[str] = None  # 연중 최저가 대비 현재가 비율
    dryy_bstp_nmix_lwpr_date: Optional[str] = None  # 연중업종지수최저가일자
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    seln_rsqn_rate: Optional[str] = None  # 매도 잔량 비율
    shnu_rsqn_rate: Optional[str] = None  # 매수2 잔량 비율
    ntby_rsqn: Optional[str] = None  # 순매수 잔량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireIndexTickprice(SQLModel, table=True):
    """Output table for inquire_index_tickprice"""
    __tablename__ = "kis_inquire_index_tickprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    bstp_nmix_prpr: Optional[str] = None  # 업종 지수 현재가
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종 지수 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    bstp_nmix_prdy_ctrt: Optional[str] = None  # 업종 지수 전일 대비율
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    acml_vol: Optional[str] = None  # 누적 거래량
    cntg_vol: Optional[str] = None  # 체결 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireIndexTimeprice(SQLModel, table=True):
    """Output table for inquire_index_timeprice"""
    __tablename__ = "kis_inquire_index_timeprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bsop_hour: Optional[str] = None  # 영업 시간
    bstp_nmix_prpr: Optional[str] = None  # 업종 지수 현재가
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종 지수 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    bstp_nmix_prdy_ctrt: Optional[str] = None  # 업종 지수 전일 대비율
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    acml_vol: Optional[str] = None  # 누적 거래량
    cntg_vol: Optional[str] = None  # 체결 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireInvestor(SQLModel, table=True):
    """Output table for inquire_investor"""
    __tablename__ = "kis_inquire_investor"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_clpr: Optional[str] = None  # 주식 종가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prsn_ntby_qty: Optional[str] = None  # 개인 순매수 수량
    frgn_ntby_qty: Optional[str] = None  # 외국인 순매수 수량
    orgn_ntby_qty: Optional[str] = None  # 기관계 순매수 수량
    prsn_ntby_tr_pbmn: Optional[str] = None  # 개인 순매수 거래 대금
    frgn_ntby_tr_pbmn: Optional[str] = None  # 외국인 순매수 거래 대금
    orgn_ntby_tr_pbmn: Optional[str] = None  # 기관계 순매수 거래 대금
    prsn_shnu_vol: Optional[str] = None  # 개인 매수2 거래량
    frgn_shnu_vol: Optional[str] = None  # 외국인 매수2 거래량
    orgn_shnu_vol: Optional[str] = None  # 기관계 매수2 거래량
    prsn_shnu_tr_pbmn: Optional[str] = None  # 개인 매수2 거래 대금
    frgn_shnu_tr_pbmn: Optional[str] = None  # 외국인 매수2 거래 대금
    orgn_shnu_tr_pbmn: Optional[str] = None  # 기관계 매수2 거래 대금
    prsn_seln_vol: Optional[str] = None  # 개인 매도 거래량
    frgn_seln_vol: Optional[str] = None  # 외국인 매도 거래량
    orgn_seln_vol: Optional[str] = None  # 기관계 매도 거래량
    prsn_seln_tr_pbmn: Optional[str] = None  # 개인 매도 거래 대금
    frgn_seln_tr_pbmn: Optional[str] = None  # 외국인 매도 거래 대금
    orgn_seln_tr_pbmn: Optional[str] = None  # 기관계 매도 거래 대금
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireInvestorDailyByMarket(SQLModel, table=True):
    """Output table for inquire_investor_daily_by_market"""
    __tablename__ = "kis_inquire_investor_daily_by_market"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    bstp_nmix_prpr: Optional[str] = None  # 업종 지수 현재가
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종 지수 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    bstp_nmix_prdy_ctrt: Optional[str] = None  # 업종 지수 전일 대비율
    bstp_nmix_oprc: Optional[str] = None  # 업종 지수 시가2
    bstp_nmix_hgpr: Optional[str] = None  # 업종 지수 최고가
    bstp_nmix_lwpr: Optional[str] = None  # 업종 지수 최저가
    stck_prdy_clpr: Optional[str] = None  # 주식 전일 종가
    frgn_ntby_qty: Optional[str] = None  # 외국인 순매수 수량
    frgn_reg_ntby_qty: Optional[str] = None  # 외국인 등록 순매수 수량
    frgn_nreg_ntby_qty: Optional[str] = None  # 외국인 비등록 순매수 수량
    prsn_ntby_qty: Optional[str] = None  # 개인 순매수 수량
    orgn_ntby_qty: Optional[str] = None  # 기관계 순매수 수량
    scrt_ntby_qty: Optional[str] = None  # 증권 순매수 수량
    ivtr_ntby_qty: Optional[str] = None  # 투자신탁 순매수 수량
    pe_fund_ntby_vol: Optional[str] = None  # 사모 펀드 순매수 거래량
    bank_ntby_qty: Optional[str] = None  # 은행 순매수 수량
    insu_ntby_qty: Optional[str] = None  # 보험 순매수 수량
    mrbn_ntby_qty: Optional[str] = None  # 종금 순매수 수량
    fund_ntby_qty: Optional[str] = None  # 기금 순매수 수량
    etc_ntby_qty: Optional[str] = None  # 기타 순매수 수량
    etc_orgt_ntby_vol: Optional[str] = None  # 기타 단체 순매수 거래량
    etc_corp_ntby_vol: Optional[str] = None  # 기타 법인 순매수 거래량
    frgn_ntby_tr_pbmn: Optional[str] = None  # 외국인 순매수 거래 대금
    frgn_reg_ntby_pbmn: Optional[str] = None  # 외국인 등록 순매수 대금
    frgn_nreg_ntby_pbmn: Optional[str] = None  # 외국인 비등록 순매수 대금
    prsn_ntby_tr_pbmn: Optional[str] = None  # 개인 순매수 거래 대금
    orgn_ntby_tr_pbmn: Optional[str] = None  # 기관계 순매수 거래 대금
    scrt_ntby_tr_pbmn: Optional[str] = None  # 증권 순매수 거래 대금
    ivtr_ntby_tr_pbmn: Optional[str] = None  # 투자신탁 순매수 거래 대금
    pe_fund_ntby_tr_pbmn: Optional[str] = None  # 사모 펀드 순매수 거래 대금
    bank_ntby_tr_pbmn: Optional[str] = None  # 은행 순매수 거래 대금
    insu_ntby_tr_pbmn: Optional[str] = None  # 보험 순매수 거래 대금
    mrbn_ntby_tr_pbmn: Optional[str] = None  # 종금 순매수 거래 대금
    fund_ntby_tr_pbmn: Optional[str] = None  # 기금 순매수 거래 대금
    etc_ntby_tr_pbmn: Optional[str] = None  # 기타 순매수 거래 대금
    etc_orgt_ntby_tr_pbmn: Optional[str] = None  # 기타 단체 순매수 거래 대금
    etc_corp_ntby_tr_pbmn: Optional[str] = None  # 기타 법인 순매수 거래 대금
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireInvestorTimeByMarket(SQLModel, table=True):
    """Output table for inquire_investor_time_by_market"""
    __tablename__ = "kis_inquire_investor_time_by_market"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    frgn_seln_vol: Optional[str] = None  # 외국인 매도 거래량
    frgn_shnu_vol: Optional[str] = None  # 외국인 매수2 거래량
    frgn_ntby_qty: Optional[str] = None  # 외국인 순매수 수량
    frgn_seln_tr_pbmn: Optional[str] = None  # 외국인 매도 거래 대금
    frgn_shnu_tr_pbmn: Optional[str] = None  # 외국인 매수2 거래 대금
    frgn_ntby_tr_pbmn: Optional[str] = None  # 외국인 순매수 거래 대금
    prsn_seln_vol: Optional[str] = None  # 개인 매도 거래량
    prsn_shnu_vol: Optional[str] = None  # 개인 매수2 거래량
    prsn_ntby_qty: Optional[str] = None  # 개인 순매수 수량
    prsn_seln_tr_pbmn: Optional[str] = None  # 개인 매도 거래 대금
    prsn_shnu_tr_pbmn: Optional[str] = None  # 개인 매수2 거래 대금
    prsn_ntby_tr_pbmn: Optional[str] = None  # 개인 순매수 거래 대금
    orgn_seln_vol: Optional[str] = None  # 기관계 매도 거래량
    orgn_shnu_vol: Optional[str] = None  # 기관계 매수2 거래량
    orgn_ntby_qty: Optional[str] = None  # 기관계 순매수 수량
    orgn_seln_tr_pbmn: Optional[str] = None  # 기관계 매도 거래 대금
    orgn_shnu_tr_pbmn: Optional[str] = None  # 기관계 매수2 거래 대금
    orgn_ntby_tr_pbmn: Optional[str] = None  # 기관계 순매수 거래 대금
    scrt_seln_vol: Optional[str] = None  # 증권 매도 거래량
    scrt_shnu_vol: Optional[str] = None  # 증권 매수2 거래량
    scrt_ntby_qty: Optional[str] = None  # 증권 순매수 수량
    scrt_seln_tr_pbmn: Optional[str] = None  # 증권 매도 거래 대금
    scrt_shnu_tr_pbmn: Optional[str] = None  # 증권 매수2 거래 대금
    scrt_ntby_tr_pbmn: Optional[str] = None  # 증권 순매수 거래 대금
    ivtr_seln_vol: Optional[str] = None  # 투자신탁 매도 거래량
    ivtr_shnu_vol: Optional[str] = None  # 투자신탁 매수2 거래량
    ivtr_ntby_qty: Optional[str] = None  # 투자신탁 순매수 수량
    ivtr_seln_tr_pbmn: Optional[str] = None  # 투자신탁 매도 거래 대금
    ivtr_shnu_tr_pbmn: Optional[str] = None  # 투자신탁 매수2 거래 대금
    ivtr_ntby_tr_pbmn: Optional[str] = None  # 투자신탁 순매수 거래 대금
    pe_fund_seln_tr_pbmn: Optional[str] = None  # 사모 펀드 매도 거래 대금
    pe_fund_seln_vol: Optional[str] = None  # 사모 펀드 매도 거래량
    pe_fund_ntby_vol: Optional[str] = None  # 사모 펀드 순매수 거래량
    pe_fund_shnu_tr_pbmn: Optional[str] = None  # 사모 펀드 매수2 거래 대금
    pe_fund_shnu_vol: Optional[str] = None  # 사모 펀드 매수2 거래량
    pe_fund_ntby_tr_pbmn: Optional[str] = None  # 사모 펀드 순매수 거래 대금
    bank_seln_vol: Optional[str] = None  # 은행 매도 거래량
    bank_shnu_vol: Optional[str] = None  # 은행 매수2 거래량
    bank_ntby_qty: Optional[str] = None  # 은행 순매수 수량
    bank_seln_tr_pbmn: Optional[str] = None  # 은행 매도 거래 대금
    bank_shnu_tr_pbmn: Optional[str] = None  # 은행 매수2 거래 대금
    bank_ntby_tr_pbmn: Optional[str] = None  # 은행 순매수 거래 대금
    insu_seln_vol: Optional[str] = None  # 보험 매도 거래량
    insu_shnu_vol: Optional[str] = None  # 보험 매수2 거래량
    insu_ntby_qty: Optional[str] = None  # 보험 순매수 수량
    insu_seln_tr_pbmn: Optional[str] = None  # 보험 매도 거래 대금
    insu_shnu_tr_pbmn: Optional[str] = None  # 보험 매수2 거래 대금
    insu_ntby_tr_pbmn: Optional[str] = None  # 보험 순매수 거래 대금
    mrbn_seln_vol: Optional[str] = None  # 종금 매도 거래량
    mrbn_shnu_vol: Optional[str] = None  # 종금 매수2 거래량
    mrbn_ntby_qty: Optional[str] = None  # 종금 순매수 수량
    mrbn_seln_tr_pbmn: Optional[str] = None  # 종금 매도 거래 대금
    mrbn_shnu_tr_pbmn: Optional[str] = None  # 종금 매수2 거래 대금
    mrbn_ntby_tr_pbmn: Optional[str] = None  # 종금 순매수 거래 대금
    fund_seln_vol: Optional[str] = None  # 기금 매도 거래량
    fund_shnu_vol: Optional[str] = None  # 기금 매수2 거래량
    fund_ntby_qty: Optional[str] = None  # 기금 순매수 수량
    fund_seln_tr_pbmn: Optional[str] = None  # 기금 매도 거래 대금
    fund_shnu_tr_pbmn: Optional[str] = None  # 기금 매수2 거래 대금
    fund_ntby_tr_pbmn: Optional[str] = None  # 기금 순매수 거래 대금
    etc_orgt_seln_vol: Optional[str] = None  # 기타 단체 매도 거래량
    etc_orgt_shnu_vol: Optional[str] = None  # 기타 단체 매수2 거래량
    etc_orgt_ntby_vol: Optional[str] = None  # 기타 단체 순매수 거래량
    etc_orgt_seln_tr_pbmn: Optional[str] = None  # 기타 단체 매도 거래 대금
    etc_orgt_shnu_tr_pbmn: Optional[str] = None  # 기타 단체 매수2 거래 대금
    etc_orgt_ntby_tr_pbmn: Optional[str] = None  # 기타 단체 순매수 거래 대금
    etc_corp_seln_vol: Optional[str] = None  # 기타 법인 매도 거래량
    etc_corp_shnu_vol: Optional[str] = None  # 기타 법인 매수2 거래량
    etc_corp_ntby_vol: Optional[str] = None  # 기타 법인 순매수 거래량
    etc_corp_seln_tr_pbmn: Optional[str] = None  # 기타 법인 매도 거래 대금
    etc_corp_shnu_tr_pbmn: Optional[str] = None  # 기타 법인 매수2 거래 대금
    etc_corp_ntby_tr_pbmn: Optional[str] = None  # 기타 법인 순매수 거래 대금
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireMember(SQLModel, table=True):
    """Output table for inquire_member"""
    __tablename__ = "kis_inquire_member"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    seln_mbcr_no1: Optional[str] = None  # 매도 회원사 번호1
    seln_mbcr_no2: Optional[str] = None  # 매도 회원사 번호2
    seln_mbcr_no3: Optional[str] = None  # 매도 회원사 번호3
    seln_mbcr_no4: Optional[str] = None  # 매도 회원사 번호4
    seln_mbcr_no5: Optional[str] = None  # 매도 회원사 번호5
    seln_mbcr_name1: Optional[str] = None  # 매도 회원사 명1
    seln_mbcr_name2: Optional[str] = None  # 매도 회원사 명2
    seln_mbcr_name3: Optional[str] = None  # 매도 회원사 명3
    seln_mbcr_name4: Optional[str] = None  # 매도 회원사 명4
    seln_mbcr_name5: Optional[str] = None  # 매도 회원사 명5
    total_seln_qty1: Optional[str] = None  # 총 매도 수량1
    total_seln_qty2: Optional[str] = None  # 총 매도 수량2
    total_seln_qty3: Optional[str] = None  # 총 매도 수량3
    total_seln_qty4: Optional[str] = None  # 총 매도 수량4
    total_seln_qty5: Optional[str] = None  # 총 매도 수량5
    seln_mbcr_rlim1: Optional[str] = None  # 매도 회원사 비중1
    seln_mbcr_rlim2: Optional[str] = None  # 매도 회원사 비중2
    seln_mbcr_rlim3: Optional[str] = None  # 매도 회원사 비중3
    seln_mbcr_rlim4: Optional[str] = None  # 매도 회원사 비중4
    seln_mbcr_rlim5: Optional[str] = None  # 매도 회원사 비중5
    seln_qty_icdc1: Optional[str] = None  # 매도 수량 증감1
    seln_qty_icdc2: Optional[str] = None  # 매도 수량 증감2
    seln_qty_icdc3: Optional[str] = None  # 매도 수량 증감3
    seln_qty_icdc4: Optional[str] = None  # 매도 수량 증감4
    seln_qty_icdc5: Optional[str] = None  # 매도 수량 증감5
    shnu_mbcr_no1: Optional[str] = None  # 매수2 회원사 번호1
    shnu_mbcr_no2: Optional[str] = None  # 매수2 회원사 번호2
    shnu_mbcr_no3: Optional[str] = None  # 매수2 회원사 번호3
    shnu_mbcr_no4: Optional[str] = None  # 매수2 회원사 번호4
    shnu_mbcr_no5: Optional[str] = None  # 매수2 회원사 번호5
    shnu_mbcr_name1: Optional[str] = None  # 매수2 회원사 명1
    shnu_mbcr_name2: Optional[str] = None  # 매수2 회원사 명2
    shnu_mbcr_name3: Optional[str] = None  # 매수2 회원사 명3
    shnu_mbcr_name4: Optional[str] = None  # 매수2 회원사 명4
    shnu_mbcr_name5: Optional[str] = None  # 매수2 회원사 명5
    total_shnu_qty1: Optional[str] = None  # 총 매수2 수량1
    total_shnu_qty2: Optional[str] = None  # 총 매수2 수량2
    total_shnu_qty3: Optional[str] = None  # 총 매수2 수량3
    total_shnu_qty4: Optional[str] = None  # 총 매수2 수량4
    total_shnu_qty5: Optional[str] = None  # 총 매수2 수량5
    shnu_mbcr_rlim1: Optional[str] = None  # 매수2 회원사 비중1
    shnu_mbcr_rlim2: Optional[str] = None  # 매수2 회원사 비중2
    shnu_mbcr_rlim3: Optional[str] = None  # 매수2 회원사 비중3
    shnu_mbcr_rlim4: Optional[str] = None  # 매수2 회원사 비중4
    shnu_mbcr_rlim5: Optional[str] = None  # 매수2 회원사 비중5
    shnu_qty_icdc1: Optional[str] = None  # 매수2 수량 증감1
    shnu_qty_icdc2: Optional[str] = None  # 매수2 수량 증감2
    shnu_qty_icdc3: Optional[str] = None  # 매수2 수량 증감3
    shnu_qty_icdc4: Optional[str] = None  # 매수2 수량 증감4
    shnu_qty_icdc5: Optional[str] = None  # 매수2 수량 증감5
    glob_total_seln_qty: Optional[str] = None  # 외국계 총 매도 수량
    glob_seln_rlim: Optional[str] = None  # 외국계 매도 비중
    glob_ntby_qty: Optional[str] = None  # 외국계 순매수 수량
    glob_total_shnu_qty: Optional[str] = None  # 외국계 총 매수2 수량
    glob_shnu_rlim: Optional[str] = None  # 외국계 매수2 비중
    seln_mbcr_glob_yn_1: Optional[str] = None  # 매도 회원사 외국계 여부1
    seln_mbcr_glob_yn_2: Optional[str] = None  # 매도 회원사 외국계 여부2
    seln_mbcr_glob_yn_3: Optional[str] = None  # 매도 회원사 외국계 여부3
    seln_mbcr_glob_yn_4: Optional[str] = None  # 매도 회원사 외국계 여부4
    seln_mbcr_glob_yn_5: Optional[str] = None  # 매도 회원사 외국계 여부5
    shnu_mbcr_glob_yn_1: Optional[str] = None  # 매수2 회원사 외국계 여부1
    shnu_mbcr_glob_yn_2: Optional[str] = None  # 매수2 회원사 외국계 여부2
    shnu_mbcr_glob_yn_3: Optional[str] = None  # 매수2 회원사 외국계 여부3
    shnu_mbcr_glob_yn_4: Optional[str] = None  # 매수2 회원사 외국계 여부4
    shnu_mbcr_glob_yn_5: Optional[str] = None  # 매수2 회원사 외국계 여부5
    glob_total_seln_qty_icdc: Optional[str] = None  # 외국계 총 매도 수량 증감
    glob_total_shnu_qty_icdc: Optional[str] = None  # 외국계 총 매수2 수량 증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireMemberDaily(SQLModel, table=True):
    """Output table for inquire_member_daily"""
    __tablename__ = "kis_inquire_member_daily"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식영업일자
    total_seln_qty: Optional[str] = None  # 총매도수량
    total_shnu_qty: Optional[str] = None  # 총매수2수량
    ntby_qty: Optional[str] = None  # 순매수수량
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireOvertimeAskingPrice(SQLModel, table=True):
    """Output table for inquire_overtime_asking_price"""
    __tablename__ = "kis_inquire_overtime_asking_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ovtm_untp_last_hour: Optional[str] = None  # 시간외 단일가 최종 시간
    ovtm_untp_askp1: Optional[str] = None  # 시간외 단일가 매도호가1
    ovtm_untp_askp2: Optional[str] = None  # 시간외 단일가 매도호가2
    ovtm_untp_askp3: Optional[str] = None  # 시간외 단일가 매도호가3
    ovtm_untp_askp4: Optional[str] = None  # 시간외 단일가 매도호가4
    ovtm_untp_askp5: Optional[str] = None  # 시간외 단일가 매도호가5
    ovtm_untp_askp6: Optional[str] = None  # 시간외 단일가 매도호가6
    ovtm_untp_askp7: Optional[str] = None  # 시간외 단일가 매도호가7
    ovtm_untp_askp8: Optional[str] = None  # 시간외 단일가 매도호가8
    ovtm_untp_askp9: Optional[str] = None  # 시간외 단일가 매도호가9
    ovtm_untp_askp10: Optional[str] = None  # 시간외 단일가 매도호가10
    ovtm_untp_bidp1: Optional[str] = None  # 시간외 단일가 매수호가1
    ovtm_untp_bidp2: Optional[str] = None  # 시간외 단일가 매수호가2
    ovtm_untp_bidp3: Optional[str] = None  # 시간외 단일가 매수호가3
    ovtm_untp_bidp4: Optional[str] = None  # 시간외 단일가 매수호가4
    ovtm_untp_bidp5: Optional[str] = None  # 시간외 단일가 매수호가5
    ovtm_untp_bidp6: Optional[str] = None  # 시간외 단일가 매수호가6
    ovtm_untp_bidp7: Optional[str] = None  # 시간외 단일가 매수호가7
    ovtm_untp_bidp8: Optional[str] = None  # 시간외 단일가 매수호가8
    ovtm_untp_bidp9: Optional[str] = None  # 시간외 단일가 매수호가9
    ovtm_untp_bidp10: Optional[str] = None  # 시간외 단일가 매수호가10
    ovtm_untp_askp_icdc1: Optional[str] = None  # 시간외 단일가 매도호가 증감1
    ovtm_untp_askp_icdc2: Optional[str] = None  # 시간외 단일가 매도호가 증감2
    ovtm_untp_askp_icdc3: Optional[str] = None  # 시간외 단일가 매도호가 증감3
    ovtm_untp_askp_icdc4: Optional[str] = None  # 시간외 단일가 매도호가 증감4
    ovtm_untp_askp_icdc5: Optional[str] = None  # 시간외 단일가 매도호가 증감5
    ovtm_untp_askp_icdc6: Optional[str] = None  # 시간외 단일가 매도호가 증감6
    ovtm_untp_askp_icdc7: Optional[str] = None  # 시간외 단일가 매도호가 증감7
    ovtm_untp_askp_icdc8: Optional[str] = None  # 시간외 단일가 매도호가 증감8
    ovtm_untp_askp_icdc9: Optional[str] = None  # 시간외 단일가 매도호가 증감9
    ovtm_untp_askp_icdc10: Optional[str] = None  # 시간외 단일가 매도호가 증감10
    ovtm_untp_bidp_icdc1: Optional[str] = None  # 시간외 단일가 매수호가 증감1
    ovtm_untp_bidp_icdc2: Optional[str] = None  # 시간외 단일가 매수호가 증감2
    ovtm_untp_bidp_icdc3: Optional[str] = None  # 시간외 단일가 매수호가 증감3
    ovtm_untp_bidp_icdc4: Optional[str] = None  # 시간외 단일가 매수호가 증감4
    ovtm_untp_bidp_icdc5: Optional[str] = None  # 시간외 단일가 매수호가 증감5
    ovtm_untp_bidp_icdc6: Optional[str] = None  # 시간외 단일가 매수호가 증감6
    ovtm_untp_bidp_icdc7: Optional[str] = None  # 시간외 단일가 매수호가 증감7
    ovtm_untp_bidp_icdc8: Optional[str] = None  # 시간외 단일가 매수호가 증감8
    ovtm_untp_bidp_icdc9: Optional[str] = None  # 시간외 단일가 매수호가 증감9
    ovtm_untp_bidp_icdc10: Optional[str] = None  # 시간외 단일가 매수호가 증감10
    ovtm_untp_askp_rsqn1: Optional[str] = None  # 시간외 단일가 매도호가 잔량1
    ovtm_untp_askp_rsqn2: Optional[str] = None  # 시간외 단일가 매도호가 잔량2
    ovtm_untp_askp_rsqn3: Optional[str] = None  # 시간외 단일가 매도호가 잔량3
    ovtm_untp_askp_rsqn4: Optional[str] = None  # 시간외 단일가 매도호가 잔량4
    ovtm_untp_askp_rsqn5: Optional[str] = None  # 시간외 단일가 매도호가 잔량5
    ovtm_untp_askp_rsqn6: Optional[str] = None  # 시간외 단일가 매도호가 잔량6
    ovtm_untp_askp_rsqn7: Optional[str] = None  # 시간외 단일가 매도호가 잔량7
    ovtm_untp_askp_rsqn8: Optional[str] = None  # 시간외 단일가 매도호가 잔량8
    ovtm_untp_askp_rsqn9: Optional[str] = None  # 시간외 단일가 매도호가 잔량9
    ovtm_untp_askp_rsqn10: Optional[str] = None  # 시간외 단일가 매도호가 잔량10
    ovtm_untp_bidp_rsqn1: Optional[str] = None  # 시간외 단일가 매수호가 잔량1
    ovtm_untp_bidp_rsqn: Optional[str] = None  # 시간외 단일가 매수호가 잔량2
    ovtm_untp_bidp_rsqn3: Optional[str] = None  # 시간외 단일가 매수호가 잔량3
    ovtm_untp_bidp_rsqn4: Optional[str] = None  # 시간외 단일가 매수호가 잔량4
    ovtm_untp_bidp_rsqn5: Optional[str] = None  # 시간외 단일가 매수호가 잔량5
    ovtm_untp_bidp_rsqn6: Optional[str] = None  # 시간외 단일가 매수호가 잔량6
    ovtm_untp_bidp_rsqn7: Optional[str] = None  # 시간외 단일가 매수호가 잔량7
    ovtm_untp_bidp_rsqn8: Optional[str] = None  # 시간외 단일가 매수호가 잔량8
    ovtm_untp_bidp_rsqn9: Optional[str] = None  # 시간외 단일가 매수호가 잔량9
    ovtm_untp_bidp_rsqn10: Optional[str] = None  # 시간외 단일가 매수호가 잔량10
    ovtm_untp_total_askp_rsqn: Optional[str] = None  # 시간외 단일가 총 매도호가 잔량
    ovtm_untp_total_bidp_rsqn: Optional[str] = None  # 시간외 단일가 총 매수호가 잔량
    ovtm_untp_total_askp_rsqn_icdc: Optional[str] = None  # 시간외 단일가 총 매도호가 잔량
    ovtm_untp_total_bidp_rsqn_icdc: Optional[str] = None  # 시간외 단일가 총 매수호가 잔량
    ovtm_untp_ntby_bidp_rsqn: Optional[str] = None  # 시간외 단일가 순매수 호가 잔량
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    total_askp_rsqn_icdc: Optional[str] = None  # 총 매도호가 잔량 증감
    total_bidp_rsqn_icdc: Optional[str] = None  # 총 매수호가 잔량 증감
    ovtm_total_askp_rsqn: Optional[str] = None  # 시간외 총 매도호가 잔량
    ovtm_total_bidp_rsqn: Optional[str] = None  # 시간외 총 매수호가 잔량
    ovtm_total_askp_icdc: Optional[str] = None  # 시간외 총 매도호가 증감
    ovtm_total_bidp_icdc: Optional[str] = None  # 시간외 총 매수호가 증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireOvertimePrice(SQLModel, table=True):
    """Output table for inquire_overtime_price"""
    __tablename__ = "kis_inquire_overtime_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bstp_kor_isnm: Optional[str] = None  # 업종 한글 종목명
    mang_issu_cls_name: Optional[str] = None  # 관리 종목 구분 명
    ovtm_untp_prpr: Optional[str] = None  # 시간외 단일가 현재가
    ovtm_untp_prdy_vrss: Optional[str] = None  # 시간외 단일가 전일 대비
    ovtm_untp_prdy_vrss_sign: Optional[str] = None  # 시간외 단일가 전일 대비 부호
    ovtm_untp_prdy_ctrt: Optional[str] = None  # 시간외 단일가 전일 대비율
    ovtm_untp_vol: Optional[str] = None  # 시간외 단일가 거래량
    ovtm_untp_tr_pbmn: Optional[str] = None  # 시간외 단일가 거래 대금
    ovtm_untp_mxpr: Optional[str] = None  # 시간외 단일가 상한가
    ovtm_untp_llam: Optional[str] = None  # 시간외 단일가 하한가
    ovtm_untp_oprc: Optional[str] = None  # 시간외 단일가 시가2
    ovtm_untp_hgpr: Optional[str] = None  # 시간외 단일가 최고가
    ovtm_untp_lwpr: Optional[str] = None  # 시간외 단일가 최저가
    marg_rate: Optional[str] = None  # 증거금 비율
    ovtm_untp_antc_cnpr: Optional[str] = None  # 시간외 단일가 예상 체결가
    ovtm_untp_antc_cntg_vrss: Optional[str] = None  # 시간외 단일가 예상 체결 대비
    ovtm_untp_antc_cntg_vrss_sign: Optional[str] = None  # 시간외 단일가 예상 체결 대비
    ovtm_untp_antc_cntg_ctrt: Optional[str] = None  # 시간외 단일가 예상 체결 대비율
    ovtm_untp_antc_cnqn: Optional[str] = None  # 시간외 단일가 예상 체결량
    crdt_able_yn: Optional[str] = None  # 신용 가능 여부
    new_lstn_cls_name: Optional[str] = None  # 신규 상장 구분 명
    sltr_yn: Optional[str] = None  # 정리매매 여부
    mang_issu_yn: Optional[str] = None  # 관리 종목 여부
    mrkt_warn_cls_code: Optional[str] = None  # 시장 경고 구분 코드
    trht_yn: Optional[str] = None  # 거래정지 여부
    vlnt_deal_cls_name: Optional[str] = None  # 임의 매매 구분 명
    ovtm_untp_sdpr: Optional[str] = None  # 시간외 단일가 기준가
    mrkt_warn_cls_name: Optional[str] = None  # 시장 경구 구분 명
    revl_issu_reas_name: Optional[str] = None  # 재평가 종목 사유 명
    insn_pbnt_yn: Optional[str] = None  # 불성실 공시 여부
    flng_cls_name: Optional[str] = None  # 락 구분 이름
    rprs_mrkt_kor_name: Optional[str] = None  # 대표 시장 한글 명
    ovtm_vi_cls_code: Optional[str] = None  # 시간외단일가VI적용구분코드
    bidp: Optional[str] = None  # 매수호가
    askp: Optional[str] = None  # 매도호가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePeriodProfit(SQLModel, table=True):
    """Output table for inquire_period_profit"""
    __tablename__ = "kis_inquire_period_profit"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    trad_day: Optional[str] = None  # 매매일
    ovrs_pdno: Optional[str] = None  # 해외상품번호
    slcl_qty: Optional[str] = None  # 매도청산수량
    pchs_avg_pric: Optional[str] = None  # 매입평균가격
    frcr_pchs_amt1: Optional[str] = None  # 외화매입금액1
    avg_sll_unpr: Optional[str] = None  # 평균매도단가
    frcr_sll_amt_smtl1: Optional[str] = None  # 외화매도금액합계1
    stck_sll_tlex: Optional[str] = None  # 주식매도제비용
    ovrs_rlzt_pfls_amt: Optional[str] = None  # 해외실현손익금액
    pftrt: Optional[str] = None  # 수익률
    exrt: Optional[str] = None  # 환율
    ovrs_excg_cd: Optional[str] = None  # 해외거래소코드
    frst_bltn_exrt: Optional[str] = None  # 최초고시환율
    stck_sll_amt_smtl: Optional[str] = None  # 주식매도금액합계
    stck_buy_amt_smtl: Optional[str] = None  # 주식매수금액합계
    smtl_fee1: Optional[str] = None  # 합계수수료1
    excc_dfrm_amt: Optional[str] = None  # 정산지급금액
    ovrs_rlzt_pfls_tot_amt: Optional[str] = None  # 해외실현손익총금액
    tot_pftrt: Optional[str] = None  # 총수익률
    bass_dt: Optional[str] = None  # 기준일자
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePeriodTradeProfit(SQLModel, table=True):
    """Output table for inquire_period_trade_profit"""
    __tablename__ = "kis_inquire_period_trade_profit"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    trad_dt: Optional[str] = None  # 매매일자
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    trad_dvsn_name: Optional[str] = None  # 매매구분명
    loan_dt: Optional[str] = None  # 대출일자
    hldg_qty: Optional[str] = None  # 보유수량
    pchs_unpr: Optional[str] = None  # 매입단가
    buy_qty: Optional[str] = None  # 매수수량
    buy_amt: Optional[str] = None  # 매수금액
    sll_pric: Optional[str] = None  # 매도가격
    sll_qty: Optional[str] = None  # 매도수량
    sll_amt: Optional[str] = None  # 매도금액
    rlzt_pfls: Optional[str] = None  # 실현손익
    pfls_rt: Optional[str] = None  # 손익률
    fee: Optional[str] = None  # 수수료
    tl_tax: Optional[str] = None  # 제세금
    loan_int: Optional[str] = None  # 대출이자
    sll_qty_smtl: Optional[str] = None  # 매도수량합계
    sll_tr_amt_smtl: Optional[str] = None  # 매도거래금액합계
    sll_fee_smtl: Optional[str] = None  # 매도수수료합계
    sll_tltx_smtl: Optional[str] = None  # 매도제세금합계
    sll_excc_amt_smtl: Optional[str] = None  # 매도정산금액합계
    buyqty_smtl: Optional[str] = None  # 매수수량합계
    buy_tr_amt_smtl: Optional[str] = None  # 매수거래금액합계
    buy_fee_smtl: Optional[str] = None  # 매수수수료합계
    buy_tax_smtl: Optional[str] = None  # 매수제세금합계
    buy_excc_amt_smtl: Optional[str] = None  # 매수정산금액합계
    tot_qty: Optional[str] = None  # 총수량
    tot_tr_amt: Optional[str] = None  # 총거래금액
    tot_fee: Optional[str] = None  # 총수수료
    tot_tltx: Optional[str] = None  # 총제세금
    tot_excc_amt: Optional[str] = None  # 총정산금액
    tot_rlzt_pfls: Optional[str] = None  # 총실현손익
    tot_pftrt: Optional[str] = None  # 총수익률
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePrice2(SQLModel, table=True):
    """Output table for inquire_price_2"""
    __tablename__ = "kis_inquire_price_2"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    rprs_mrkt_kor_name: Optional[str] = None  # 대표 시장 한글 명
    new_hgpr_lwpr_cls_code: Optional[str] = None  # 신 고가 저가 구분 코드
    mxpr_llam_cls_code: Optional[str] = None  # 상하한가 구분 코드
    crdt_able_yn: Optional[str] = None  # 신용 가능 여부
    stck_mxpr: Optional[str] = None  # 주식 상한가
    elw_pblc_yn: Optional[str] = None  # ELW 발행 여부
    prdy_clpr_vrss_oprc_rate: Optional[str] = None  # 전일 종가 대비 시가2 비율
    crdt_rate: Optional[str] = None  # 신용 비율
    marg_rate: Optional[str] = None  # 증거금 비율
    lwpr_vrss_prpr: Optional[str] = None  # 최저가 대비 현재가
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가 대비 현재가 부호
    prdy_clpr_vrss_lwpr_rate: Optional[str] = None  # 전일 종가 대비 최저가 비율
    stck_lwpr: Optional[str] = None  # 주식 최저가
    hgpr_vrss_prpr: Optional[str] = None  # 최고가 대비 현재가
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가 대비 현재가 부호
    prdy_clpr_vrss_hgpr_rate: Optional[str] = None  # 전일 종가 대비 최고가 비율
    stck_hgpr: Optional[str] = None  # 주식 최고가
    oprc_vrss_prpr: Optional[str] = None  # 시가2 대비 현재가
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2 대비 현재가 부호
    mang_issu_yn: Optional[str] = None  # 관리 종목 여부
    divi_app_cls_code: Optional[str] = None  # 동시호가배분처리코드
    short_over_yn: Optional[str] = None  # 단기과열여부
    mrkt_warn_cls_code: Optional[str] = None  # 시장경고코드
    invt_caful_yn: Optional[str] = None  # 투자유의여부
    stange_runup_yn: Optional[str] = None  # 이상급등여부
    ssts_hot_yn: Optional[str] = None  # 공매도과열 여부
    low_current_yn: Optional[str] = None  # 저유동성 종목 여부
    vi_cls_code: Optional[str] = None  # VI적용구분코드
    short_over_cls_code: Optional[str] = None  # 단기과열구분코드
    stck_llam: Optional[str] = None  # 주식 하한가
    new_lstn_cls_name: Optional[str] = None  # 신규 상장 구분 명
    vlnt_deal_cls_name: Optional[str] = None  # 임의 매매 구분 명
    flng_cls_name: Optional[str] = None  # 락 구분 이름
    revl_issu_reas_name: Optional[str] = None  # 재평가 종목 사유 명
    mrkt_warn_cls_name: Optional[str] = None  # 시장 경고 구분 명
    stck_sdpr: Optional[str] = None  # 주식 기준가
    bstp_cls_code: Optional[str] = None  # 업종 구분 코드
    stck_prdy_clpr: Optional[str] = None  # 주식 전일 종가
    insn_pbnt_yn: Optional[str] = None  # 불성실 공시 여부
    fcam_mod_cls_name: Optional[str] = None  # 액면가 변경 구분 명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    acml_vol: Optional[str] = None  # 누적 거래량
    prdy_vrss_vol_rate: Optional[str] = None  # 전일 대비 거래량 비율
    bstp_kor_isnm: Optional[str] = None  # 업종 한글 종목명
    sltr_yn: Optional[str] = None  # 정리매매 여부
    trht_yn: Optional[str] = None  # 거래정지 여부
    oprc_rang_cont_yn: Optional[str] = None  # 시가 범위 연장 여부
    vlnt_fin_cls_code: Optional[str] = None  # 임의 종료 구분 코드
    stck_oprc: Optional[str] = None  # 주식 시가2
    prdy_vol: Optional[str] = None  # 전일 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePsblSell(SQLModel, table=True):
    """Output table for inquire_psbl_sell"""
    __tablename__ = "kis_inquire_psbl_sell"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pdno: Optional[str] = None  # 상품번호
    buy_qty: Optional[str] = None  # 매수수량
    sll_qty: Optional[str] = None  # 매도수량
    cblc_qty: Optional[str] = None  # 잔고수량
    nsvg_qty: Optional[str] = None  # 비저축수량
    ord_psbl_qty: Optional[str] = None  # 주문가능수량
    pchs_avg_pric: Optional[str] = None  # 매입평균가격
    pchs_amt: Optional[str] = None  # 매입금액
    now_pric: Optional[str] = None  # 현재가
    evlu_amt: Optional[str] = None  # 평가금액
    evlu_pfls_amt: Optional[str] = None  # 평가손익금액
    evlu_pfls_rt: Optional[str] = None  # 평가손익율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireTimeDailychartprice(SQLModel, table=True):
    """Output table for inquire_time_dailychartprice"""
    __tablename__ = "kis_inquire_time_dailychartprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    stck_prdy_clpr: Optional[str] = None  # 주식 전일 종가
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    stck_oprc: Optional[str] = None  # 주식 시가2
    stck_hgpr: Optional[str] = None  # 주식 최고가
    stck_lwpr: Optional[str] = None  # 주식 최저가
    cntg_vol: Optional[str] = None  # 체결 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireTimeIndexchartprice(SQLModel, table=True):
    """Output table for inquire_time_indexchartprice"""
    __tablename__ = "kis_inquire_time_indexchartprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ovrs_nmix_prdy_vrss: Optional[str] = None  # 해외 지수 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    ovrs_nmix_prdy_clpr: Optional[str] = None  # 해외 지수 전일 종가
    acml_vol: Optional[str] = None  # 누적 거래량
    ovrs_nmix_prpr: Optional[str] = None  # 해외 지수 현재가
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    ovrs_prod_oprc: Optional[str] = None  # 해외 상품 시가2
    ovrs_prod_hgpr: Optional[str] = None  # 해외 상품 최고가
    ovrs_prod_lwpr: Optional[str] = None  # 해외 상품 최저가
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    optn_prpr: Optional[str] = None  # 옵션 현재가
    optn_oprc: Optional[str] = None  # 옵션 시가2
    optn_hgpr: Optional[str] = None  # 옵션 최고가
    optn_lwpr: Optional[str] = None  # 옵션 최저가
    cntg_vol: Optional[str] = None  # 체결 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireTimeItemchartprice(SQLModel, table=True):
    """Output table for inquire_time_itemchartprice"""
    __tablename__ = "kis_inquire_time_itemchartprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    rsym: Optional[str] = None  # 실시간종목코드
    zdiv: Optional[str] = None  # 소수점자리수
    stim: Optional[str] = None  # 장시작현지시간
    etim: Optional[str] = None  # 장종료현지시간
    sktm: Optional[str] = None  # 장시작한국시간
    ektm: Optional[str] = None  # 장종료한국시간
    next: Optional[str] = None  # 다음가능여부
    more: Optional[str] = None  # 추가데이타여부
    nrec: Optional[str] = None  # 레코드갯수
    tymd: Optional[str] = None  # 현지영업일자
    xymd: Optional[str] = None  # 현지기준일자
    xhms: Optional[str] = None  # 현지기준시간
    kymd: Optional[str] = None  # 한국기준일자
    khms: Optional[str] = None  # 한국기준시간
    open: Optional[str] = None  # 시가
    high: Optional[str] = None  # 고가
    low: Optional[str] = None  # 저가
    last: Optional[str] = None  # 종가
    evol: Optional[str] = None  # 체결량
    eamt: Optional[str] = None  # 체결대금
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireTimeItemconclusion(SQLModel, table=True):
    """Output table for inquire_time_itemconclusion"""
    __tablename__ = "kis_inquire_time_itemconclusion"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    prdy_vol: Optional[str] = None  # 전일 거래량
    rprs_mrkt_kor_name: Optional[str] = None  # 대표 시장 한글 명
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    stck_pbpr: Optional[str] = None  # 주식 현재가
    askp: Optional[str] = None  # 매도호가
    bidp: Optional[str] = None  # 매수호가
    tday_rltv: Optional[str] = None  # 당일 체결강도
    cnqn: Optional[str] = None  # 체결량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireTimeOvertimeconclusion(SQLModel, table=True):
    """Output table for inquire_time_overtimeconclusion"""
    __tablename__ = "kis_inquire_time_overtimeconclusion"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ovtm_untp_prpr: Optional[str] = None  # 시간외 단일가 현재가
    ovtm_untp_prdy_vrss: Optional[str] = None  # 시간외 단일가 전일 대비
    ovtm_untp_prdy_vrss_sign: Optional[str] = None  # 시간외 단일가 전일 대비 부호
    ovtm_untp_prdy_ctrt: Optional[str] = None  # 시간외 단일가 전일 대비율
    ovtm_untp_vol: Optional[str] = None  # 시간외 단일가 거래량
    ovtm_untp_tr_pbmn: Optional[str] = None  # 시간외 단일가 거래 대금
    ovtm_untp_mxpr: Optional[str] = None  # 시간외 단일가 상한가
    ovtm_untp_llam: Optional[str] = None  # 시간외 단일가 하한가
    ovtm_untp_oprc: Optional[str] = None  # 시간외 단일가 시가2
    ovtm_untp_hgpr: Optional[str] = None  # 시간외 단일가 최고가
    ovtm_untp_lwpr: Optional[str] = None  # 시간외 단일가 최저가
    ovtm_untp_antc_cnpr: Optional[str] = None  # 시간외 단일가 예상 체결가
    ovtm_untp_antc_cntg_vrss: Optional[str] = None  # 시간외 단일가 예상 체결 대비
    ovtm_untp_antc_cntg_vrss_sign: Optional[str] = None  # 시간외 단일가 예상 체결 대비 부호
    ovtm_untp_antc_cntg_ctrt: Optional[str] = None  # 시간외 단일가 예상 체결 대비율
    ovtm_untp_antc_vol: Optional[str] = None  # 시간외 단일가 예상 거래량
    uplm_sign: Optional[str] = None  # 상한 부호
    lslm_sign: Optional[str] = None  # 하한 부호
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    askp: Optional[str] = None  # 매도호가
    bidp: Optional[str] = None  # 매수호가
    acml_vol: Optional[str] = None  # 누적 거래량
    cntg_vol: Optional[str] = None  # 체결 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireViStatus(SQLModel, table=True):
    """Output table for inquire_vi_status"""
    __tablename__ = "kis_inquire_vi_status"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    Output1: Optional[str] = None  # 응답상세
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    vi_cls_code: Optional[str] = None  # VI발동상태
    bsop_date: Optional[str] = None  # 영업 일자
    cntg_vi_hour: Optional[str] = None  # VI발동시간
    vi_cncl_hour: Optional[str] = None  # VI해제시간
    vi_kind_code: Optional[str] = None  # VI종류코드
    vi_prc: Optional[str] = None  # VI발동가격
    vi_stnd_prc: Optional[str] = None  # 정적VI발동기준가격
    vi_dprt: Optional[str] = None  # 정적VI발동괴리율
    vi_dmc_stnd_prc: Optional[str] = None  # 동적VI발동기준가격
    vi_dmc_dprt: Optional[str] = None  # 동적VI발동괴리율
    vi_count: Optional[str] = None  # VI발동횟수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IntgrMargin(SQLModel, table=True):
    """Output table for intgr_margin"""
    __tablename__ = "kis_intgr_margin"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    acmga_rt: Optional[str] = None  # 계좌증거금율
    acmga_pct100_aptm_rson: Optional[str] = None  # 계좌증거금100퍼센트지정사유
    stck_cash_objt_amt: Optional[str] = None  # 주식현금대상금액
    stck_sbst_objt_amt: Optional[str] = None  # 주식대용대상금액
    stck_evlu_objt_amt: Optional[str] = None  # 주식평가대상금액
    stck_ruse_psbl_objt_amt: Optional[str] = None  # 주식재사용가능대상금액
    stck_fund_rpch_chgs_objt_amt: Optional[str] = None  # 주식펀드환매대금대상금액
    stck_fncg_rdpt_objt_atm: Optional[str] = None  # 주식융자상환금대상금액
    bond_ruse_psbl_objt_amt: Optional[str] = None  # 채권재사용가능대상금액
    stck_cash_use_amt: Optional[str] = None  # 주식현금사용금액
    stck_sbst_use_amt: Optional[str] = None  # 주식대용사용금액
    stck_evlu_use_amt: Optional[str] = None  # 주식평가사용금액
    stck_ruse_psbl_amt_use_amt: Optional[str] = None  # 주식재사용가능금사용금액
    stck_fund_rpch_chgs_use_amt: Optional[str] = None  # 주식펀드환매대금사용금액
    stck_fncg_rdpt_amt_use_amt: Optional[str] = None  # 주식융자상환금사용금액
    bond_ruse_psbl_amt_use_amt: Optional[str] = None  # 채권재사용가능금사용금액
    stck_cash_ord_psbl_amt: Optional[str] = None  # 주식현금주문가능금액
    stck_sbst_ord_psbl_amt: Optional[str] = None  # 주식대용주문가능금액
    stck_evlu_ord_psbl_amt: Optional[str] = None  # 주식평가주문가능금액
    stck_ruse_psbl_ord_psbl_amt: Optional[str] = None  # 주식재사용가능주문가능금액
    stck_fund_rpch_ord_psbl_amt: Optional[str] = None  # 주식펀드환매주문가능금액
    bond_ruse_psbl_ord_psbl_amt: Optional[str] = None  # 채권재사용가능주문가능금액
    rcvb_amt: Optional[str] = None  # 미수금액
    stck_loan_grta_ruse_psbl_amt: Optional[str] = None  # 주식대출보증금재사용가능금액
    stck_cash20_max_ord_psbl_amt: Optional[str] = None  # 주식현금20최대주문가능금액
    stck_cash30_max_ord_psbl_amt: Optional[str] = None  # 주식현금30최대주문가능금액
    stck_cash40_max_ord_psbl_amt: Optional[str] = None  # 주식현금40최대주문가능금액
    stck_cash50_max_ord_psbl_amt: Optional[str] = None  # 주식현금50최대주문가능금액
    stck_cash60_max_ord_psbl_amt: Optional[str] = None  # 주식현금60최대주문가능금액
    stck_cash100_max_ord_psbl_amt: Optional[str] = None  # 주식현금100최대주문가능금액
    stck_rsip100_max_ord_psbl_amt: Optional[str] = None  # 주식재사용불가100최대주문가능
    bond_max_ord_psbl_amt: Optional[str] = None  # 채권최대주문가능금액
    stck_fncg45_max_ord_psbl_amt: Optional[str] = None  # 주식융자45최대주문가능금액
    stck_fncg50_max_ord_psbl_amt: Optional[str] = None  # 주식융자50최대주문가능금액
    stck_fncg60_max_ord_psbl_amt: Optional[str] = None  # 주식융자60최대주문가능금액
    stck_fncg70_max_ord_psbl_amt: Optional[str] = None  # 주식융자70최대주문가능금액
    stck_stln_max_ord_psbl_amt: Optional[str] = None  # 주식대주최대주문가능금액
    lmt_amt: Optional[str] = None  # 한도금액
    ovrs_stck_itgr_mgna_dvsn_name: Optional[str] = None  # 해외주식통합증거금구분명
    usd_objt_amt: Optional[str] = None  # 미화대상금액
    usd_use_amt: Optional[str] = None  # 미화사용금액
    usd_ord_psbl_amt: Optional[str] = None  # 미화주문가능금액
    hkd_objt_amt: Optional[str] = None  # 홍콩달러대상금액
    hkd_use_amt: Optional[str] = None  # 홍콩달러사용금액
    hkd_ord_psbl_amt: Optional[str] = None  # 홍콩달러주문가능금액
    jpy_objt_amt: Optional[str] = None  # 엔화대상금액
    jpy_use_amt: Optional[str] = None  # 엔화사용금액
    jpy_ord_psbl_amt: Optional[str] = None  # 엔화주문가능금액
    cny_objt_amt: Optional[str] = None  # 위안화대상금액
    cny_use_amt: Optional[str] = None  # 위안화사용금액
    cny_ord_psbl_amt: Optional[str] = None  # 위안화주문가능금액
    usd_ruse_objt_amt: Optional[str] = None  # 미화재사용대상금액
    usd_ruse_amt: Optional[str] = None  # 미화재사용금액
    usd_ruse_ord_psbl_amt: Optional[str] = None  # 미화재사용주문가능금액
    hkd_ruse_objt_amt: Optional[str] = None  # 홍콩달러재사용대상금액
    hkd_ruse_amt: Optional[str] = None  # 홍콩달러재사용금액
    hkd_ruse_ord_psbl_amt: Optional[str] = None  # 홍콩달러재사용주문가능금액
    jpy_ruse_objt_amt: Optional[str] = None  # 엔화재사용대상금액
    jpy_ruse_amt: Optional[str] = None  # 엔화재사용금액
    jpy_ruse_ord_psbl_amt: Optional[str] = None  # 엔화재사용주문가능금액
    cny_ruse_objt_amt: Optional[str] = None  # 위안화재사용대상금액
    cny_ruse_amt: Optional[str] = None  # 위안화재사용금액
    cny_ruse_ord_psbl_amt: Optional[str] = None  # 위안화재사용주문가능금액
    usd_gnrl_ord_psbl_amt: Optional[str] = None  # 미화일반주문가능금액
    usd_itgr_ord_psbl_amt: Optional[str] = None  # 미화통합주문가능금액
    hkd_gnrl_ord_psbl_amt: Optional[str] = None  # 홍콩달러일반주문가능금액
    hkd_itgr_ord_psbl_amt: Optional[str] = None  # 홍콩달러통합주문가능금액
    jpy_gnrl_ord_psbl_amt: Optional[str] = None  # 엔화일반주문가능금액
    jpy_itgr_ord_psbl_amt: Optional[str] = None  # 엔화통합주문가능금액
    cny_gnrl_ord_psbl_amt: Optional[str] = None  # 위안화일반주문가능금액
    cny_itgr_ord_psbl_amt: Optional[str] = None  # 위안화통합주문가능금액
    stck_itgr_cash20_ord_psbl_amt: Optional[str] = None  # 주식통합현금20주문가능금액
    stck_itgr_cash30_ord_psbl_amt: Optional[str] = None  # 주식통합현금30주문가능금액
    stck_itgr_cash40_ord_psbl_amt: Optional[str] = None  # 주식통합현금40주문가능금액
    stck_itgr_cash50_ord_psbl_amt: Optional[str] = None  # 주식통합현금50주문가능금액
    stck_itgr_cash60_ord_psbl_amt: Optional[str] = None  # 주식통합현금60주문가능금액
    stck_itgr_cash100_ord_psbl_amt: Optional[str] = None  # 주식통합현금100주문가능금액
    stck_itgr_100_ord_psbl_amt: Optional[str] = None  # 주식통합100주문가능금액
    stck_itgr_fncg45_ord_psbl_amt: Optional[str] = None  # 주식통합융자45주문가능금액
    stck_itgr_fncg50_ord_psbl_amt: Optional[str] = None  # 주식통합융자50주문가능금액
    stck_itgr_fncg60_ord_psbl_amt: Optional[str] = None  # 주식통합융자60주문가능금액
    stck_itgr_fncg70_ord_psbl_amt: Optional[str] = None  # 주식통합융자70주문가능금액
    stck_itgr_stln_ord_psbl_amt: Optional[str] = None  # 주식통합대주주문가능금액
    bond_itgr_ord_psbl_amt: Optional[str] = None  # 채권통합주문가능금액
    stck_cash_ovrs_use_amt: Optional[str] = None  # 주식현금해외사용금액
    stck_sbst_ovrs_use_amt: Optional[str] = None  # 주식대용해외사용금액
    stck_evlu_ovrs_use_amt: Optional[str] = None  # 주식평가해외사용금액
    stck_re_use_amt_ovrs_use_amt: Optional[str] = None  # 주식재사용금액해외사용금액
    stck_fund_rpch_ovrs_use_amt: Optional[str] = None  # 주식펀드환매해외사용금액
    stck_fncg_rdpt_ovrs_use_amt: Optional[str] = None  # 주식융자상환해외사용금액
    bond_re_use_ovrs_use_amt: Optional[str] = None  # 채권재사용해외사용금액
    usd_oth_mket_use_amt: Optional[str] = None  # 미화타시장사용금액
    jpy_oth_mket_use_amt: Optional[str] = None  # 엔화타시장사용금액
    cny_oth_mket_use_amt: Optional[str] = None  # 위안화타시장사용금액
    hkd_oth_mket_use_amt: Optional[str] = None  # 홍콩달러타시장사용금액
    usd_re_use_oth_mket_use_amt: Optional[str] = None  # 미화재사용타시장사용금액
    jpy_re_use_oth_mket_use_amt: Optional[str] = None  # 엔화재사용타시장사용금액
    cny_re_use_oth_mket_use_amt: Optional[str] = None  # 위안화재사용타시장사용금액
    hkd_re_use_oth_mket_use_amt: Optional[str] = None  # 홍콩달러재사용타시장사용금액
    hgkg_cny_re_use_amt: Optional[str] = None  # 홍콩위안화재사용금액
    usd_frst_bltn_exrt: Optional[str] = None  # 미국달러최초고시환율
    hkd_frst_bltn_exrt: Optional[str] = None  # 홍콩달러최초고시환율
    jpy_frst_bltn_exrt: Optional[str] = None  # 일본엔화최초고시환율
    cny_frst_bltn_exrt: Optional[str] = None  # 중국위안화최초고시환율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IntstockGrouplist(SQLModel, table=True):
    """Output table for intstock_grouplist"""
    __tablename__ = "kis_intstock_grouplist"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    date: Optional[str] = None  # 일자
    trnm_hour: Optional[str] = None  # 전송 시간
    data_rank: Optional[str] = None  # 데이터 순위
    inter_grp_code: Optional[str] = None  # 관심 그룹 코드
    inter_grp_name: Optional[str] = None  # 관심 그룹 명
    ask_cnt: Optional[str] = None  # 요청 개수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IntstockMultprice(SQLModel, table=True):
    """Output table for intstock_multprice"""
    __tablename__ = "kis_intstock_multprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    kospi_kosdaq_cls_name: Optional[str] = None  # 코스피 코스닥 구분 명
    mrkt_trtm_cls_name: Optional[str] = None  # 시장 조치 구분 명
    hour_cls_code: Optional[str] = None  # 시간 구분 코드
    inter_shrn_iscd: Optional[str] = None  # 관심 단축 종목코드
    inter_kor_isnm: Optional[str] = None  # 관심 한글 종목명
    inter2_prpr: Optional[str] = None  # 관심2 현재가
    inter2_prdy_vrss: Optional[str] = None  # 관심2 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    inter2_oprc: Optional[str] = None  # 관심2 시가
    inter2_hgpr: Optional[str] = None  # 관심2 고가
    inter2_lwpr: Optional[str] = None  # 관심2 저가
    inter2_llam: Optional[str] = None  # 관심2 하한가
    inter2_mxpr: Optional[str] = None  # 관심2 상한가
    inter2_askp: Optional[str] = None  # 관심2 매도호가
    inter2_bidp: Optional[str] = None  # 관심2 매수호가
    seln_rsqn: Optional[str] = None  # 매도 잔량
    shnu_rsqn: Optional[str] = None  # 매수2 잔량
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    inter2_prdy_clpr: Optional[str] = None  # 관심2 전일 종가
    oprc_vrss_hgpr_rate: Optional[str] = None  # 시가 대비 최고가 비율
    intr_antc_cntg_vrss: Optional[str] = None  # 관심 예상 체결 대비
    intr_antc_cntg_vrss_sign: Optional[str] = None  # 관심 예상 체결 대비 부호
    intr_antc_cntg_prdy_ctrt: Optional[str] = None  # 관심 예상 체결 전일 대비율
    intr_antc_vol: Optional[str] = None  # 관심 예상 거래량
    inter2_sdpr: Optional[str] = None  # 관심2 기준가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IntstockStocklistByGroup(SQLModel, table=True):
    """Output table for intstock_stocklist_by_group"""
    __tablename__ = "kis_intstock_stocklist_by_group"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    fid_mrkt_cls_code: Optional[str] = None  # FID 시장 구분 코드
    data_rank: Optional[str] = None  # 데이터 순위
    exch_code: Optional[str] = None  # 거래소코드
    jong_code: Optional[str] = None  # 종목코드
    color_code: Optional[str] = None  # 생상 코드
    memo: Optional[str] = None  # 메모
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    fxdt_ntby_qty: Optional[str] = None  # 기준일 순매수 수량
    cntg_unpr: Optional[str] = None  # 체결단가
    cntg_cls_code: Optional[str] = None  # 체결 구분 코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InvestorProgramTradeToday(SQLModel, table=True):
    """Output table for investor_program_trade_today"""
    __tablename__ = "kis_investor_program_trade_today"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    invr_cls_code: Optional[str] = None  # 투자자코드
    all_seln_qty: Optional[str] = None  # 전체매도수량
    all_seln_amt: Optional[str] = None  # 전체매도대금
    invr_cls_name: Optional[str] = None  # 투자자 구분 명
    all_shnu_qty: Optional[str] = None  # 전체매수수량
    all_shnu_amt: Optional[str] = None  # 전체매수대금
    all_ntby_amt: Optional[str] = None  # 전체순매수대금
    arbt_seln_qty: Optional[str] = None  # 차익매도수량
    all_ntby_qty: Optional[str] = None  # 전체순매수수량
    arbt_shnu_qty: Optional[str] = None  # 차익매수수량
    arbt_ntby_qty: Optional[str] = None  # 차익순매수수량
    arbt_seln_amt: Optional[str] = None  # 차익매도대금
    arbt_shnu_amt: Optional[str] = None  # 차익매수대금
    arbt_ntby_amt: Optional[str] = None  # 차익순매수대금
    nabt_seln_qty: Optional[str] = None  # 비차익매도수량
    nabt_shnu_qty: Optional[str] = None  # 비차익매수수량
    nabt_ntby_qty: Optional[str] = None  # 비차익순매수수량
    nabt_seln_amt: Optional[str] = None  # 비차익매도대금
    nabt_shnu_amt: Optional[str] = None  # 비차익매수대금
    nabt_ntby_amt: Optional[str] = None  # 비차익순매수대금
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InvestorTradeByStockDaily(SQLModel, table=True):
    """Output table for investor_trade_by_stock_daily"""
    __tablename__ = "kis_investor_trade_by_stock_daily"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    prdy_vol: Optional[str] = None  # 전일 거래량
    rprs_mrkt_kor_name: Optional[str] = None  # 대표 시장 한글 명
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_clpr: Optional[str] = None  # 주식 종가
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    stck_oprc: Optional[str] = None  # 주식 시가2
    stck_hgpr: Optional[str] = None  # 주식 최고가
    stck_lwpr: Optional[str] = None  # 주식 최저가
    frgn_ntby_qty: Optional[str] = None  # 외국인 순매수 수량
    frgn_reg_ntby_qty: Optional[str] = None  # 외국인 등록 순매수 수량
    frgn_nreg_ntby_qty: Optional[str] = None  # 외국인 비등록 순매수 수량
    prsn_ntby_qty: Optional[str] = None  # 개인 순매수 수량
    orgn_ntby_qty: Optional[str] = None  # 기관계 순매수 수량
    scrt_ntby_qty: Optional[str] = None  # 증권 순매수 수량
    ivtr_ntby_qty: Optional[str] = None  # 투자신탁 순매수 수량
    pe_fund_ntby_vol: Optional[str] = None  # 사모 펀드 순매수 거래량
    bank_ntby_qty: Optional[str] = None  # 은행 순매수 수량
    insu_ntby_qty: Optional[str] = None  # 보험 순매수 수량
    mrbn_ntby_qty: Optional[str] = None  # 종금 순매수 수량
    fund_ntby_qty: Optional[str] = None  # 기금 순매수 수량
    etc_ntby_qty: Optional[str] = None  # 기타 순매수 수량
    etc_corp_ntby_vol: Optional[str] = None  # 기타 법인 순매수 거래량
    etc_orgt_ntby_vol: Optional[str] = None  # 기타 단체 순매수 거래량
    frgn_reg_ntby_pbmn: Optional[str] = None  # 외국인 등록 순매수 대금
    frgn_ntby_tr_pbmn: Optional[str] = None  # 외국인 순매수 거래 대금
    frgn_nreg_ntby_pbmn: Optional[str] = None  # 외국인 비등록 순매수 대금
    prsn_ntby_tr_pbmn: Optional[str] = None  # 개인 순매수 거래 대금
    orgn_ntby_tr_pbmn: Optional[str] = None  # 기관계 순매수 거래 대금
    scrt_ntby_tr_pbmn: Optional[str] = None  # 증권 순매수 거래 대금
    pe_fund_ntby_tr_pbmn: Optional[str] = None  # 사모 펀드 순매수 거래 대금
    ivtr_ntby_tr_pbmn: Optional[str] = None  # 투자신탁 순매수 거래 대금
    bank_ntby_tr_pbmn: Optional[str] = None  # 은행 순매수 거래 대금
    insu_ntby_tr_pbmn: Optional[str] = None  # 보험 순매수 거래 대금
    mrbn_ntby_tr_pbmn: Optional[str] = None  # 종금 순매수 거래 대금
    fund_ntby_tr_pbmn: Optional[str] = None  # 기금 순매수 거래 대금
    etc_ntby_tr_pbmn: Optional[str] = None  # 기타 순매수 거래 대금
    etc_corp_ntby_tr_pbmn: Optional[str] = None  # 기타 법인 순매수 거래 대금
    etc_orgt_ntby_tr_pbmn: Optional[str] = None  # 기타 단체 순매수 거래 대금
    frgn_seln_vol: Optional[str] = None  # 외국인 매도 거래량
    frgn_shnu_vol: Optional[str] = None  # 외국인 매수2 거래량
    frgn_seln_tr_pbmn: Optional[str] = None  # 외국인 매도 거래 대금
    frgn_shnu_tr_pbmn: Optional[str] = None  # 외국인 매수2 거래 대금
    frgn_reg_askp_qty: Optional[str] = None  # 외국인 등록 매도 수량
    frgn_reg_bidp_qty: Optional[str] = None  # 외국인 등록 매수 수량
    frgn_reg_askp_pbmn: Optional[str] = None  # 외국인 등록 매도 대금
    frgn_reg_bidp_pbmn: Optional[str] = None  # 외국인 등록 매수 대금
    frgn_nreg_askp_qty: Optional[str] = None  # 외국인 비등록 매도 수량
    frgn_nreg_bidp_qty: Optional[str] = None  # 외국인 비등록 매수 수량
    frgn_nreg_askp_pbmn: Optional[str] = None  # 외국인 비등록 매도 대금
    frgn_nreg_bidp_pbmn: Optional[str] = None  # 외국인 비등록 매수 대금
    prsn_seln_vol: Optional[str] = None  # 개인 매도 거래량
    prsn_shnu_vol: Optional[str] = None  # 개인 매수2 거래량
    prsn_seln_tr_pbmn: Optional[str] = None  # 개인 매도 거래 대금
    prsn_shnu_tr_pbmn: Optional[str] = None  # 개인 매수2 거래 대금
    orgn_seln_vol: Optional[str] = None  # 기관계 매도 거래량
    orgn_shnu_vol: Optional[str] = None  # 기관계 매수2 거래량
    orgn_seln_tr_pbmn: Optional[str] = None  # 기관계 매도 거래 대금
    orgn_shnu_tr_pbmn: Optional[str] = None  # 기관계 매수2 거래 대금
    scrt_seln_vol: Optional[str] = None  # 증권 매도 거래량
    scrt_shnu_vol: Optional[str] = None  # 증권 매수2 거래량
    scrt_seln_tr_pbmn: Optional[str] = None  # 증권 매도 거래 대금
    scrt_shnu_tr_pbmn: Optional[str] = None  # 증권 매수2 거래 대금
    ivtr_seln_vol: Optional[str] = None  # 투자신탁 매도 거래량
    ivtr_shnu_vol: Optional[str] = None  # 투자신탁 매수2 거래량
    ivtr_seln_tr_pbmn: Optional[str] = None  # 투자신탁 매도 거래 대금
    ivtr_shnu_tr_pbmn: Optional[str] = None  # 투자신탁 매수2 거래 대금
    pe_fund_seln_tr_pbmn: Optional[str] = None  # 사모 펀드 매도 거래 대금
    pe_fund_seln_vol: Optional[str] = None  # 사모 펀드 매도 거래량
    pe_fund_shnu_tr_pbmn: Optional[str] = None  # 사모 펀드 매수2 거래 대금
    pe_fund_shnu_vol: Optional[str] = None  # 사모 펀드 매수2 거래량
    bank_seln_vol: Optional[str] = None  # 은행 매도 거래량
    bank_shnu_vol: Optional[str] = None  # 은행 매수2 거래량
    bank_seln_tr_pbmn: Optional[str] = None  # 은행 매도 거래 대금
    bank_shnu_tr_pbmn: Optional[str] = None  # 은행 매수2 거래 대금
    insu_seln_vol: Optional[str] = None  # 보험 매도 거래량
    insu_shnu_vol: Optional[str] = None  # 보험 매수2 거래량
    insu_seln_tr_pbmn: Optional[str] = None  # 보험 매도 거래 대금
    insu_shnu_tr_pbmn: Optional[str] = None  # 보험 매수2 거래 대금
    mrbn_seln_vol: Optional[str] = None  # 종금 매도 거래량
    mrbn_shnu_vol: Optional[str] = None  # 종금 매수2 거래량
    mrbn_seln_tr_pbmn: Optional[str] = None  # 종금 매도 거래 대금
    mrbn_shnu_tr_pbmn: Optional[str] = None  # 종금 매수2 거래 대금
    fund_seln_vol: Optional[str] = None  # 기금 매도 거래량
    fund_shnu_vol: Optional[str] = None  # 기금 매수2 거래량
    fund_seln_tr_pbmn: Optional[str] = None  # 기금 매도 거래 대금
    fund_shnu_tr_pbmn: Optional[str] = None  # 기금 매수2 거래 대금
    etc_seln_vol: Optional[str] = None  # 기타 매도 거래량
    etc_shnu_vol: Optional[str] = None  # 기타 매수2 거래량
    etc_seln_tr_pbmn: Optional[str] = None  # 기타 매도 거래 대금
    etc_shnu_tr_pbmn: Optional[str] = None  # 기타 매수2 거래 대금
    etc_orgt_seln_vol: Optional[str] = None  # 기타 단체 매도 거래량
    etc_orgt_shnu_vol: Optional[str] = None  # 기타 단체 매수2 거래량
    etc_orgt_seln_tr_pbmn: Optional[str] = None  # 기타 단체 매도 거래 대금
    etc_orgt_shnu_tr_pbmn: Optional[str] = None  # 기타 단체 매수2 거래 대금
    etc_corp_seln_vol: Optional[str] = None  # 기타 법인 매도 거래량
    etc_corp_shnu_vol: Optional[str] = None  # 기타 법인 매수2 거래량
    etc_corp_seln_tr_pbmn: Optional[str] = None  # 기타 법인 매도 거래 대금
    etc_corp_shnu_tr_pbmn: Optional[str] = None  # 기타 법인 매수2 거래 대금
    bold_yn: Optional[str] = None  # BOLD 여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InvestorTrendEstimate(SQLModel, table=True):
    """Output table for investor_trend_estimate"""
    __tablename__ = "kis_investor_trend_estimate"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bsop_hour_gb: Optional[str] = None  # 입력구분
    frgn_fake_ntby_qty: Optional[str] = None  # 외국인수량(가집계)
    orgn_fake_ntby_qty: Optional[str] = None  # 기관수량(가집계)
    sum_fake_ntby_qty: Optional[str] = None  # 합산수량(가집계)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InvestOpbysec(SQLModel, table=True):
    """Output table for invest_opbysec"""
    __tablename__ = "kis_invest_opbysec"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식영업일자
    stck_shrn_iscd: Optional[str] = None  # 주식단축종목코드
    hts_kor_isnm: Optional[str] = None  # HTS한글종목명
    invt_opnn: Optional[str] = None  # 투자의견
    invt_opnn_cls_code: Optional[str] = None  # 투자의견구분코드
    rgbf_invt_opnn: Optional[str] = None  # 직전투자의견
    rgbf_invt_opnn_cls_code: Optional[str] = None  # 직전투자의견구분코드
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    hts_goal_prc: Optional[str] = None  # HTS목표가격
    stck_prdy_clpr: Optional[str] = None  # 주식전일종가
    stft_esdg: Optional[str] = None  # 주식선물괴리도
    dprt: Optional[str] = None  # 괴리율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InvestOpinion(SQLModel, table=True):
    """Output table for invest_opinion"""
    __tablename__ = "kis_invest_opinion"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식영업일자
    invt_opnn: Optional[str] = None  # 투자의견
    invt_opnn_cls_code: Optional[str] = None  # 투자의견구분코드
    rgbf_invt_opnn: Optional[str] = None  # 직전투자의견
    rgbf_invt_opnn_cls_code: Optional[str] = None  # 직전투자의견구분코드
    hts_goal_prc: Optional[str] = None  # HTS목표가격
    stck_prdy_clpr: Optional[str] = None  # 주식전일종가
    stck_nday_esdg: Optional[str] = None  # 주식N일괴리도
    nday_dprt: Optional[str] = None  # N일괴리율
    stft_esdg: Optional[str] = None  # 주식선물괴리도
    dprt: Optional[str] = None  # 괴리율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoBonusIssue(SQLModel, table=True):
    """Output table for ksdinfo_bonus_issue"""
    __tablename__ = "kis_ksdinfo_bonus_issue"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    record_date: Optional[str] = None  # 기준일
    sht_cd: Optional[str] = None  # 종목코드
    fix_rate: Optional[str] = None  # 확정배정율
    odd_rec_price: Optional[str] = None  # 단주기준가
    right_dt: Optional[str] = None  # 권리락일
    odd_pay_dt: Optional[str] = None  # 단주대금지급일
    list_date: Optional[str] = None  # 상장/등록일
    tot_issue_stk_qty: Optional[str] = None  # 발행주식
    issue_stk_qty: Optional[str] = None  # 발행할주식
    stk_kind: Optional[str] = None  # 주식종류
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoCapDcrs(SQLModel, table=True):
    """Output table for ksdinfo_cap_dcrs"""
    __tablename__ = "kis_ksdinfo_cap_dcrs"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    record_date: Optional[str] = None  # 기준일
    sht_cd: Optional[str] = None  # 종목코드
    stk_kind: Optional[str] = None  # 주식종류
    reduce_cap_type: Optional[str] = None  # 감자구분
    reduce_cap_rate: Optional[str] = None  # 감자배정율
    comp_way: Optional[str] = None  # 계산방법
    td_stop_dt: Optional[str] = None  # 매매거래정지기간
    list_dt: Optional[str] = None  # 상장/등록일
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoDividend(SQLModel, table=True):
    """Output table for ksdinfo_dividend"""
    __tablename__ = "kis_ksdinfo_dividend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    record_date: Optional[str] = None  # 기준일
    sht_cd: Optional[str] = None  # 종목코드
    divi_kind: Optional[str] = None  # 배당종류
    face_val: Optional[str] = None  # 액면가
    per_sto_divi_amt: Optional[str] = None  # 현금배당금
    divi_rate: Optional[str] = None  # 현금배당률(%)
    stk_divi_rate: Optional[str] = None  # 주식배당률(%)
    divi_pay_dt: Optional[str] = None  # 배당금지급일
    stk_div_pay_dt: Optional[str] = None  # 주식배당지급일
    odd_pay_dt: Optional[str] = None  # 단주대금지급일
    stk_kind: Optional[str] = None  # 주식종류
    high_divi_gb: Optional[str] = None  # 고배당종목여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoForfeit(SQLModel, table=True):
    """Output table for ksdinfo_forfeit"""
    __tablename__ = "kis_ksdinfo_forfeit"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    record_date: Optional[str] = None  # 기준일
    sht_cd: Optional[str] = None  # 종목코드
    subscr_dt: Optional[str] = None  # 청약일
    subscr_price: Optional[str] = None  # 공모가
    subscr_stk_qty: Optional[str] = None  # 공모주식수
    refund_dt: Optional[str] = None  # 환불일
    list_dt: Optional[str] = None  # 상장/등록일
    lead_mgr: Optional[str] = None  # 주간사
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoListInfo(SQLModel, table=True):
    """Output table for ksdinfo_list_info"""
    __tablename__ = "kis_ksdinfo_list_info"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    list_dt: Optional[str] = None  # 상장/등록일
    sht_cd: Optional[str] = None  # 종목코드
    stk_kind: Optional[str] = None  # 주식종류
    issue_type: Optional[str] = None  # 사유
    issue_stk_qty: Optional[str] = None  # 상장주식수
    tot_issue_stk_qty: Optional[str] = None  # 총발행주식수
    issue_price: Optional[str] = None  # 발행가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoMandDeposit(SQLModel, table=True):
    """Output table for ksdinfo_mand_deposit"""
    __tablename__ = "kis_ksdinfo_mand_deposit"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    sht_cd: Optional[str] = None  # 종목코드
    stk_qty: Optional[str] = None  # 주식수
    depo_date: Optional[str] = None  # 예치일
    depo_reason: Optional[str] = None  # 사유
    tot_issue_qty_per_rate: Optional[str] = None  # 총발행주식수대비비율(%)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoMergerSplit(SQLModel, table=True):
    """Output table for ksdinfo_merger_split"""
    __tablename__ = "kis_ksdinfo_merger_split"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    record_date: Optional[str] = None  # 기준일
    sht_cd: Optional[str] = None  # 종목코드
    opp_cust_cd: Optional[str] = None  # 피합병(피분할)회사코드
    opp_cust_nm: Optional[str] = None  # 피합병(피분할)회사명
    cust_cd: Optional[str] = None  # 합병(분할)회사코드
    cust_nm: Optional[str] = None  # 합병(분할)회사명
    merge_type: Optional[str] = None  # 합병사유
    merge_rate: Optional[str] = None  # 비율
    td_stop_dt: Optional[str] = None  # 매매거래정지기간
    list_dt: Optional[str] = None  # 상장/등록일
    odd_amt_pay_dt: Optional[str] = None  # 단주대금지급일
    tot_issue_stk_qty: Optional[str] = None  # 발행주식
    issue_stk_qty: Optional[str] = None  # 발행할주식
    seq: Optional[str] = None  # 연번
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoPaidinCapin(SQLModel, table=True):
    """Output table for ksdinfo_paidin_capin"""
    __tablename__ = "kis_ksdinfo_paidin_capin"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    record_date: Optional[str] = None  # 기준일
    sht_cd: Optional[str] = None  # 종목코드
    tot_issue_stk_qty: Optional[str] = None  # 발행주식
    issue_stk_qty: Optional[str] = None  # 발행할주식
    fix_rate: Optional[str] = None  # 확정배정율
    disc_rate: Optional[str] = None  # 할인율
    fix_price: Optional[str] = None  # 발행예정가
    right_dt: Optional[str] = None  # 권리락일
    sub_term_ft: Optional[str] = None  # 청약기간
    sub_term: Optional[str] = None  # 청약기간
    list_date: Optional[str] = None  # 상장/등록일
    stk_kind: Optional[str] = None  # 주식종류
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoPubOffer(SQLModel, table=True):
    """Output table for ksdinfo_pub_offer"""
    __tablename__ = "kis_ksdinfo_pub_offer"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    record_date: Optional[str] = None  # 기준일
    sht_cd: Optional[str] = None  # 종목코드
    fix_subscr_pri: Optional[str] = None  # 공모가
    face_value: Optional[str] = None  # 액면가
    subscr_dt: Optional[str] = None  # 청약기간
    pay_dt: Optional[str] = None  # 납입일
    refund_dt: Optional[str] = None  # 환불일
    list_dt: Optional[str] = None  # 상장/등록일
    lead_mgr: Optional[str] = None  # 주간사
    pub_bf_cap: Optional[str] = None  # 공모전자본금
    pub_af_cap: Optional[str] = None  # 공모후자본금
    assign_stk_qty: Optional[str] = None  # 당사배정물량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoPurreq(SQLModel, table=True):
    """Output table for ksdinfo_purreq"""
    __tablename__ = "kis_ksdinfo_purreq"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    record_date: Optional[str] = None  # 기준일
    sht_cd: Optional[str] = None  # 종목코드
    stk_kind: Optional[str] = None  # 주식종류
    opp_opi_rcpt_term: Optional[str] = None  # 반대의사접수시한
    buy_req_rcpt_term: Optional[str] = None  # 매수청구접수시한
    buy_req_price: Optional[str] = None  # 매수청구가격
    buy_amt_pay_dt: Optional[str] = None  # 매수대금지급일
    meet_dt: Optional[str] = None  # 주총일
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoRevSplit(SQLModel, table=True):
    """Output table for ksdinfo_rev_split"""
    __tablename__ = "kis_ksdinfo_rev_split"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    record_date: Optional[str] = None  # 기준일
    sht_cd: Optional[str] = None  # 종목코드
    inter_bf_face_amt: Optional[str] = None  # 변경전액면가
    inter_af_face_amt: Optional[str] = None  # 변경후액면가
    td_stop_dt: Optional[str] = None  # 매매거래정지기간
    list_dt: Optional[str] = None  # 상장/등록일
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KsdinfoSharehldMeet(SQLModel, table=True):
    """Output table for ksdinfo_sharehld_meet"""
    __tablename__ = "kis_ksdinfo_sharehld_meet"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    record_date: Optional[str] = None  # 기준일
    sht_cd: Optional[str] = None  # 종목코드
    gen_meet_dt: Optional[str] = None  # 주총일자
    gen_meet_type: Optional[str] = None  # 주총사유
    agenda: Optional[str] = None  # 주총의안
    vote_tot_qty: Optional[str] = None  # 의결권주식총수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class LendableByCompany(SQLModel, table=True):
    """Output table for lendable_by_company"""
    __tablename__ = "kis_lendable_by_company"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pdno: Optional[str] = None  # 상품번호
    papr: Optional[str] = None  # 액면가
    bfdy_clpr: Optional[str] = None  # 전일종가
    sbst_prvs: Optional[str] = None  # 대용가
    lmt_qty1: Optional[str] = None  # 한도수량1
    use_qty1: Optional[str] = None  # 사용수량1
    trad_psbl_qty2: Optional[str] = None  # 매매가능수량2
    rght_type_cd: Optional[str] = None  # 권리유형코드
    bass_dt: Optional[str] = None  # 기준일자
    psbl_yn: Optional[str] = None  # 가능여부
    tot_stup_lmt_qty: Optional[str] = None  # 총설정한도수량
    brch_lmt_qty: Optional[str] = None  # 지점한도수량
    rqst_psbl_qty: Optional[str] = None  # 신청가능수량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MarketCap(SQLModel, table=True):
    """Output table for market_cap"""
    __tablename__ = "kis_market_cap"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태정보
    crec: Optional[str] = None  # 현재조회종목수
    trec: Optional[str] = None  # 전체조회종목수
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    tvol: Optional[str] = None  # 거래량
    shar: Optional[str] = None  # 상장주식수
    tomv: Optional[str] = None  # 시가총액
    grav: Optional[str] = None  # 비중
    rank: Optional[str] = None  # 순위
    ename: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    tamt: Optional[str] = None  # 거래대금
    mcap: Optional[str] = None  # 시가총액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MarketStatusKrx(SQLModel, table=True):
    """Output table for market_status_krx"""
    __tablename__ = "kis_market_status_krx"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    trht_yn: Optional[str] = None  # 거래정지여부
    tr_susp_reas_cntt: Optional[str] = None  # 거래정지사유내용
    mkop_cls_code: Optional[str] = None  # 장운영구분코드
    antc_mkop_cls_code: Optional[str] = None  # 예상장운영구분코드
    mrkt_trtm_cls_code: Optional[str] = None  # 임의연장구분코드
    divi_app_cls_code: Optional[str] = None  # 동시호가배분처리구분코드
    iscd_stat_cls_code: Optional[str] = None  # 종목상태구분코드
    vi_cls_code: Optional[str] = None  # VI적용구분코드
    ovtm_vi_cls_code: Optional[str] = None  # 시간외단일가VI적용구분코드
    EXCH_CLS_CODE: Optional[str] = None  # 거래소구분코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MarketStatusNxt(SQLModel, table=True):
    """Output table for market_status_nxt"""
    __tablename__ = "kis_market_status_nxt"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 종목코드
    TRHT_YN: Optional[str] = None  # 거래정지 여부
    TR_SUSP_REAS_CNTT: Optional[str] = None  # 거래 정지 사유 내용
    MKOP_CLS_CODE: Optional[str] = None  # 장운영 구분 코드
    ANTC_MKOP_CLS_CODE: Optional[str] = None  # 예상 장운영 구분 코드
    MRKT_TRTM_CLS_CODE: Optional[str] = None  # 임의연장구분코드
    DIVI_APP_CLS_CODE: Optional[str] = None  # 동시호가배분처리구분코드
    ISCD_STAT_CLS_CODE: Optional[str] = None  # 종목상태구분코드
    VI_CLS_CODE: Optional[str] = None  # VI적용구분코드
    OVTM_VI_CLS_CODE: Optional[str] = None  # 시간외단일가VI적용구분코드
    EXCH_CLS_CODE: Optional[str] = None  # 거래소 구분코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MarketStatusTotal(SQLModel, table=True):
    """Output table for market_status_total"""
    __tablename__ = "kis_market_status_total"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    TRHT_YN: Optional[str] = None  # 거래정지 여부
    TR_SUSP_REAS_CNTT: Optional[str] = None  # 거래 정지 사유 내용
    MKOP_CLS_CODE: Optional[str] = None  # 장운영 구분 코드
    ANTC_MKOP_CLS_CODE: Optional[str] = None  # 예상 장운영 구분 코드
    MRKT_TRTM_CLS_CODE: Optional[str] = None  # 임의연장구분코드
    DIVI_APP_CLS_CODE: Optional[str] = None  # 동시호가배분처리구분코드
    ISCD_STAT_CLS_CODE: Optional[str] = None  # 종목상태구분코드
    VI_CLS_CODE: Optional[str] = None  # VI적용구분코드
    OVTM_VI_CLS_CODE: Optional[str] = None  # 시간외단일가VI적용구분코드
    EXCH_CLS_CODE: Optional[str] = None  # 거래소 구분코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MarketTime(SQLModel, table=True):
    """Output table for market_time"""
    __tablename__ = "kis_market_time"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    fm_pdgr_cd: Optional[str] = None  # FM상품군코드
    fm_pdgr_name: Optional[str] = None  # FM상품군명
    fm_excg_cd: Optional[str] = None  # FM거래소코드
    fm_excg_name: Optional[str] = None  # FM거래소명
    fuop_dvsn_name: Optional[str] = None  # 선물옵션구분명
    fm_clas_cd: Optional[str] = None  # FM클래스코드
    fm_clas_name: Optional[str] = None  # FM클래스명
    am_mkmn_strt_tmd: Optional[str] = None  # 오전장운영시작시각
    am_mkmn_end_tmd: Optional[str] = None  # 오전장운영종료시각
    pm_mkmn_strt_tmd: Optional[str] = None  # 오후장운영시작시각
    pm_mkmn_end_tmd: Optional[str] = None  # 오후장운영종료시각
    mkmn_nxdy_strt_tmd: Optional[str] = None  # 장운영익일시작시각
    mkmn_nxdy_end_tmd: Optional[str] = None  # 장운영익일종료시각
    base_mket_strt_tmd: Optional[str] = None  # 기본시장시작시각
    base_mket_end_tmd: Optional[str] = None  # 기본시장종료시각
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MarketValue(SQLModel, table=True):
    """Output table for market_value"""
    __tablename__ = "kis_market_value"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    data_rank: Optional[str] = None  # 데이터 순위
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    per: Optional[str] = None  # PER
    pbr: Optional[str] = None  # PBR
    pcr: Optional[str] = None  # PCR
    psr: Optional[str] = None  # PSR
    eps: Optional[str] = None  # EPS
    eva: Optional[str] = None  # EVA
    ebitda: Optional[str] = None  # EBITDA
    pv_div_ebitda: Optional[str] = None  # PV DIV EBITDA
    ebitda_div_fnnc_expn: Optional[str] = None  # EBITDA DIV 금융비용
    stac_month: Optional[str] = None  # 결산 월
    stac_month_cls_code: Optional[str] = None  # 결산 월 구분 코드
    iqry_csnu: Optional[str] = None  # 조회 건수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MemberKrx(SQLModel, table=True):
    """Output table for member_krx"""
    __tablename__ = "kis_member_krx"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    seln2_mbcr_name1: Optional[str] = None  # 매도2회원사명1
    seln2_mbcr_name2: Optional[str] = None  # 매도2회원사명2
    seln2_mbcr_name3: Optional[str] = None  # 매도2회원사명3
    seln2_mbcr_name4: Optional[str] = None  # 매도2회원사명4
    seln2_mbcr_name5: Optional[str] = None  # 매도2회원사명5
    byov_mbcr_name1: Optional[str] = None  # 매수회원사명1
    byov_mbcr_name2: Optional[str] = None  # 매수회원사명2
    byov_mbcr_name3: Optional[str] = None  # 매수회원사명3
    byov_mbcr_name4: Optional[str] = None  # 매수회원사명4
    byov_mbcr_name5: Optional[str] = None  # 매수회원사명5
    total_seln_qty1: Optional[str] = None  # 총매도수량1
    total_seln_qty2: Optional[str] = None  # 총매도수량2
    total_seln_qty3: Optional[str] = None  # 총매도수량3
    total_seln_qty4: Optional[str] = None  # 총매도수량4
    total_seln_qty5: Optional[str] = None  # 총매도수량5
    total_shnu_qty1: Optional[str] = None  # 총매수2수량1
    total_shnu_qty2: Optional[str] = None  # 총매수2수량2
    total_shnu_qty3: Optional[str] = None  # 총매수2수량3
    total_shnu_qty4: Optional[str] = None  # 총매수2수량4
    total_shnu_qty5: Optional[str] = None  # 총매수2수량5
    seln_mbcr_glob_yn_1: Optional[str] = None  # 매도거래원구분1
    seln_mbcr_glob_yn_2: Optional[str] = None  # 매도거래원구분2
    seln_mbcr_glob_yn_3: Optional[str] = None  # 매도거래원구분3
    seln_mbcr_glob_yn_4: Optional[str] = None  # 매도거래원구분4
    seln_mbcr_glob_yn_5: Optional[str] = None  # 매도거래원구분5
    shnu_mbcr_glob_yn_1: Optional[str] = None  # 매수거래원구분1
    shnu_mbcr_glob_yn_2: Optional[str] = None  # 매수거래원구분2
    shnu_mbcr_glob_yn_3: Optional[str] = None  # 매수거래원구분3
    shnu_mbcr_glob_yn_4: Optional[str] = None  # 매수거래원구분4
    shnu_mbcr_glob_yn_5: Optional[str] = None  # 매수거래원구분5
    seln_mbcr_no1: Optional[str] = None  # 매도거래원코드1
    seln_mbcr_no2: Optional[str] = None  # 매도거래원코드2
    seln_mbcr_no3: Optional[str] = None  # 매도거래원코드3
    seln_mbcr_no4: Optional[str] = None  # 매도거래원코드4
    seln_mbcr_no5: Optional[str] = None  # 매도거래원코드5
    shnu_mbcr_no1: Optional[str] = None  # 매수거래원코드1
    shnu_mbcr_no2: Optional[str] = None  # 매수거래원코드2
    shnu_mbcr_no3: Optional[str] = None  # 매수거래원코드3
    shnu_mbcr_no4: Optional[str] = None  # 매수거래원코드4
    shnu_mbcr_no5: Optional[str] = None  # 매수거래원코드5
    seln_mbcr_rlim1: Optional[str] = None  # 매도회원사비중1
    seln_mbcr_rlim2: Optional[str] = None  # 매도회원사비중2
    seln_mbcr_rlim3: Optional[str] = None  # 매도회원사비중3
    seln_mbcr_rlim4: Optional[str] = None  # 매도회원사비중4
    seln_mbcr_rlim5: Optional[str] = None  # 매도회원사비중5
    shnu_mbcr_rlim1: Optional[str] = None  # 매수2회원사비중1
    shnu_mbcr_rlim2: Optional[str] = None  # 매수2회원사비중2
    shnu_mbcr_rlim3: Optional[str] = None  # 매수2회원사비중3
    shnu_mbcr_rlim4: Optional[str] = None  # 매수2회원사비중4
    shnu_mbcr_rlim5: Optional[str] = None  # 매수2회원사비중5
    seln_qty_icdc1: Optional[str] = None  # 매도수량증감1
    seln_qty_icdc2: Optional[str] = None  # 매도수량증감2
    seln_qty_icdc3: Optional[str] = None  # 매도수량증감3
    seln_qty_icdc4: Optional[str] = None  # 매도수량증감4
    seln_qty_icdc5: Optional[str] = None  # 매도수량증감5
    shnu_qty_icdc1: Optional[str] = None  # 매수2수량증감1
    shnu_qty_icdc2: Optional[str] = None  # 매수2수량증감2
    shnu_qty_icdc3: Optional[str] = None  # 매수2수량증감3
    shnu_qty_icdc4: Optional[str] = None  # 매수2수량증감4
    shnu_qty_icdc5: Optional[str] = None  # 매수2수량증감5
    glob_total_seln_qty: Optional[str] = None  # 외국계총매도수량
    glob_total_shnu_qty: Optional[str] = None  # 외국계총매수2수량
    glob_total_seln_qty_icdc: Optional[str] = None  # 외국계총매도수량증감
    glob_total_shnu_qty_icdc: Optional[str] = None  # 외국계총매수2수량증감
    glob_ntby_qty: Optional[str] = None  # 외국계순매수수량
    glob_seln_rlim: Optional[str] = None  # 외국계매도비중
    glob_shnu_rlim: Optional[str] = None  # 외국계매수2비중
    seln2_mbcr_eng_name1: Optional[str] = None  # 매도2영문회원사명1
    seln2_mbcr_eng_name2: Optional[str] = None  # 매도2영문회원사명2
    seln2_mbcr_eng_name3: Optional[str] = None  # 매도2영문회원사명3
    seln2_mbcr_eng_name4: Optional[str] = None  # 매도2영문회원사명4
    seln2_mbcr_eng_name5: Optional[str] = None  # 매도2영문회원사명5
    byov_mbcr_eng_name1: Optional[str] = None  # 매수영문회원사명1
    byov_mbcr_eng_name2: Optional[str] = None  # 매수영문회원사명2
    byov_mbcr_eng_name3: Optional[str] = None  # 매수영문회원사명3
    byov_mbcr_eng_name4: Optional[str] = None  # 매수영문회원사명4
    byov_mbcr_eng_name5: Optional[str] = None  # 매수영문회원사명5
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MemberNxt(SQLModel, table=True):
    """Output table for member_nxt"""
    __tablename__ = "kis_member_nxt"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권 단축 종목코드
    SELN2_MBCR_NAME1: Optional[str] = None  # 매도2 회원사명1
    SELN2_MBCR_NAME2: Optional[str] = None  # 매도2 회원사명2
    SELN2_MBCR_NAME3: Optional[str] = None  # 매도2 회원사명3
    SELN2_MBCR_NAME4: Optional[str] = None  # 매도2 회원사명4
    SELN2_MBCR_NAME5: Optional[str] = None  # 매도2 회원사명5
    BYOV_MBCR_NAME1: Optional[str] = None  # 매수 회원사명1
    BYOV_MBCR_NAME2: Optional[str] = None  # 매수 회원사명2
    BYOV_MBCR_NAME3: Optional[str] = None  # 매수 회원사명3
    BYOV_MBCR_NAME4: Optional[str] = None  # 매수 회원사명4
    BYOV_MBCR_NAME5: Optional[str] = None  # 매수 회원사명5
    TOTAL_SELN_QTY1: Optional[str] = None  # 총 매도 수량1
    TOTAL_SELN_QTY2: Optional[str] = None  # 총 매도 수량2
    TOTAL_SELN_QTY3: Optional[str] = None  # 총 매도 수량3
    TOTAL_SELN_QTY4: Optional[str] = None  # 총 매도 수량4
    TOTAL_SELN_QTY5: Optional[str] = None  # 총 매도 수량5
    TOTAL_SHNU_QTY1: Optional[str] = None  # 총 매수2 수량1
    TOTAL_SHNU_QTY2: Optional[str] = None  # 총 매수2 수량2
    TOTAL_SHNU_QTY3: Optional[str] = None  # 총 매수2 수량3
    TOTAL_SHNU_QTY4: Optional[str] = None  # 총 매수2 수량4
    TOTAL_SHNU_QTY5: Optional[str] = None  # 총 매수2 수량5
    SELN_MBCR_GLOB_YN_1: Optional[str] = None  # 매도거래원구분1
    SELN_MBCR_GLOB_YN_2: Optional[str] = None  # 매도거래원구분2
    SELN_MBCR_GLOB_YN_3: Optional[str] = None  # 매도거래원구분3
    SELN_MBCR_GLOB_YN_4: Optional[str] = None  # 매도거래원구분4
    SELN_MBCR_GLOB_YN_5: Optional[str] = None  # 매도거래원구분5
    SHNU_MBCR_GLOB_YN_1: Optional[str] = None  # 매수거래원구분1
    SHNU_MBCR_GLOB_YN_2: Optional[str] = None  # 매수거래원구분2
    SHNU_MBCR_GLOB_YN_3: Optional[str] = None  # 매수거래원구분3
    SHNU_MBCR_GLOB_YN_4: Optional[str] = None  # 매수거래원구분4
    SHNU_MBCR_GLOB_YN_5: Optional[str] = None  # 매수거래원구분5
    SELN_MBCR_NO1: Optional[str] = None  # 매도거래원코드1
    SELN_MBCR_NO2: Optional[str] = None  # 매도거래원코드2
    SELN_MBCR_NO3: Optional[str] = None  # 매도거래원코드3
    SELN_MBCR_NO4: Optional[str] = None  # 매도거래원코드4
    SELN_MBCR_NO5: Optional[str] = None  # 매도거래원코드5
    SHNU_MBCR_NO1: Optional[str] = None  # 매수거래원코드1
    SHNU_MBCR_NO2: Optional[str] = None  # 매수거래원코드2
    SHNU_MBCR_NO3: Optional[str] = None  # 매수거래원코드3
    SHNU_MBCR_NO4: Optional[str] = None  # 매수거래원코드4
    SHNU_MBCR_NO5: Optional[str] = None  # 매수거래원코드5
    SELN_MBCR_RLIM1: Optional[str] = None  # 매도 회원사 비중1
    SELN_MBCR_RLIM2: Optional[str] = None  # 매도 회원사 비중2
    SELN_MBCR_RLIM3: Optional[str] = None  # 매도 회원사 비중3
    SELN_MBCR_RLIM4: Optional[str] = None  # 매도 회원사 비중4
    SELN_MBCR_RLIM5: Optional[str] = None  # 매도 회원사 비중5
    SHNU_MBCR_RLIM1: Optional[str] = None  # 매수2 회원사 비중1
    SHNU_MBCR_RLIM2: Optional[str] = None  # 매수2 회원사 비중2
    SHNU_MBCR_RLIM3: Optional[str] = None  # 매수2 회원사 비중3
    SHNU_MBCR_RLIM4: Optional[str] = None  # 매수2 회원사 비중4
    SHNU_MBCR_RLIM5: Optional[str] = None  # 매수2 회원사 비중5
    SELN_QTY_ICDC1: Optional[str] = None  # 매도 수량 증감1
    SELN_QTY_ICDC2: Optional[str] = None  # 매도 수량 증감2
    SELN_QTY_ICDC3: Optional[str] = None  # 매도 수량 증감3
    SELN_QTY_ICDC4: Optional[str] = None  # 매도 수량 증감4
    SELN_QTY_ICDC5: Optional[str] = None  # 매도 수량 증감5
    SHNU_QTY_ICDC1: Optional[str] = None  # 매수2 수량 증감1
    SHNU_QTY_ICDC2: Optional[str] = None  # 매수2 수량 증감2
    SHNU_QTY_ICDC3: Optional[str] = None  # 매수2 수량 증감3
    SHNU_QTY_ICDC4: Optional[str] = None  # 매수2 수량 증감4
    SHNU_QTY_ICDC5: Optional[str] = None  # 매수2 수량 증감5
    GLOB_TOTAL_SELN_QTY: Optional[str] = None  # 외국계 총 매도 수량
    GLOB_TOTAL_SHNU_QTY: Optional[str] = None  # 외국계 총 매수2 수량
    GLOB_TOTAL_SELN_QTY_ICDC: Optional[str] = None  # 외국계 총 매도 수량 증감
    GLOB_TOTAL_SHNU_QTY_ICDC: Optional[str] = None  # 외국계 총 매수2 수량 증감
    GLOB_NTBY_QTY: Optional[str] = None  # 외국계 순매수 수량
    GLOB_SELN_RLIM: Optional[str] = None  # 외국계 매도 비중
    GLOB_SHNU_RLIM: Optional[str] = None  # 외국계 매수2 비중
    SELN2_MBCR_ENG_NAME1: Optional[str] = None  # 매도2 영문회원사명1
    SELN2_MBCR_ENG_NAME2: Optional[str] = None  # 매도2 영문회원사명2
    SELN2_MBCR_ENG_NAME3: Optional[str] = None  # 매도2 영문회원사명3
    SELN2_MBCR_ENG_NAME4: Optional[str] = None  # 매도2 영문회원사명4
    SELN2_MBCR_ENG_NAME5: Optional[str] = None  # 매도2 영문회원사명5
    BYOV_MBCR_ENG_NAME1: Optional[str] = None  # 매수 영문회원사명1
    BYOV_MBCR_ENG_NAME2: Optional[str] = None  # 매수 영문회원사명2
    BYOV_MBCR_ENG_NAME3: Optional[str] = None  # 매수 영문회원사명3
    BYOV_MBCR_ENG_NAME4: Optional[str] = None  # 매수 영문회원사명4
    BYOV_MBCR_ENG_NAME5: Optional[str] = None  # 매수 영문회원사명5
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MemberTotal(SQLModel, table=True):
    """Output table for member_total"""
    __tablename__ = "kis_member_total"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권 단축 종목코드
    SELN2_MBCR_NAME1: Optional[str] = None  # 매도2 회원사명1
    SELN2_MBCR_NAME2: Optional[str] = None  # 매도2 회원사명2
    SELN2_MBCR_NAME3: Optional[str] = None  # 매도2 회원사명3
    SELN2_MBCR_NAME4: Optional[str] = None  # 매도2 회원사명4
    SELN2_MBCR_NAME5: Optional[str] = None  # 매도2 회원사명5
    BYOV_MBCR_NAME1: Optional[str] = None  # 매수 회원사명1
    BYOV_MBCR_NAME2: Optional[str] = None  # 매수 회원사명2
    BYOV_MBCR_NAME3: Optional[str] = None  # 매수 회원사명3
    BYOV_MBCR_NAME4: Optional[str] = None  # 매수 회원사명4
    BYOV_MBCR_NAME5: Optional[str] = None  # 매수 회원사명5
    TOTAL_SELN_QTY1: Optional[str] = None  # 총 매도 수량1
    TOTAL_SELN_QTY2: Optional[str] = None  # 총 매도 수량2
    TOTAL_SELN_QTY3: Optional[str] = None  # 총 매도 수량3
    TOTAL_SELN_QTY4: Optional[str] = None  # 총 매도 수량4
    TOTAL_SELN_QTY5: Optional[str] = None  # 총 매도 수량5
    TOTAL_SHNU_QTY1: Optional[str] = None  # 총 매수2 수량1
    TOTAL_SHNU_QTY2: Optional[str] = None  # 총 매수2 수량2
    TOTAL_SHNU_QTY3: Optional[str] = None  # 총 매수2 수량3
    TOTAL_SHNU_QTY4: Optional[str] = None  # 총 매수2 수량4
    TOTAL_SHNU_QTY5: Optional[str] = None  # 총 매수2 수량5
    SELN_MBCR_GLOB_YN_1: Optional[str] = None  # 매도거래원구분1
    SELN_MBCR_GLOB_YN_2: Optional[str] = None  # 매도거래원구분2
    SELN_MBCR_GLOB_YN_3: Optional[str] = None  # 매도거래원구분3
    SELN_MBCR_GLOB_YN_4: Optional[str] = None  # 매도거래원구분4
    SELN_MBCR_GLOB_YN_5: Optional[str] = None  # 매도거래원구분5
    SHNU_MBCR_GLOB_YN_1: Optional[str] = None  # 매수거래원구분1
    SHNU_MBCR_GLOB_YN_2: Optional[str] = None  # 매수거래원구분2
    SHNU_MBCR_GLOB_YN_3: Optional[str] = None  # 매수거래원구분3
    SHNU_MBCR_GLOB_YN_4: Optional[str] = None  # 매수거래원구분4
    SHNU_MBCR_GLOB_YN_5: Optional[str] = None  # 매수거래원구분5
    SELN_MBCR_NO1: Optional[str] = None  # 매도거래원코드1
    SELN_MBCR_NO2: Optional[str] = None  # 매도거래원코드2
    SELN_MBCR_NO3: Optional[str] = None  # 매도거래원코드3
    SELN_MBCR_NO4: Optional[str] = None  # 매도거래원코드4
    SELN_MBCR_NO5: Optional[str] = None  # 매도거래원코드5
    SHNU_MBCR_NO1: Optional[str] = None  # 매수거래원코드1
    SHNU_MBCR_NO2: Optional[str] = None  # 매수거래원코드2
    SHNU_MBCR_NO3: Optional[str] = None  # 매수거래원코드3
    SHNU_MBCR_NO4: Optional[str] = None  # 매수거래원코드4
    SHNU_MBCR_NO5: Optional[str] = None  # 매수거래원코드5
    SELN_MBCR_RLIM1: Optional[str] = None  # 매도 회원사 비중1
    SELN_MBCR_RLIM2: Optional[str] = None  # 매도 회원사 비중2
    SELN_MBCR_RLIM3: Optional[str] = None  # 매도 회원사 비중3
    SELN_MBCR_RLIM4: Optional[str] = None  # 매도 회원사 비중4
    SELN_MBCR_RLIM5: Optional[str] = None  # 매도 회원사 비중5
    SHNU_MBCR_RLIM1: Optional[str] = None  # 매수2 회원사 비중1
    SHNU_MBCR_RLIM2: Optional[str] = None  # 매수2 회원사 비중2
    SHNU_MBCR_RLIM3: Optional[str] = None  # 매수2 회원사 비중3
    SHNU_MBCR_RLIM4: Optional[str] = None  # 매수2 회원사 비중4
    SHNU_MBCR_RLIM5: Optional[str] = None  # 매수2 회원사 비중5
    SELN_QTY_ICDC1: Optional[str] = None  # 매도 수량 증감1
    SELN_QTY_ICDC2: Optional[str] = None  # 매도 수량 증감2
    SELN_QTY_ICDC3: Optional[str] = None  # 매도 수량 증감3
    SELN_QTY_ICDC4: Optional[str] = None  # 매도 수량 증감4
    SELN_QTY_ICDC5: Optional[str] = None  # 매도 수량 증감5
    SHNU_QTY_ICDC1: Optional[str] = None  # 매수2 수량 증감1
    SHNU_QTY_ICDC2: Optional[str] = None  # 매수2 수량 증감2
    SHNU_QTY_ICDC3: Optional[str] = None  # 매수2 수량 증감3
    SHNU_QTY_ICDC4: Optional[str] = None  # 매수2 수량 증감4
    SHNU_QTY_ICDC5: Optional[str] = None  # 매수2 수량 증감5
    GLOB_TOTAL_SELN_QTY: Optional[str] = None  # 외국계 총 매도 수량
    GLOB_TOTAL_SHNU_QTY: Optional[str] = None  # 외국계 총 매수2 수량
    GLOB_TOTAL_SELN_QTY_ICDC: Optional[str] = None  # 외국계 총 매도 수량 증감
    GLOB_TOTAL_SHNU_QTY_ICDC: Optional[str] = None  # 외국계 총 매수2 수량 증감
    GLOB_NTBY_QTY: Optional[str] = None  # 외국계 순매수 수량
    GLOB_SELN_RLIM: Optional[str] = None  # 외국계 매도 비중
    GLOB_SHNU_RLIM: Optional[str] = None  # 외국계 매수2 비중
    SELN2_MBCR_ENG_NAME1: Optional[str] = None  # 매도2 영문회원사명1
    SELN2_MBCR_ENG_NAME2: Optional[str] = None  # 매도2 영문회원사명2
    SELN2_MBCR_ENG_NAME3: Optional[str] = None  # 매도2 영문회원사명3
    SELN2_MBCR_ENG_NAME4: Optional[str] = None  # 매도2 영문회원사명4
    SELN2_MBCR_ENG_NAME5: Optional[str] = None  # 매도2 영문회원사명5
    BYOV_MBCR_ENG_NAME1: Optional[str] = None  # 매수 영문회원사명1
    BYOV_MBCR_ENG_NAME2: Optional[str] = None  # 매수 영문회원사명2
    BYOV_MBCR_ENG_NAME3: Optional[str] = None  # 매수 영문회원사명3
    BYOV_MBCR_ENG_NAME4: Optional[str] = None  # 매수 영문회원사명4
    BYOV_MBCR_ENG_NAME5: Optional[str] = None  # 매수 영문회원사명5
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Mktfunds(SQLModel, table=True):
    """Output table for mktfunds"""
    __tablename__ = "kis_mktfunds"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bsop_date: Optional[str] = None  # 영업일자
    bstp_nmix_prpr: Optional[str] = None  # 업종지수현재가
    bstp_nmix_prdy_vrss: Optional[str] = None  # 업종지수전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    hts_avls: Optional[str] = None  # HTS시가총액
    cust_dpmn_amt: Optional[str] = None  # 고객예탁금금액
    cust_dpmn_amt_prdy_vrss: Optional[str] = None  # 고객예탁금금액전일대비
    amt_tnrt: Optional[str] = None  # 금액회전율
    uncl_amt: Optional[str] = None  # 미수금액
    crdt_loan_rmnd: Optional[str] = None  # 신용융자잔고
    futs_tfam_amt: Optional[str] = None  # 선물예수금금액
    sttp_amt: Optional[str] = None  # 주식형금액
    mxtp_amt: Optional[str] = None  # 혼합형금액
    bntp_amt: Optional[str] = None  # 채권형금액
    mmf_amt: Optional[str] = None  # MMF금액
    secu_lend_amt: Optional[str] = None  # 담보대출잔고금액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NearNewHighlow(SQLModel, table=True):
    """Output table for near_new_highlow"""
    __tablename__ = "kis_near_new_highlow"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    askp: Optional[str] = None  # 매도호가
    askp_rsqn1: Optional[str] = None  # 매도호가 잔량1
    bidp: Optional[str] = None  # 매수호가
    bidp_rsqn1: Optional[str] = None  # 매수호가 잔량1
    acml_vol: Optional[str] = None  # 누적 거래량
    new_hgpr: Optional[str] = None  # 신 최고가
    hprc_near_rate: Optional[str] = None  # 고가 근접 비율
    new_lwpr: Optional[str] = None  # 신 최저가
    lwpr_near_rate: Optional[str] = None  # 저가 근접 비율
    stck_sdpr: Optional[str] = None  # 주식 기준가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NewsTitle(SQLModel, table=True):
    """Output table for news_title"""
    __tablename__ = "kis_news_title"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    info_gb: Optional[str] = None  # 뉴스구분
    news_key: Optional[str] = None  # 뉴스키
    data_dt: Optional[str] = None  # 조회일자
    data_tm: Optional[str] = None  # 조회시간
    class_cd: Optional[str] = None  # 중분류
    class_name: Optional[str] = None  # 중분류명
    source: Optional[str] = None  # 자료원
    nation_cd: Optional[str] = None  # 국가코드
    exchange_cd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    symb_name: Optional[str] = None  # 종목명
    title: Optional[str] = None  # 제목
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OrderCash(SQLModel, table=True):
    """Output table for order_cash"""
    __tablename__ = "kis_order_cash"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    KRX_FWDG_ORD_ORGNO: Optional[str] = None  # 거래소코드
    ODNO: Optional[str] = None  # 주문번호
    ORD_TMD: Optional[str] = None  # 주문시간
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OrderCredit(SQLModel, table=True):
    """Output table for order_credit"""
    __tablename__ = "kis_order_credit"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    krx_fwdg_ord_orgno: Optional[str] = None  # 한국거래소전송주문조직번호
    odno: Optional[str] = None  # 주문번호
    ord_tmd: Optional[str] = None  # 주문시간
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OrderResv(SQLModel, table=True):
    """Output table for order_resv"""
    __tablename__ = "kis_order_resv"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ODNO: Optional[str] = None  # 한국거래소전송주문조직번호
    RSVN_ORD_RCIT_DT: Optional[str] = None  # 예약주문접수일자
    OVRS_RSVN_ODNO: Optional[str] = None  # 해외예약주문번호
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OrderResvCcnl(SQLModel, table=True):
    """Output table for order_resv_ccnl"""
    __tablename__ = "kis_order_resv_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    OVRS_RSVN_ODNO: Optional[str] = None  # 해외예약주문번호
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OrderResvRvsecncl(SQLModel, table=True):
    """Output table for order_resv_rvsecncl"""
    __tablename__ = "kis_order_resv_rvsecncl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    nrml_prcs_yn: Optional[str] = None  # 정상처리여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OvertimeAskingPriceKrx(SQLModel, table=True):
    """Output table for overtime_asking_price_krx"""
    __tablename__ = "kis_overtime_asking_price_krx"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    hour_cls_code: Optional[str] = None  # 시간구분코드
    askp1: Optional[str] = None  # 매도호가1
    askp2: Optional[str] = None  # 매도호가2
    askp3: Optional[str] = None  # 매도호가3
    askp4: Optional[str] = None  # 매도호가4
    askp5: Optional[str] = None  # 매도호가5
    askp6: Optional[str] = None  # 매도호가6
    askp7: Optional[str] = None  # 매도호가7
    askp8: Optional[str] = None  # 매도호가8
    askp9: Optional[str] = None  # 매도호가9
    bidp1: Optional[str] = None  # 매수호가1
    bidp2: Optional[str] = None  # 매수호가2
    bidp3: Optional[str] = None  # 매수호가3
    bidp4: Optional[str] = None  # 매수호가4
    bidp5: Optional[str] = None  # 매수호가5
    bidp6: Optional[str] = None  # 매수호가6
    bidp7: Optional[str] = None  # 매수호가7
    bidp8: Optional[str] = None  # 매수호가8
    bidp9: Optional[str] = None  # 매수호가9
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    askp_rsqn2: Optional[str] = None  # 매도호가잔량2
    askp_rsqn3: Optional[str] = None  # 매도호가잔량3
    askp_rsqn4: Optional[str] = None  # 매도호가잔량4
    askp_rsqn5: Optional[str] = None  # 매도호가잔량5
    askp_rsqn6: Optional[str] = None  # 매도호가잔량6
    askp_rsqn7: Optional[str] = None  # 매도호가잔량7
    askp_rsqn8: Optional[str] = None  # 매도호가잔량8
    askp_rsqn9: Optional[str] = None  # 매도호가잔량9
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    bidp_rsqn2: Optional[str] = None  # 매수호가잔량2
    bidp_rsqn3: Optional[str] = None  # 매수호가잔량3
    bidp_rsqn4: Optional[str] = None  # 매수호가잔량4
    bidp_rsqn5: Optional[str] = None  # 매수호가잔량5
    bidp_rsqn6: Optional[str] = None  # 매수호가잔량6
    bidp_rsqn7: Optional[str] = None  # 매수호가잔량7
    bidp_rsqn8: Optional[str] = None  # 매수호가잔량8
    bidp_rsqn9: Optional[str] = None  # 매수호가잔량9
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    ovtm_total_askp_rsqn: Optional[str] = None  # 시간외총매도호가잔량
    ovtm_total_bidp_rsqn: Optional[str] = None  # 시간외총매수호가잔량
    antc_cnpr: Optional[str] = None  # 예상체결가
    antc_cnqn: Optional[str] = None  # 예상체결량
    antc_vol: Optional[str] = None  # 예상거래량
    antc_cntg_vrss: Optional[str] = None  # 예상체결대비
    antc_cntg_vrss_sign: Optional[str] = None  # 예상체결대비부호
    antc_cntg_prdy_ctrt: Optional[str] = None  # 예상체결전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    total_askp_rsqn_icdc: Optional[str] = None  # 총매도호가잔량증감
    total_bidp_rsqn_icdc: Optional[str] = None  # 총매수호가잔량증감
    ovtm_total_askp_icdc: Optional[str] = None  # 시간외총매도호가증감
    ovtm_total_bidp_icdc: Optional[str] = None  # 시간외총매수호가증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OvertimeCcnlKrx(SQLModel, table=True):
    """Output table for overtime_ccnl_krx"""
    __tablename__ = "kis_overtime_ccnl_krx"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비구분
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 등락율
    wghn_avrg_stck_prc: Optional[str] = None  # 가중평균주식가격
    stck_oprc: Optional[str] = None  # 시가
    stck_hgpr: Optional[str] = None  # 고가
    stck_lwpr: Optional[str] = None  # 저가
    askp1: Optional[str] = None  # 매도호가
    bidp1: Optional[str] = None  # 매수호가
    cntg_vol: Optional[str] = None  # 거래량
    acml_vol: Optional[str] = None  # 누적거래량
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    seln_cntg_csnu: Optional[str] = None  # 매도체결건수
    shnu_cntg_csnu: Optional[str] = None  # 매수체결건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수체결건수
    cttr: Optional[str] = None  # 체결강도
    seln_cntg_smtn: Optional[str] = None  # 총매도수량
    shnu_cntg_smtn: Optional[str] = None  # 총매수수량
    cntg_cls_code: Optional[str] = None  # 체결구분
    shnu_rate: Optional[str] = None  # 매수비율
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일거래량대비등락율
    oprc_hour: Optional[str] = None  # 시가시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가대비구분
    oprc_vrss_prpr: Optional[str] = None  # 시가대비
    hgpr_hour: Optional[str] = None  # 최고가시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 고가대비구분
    hgpr_vrss_prpr: Optional[str] = None  # 고가대비
    lwpr_hour: Optional[str] = None  # 최저가시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 저가대비구분
    lwpr_vrss_prpr: Optional[str] = None  # 저가대비
    bsop_date: Optional[str] = None  # 영업일자
    new_mkop_cls_code: Optional[str] = None  # 신장운영구분코드
    trht_yn: Optional[str] = None  # 거래정지여부
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    vol_tnrt: Optional[str] = None  # 거래량회전율
    prdy_smns_hour_acml_vol: Optional[str] = None  # 전일동시간누적거래량
    prdy_smns_hour_acml_vol_rate: Optional[str] = None  # 전일동시간누적거래량비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OvertimeExpCcnlKrx(SQLModel, table=True):
    """Output table for overtime_exp_ccnl_krx"""
    __tablename__ = "kis_overtime_exp_ccnl_krx"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비구분
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 등락율
    wghn_avrg_stck_prc: Optional[str] = None  # 가중평균주식가격
    stck_oprc: Optional[str] = None  # 시가
    stck_hgpr: Optional[str] = None  # 고가
    stck_lwpr: Optional[str] = None  # 저가
    askp1: Optional[str] = None  # 매도호가
    bidp1: Optional[str] = None  # 매수호가
    cntg_vol: Optional[str] = None  # 거래량
    acml_vol: Optional[str] = None  # 누적거래량
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    seln_cntg_csnu: Optional[str] = None  # 매도체결건수
    shnu_cntg_csnu: Optional[str] = None  # 매수체결건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수체결건수
    cttr: Optional[str] = None  # 체결강도
    seln_cntg_smtn: Optional[str] = None  # 총매도수량
    shnu_cntg_smtn: Optional[str] = None  # 총매수수량
    cntg_cls_code: Optional[str] = None  # 체결구분
    shnu_rate: Optional[str] = None  # 매수비율
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일거래량대비등락율
    oprc_hour: Optional[str] = None  # 시가시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가대비구분
    oprc_vrss_prpr: Optional[str] = None  # 시가대비
    hgpr_hour: Optional[str] = None  # 최고가시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 고가대비구분
    hgpr_vrss_prpr: Optional[str] = None  # 고가대비
    lwpr_hour: Optional[str] = None  # 최저가시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 저가대비구분
    lwpr_vrss_prpr: Optional[str] = None  # 저가대비
    bsop_date: Optional[str] = None  # 영업일자
    new_mkop_cls_code: Optional[str] = None  # 신장운영구분코드
    trht_yn: Optional[str] = None  # 거래정지여부
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    vol_tnrt: Optional[str] = None  # 거래량회전율
    prdy_smns_hour_acml_vol: Optional[str] = None  # 전일동시간누적거래량
    prdy_smns_hour_acml_vol_rate: Optional[str] = None  # 전일동시간누적거래량비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OvertimeExpTransFluct(SQLModel, table=True):
    """Output table for overtime_exp_trans_fluct"""
    __tablename__ = "kis_overtime_exp_trans_fluct"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    data_rank: Optional[str] = None  # 데이터 순위
    iscd_stat_cls_code: Optional[str] = None  # 종목 상태 구분 코드
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    ovtm_untp_antc_cnpr: Optional[str] = None  # 시간외 단일가 예상 체결가
    ovtm_untp_antc_cntg_vrss: Optional[str] = None  # 시간외 단일가 예상 체결 대비
    ovtm_untp_antc_cntg_vrsssign: Optional[str] = None  # 시간외 단일가 예상 체결 대비
    ovtm_untp_antc_cntg_ctrt: Optional[str] = None  # 시간외 단일가 예상 체결 대비율
    ovtm_untp_askp_rsqn1: Optional[str] = None  # 시간외 단일가 매도호가 잔량1
    ovtm_untp_bidp_rsqn1: Optional[str] = None  # 시간외 단일가 매수호가 잔량1
    ovtm_untp_antc_cnqn: Optional[str] = None  # 시간외 단일가 예상 체결량
    itmt_vol: Optional[str] = None  # 장중 거래량
    stck_prpr: Optional[str] = None  # 주식 현재가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OvertimeFluctuation(SQLModel, table=True):
    """Output table for overtime_fluctuation"""
    __tablename__ = "kis_overtime_fluctuation"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ovtm_untp_uplm_issu_cnt: Optional[str] = None  # 시간외 단일가 상한 종목 수
    ovtm_untp_ascn_issu_cnt: Optional[str] = None  # 시간외 단일가 상승 종목 수
    ovtm_untp_stnr_issu_cnt: Optional[str] = None  # 시간외 단일가 보합 종목 수
    ovtm_untp_lslm_issu_cnt: Optional[str] = None  # 시간외 단일가 하한 종목 수
    ovtm_untp_down_issu_cnt: Optional[str] = None  # 시간외 단일가 하락 종목 수
    ovtm_untp_acml_vol: Optional[str] = None  # 시간외 단일가 누적 거래량
    ovtm_untp_acml_tr_pbmn: Optional[str] = None  # 시간외 단일가 누적 거래대금
    ovtm_untp_exch_vol: Optional[str] = None  # 시간외 단일가 거래소 거래량
    ovtm_untp_exch_tr_pbmn: Optional[str] = None  # 시간외 단일가 거래소 거래대금
    ovtm_untp_kosdaq_vol: Optional[str] = None  # 시간외 단일가 KOSDAQ 거래량
    ovtm_untp_kosdaq_tr_pbmn: Optional[str] = None  # 시간외 단일가 KOSDAQ 거래대금
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    ovtm_untp_prpr: Optional[str] = None  # 시간외 단일가 현재가
    ovtm_untp_prdy_vrss: Optional[str] = None  # 시간외 단일가 전일 대비
    ovtm_untp_prdy_vrss_sign: Optional[str] = None  # 시간외 단일가 전일 대비 부호
    ovtm_untp_prdy_ctrt: Optional[str] = None  # 시간외 단일가 전일 대비율
    ovtm_untp_askp1: Optional[str] = None  # 시간외 단일가 매도호가1
    ovtm_untp_seln_rsqn: Optional[str] = None  # 시간외 단일가 매도 잔량
    ovtm_untp_bidp1: Optional[str] = None  # 시간외 단일가 매수호가1
    ovtm_untp_shnu_rsqn: Optional[str] = None  # 시간외 단일가 매수 잔량
    ovtm_untp_vol: Optional[str] = None  # 시간외 단일가 거래량
    ovtm_vrss_acml_vol_rlim: Optional[str] = None  # 시간외 대비 누적 거래량 비중
    stck_prpr: Optional[str] = None  # 주식 현재가
    acml_vol: Optional[str] = None  # 누적 거래량
    bidp: Optional[str] = None  # 매수호가
    askp: Optional[str] = None  # 매도호가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OvertimeVolume(SQLModel, table=True):
    """Output table for overtime_volume"""
    __tablename__ = "kis_overtime_volume"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ovtm_untp_exch_vol: Optional[str] = None  # 시간외 단일가 거래소 거래량
    ovtm_untp_exch_tr_pbmn: Optional[str] = None  # 시간외 단일가 거래소 거래대금
    ovtm_untp_kosdaq_vol: Optional[str] = None  # 시간외 단일가 KOSDAQ 거래량
    ovtm_untp_kosdaq_tr_pbmn: Optional[str] = None  # 시간외 단일가 KOSDAQ 거래대금
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    ovtm_untp_prpr: Optional[str] = None  # 시간외 단일가 현재가
    ovtm_untp_prdy_vrss: Optional[str] = None  # 시간외 단일가 전일 대비
    ovtm_untp_prdy_vrss_sign: Optional[str] = None  # 시간외 단일가 전일 대비 부호
    ovtm_untp_prdy_ctrt: Optional[str] = None  # 시간외 단일가 전일 대비율
    ovtm_untp_seln_rsqn: Optional[str] = None  # 시간외 단일가 매도 잔량
    ovtm_untp_shnu_rsqn: Optional[str] = None  # 시간외 단일가 매수 잔량
    ovtm_untp_vol: Optional[str] = None  # 시간외 단일가 거래량
    ovtm_vrss_acml_vol_rlim: Optional[str] = None  # 시간외 대비 누적 거래량 비중
    stck_prpr: Optional[str] = None  # 주식 현재가
    acml_vol: Optional[str] = None  # 누적 거래량
    bidp: Optional[str] = None  # 매수호가
    askp: Optional[str] = None  # 매도호가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PbarTratio(SQLModel, table=True):
    """Output table for pbar_tratio"""
    __tablename__ = "kis_pbar_tratio"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    rprs_mrkt_kor_name: Optional[str] = None  # 대표시장한글명
    stck_shrn_iscd: Optional[str] = None  # 주식단축종목코드
    hts_kor_isnm: Optional[str] = None  # HTS한글종목명
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    prdy_vol: Optional[str] = None  # 전일거래량
    wghn_avrg_stck_prc: Optional[str] = None  # 가중평균주식가격
    lstn_stcn: Optional[str] = None  # 상장주수
    data_rank: Optional[str] = None  # 데이터순위
    cntg_vol: Optional[str] = None  # 체결거래량
    acml_vol_rlim: Optional[str] = None  # 누적거래량비중
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PensionInquireBalance(SQLModel, table=True):
    """Output table for pension_inquire_balance"""
    __tablename__ = "kis_pension_inquire_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cblc_dvsn_name: Optional[str] = None  # 잔고구분명
    prdt_name: Optional[str] = None  # 상품명
    pdno: Optional[str] = None  # 상품번호
    item_dvsn_name: Optional[str] = None  # 종목구분명
    thdt_buyqty: Optional[str] = None  # 금일매수수량
    thdt_sll_qty: Optional[str] = None  # 금일매도수량
    hldg_qty: Optional[str] = None  # 보유수량
    ord_psbl_qty: Optional[str] = None  # 주문가능수량
    pchs_avg_pric: Optional[str] = None  # 매입평균가격
    pchs_amt: Optional[str] = None  # 매입금액
    prpr: Optional[str] = None  # 현재가
    evlu_amt: Optional[str] = None  # 평가금액
    evlu_pfls_amt: Optional[str] = None  # 평가손익금액
    evlu_erng_rt: Optional[str] = None  # 평가수익율
    dnca_tot_amt: Optional[str] = None  # 예수금총금액
    nxdy_excc_amt: Optional[str] = None  # 익일정산금액
    prvs_rcdl_excc_amt: Optional[str] = None  # 가수도정산금액
    thdt_buy_amt: Optional[str] = None  # 금일매수금액
    thdt_sll_amt: Optional[str] = None  # 금일매도금액
    thdt_tlex_amt: Optional[str] = None  # 금일제비용금액
    scts_evlu_amt: Optional[str] = None  # 유가평가금액
    tot_evlu_amt: Optional[str] = None  # 총평가금액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PensionInquireDailyCcld(SQLModel, table=True):
    """Output table for pension_inquire_daily_ccld"""
    __tablename__ = "kis_pension_inquire_daily_ccld"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ord_gno_brno: Optional[str] = None  # 주문채번지점번호
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    trad_dvsn_name: Optional[str] = None  # 매매구분명
    odno: Optional[str] = None  # 주문번호
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    ord_unpr: Optional[str] = None  # 주문단가
    ord_qty: Optional[str] = None  # 주문수량
    tot_ccld_qty: Optional[str] = None  # 총체결수량
    nccs_qty: Optional[str] = None  # 미체결수량
    ord_dvsn_cd: Optional[str] = None  # 주문구분코드
    ord_dvsn_name: Optional[str] = None  # 주문구분명
    orgn_odno: Optional[str] = None  # 원주문번호
    ord_tmd: Optional[str] = None  # 주문시각
    objt_cust_dvsn_name: Optional[str] = None  # 대상고객구분명
    pchs_avg_pric: Optional[str] = None  # 매입평균가격
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PensionInquireDeposit(SQLModel, table=True):
    """Output table for pension_inquire_deposit"""
    __tablename__ = "kis_pension_inquire_deposit"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    dnca_tota: Optional[str] = None  # 예수금총액
    nxdy_excc_amt: Optional[str] = None  # 익일정산액
    nxdy_sttl_amt: Optional[str] = None  # 익일결제금액
    nx2_day_sttl_amt: Optional[str] = None  # 2익일결제금액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PensionInquirePresentBalance(SQLModel, table=True):
    """Output table for pension_inquire_present_balance"""
    __tablename__ = "kis_pension_inquire_present_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cblc_dvsn: Optional[str] = None  # 잔고구분
    cblc_dvsn_name: Optional[str] = None  # 잔고구분명
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    hldg_qty: Optional[str] = None  # 보유수량
    slpsb_qty: Optional[str] = None  # 매도가능수량
    pchs_avg_pric: Optional[str] = None  # 매입평균가격
    evlu_pfls_amt: Optional[str] = None  # 평가손익금액
    evlu_pfls_rt: Optional[str] = None  # 평가손익율
    prpr: Optional[str] = None  # 현재가
    evlu_amt: Optional[str] = None  # 평가금액
    pchs_amt: Optional[str] = None  # 매입금액
    cblc_weit: Optional[str] = None  # 잔고비중
    pchs_amt_smtl_amt: Optional[str] = None  # 매입금액합계금액
    evlu_amt_smtl_amt: Optional[str] = None  # 평가금액합계금액
    evlu_pfls_smtl_amt: Optional[str] = None  # 평가손익합계금액
    trad_pfls_smtl: Optional[str] = None  # 매매손익합계
    thdt_tot_pfls_amt: Optional[str] = None  # 당일총손익금액
    pftrt: Optional[str] = None  # 수익률
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PensionInquirePsblOrder(SQLModel, table=True):
    """Output table for pension_inquire_psbl_order"""
    __tablename__ = "kis_pension_inquire_psbl_order"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ord_psbl_cash: Optional[str] = None  # 주문가능현금
    ruse_psbl_amt: Optional[str] = None  # 재사용가능금액
    psbl_qty_calc_unpr: Optional[str] = None  # 가능수량계산단가
    max_buy_amt: Optional[str] = None  # 최대매수금액
    max_buy_qty: Optional[str] = None  # 최대매수수량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PeriodRights(SQLModel, table=True):
    """Output table for period_rights"""
    __tablename__ = "kis_period_rights"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bass_dt: Optional[str] = None  # 기준일자
    rght_type_cd: Optional[str] = None  # 권리유형코드
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    std_pdno: Optional[str] = None  # 표준상품번호
    acpl_bass_dt: Optional[str] = None  # 현지기준일자
    sbsc_strt_dt: Optional[str] = None  # 청약시작일자
    sbsc_end_dt: Optional[str] = None  # 청약종료일자
    cash_alct_rt: Optional[str] = None  # 현금배정비율
    stck_alct_rt: Optional[str] = None  # 주식배정비율
    crcy_cd: Optional[str] = None  # 통화코드
    crcy_cd2: Optional[str] = None  # 통화코드2
    crcy_cd3: Optional[str] = None  # 통화코드3
    crcy_cd4: Optional[str] = None  # 통화코드4
    alct_frcr_unpr: Optional[str] = None  # 배정외화단가
    stkp_dvdn_frcr_amt2: Optional[str] = None  # 주당배당외화금액2
    stkp_dvdn_frcr_amt3: Optional[str] = None  # 주당배당외화금액3
    stkp_dvdn_frcr_amt4: Optional[str] = None  # 주당배당외화금액4
    dfnt_yn: Optional[str] = None  # 확정여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PreferDisparateRatio(SQLModel, table=True):
    """Output table for prefer_disparate_ratio"""
    __tablename__ = "kis_prefer_disparate_ratio"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    data_rank: Optional[str] = None  # 데이터 순위
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    acml_vol: Optional[str] = None  # 누적 거래량
    prst_iscd: Optional[str] = None  # 우선주 종목코드
    prst_kor_isnm: Optional[str] = None  # 우선주 한글 종목명
    prst_prpr: Optional[str] = None  # 우선주 현재가
    prst_prdy_vrss: Optional[str] = None  # 우선주 전일대비
    prst_prdy_vrss_sign: Optional[str] = None  # 우선주 전일 대비 부호
    prst_acml_vol: Optional[str] = None  # 우선주 누적 거래량
    diff_prpr: Optional[str] = None  # 차이 현재가
    dprt: Optional[str] = None  # 괴리율
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    prst_prdy_ctrt: Optional[str] = None  # 우선주 전일 대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ProfitAssetIndex(SQLModel, table=True):
    """Output table for profit_asset_index"""
    __tablename__ = "kis_profit_asset_index"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    data_rank: Optional[str] = None  # 데이터 순위
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    sale_totl_prfi: Optional[str] = None  # 매출 총 이익
    bsop_prti: Optional[str] = None  # 영업 이익
    op_prfi: Optional[str] = None  # 경상 이익
    thtr_ntin: Optional[str] = None  # 당기순이익
    total_aset: Optional[str] = None  # 자산총계
    total_lblt: Optional[str] = None  # 부채총계
    total_cptl: Optional[str] = None  # 자본총계
    stac_month: Optional[str] = None  # 결산 월
    stac_month_cls_code: Optional[str] = None  # 결산 월 구분 코드
    iqry_csnu: Optional[str] = None  # 조회 건수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ProgramTradeByStock(SQLModel, table=True):
    """Output table for program_trade_by_stock"""
    __tablename__ = "kis_program_trade_by_stock"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bsop_hour: Optional[str] = None  # 영업 시간
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    whol_smtn_seln_vol: Optional[str] = None  # 전체 합계 매도 거래량
    whol_smtn_shnu_vol: Optional[str] = None  # 전체 합계 매수2 거래량
    whol_smtn_ntby_qty: Optional[str] = None  # 전체 합계 순매수 수량
    whol_smtn_seln_tr_pbmn: Optional[str] = None  # 전체 합계 매도 거래 대금
    whol_smtn_shnu_tr_pbmn: Optional[str] = None  # 전체 합계 매수2 거래 대금
    whol_smtn_ntby_tr_pbmn: Optional[str] = None  # 전체 합계 순매수 거래 대금
    whol_ntby_vol_icdc: Optional[str] = None  # 전체 순매수 거래량 증감
    whol_ntby_tr_pbmn_icdc: Optional[str] = None  # 전체 순매수 거래 대금 증감
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ProgramTradeByStockDaily(SQLModel, table=True):
    """Output table for program_trade_by_stock_daily"""
    __tablename__ = "kis_program_trade_by_stock_daily"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_clpr: Optional[str] = None  # 주식 종가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    whol_smtn_seln_vol: Optional[str] = None  # 전체 합계 매도 거래량
    whol_smtn_shnu_vol: Optional[str] = None  # 전체 합계 매수2 거래량
    whol_smtn_ntby_qty: Optional[str] = None  # 전체 합계 순매수 수량
    whol_smtn_seln_tr_pbmn: Optional[str] = None  # 전체 합계 매도 거래 대금
    whol_smtn_shnu_tr_pbmn: Optional[str] = None  # 전체 합계 매수2 거래 대금
    whol_smtn_ntby_tr_pbmn: Optional[str] = None  # 전체 합계 순매수 거래 대금
    whol_ntby_vol_icdc: Optional[str] = None  # 전체 순매수 거래량 증감
    whol_ntby_tr_pbmn_icdc2: Optional[str] = None  # 전체 순매수 거래 대금 증감2
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ProgramTradeKrx(SQLModel, table=True):
    """Output table for program_trade_krx"""
    __tablename__ = "kis_program_trade_krx"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    seln_cnqn: Optional[str] = None  # 매도체결량
    seln_tr_pbmn: Optional[str] = None  # 매도거래대금
    shnu_cnqn: Optional[str] = None  # 매수2체결량
    shnu_tr_pbmn: Optional[str] = None  # 매수2거래대금
    ntby_cnqn: Optional[str] = None  # 순매수체결량
    ntby_tr_pbmn: Optional[str] = None  # 순매수거래대금
    seln_rsqn: Optional[str] = None  # 매도호가잔량
    shnu_rsqn: Optional[str] = None  # 매수호가잔량
    whol_ntby_qty: Optional[str] = None  # 전체순매수호가잔량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ProgramTradeNxt(SQLModel, table=True):
    """Output table for program_trade_nxt"""
    __tablename__ = "kis_program_trade_nxt"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권 단축 종목코드
    STCK_CNTG_HOUR: Optional[str] = None  # 주식 체결 시간
    SELN_CNQN: Optional[str] = None  # 매도 체결량
    SELN_TR_PBMN: Optional[str] = None  # 매도 거래 대금
    SHNU_CNQN: Optional[str] = None  # 매수2 체결량
    SHNU_TR_PBMN: Optional[str] = None  # 매수2 거래 대금
    NTBY_CNQN: Optional[str] = None  # 순매수 체결량
    NTBY_TR_PBMN: Optional[str] = None  # 순매수 거래 대금
    SELN_RSQN: Optional[str] = None  # 매도호가잔량
    SHNU_RSQN: Optional[str] = None  # 매수호가잔량
    WHOL_NTBY_QTY: Optional[str] = None  # 전체순매수호가잔량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ProgramTradeTotal(SQLModel, table=True):
    """Output table for program_trade_total"""
    __tablename__ = "kis_program_trade_total"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    MKSC_SHRN_ISCD: Optional[str] = None  # 유가증권 단축 종목코드
    STCK_CNTG_HOUR: Optional[str] = None  # 주식 체결 시간
    SELN_CNQN: Optional[str] = None  # 매도 체결량
    SELN_TR_PBMN: Optional[str] = None  # 매도 거래 대금
    SHNU_CNQN: Optional[str] = None  # 매수2 체결량
    SHNU_TR_PBMN: Optional[str] = None  # 매수2 거래 대금
    NTBY_CNQN: Optional[str] = None  # 순매수 체결량
    NTBY_TR_PBMN: Optional[str] = None  # 순매수 거래 대금
    SELN_RSQN: Optional[str] = None  # 매도호가잔량
    SHNU_RSQN: Optional[str] = None  # 매수호가잔량
    WHOL_NTBY_QTY: Optional[str] = None  # 전체순매수호가잔량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PsearchResult(SQLModel, table=True):
    """Output table for psearch_result"""
    __tablename__ = "kis_psearch_result"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    code: Optional[str] = None  # 종목코드
    name: Optional[str] = None  # 종목명
    daebi: Optional[str] = None  # 전일대비부호
    price: Optional[str] = None  # 현재가
    chgrate: Optional[str] = None  # 등락율
    acml_vol: Optional[str] = None  # 거래량
    trade_amt: Optional[str] = None  # 거래대금
    change: Optional[str] = None  # 전일대비
    cttr: Optional[str] = None  # 체결강도
    open: Optional[str] = None  # 시가
    high: Optional[str] = None  # 고가
    low: Optional[str] = None  # 저가
    high52: Optional[str] = None  # 52주최고가
    low52: Optional[str] = None  # 52주최저가
    expprice: Optional[str] = None  # 예상체결가
    expchange: Optional[str] = None  # 예상대비
    expchggrate: Optional[str] = None  # 예상등락률
    expcvol: Optional[str] = None  # 예상체결수량
    chgrate2: Optional[str] = None  # 전일거래량대비율
    expdaebi: Optional[str] = None  # 예상대비부호
    recprice: Optional[str] = None  # 기준가
    uplmtprice: Optional[str] = None  # 상한가
    dnlmtprice: Optional[str] = None  # 하한가
    stotprice: Optional[str] = None  # 시가총액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PsearchTitle(SQLModel, table=True):
    """Output table for psearch_title"""
    __tablename__ = "kis_psearch_title"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    user_id: Optional[str] = None  # HTS ID
    seq: Optional[str] = None  # 조건키값
    grp_nm: Optional[str] = None  # 그룹명
    condition_nm: Optional[str] = None  # 조건명
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class QuoteBalance(SQLModel, table=True):
    """Output table for quote_balance"""
    __tablename__ = "kis_quote_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    data_rank: Optional[str] = None  # 데이터 순위
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    total_askp_rsqn: Optional[str] = None  # 총 매도호가 잔량
    total_bidp_rsqn: Optional[str] = None  # 총 매수호가 잔량
    total_ntsl_bidp_rsqn: Optional[str] = None  # 총 순 매수호가 잔량
    shnu_rsqn_rate: Optional[str] = None  # 매수 잔량 비율
    seln_rsqn_rate: Optional[str] = None  # 매도 잔량 비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SearchInfo(SQLModel, table=True):
    """Output table for search_info"""
    __tablename__ = "kis_search_info"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    std_pdno: Optional[str] = None  # 표준상품번호
    prdt_eng_name: Optional[str] = None  # 상품영문명
    natn_cd: Optional[str] = None  # 국가코드
    natn_name: Optional[str] = None  # 국가명
    tr_mket_cd: Optional[str] = None  # 거래시장코드
    tr_mket_name: Optional[str] = None  # 거래시장명
    ovrs_excg_cd: Optional[str] = None  # 해외거래소코드
    ovrs_excg_name: Optional[str] = None  # 해외거래소명
    tr_crcy_cd: Optional[str] = None  # 거래통화코드
    ovrs_papr: Optional[str] = None  # 해외액면가
    crcy_name: Optional[str] = None  # 통화명
    ovrs_stck_dvsn_cd: Optional[str] = None  # 해외주식구분코드
    prdt_clsf_cd: Optional[str] = None  # 상품분류코드
    prdt_clsf_name: Optional[str] = None  # 상품분류명
    sll_unit_qty: Optional[str] = None  # 매도단위수량
    buy_unit_qty: Optional[str] = None  # 매수단위수량
    tr_unit_amt: Optional[str] = None  # 거래단위금액
    lstg_stck_num: Optional[str] = None  # 상장주식수
    lstg_dt: Optional[str] = None  # 상장일자
    ovrs_stck_tr_stop_dvsn_cd: Optional[str] = None  # 해외주식거래정지구분코드
    lstg_abol_item_yn: Optional[str] = None  # 상장폐지종목여부
    ovrs_stck_prdt_grp_no: Optional[str] = None  # 해외주식상품그룹번호
    lstg_yn: Optional[str] = None  # 상장여부
    tax_levy_yn: Optional[str] = None  # 세금징수여부
    ovrs_stck_erlm_rosn_cd: Optional[str] = None  # 해외주식등록사유코드
    ovrs_stck_hist_rght_dvsn_cd: Optional[str] = None  # 해외주식이력권리구분코드
    chng_bf_pdno: Optional[str] = None  # 변경전상품번호
    prdt_type_cd_2: Optional[str] = None  # 상품유형코드2
    ovrs_item_name: Optional[str] = None  # 해외종목명
    sedol_no: Optional[str] = None  # SEDOL번호
    blbg_tckr_text: Optional[str] = None  # 블름버그티커내용
    ovrs_stck_etf_risk_drtp_cd: Optional[str] = None  # 해외주식ETF위험지표코드
    etp_chas_erng_rt_dbnb: Optional[str] = None  # ETP추적수익율배수
    istt_usge_isin_cd: Optional[str] = None  # 기관용도ISIN코드
    mint_svc_yn: Optional[str] = None  # MINT서비스여부
    mint_svc_yn_chng_dt: Optional[str] = None  # MINT서비스여부변경일자
    prdt_name: Optional[str] = None  # 상품명
    lei_cd: Optional[str] = None  # LEI코드
    ovrs_stck_stop_rson_cd: Optional[str] = None  # 해외주식정지사유코드
    lstg_abol_dt: Optional[str] = None  # 상장폐지일자
    mini_stk_tr_stat_dvsn_cd: Optional[str] = None  # 미니스탁거래상태구분코드
    mint_frst_svc_erlm_dt: Optional[str] = None  # MINT최초서비스등록일자
    mint_dcpt_trad_psbl_yn: Optional[str] = None  # MINT소수점매매가능여부
    mint_fnum_trad_psbl_yn: Optional[str] = None  # MINT정수매매가능여부
    mint_cblc_cvsn_ipsb_yn: Optional[str] = None  # MINT잔고전환불가여부
    ptp_item_yn: Optional[str] = None  # PTP종목여부
    ptp_item_trfx_exmt_yn: Optional[str] = None  # PTP종목양도세면제여부
    ptp_item_trfx_exmt_strt_dt: Optional[str] = None  # PTP종목양도세면제시작일자
    ptp_item_trfx_exmt_end_dt: Optional[str] = None  # PTP종목양도세면제종료일자
    dtm_tr_psbl_yn: Optional[str] = None  # 주간거래가능여부
    sdrf_stop_ecls_yn: Optional[str] = None  # 급등락정지제외여부
    sdrf_stop_ecls_erlm_dt: Optional[str] = None  # 급등락정지제외등록일자
    memo_text1: Optional[str] = None  # 메모내용1
    ovrs_now_pric1: Optional[str] = None  # 해외현재가격1
    last_rcvg_dtime: Optional[str] = None  # 최종수신일시
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SearchStockInfo(SQLModel, table=True):
    """Output table for search_stock_info"""
    __tablename__ = "kis_search_stock_info"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pdno: Optional[str] = None  # 상품번호
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    prdt_name: Optional[str] = None  # 상품명
    prdt_name120: Optional[str] = None  # 상품명(120자)
    prdt_abrv_name: Optional[str] = None  # 상품약어명
    prdt_eng_name: Optional[str] = None  # 상품영문명
    prdt_eng_name120: Optional[str] = None  # 상품영문명(120자)
    prdt_eng_abrv_name: Optional[str] = None  # 상품영문약어명
    mket_id_cd: Optional[str] = None  # 시장ID코드
    scty_grp_id_cd: Optional[str] = None  # 증권그룹ID코드
    excg_dvsn_cd: Optional[str] = None  # 거래소구분코드
    setl_mmdd: Optional[str] = None  # 결산월일
    lstg_stqt: Optional[str] = None  # 상장주수
    lstg_cptl_amt: Optional[str] = None  # 상장자본금액
    cpta: Optional[str] = None  # 자본금
    papr: Optional[str] = None  # 액면가
    issu_pric: Optional[str] = None  # 발행가격
    kospi200_item_yn: Optional[str] = None  # 코스피200종목여부
    scts_mket_lstg_dt: Optional[str] = None  # 유가증권시장상장일자
    scts_mket_lstg_abol_dt: Optional[str] = None  # 유가증권시장상장폐지일자
    kosdaq_mket_lstg_dt: Optional[str] = None  # 코스닥시장상장일자
    kosdaq_mket_lstg_abol_dt: Optional[str] = None  # 코스닥시장상장폐지일자
    frbd_mket_lstg_dt: Optional[str] = None  # 프리보드시장상장일자
    frbd_mket_lstg_abol_dt: Optional[str] = None  # 프리보드시장상장폐지일자
    reits_kind_cd: Optional[str] = None  # 리츠종류코드
    etf_dvsn_cd: Optional[str] = None  # ETF구분코드
    oilf_fund_yn: Optional[str] = None  # 유전펀드여부
    idx_bztp_lcls_cd: Optional[str] = None  # 지수업종대분류코드
    idx_bztp_mcls_cd: Optional[str] = None  # 지수업종중분류코드
    idx_bztp_scls_cd: Optional[str] = None  # 지수업종소분류코드
    idx_bztp_lcls_cd_name: Optional[str] = None  # 지수업종대분류코드명
    idx_bztp_mcls_cd_name: Optional[str] = None  # 지수업종중분류코드명
    idx_bztp_scls_cd_name: Optional[str] = None  # 지수업종소분류코드명
    stck_kind_cd: Optional[str] = None  # 주식종류코드
    mfnd_opng_dt: Optional[str] = None  # 뮤추얼펀드개시일자
    mfnd_end_dt: Optional[str] = None  # 뮤추얼펀드종료일자
    dpsi_erlm_cncl_dt: Optional[str] = None  # 예탁등록취소일자
    etf_cu_qty: Optional[str] = None  # ETFCU수량
    std_pdno: Optional[str] = None  # 표준상품번호
    dpsi_aptm_erlm_yn: Optional[str] = None  # 예탁지정등록여부
    etf_txtn_type_cd: Optional[str] = None  # ETF과세유형코드
    etf_type_cd: Optional[str] = None  # ETF유형코드
    lstg_abol_dt: Optional[str] = None  # 상장폐지일자
    nwst_odst_dvsn_cd: Optional[str] = None  # 신주구주구분코드
    sbst_pric: Optional[str] = None  # 대용가격
    thco_sbst_pric: Optional[str] = None  # 당사대용가격
    thco_sbst_pric_chng_dt: Optional[str] = None  # 당사대용가격변경일자
    tr_stop_yn: Optional[str] = None  # 거래정지여부
    admn_item_yn: Optional[str] = None  # 관리종목여부
    thdt_clpr: Optional[str] = None  # 당일종가
    bfdy_clpr: Optional[str] = None  # 전일종가
    clpr_chng_dt: Optional[str] = None  # 종가변경일자
    std_idst_clsf_cd: Optional[str] = None  # 표준산업분류코드
    std_idst_clsf_cd_name: Optional[str] = None  # 표준산업분류코드명
    ocr_no: Optional[str] = None  # OCR번호
    crfd_item_yn: Optional[str] = None  # 크라우드펀딩종목여부
    elec_scty_yn: Optional[str] = None  # 전자증권여부
    issu_istt_cd: Optional[str] = None  # 발행기관코드
    etf_chas_erng_rt_dbnb: Optional[str] = None  # ETF추적수익율배수
    etf_etn_ivst_heed_item_yn: Optional[str] = None  # ETFETN투자유의종목여부
    stln_int_rt_dvsn_cd: Optional[str] = None  # 대주이자율구분코드
    frnr_psnl_lmt_rt: Optional[str] = None  # 외국인개인한도비율
    lstg_rqsr_issu_istt_cd: Optional[str] = None  # 상장신청인발행기관코드
    lstg_rqsr_item_cd: Optional[str] = None  # 상장신청인종목코드
    trst_istt_issu_istt_cd: Optional[str] = None  # 신탁기관발행기관코드
    cptt_trad_tr_psbl_yn: Optional[str] = None  # NXT 거래종목여부
    nxt_tr_stop_yn: Optional[str] = None  # NXT 거래정지여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ShortSale(SQLModel, table=True):
    """Output table for short_sale"""
    __tablename__ = "kis_short_sale"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    ssts_cntg_qty: Optional[str] = None  # 공매도 체결 수량
    ssts_vol_rlim: Optional[str] = None  # 공매도 거래량 비중
    ssts_tr_pbmn: Optional[str] = None  # 공매도 거래 대금
    ssts_tr_pbmn_rlim: Optional[str] = None  # 공매도 거래대금 비중
    stnd_date1: Optional[str] = None  # 기준 일자1
    stnd_date2: Optional[str] = None  # 기준 일자2
    avrg_prc: Optional[str] = None  # 평균가격
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TopInterestStock(SQLModel, table=True):
    """Output table for top_interest_stock"""
    __tablename__ = "kis_top_interest_stock"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    askp: Optional[str] = None  # 매도호가
    bidp: Optional[str] = None  # 매수호가
    data_rank: Optional[str] = None  # 데이터 순위
    inter_issu_reg_csnu: Optional[str] = None  # 관심 종목 등록 건수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TradedByCompany(SQLModel, table=True):
    """Output table for traded_by_company"""
    __tablename__ = "kis_traded_by_company"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    data_rank: Optional[str] = None  # 데이터 순위
    mksc_shrn_iscd: Optional[str] = None  # 유가증권 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    seln_cnqn_smtn: Optional[str] = None  # 매도 체결량 합계
    shnu_cnqn_smtn: Optional[str] = None  # 매수2 체결량 합계
    ntby_cnqn: Optional[str] = None  # 순매수 체결량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TradprtByamt(SQLModel, table=True):
    """Output table for tradprt_byamt"""
    __tablename__ = "kis_tradprt_byamt"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    prpr_name: Optional[str] = None  # 가격명
    smtn_avrg_prpr: Optional[str] = None  # 합계 평균가격
    acml_vol: Optional[str] = None  # 합계 거래량
    whol_ntby_qty_rate: Optional[str] = None  # 합계 순매수비율
    ntby_cntg_csnu: Optional[str] = None  # 합계 순매수건수
    seln_cnqn_smtn: Optional[str] = None  # 매도 거래량
    whol_seln_vol_rate: Optional[str] = None  # 매도 거래량비율
    seln_cntg_csnu: Optional[str] = None  # 매도 건수
    shnu_cnqn_smtn: Optional[str] = None  # 매수 거래량
    whol_shun_vol_rate: Optional[str] = None  # 매수 거래량비율
    shnu_cntg_csnu: Optional[str] = None  # 매수 건수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class VolumePower(SQLModel, table=True):
    """Output table for volume_power"""
    __tablename__ = "kis_volume_power"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    knam: Optional[str] = None  # 종목명
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    tvol: Optional[str] = None  # 거래량
    pask: Optional[str] = None  # 매도호가
    pbid: Optional[str] = None  # 매수호가
    tpow: Optional[str] = None  # 당일체결강도
    powx: Optional[str] = None  # 체결강도
    enam: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    tamt: Optional[str] = None  # 거래대금
    bivl: Optional[str] = None  # 매도체결량
    asvl: Optional[str] = None  # 매수체결량
    strn: Optional[str] = None  # 체결강도
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class VolumeRank(SQLModel, table=True):
    """Output table for volume_rank"""
    __tablename__ = "kis_volume_rank"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    elw_kor_isnm: Optional[str] = None  # ELW한글종목명
    elw_shrn_iscd: Optional[str] = None  # ELW단축종목코드
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    lstn_stcn: Optional[str] = None  # 상장주수
    acml_vol: Optional[str] = None  # 누적거래량
    n_prdy_vol: Optional[str] = None  # N전일거래량
    n_prdy_vol_vrss: Optional[str] = None  # N전일거래량대비
    vol_inrt: Optional[str] = None  # 거래량증가율
    vol_tnrt: Optional[str] = None  # 거래량회전율
    nday_vol_tnrt: Optional[str] = None  # N일거래량회전율
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    n_prdy_tr_pbmn: Optional[str] = None  # N전일거래대금
    n_prdy_tr_pbmn_vrss: Optional[str] = None  # N전일거래대금대비
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    ntsl_rsqn: Optional[str] = None  # 순매도잔량
    ntby_rsqn: Optional[str] = None  # 순매수잔량
    seln_rsqn_rate: Optional[str] = None  # 매도잔량비율
    shnu_rsqn_rate: Optional[str] = None  # 매수2잔량비율
    stck_cnvr_rate: Optional[str] = None  # 주식전환비율
    hts_rmnn_dynu: Optional[str] = None  # HTS잔존일수
    invl_val: Optional[str] = None  # 내재가치값
    tmvl_val: Optional[str] = None  # 시간가치값
    acpr: Optional[str] = None  # 행사가
    unas_isnm: Optional[str] = None  # 기초자산명
    stck_last_tr_date: Optional[str] = None  # 최종거래일
    unas_shrn_iscd: Optional[str] = None  # 기초자산코드
    prdy_vol: Optional[str] = None  # 전일거래량
    lp_hldn_rate: Optional[str] = None  # LP보유비율
    prit: Optional[str] = None  # 패리티
    prls_qryr_stpr_prc: Optional[str] = None  # 손익분기주가가격
    delta_val: Optional[str] = None  # 델타값
    theta: Optional[str] = None  # 세타
    prls_qryr_rate: Optional[str] = None  # 손익분기비율
    stck_lstn_date: Optional[str] = None  # 주식상장일자
    hts_ints_vltl: Optional[str] = None  # HTS내재변동성
    lvrg_val: Optional[str] = None  # 레버리지값
    lp_ntby_qty: Optional[str] = None  # LP순매도량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CompareStocks(SQLModel, table=True):
    """Output table for compare_stocks"""
    __tablename__ = "kis_compare_stocks"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    elw_shrn_iscd: Optional[str] = None  # ELW단축종목코드
    elw_kor_isnm: Optional[str] = None  # ELW한글종목명
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CondSearch(SQLModel, table=True):
    """Output table for cond_search"""
    __tablename__ = "kis_cond_search"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bond_shrn_iscd: Optional[str] = None  # 채권단축종목코드
    hts_kor_isnm: Optional[str] = None  # HTS한글종목명
    rght_type_name: Optional[str] = None  # 권리유형명
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    acpr: Optional[str] = None  # 행사가
    stck_cnvr_rate: Optional[str] = None  # 주식전환비율
    stck_lstn_date: Optional[str] = None  # 주식상장일자
    stck_last_tr_date: Optional[str] = None  # 주식최종거래일자
    hts_rmnn_dynu: Optional[str] = None  # HTS잔존일수
    unas_isnm: Optional[str] = None  # 기초자산종목명
    unas_prpr: Optional[str] = None  # 기초자산현재가
    unas_prdy_vrss: Optional[str] = None  # 기초자산전일대비
    unas_prdy_vrss_sign: Optional[str] = None  # 기초자산전일대비부호
    unas_prdy_ctrt: Optional[str] = None  # 기초자산전일대비율
    unas_acml_vol: Optional[str] = None  # 기초자산누적거래량
    moneyness: Optional[str] = None  # MONEYNESS
    atm_cls_name: Optional[str] = None  # ATM구분명
    prit: Optional[str] = None  # 패리티
    delta_val: Optional[str] = None  # 델타값
    hts_ints_vltl: Optional[str] = None  # HTS내재변동성
    tmvl_val: Optional[str] = None  # 시간가치값
    gear: Optional[str] = None  # 기어링
    lvrg_val: Optional[str] = None  # 레버리지값
    prls_qryr_rate: Optional[str] = None  # 손익분기비율
    cfp: Optional[str] = None  # 자본지지점
    lstn_stcn: Optional[str] = None  # 상장주수
    pblc_co_name: Optional[str] = None  # 발행회사명
    lp_mbcr_name: Optional[str] = None  # LP회원사명
    lp_hldn_rate: Optional[str] = None  # LP보유비율
    elw_rght_form: Optional[str] = None  # ELW권리형태
    elw_ko_barrier: Optional[str] = None  # 조기종료발생기준가격
    apprch_rate: Optional[str] = None  # 접근도
    unas_shrn_iscd: Optional[str] = None  # 기초자산단축종목코드
    mtrt_date: Optional[str] = None  # 만기일자
    prmm_val: Optional[str] = None  # 프리미엄값
    stck_lp_fin_date: Optional[str] = None  # 주식LP종료일자
    tick_conv_prc: Optional[str] = None  # 틱환산가
    prls_qryr_stpr_prc: Optional[str] = None  # 손익분기주가가격
    lp_hvol: Optional[str] = None  # LP보유량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ElwAskingPrice(SQLModel, table=True):
    """Output table for elw_asking_price"""
    __tablename__ = "kis_elw_asking_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    bsop_hour: Optional[str] = None  # 영업시간
    hour_cls_code: Optional[str] = None  # 시간구분코드
    askp1: Optional[str] = None  # 매도호가1
    askp2: Optional[str] = None  # 매도호가2
    askp3: Optional[str] = None  # 매도호가3
    askp4: Optional[str] = None  # 매도호가4
    askp5: Optional[str] = None  # 매도호가5
    askp6: Optional[str] = None  # 매도호가6
    askp7: Optional[str] = None  # 매도호가7
    askp8: Optional[str] = None  # 매도호가8
    askp9: Optional[str] = None  # 매도호가9
    askp10: Optional[str] = None  # 매도호가10
    bidp1: Optional[str] = None  # 매수호가1
    bidp2: Optional[str] = None  # 매수호가2
    bidp3: Optional[str] = None  # 매수호가3
    bidp4: Optional[str] = None  # 매수호가4
    bidp5: Optional[str] = None  # 매수호가5
    bidp6: Optional[str] = None  # 매수호가6
    bidp7: Optional[str] = None  # 매수호가7
    bidp8: Optional[str] = None  # 매수호가8
    bidp9: Optional[str] = None  # 매수호가9
    bidp10: Optional[str] = None  # 매수호가10
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    askp_rsqn2: Optional[str] = None  # 매도호가잔량2
    askp_rsqn3: Optional[str] = None  # 매도호가잔량3
    askp_rsqn4: Optional[str] = None  # 매도호가잔량4
    askp_rsqn5: Optional[str] = None  # 매도호가잔량5
    askp_rsqn6: Optional[str] = None  # 매도호가잔량6
    askp_rsqn7: Optional[str] = None  # 매도호가잔량7
    askp_rsqn8: Optional[str] = None  # 매도호가잔량8
    askp_rsqn9: Optional[str] = None  # 매도호가잔량9
    askp_rsqn10: Optional[str] = None  # 매도호가잔량10
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    bidp_rsqn2: Optional[str] = None  # 매수호가잔량2
    bidp_rsqn3: Optional[str] = None  # 매수호가잔량3
    bidp_rsqn4: Optional[str] = None  # 매수호가잔량4
    bidp_rsqn5: Optional[str] = None  # 매수호가잔량5
    bidp_rsqn6: Optional[str] = None  # 매수호가잔량6
    bidp_rsqn7: Optional[str] = None  # 매수호가잔량7
    bidp_rsqn8: Optional[str] = None  # 매수호가잔량8
    bidp_rsqn9: Optional[str] = None  # 매수호가잔량9
    bidp_rsqn10: Optional[str] = None  # 매수호가잔량10
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    antc_cnpr: Optional[str] = None  # 예상체결가
    antc_cnqn: Optional[str] = None  # 예상체결량
    antc_cntg_vrss_sign: Optional[str] = None  # 예상체결대비부호
    antc_cntg_vrss: Optional[str] = None  # 예상체결대비
    antc_cntg_prdy_ctrt: Optional[str] = None  # 예상체결전일대비율
    lp_askp_rsqn1: Optional[str] = None  # LP매도호가잔량1
    lp_askp_rsqn2: Optional[str] = None  # LP매도호가잔량2
    lp_askp_rsqn3: Optional[str] = None  # LP매도호가잔량3
    lp_bidp_rsqn4: Optional[str] = None  # LP매수호가잔량4
    lp_askp_rsqn4: Optional[str] = None  # LP매도호가잔량4
    lp_bidp_rsqn5: Optional[str] = None  # LP매수호가잔량5
    lp_askp_rsqn5: Optional[str] = None  # LP매도호가잔량5
    lp_bidp_rsqn6: Optional[str] = None  # LP매수호가잔량6
    lp_askp_rsqn6: Optional[str] = None  # LP매도호가잔량6
    lp_bidp_rsqn7: Optional[str] = None  # LP매수호가잔량7
    lp_askp_rsqn7: Optional[str] = None  # LP매도호가잔량7
    lp_askp_rsqn8: Optional[str] = None  # LP매도호가잔량8
    lp_bidp_rsqn8: Optional[str] = None  # LP매수호가잔량8
    lp_askp_rsqn9: Optional[str] = None  # LP매도호가잔량9
    lp_bidp_rsqn9: Optional[str] = None  # LP매수호가잔량9
    lp_askp_rsqn10: Optional[str] = None  # LP매도호가잔량10
    lp_bidp_rsqn10: Optional[str] = None  # LP매수호가잔량10
    lp_bidp_rsqn1: Optional[str] = None  # LP매수호가잔량1
    lp_total_askp_rsqn: Optional[str] = None  # LP총매도호가잔량
    lp_bidp_rsqn2: Optional[str] = None  # LP매수호가잔량2
    lp_total_bidp_rsqn: Optional[str] = None  # LP총매수호가잔량
    lp_bidp_rsqn3: Optional[str] = None  # LP매수호가잔량3
    antc_vol: Optional[str] = None  # 예상거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ElwCcnl(SQLModel, table=True):
    """Output table for elw_ccnl"""
    __tablename__ = "kis_elw_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    wghn_avrg_stck_prc: Optional[str] = None  # 가중평균주식가격
    stck_oprc: Optional[str] = None  # 주식시가2
    stck_hgpr: Optional[str] = None  # 주식최고가
    stck_lwpr: Optional[str] = None  # 주식최저가
    askp1: Optional[str] = None  # 매도호가1
    bidp1: Optional[str] = None  # 매수호가1
    cntg_vol: Optional[str] = None  # 체결거래량
    acml_vol: Optional[str] = None  # 누적거래량
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    seln_cntg_csnu: Optional[str] = None  # 매도체결건수
    shnu_cntg_csnu: Optional[str] = None  # 매수체결건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수체결건수
    cttr: Optional[str] = None  # 체결강도
    seln_cntg_smtn: Optional[str] = None  # 총매도수량
    shnu_cntg_smtn: Optional[str] = None  # 총매수수량
    cntg_cls_code: Optional[str] = None  # 체결구분코드
    shnu_rate: Optional[str] = None  # 매수2비율
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일거래량대비등락율
    oprc_hour: Optional[str] = None  # 시가시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2대비현재가부호
    oprc_vrss_prpr: Optional[str] = None  # 시가2대비현재가
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가대비현재가부호
    hgpr_vrss_prpr: Optional[str] = None  # 최고가대비현재가
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가대비현재가부호
    lwpr_vrss_prpr: Optional[str] = None  # 최저가대비현재가
    bsop_date: Optional[str] = None  # 기준일자
    new_mkop_cls_code: Optional[str] = None  # 신규시장분류코드
    trht_yn: Optional[str] = None  # 거래정지여부
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    vol_rate: Optional[str] = None  # 거래량비율
    prdy_vrss_vol_rate: Optional[str] = None  # 전일대비거래량비율
    askp_rsqn_icdc: Optional[str] = None  # 매도호가잔량증감
    bidp_rsqn_icdc: Optional[str] = None  # 매수호가잔량증감
    hour_cls_code: Optional[str] = None  # 시간구분코드
    mrkt_trtm_cls_code: Optional[str] = None  # 시장거래시간구분코드
    vi_cls_code: Optional[str] = None  # VI구분코드
    timr_val: Optional[str] = None  # 시간가치값
    parity: Optional[str] = None  # 패리티
    prm_val: Optional[str] = None  # 프리미엄값
    gear: Optional[str] = None  # 기어링
    bep_rate: Optional[str] = None  # 손익분기비율
    itmv_val: Optional[str] = None  # 내재가치값
    prm_rate: Optional[str] = None  # 프리미엄비율
    sppt_pnt: Optional[str] = None  # 자본지지점
    lvrg_val: Optional[str] = None  # 레버리지값
    delta: Optional[str] = None  # 델타
    gamma: Optional[str] = None  # 감마
    vega: Optional[str] = None  # 베가
    theta: Optional[str] = None  # 세타
    rho: Optional[str] = None  # 로우
    hts_antc_vol: Optional[str] = None  # HTS내재변동성
    hts_theo_prc: Optional[str] = None  # HTS이론가
    vol_tnrt: Optional[str] = None  # 거래량회전율
    prdy_smns_hour_acml_vol: Optional[str] = None  # 전일동시간누적거래량
    prdy_smns_hour_acml_vol_rate: Optional[str] = None  # 전일동시간누적거래량비율
    apprch_rate: Optional[str] = None  # 접근도
    lp_hvol: Optional[str] = None  # LP보유량
    lp_hldn_rate: Optional[str] = None  # LP보유비율
    lp_ntby_qty: Optional[str] = None  # LP순매도량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ElwExpCcnl(SQLModel, table=True):
    """Output table for elw_exp_ccnl"""
    __tablename__ = "kis_elw_exp_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    stck_prpr: Optional[str] = None  # 주식현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    wghn_avrg_stck_prc: Optional[str] = None  # 가중평균주식가격
    stck_oprc: Optional[str] = None  # 주식시가2
    stck_hgpr: Optional[str] = None  # 주식최고가
    stck_lwpr: Optional[str] = None  # 주식최저가
    askp1: Optional[str] = None  # 매도호가1
    bidp1: Optional[str] = None  # 매수호가1
    cntg_vol: Optional[str] = None  # 체결거래량
    acml_vol: Optional[str] = None  # 누적거래량
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    seln_cntg_csnu: Optional[str] = None  # 매도체결건수
    shnu_cntg_csnu: Optional[str] = None  # 매수체결건수
    ntby_cntg_csnu: Optional[str] = None  # 순매수체결건수
    cttr: Optional[str] = None  # 체결강도
    seln_cntg_smtn: Optional[str] = None  # 총매도수량
    shnu_cntg_smtn: Optional[str] = None  # 총매수수량
    cntg_cls_code: Optional[str] = None  # 체결구분코드
    shnu_rate: Optional[str] = None  # 매수2비율
    prdy_vol_vrss_acml_vol_rate: Optional[str] = None  # 전일거래량대비등락율
    oprc_hour: Optional[str] = None  # 시가시간
    oprc_vrss_prpr_sign: Optional[str] = None  # 시가2대비현재가부호
    oprc_vrss_prpr: Optional[str] = None  # 시가2대비현재가
    hgpr_hour: Optional[str] = None  # 최고가시간
    hgpr_vrss_prpr_sign: Optional[str] = None  # 최고가대비현재가부호
    hgpr_vrss_prpr: Optional[str] = None  # 최고가대비현재가
    lwpr_hour: Optional[str] = None  # 최저가시간
    lwpr_vrss_prpr_sign: Optional[str] = None  # 최저가대비현재가부호
    lwpr_vrss_prpr: Optional[str] = None  # 최저가대비현재가
    bsop_date: Optional[str] = None  # 영업일자
    new_mkop_cls_code: Optional[str] = None  # 신장운영구분코드
    trht_yn: Optional[str] = None  # 거래정지여부
    askp_rsqn1: Optional[str] = None  # 매도호가잔량1
    bidp_rsqn1: Optional[str] = None  # 매수호가잔량1
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    tmvl_val: Optional[str] = None  # 시간가치값
    prit: Optional[str] = None  # 패리티
    prmm_val: Optional[str] = None  # 프리미엄값
    gear: Optional[str] = None  # 기어링
    prls_qryr_rate: Optional[str] = None  # 손익분기비율
    invl_val: Optional[str] = None  # 내재가치값
    prmm_rate: Optional[str] = None  # 프리미엄비율
    cfp: Optional[str] = None  # 자본지지점
    lvrg_val: Optional[str] = None  # 레버리지값
    delta: Optional[str] = None  # 델타
    gama: Optional[str] = None  # 감마
    vega: Optional[str] = None  # 베가
    theta: Optional[str] = None  # 세타
    rho: Optional[str] = None  # 로우
    hts_ints_vltl: Optional[str] = None  # HTS내재변동성
    hts_thpr: Optional[str] = None  # HTS이론가
    vol_tnrt: Optional[str] = None  # 거래량회전율
    lp_hvol: Optional[str] = None  # LP보유량
    lp_hldn_rate: Optional[str] = None  # LP보유비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ExpirationStocks(SQLModel, table=True):
    """Output table for expiration_stocks"""
    __tablename__ = "kis_expiration_stocks"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    elw_shrn_iscd: Optional[str] = None  # ELW단축종목코드
    elw_kor_isnm: Optional[str] = None  # ELW한글종목명
    unas_isnm: Optional[str] = None  # 기초자산종목명
    unas_prpr: Optional[str] = None  # 기초자산현재가
    acpr: Optional[str] = None  # 행사가
    stck_cnvr_rate: Optional[str] = None  # 주식전환비율
    elw_prpr: Optional[str] = None  # ELW현재가
    stck_lstn_date: Optional[str] = None  # 주식상장일자
    stck_last_tr_date: Optional[str] = None  # 주식최종거래일자
    total_rdmp_amt: Optional[str] = None  # 총상환금액
    rdmp_amt: Optional[str] = None  # 상환금액
    lstn_stcn: Optional[str] = None  # 상장주수
    lp_hvol: Optional[str] = None  # LP보유량
    ccls_paym_prc: Optional[str] = None  # 확정지급2가격
    mtrt_vltn_amt: Optional[str] = None  # 만기평가금액
    evnt_prd_fin_date: Optional[str] = None  # 행사2기간종료일자
    stlm_date: Optional[str] = None  # 결제일자
    pblc_prc: Optional[str] = None  # 발행가격
    unas_shrn_iscd: Optional[str] = None  # 기초자산단축종목코드
    stnd_iscd: Optional[str] = None  # 표준종목코드
    rdmp_ask_amt: Optional[str] = None  # 상환청구금액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Indicator(SQLModel, table=True):
    """Output table for indicator"""
    __tablename__ = "kis_indicator"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    elw_shrn_iscd: Optional[str] = None  # ELW단축종목코드
    elw_kor_isnm: Optional[str] = None  # ELW한글종목명
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    stck_cnvr_rate: Optional[str] = None  # 주식전환비율
    lvrg_val: Optional[str] = None  # 레버리지값
    acpr: Optional[str] = None  # 행사가
    tmvl_val: Optional[str] = None  # 시간가치값
    invl_val: Optional[str] = None  # 내재가치값
    elw_ko_barrier: Optional[str] = None  # 조기종료발생기준가격
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndicatorTrendCcnl(SQLModel, table=True):
    """Output table for indicator_trend_ccnl"""
    __tablename__ = "kis_indicator_trend_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    lvrg_val: Optional[str] = None  # 레버리지값
    gear: Optional[str] = None  # 기어링
    tmvl_val: Optional[str] = None  # 시간가치값
    invl_val: Optional[str] = None  # 내재가치값
    prit: Optional[str] = None  # 패리티
    apprch_rate: Optional[str] = None  # 접근도
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndicatorTrendDaily(SQLModel, table=True):
    """Output table for indicator_trend_daily"""
    __tablename__ = "kis_indicator_trend_daily"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식영업일자
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    lvrg_val: Optional[str] = None  # 레버리지값
    gear: Optional[str] = None  # 기어링
    tmvl_val: Optional[str] = None  # 시간가치값
    invl_val: Optional[str] = None  # 내재가치값
    prit: Optional[str] = None  # 패리티
    elw_oprc: Optional[str] = None  # ELW시가2
    elw_hgpr: Optional[str] = None  # ELW최고가
    elw_lwpr: Optional[str] = None  # ELW최저가
    apprch_rate: Optional[str] = None  # 접근도
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndicatorTrendMinute(SQLModel, table=True):
    """Output table for indicator_trend_minute"""
    __tablename__ = "kis_indicator_trend_minute"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식영업일자
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    elw_prpr: Optional[str] = None  # ELW현재가
    elw_oprc: Optional[str] = None  # ELW시가2
    elw_hgpr: Optional[str] = None  # ELW최고가
    elw_lwpr: Optional[str] = None  # ELW최저가
    lvrg_val: Optional[str] = None  # 레버리지값
    gear: Optional[str] = None  # 기어링
    prmm_val: Optional[str] = None  # 프리미엄값
    invl_val: Optional[str] = None  # 내재가치값
    prit: Optional[str] = None  # 패리티
    acml_vol: Optional[str] = None  # 누적거래량
    cntg_vol: Optional[str] = None  # 체결거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class LpTradeTrend(SQLModel, table=True):
    """Output table for lp_trade_trend"""
    __tablename__ = "kis_lp_trade_trend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cntg_hour: Optional[str] = None  # 체결시간
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    acml_tr_pbmn: Optional[str] = None  # 누적거래대금
    lp_buy_qty: Optional[str] = None  # LP매수수량
    lp_sell_qty: Optional[str] = None  # LP매도수량
    lp_ntby_qty: Optional[str] = None  # LP순매수수량
    lp_buy_amt: Optional[str] = None  # LP매수금액
    lp_sell_amt: Optional[str] = None  # LP매도금액
    lp_ntby_amt: Optional[str] = None  # LP순매수금액
    inst_deal_qty: Optional[str] = None  # 기관매매수량
    frgn_deal_qty: Optional[str] = None  # 외국인매매수량
    prsn_deal_qty: Optional[str] = None  # 개인매매수량
    apprch_rate: Optional[str] = None  # 접근도
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NewlyListed(SQLModel, table=True):
    """Output table for newly_listed"""
    __tablename__ = "kis_newly_listed"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    elw_shrn_iscd: Optional[str] = None  # ELW단축종목코드
    unas_isnm: Optional[str] = None  # 기초자산종목명
    lstn_stcn: Optional[str] = None  # 상장주수
    acpr: Optional[str] = None  # 행사가
    stck_last_tr_date: Optional[str] = None  # 주식최종거래일자
    elw_ko_barrier: Optional[str] = None  # 조기종료발생기준가격
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class QuickChange(SQLModel, table=True):
    """Output table for quick_change"""
    __tablename__ = "kis_quick_change"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    elw_shrn_iscd: Optional[str] = None  # ELW단축종목코드
    elw_kor_isnm: Optional[str] = None  # ELW한글종목명
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_ctrt: Optional[str] = None  # 전일대비율
    askp: Optional[str] = None  # 매도호가
    bidp: Optional[str] = None  # 매수호가
    total_askp_rsqn: Optional[str] = None  # 총매도호가잔량
    total_bidp_rsqn: Optional[str] = None  # 총매수호가잔량
    acml_vol: Optional[str] = None  # 누적거래량
    stnd_val: Optional[str] = None  # 기준값
    stnd_val_vrss: Optional[str] = None  # 기준값대비
    stnd_val_ctrt: Optional[str] = None  # 기준값대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Sensitivity(SQLModel, table=True):
    """Output table for sensitivity"""
    __tablename__ = "kis_sensitivity"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    elw_shrn_iscd: Optional[str] = None  # ELW단축종목코드
    elw_kor_isnm: Optional[str] = None  # ELW한글종목명
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    hts_thpr: Optional[str] = None  # HTS이론가
    delta_val: Optional[str] = None  # 델타값
    gama: Optional[str] = None  # 감마
    theta: Optional[str] = None  # 세타
    vega: Optional[str] = None  # 베가
    rho: Optional[str] = None  # 로우
    hts_ints_vltl: Optional[str] = None  # HTS내재변동성
    d90_hist_vltl: Optional[str] = None  # 90일역사적변동성
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SensitivityTrendCcnl(SQLModel, table=True):
    """Output table for sensitivity_trend_ccnl"""
    __tablename__ = "kis_sensitivity_trend_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    hts_thpr: Optional[str] = None  # hts 이론가
    delta_val: Optional[str] = None  # 델타 값
    gama: Optional[str] = None  # 감마
    theta: Optional[str] = None  # 세타
    vega: Optional[str] = None  # 베가
    rho: Optional[str] = None  # 로우
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SensitivityTrendDaily(SQLModel, table=True):
    """Output table for sensitivity_trend_daily"""
    __tablename__ = "kis_sensitivity_trend_daily"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식영업일자
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    hts_thpr: Optional[str] = None  # HTS이론가
    delta_val: Optional[str] = None  # 델타값
    gama: Optional[str] = None  # 감마
    theta: Optional[str] = None  # 세타
    vega: Optional[str] = None  # 베가
    rho: Optional[str] = None  # 로우
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UdrlAssetList(SQLModel, table=True):
    """Output table for udrl_asset_list"""
    __tablename__ = "kis_udrl_asset_list"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    unas_shrn_iscd: Optional[str] = None  # 기초자산단축종목코드
    unas_isnm: Optional[str] = None  # 기초자산종목명
    unas_prpr: Optional[str] = None  # 기초자산현재가
    unas_prdy_vrss: Optional[str] = None  # 기초자산전일대비
    unas_prdy_vrss_sign: Optional[str] = None  # 기초자산전일대비부호
    unas_prdy_ctrt: Optional[str] = None  # 기초자산전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UdrlAssetPrice(SQLModel, table=True):
    """Output table for udrl_asset_price"""
    __tablename__ = "kis_udrl_asset_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    elw_shrn_iscd: Optional[str] = None  # ELW단축종목코드
    hts_kor_isnm: Optional[str] = None  # HTS한글종목명
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    acml_vol: Optional[str] = None  # 누적거래량
    acpr: Optional[str] = None  # 행사가
    prls_qryr_stpr_prc: Optional[str] = None  # 손익분기주가가격
    hts_rmnn_dynu: Optional[str] = None  # HTS잔존일수
    hts_ints_vltl: Optional[str] = None  # HTS내재변동성
    stck_cnvr_rate: Optional[str] = None  # 주식전환비율
    lp_hvol: Optional[str] = None  # LP보유량
    lp_rlim: Optional[str] = None  # LP비중
    lvrg_val: Optional[str] = None  # 레버리지값
    gear: Optional[str] = None  # 기어링
    delta_val: Optional[str] = None  # 델타값
    gama: Optional[str] = None  # 감마
    vega: Optional[str] = None  # 베가
    theta: Optional[str] = None  # 세타
    prls_qryr_rate: Optional[str] = None  # 손익분기비율
    cfp: Optional[str] = None  # 자본지지점
    prit: Optional[str] = None  # 패리티
    invl_val: Optional[str] = None  # 내재가치값
    tmvl_val: Optional[str] = None  # 시간가치값
    hts_thpr: Optional[str] = None  # HTS이론가
    stck_lstn_date: Optional[str] = None  # 주식상장일자
    stck_last_tr_date: Optional[str] = None  # 주식최종거래일자
    lp_ntby_qty: Optional[str] = None  # LP순매도량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UpdownRate(SQLModel, table=True):
    """Output table for updown_rate"""
    __tablename__ = "kis_updown_rate"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태정보
    crec: Optional[str] = None  # 현재조회종목수
    trec: Optional[str] = None  # 전체조회종목수
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    tvol: Optional[str] = None  # 거래량
    pask: Optional[str] = None  # 매도호가
    pbid: Optional[str] = None  # 매수호가
    n_base: Optional[str] = None  # 기준가격
    n_diff: Optional[str] = None  # 기준가격대비
    n_rate: Optional[str] = None  # 기준가격대비율
    rank: Optional[str] = None  # 순위
    ename: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    tamt: Optional[str] = None  # 거래대금
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class VolatilityTrendCcnl(SQLModel, table=True):
    """Output table for volatility_trend_ccnl"""
    __tablename__ = "kis_volatility_trend_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_cntg_hour: Optional[str] = None  # 주식체결시간
    elw_prpr: Optional[str] = None  # ELW현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    bidp: Optional[str] = None  # 매수호가
    askp: Optional[str] = None  # 매도호가
    acml_vol: Optional[str] = None  # 누적거래량
    hts_ints_vltl: Optional[str] = None  # HTS내재변동성
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class VolatilityTrendDaily(SQLModel, table=True):
    """Output table for volatility_trend_daily"""
    __tablename__ = "kis_volatility_trend_daily"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    elw_prpr: Optional[str] = None  # ELW 현재가
    prdy_vrss: Optional[str] = None  # 전일대비
    prdy_vrss_sign: Optional[str] = None  # 전일대비부호
    prdy_ctrt: Optional[str] = None  # 전일대비율
    elw_oprc: Optional[str] = None  # elw 시가2
    elw_hgpr: Optional[str] = None  # elw 최고가
    elw_lwpr: Optional[str] = None  # elw 최저가
    acml_vol: Optional[str] = None  # 누적 거래량
    d10_hist_vltl: Optional[str] = None  # 10일 역사적 변동성
    d20_hist_vltl: Optional[str] = None  # 20일 역사적 변동성
    d30_hist_vltl: Optional[str] = None  # 30일 역사적 변동성
    d60_hist_vltl: Optional[str] = None  # 60일 역사적 변동성
    d90_hist_vltl: Optional[str] = None  # 90일 역사적 변동성
    hts_ints_vltl: Optional[str] = None  # HTS 내재 변동성
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class VolatilityTrendMinute(SQLModel, table=True):
    """Output table for volatility_trend_minute"""
    __tablename__ = "kis_volatility_trend_minute"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_cntg_hour: Optional[str] = None  # 주식 체결 시간
    stck_prpr: Optional[str] = None  # 주식 현재가
    elw_oprc: Optional[str] = None  # ELW 시가2
    elw_hgpr: Optional[str] = None  # ELW 최고가
    elw_lwpr: Optional[str] = None  # ELW 최저가
    hts_ints_vltl: Optional[str] = None  # HTS 내재 변동성
    hist_vltl: Optional[str] = None  # 역사적 변동성
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class VolatilityTrendTick(SQLModel, table=True):
    """Output table for volatility_trend_tick"""
    __tablename__ = "kis_volatility_trend_tick"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bsop_date: Optional[str] = None  # 주식영업일자
    stck_cntg_hour: Optional[str] = None  # ELW현재가
    elw_prpr: Optional[str] = None  # 전일대비
    hts_ints_vltl: Optional[str] = None  # 전일대비부호
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class EtfNavTrend(SQLModel, table=True):
    """Output table for etf_nav_trend"""
    __tablename__ = "kis_etf_nav_trend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    rt_cd: Optional[str] = None  # 성공 실패 여부
    msg_cd: Optional[str] = None  # 응답코드
    mksc_shrn_iscd: Optional[str] = None  # 유가증권단축종목코드
    nav: Optional[str] = None  # NAV
    nav_prdy_vrss_sign: Optional[str] = None  # NAV전일대비부호
    nav_prdy_vrss: Optional[str] = None  # NAV전일대비
    nav_prdy_ctrt: Optional[str] = None  # NAV전일대비율
    oprc_nav: Optional[str] = None  # NAV시가
    hprc_nav: Optional[str] = None  # NAV고가
    lprc_nav: Optional[str] = None  # NAV저가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireComponentStockPrice(SQLModel, table=True):
    """Output table for inquire_component_stock_price"""
    __tablename__ = "kis_inquire_component_stock_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_prpr: Optional[str] = None  # 매매 일자
    prdy_vrss: Optional[str] = None  # 주식 현재가
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비
    etf_cnfg_issu_avls: Optional[str] = None  # 전일 대비율
    nav: Optional[str] = None  # 누적 거래량
    nav_prdy_vrss_sign: Optional[str] = None  # 결제 일자
    nav_prdy_vrss: Optional[str] = None  # 전체 융자 신규 주수
    nav_prdy_ctrt: Optional[str] = None  # 전체 융자 상환 주수
    etf_ntas_ttam: Optional[str] = None  # 전체 융자 잔고 주수
    prdy_clpr_nav: Optional[str] = None  # 전체 융자 신규 금액
    oprc_nav: Optional[str] = None  # 전체 융자 상환 금액
    hprc_nav: Optional[str] = None  # 전체 융자 잔고 금액
    lprc_nav: Optional[str] = None  # 전체 융자 잔고 비율
    etf_cu_unit_scrt_cnt: Optional[str] = None  # 전체 융자 공여율
    etf_cnfg_issu_cnt: Optional[str] = None  # 전체 대주 신규 주수
    stck_shrn_iscd: Optional[str] = None  # 주식 단축 종목코드
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    tday_rsfl_rate: Optional[str] = None  # 당일 등락 비율
    prdy_vrss_vol: Optional[str] = None  # 전일 대비 거래량
    tr_pbmn_tnrt: Optional[str] = None  # 거래대금회전율
    hts_avls: Optional[str] = None  # HTS 시가총액
    etf_vltn_amt: Optional[str] = None  # ETF구성종목내평가금액
    etf_cnfg_issu_rlim: Optional[str] = None  # ETF구성종목비중
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NavComparisonDailyTrend(SQLModel, table=True):
    """Output table for nav_comparison_daily_trend"""
    __tablename__ = "kis_nav_comparison_daily_trend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_bsop_date: Optional[str] = None  # 주식 영업 일자
    stck_clpr: Optional[str] = None  # 주식 종가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    cntg_vol: Optional[str] = None  # 체결 거래량
    dprt: Optional[str] = None  # 괴리율
    nav_vrss_prpr: Optional[str] = None  # NAV 대비 현재가
    nav: Optional[str] = None  # NAV
    nav_prdy_vrss_sign: Optional[str] = None  # NAV 전일 대비 부호
    nav_prdy_vrss: Optional[str] = None  # NAV 전일 대비
    nav_prdy_ctrt: Optional[str] = None  # NAV 전일 대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NavComparisonTimeTrend(SQLModel, table=True):
    """Output table for nav_comparison_time_trend"""
    __tablename__ = "kis_nav_comparison_time_trend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    bsop_hour: Optional[str] = None  # 영업 시간
    nav: Optional[str] = None  # NAV
    nav_prdy_vrss_sign: Optional[str] = None  # NAV 전일 대비 부호
    nav_prdy_vrss: Optional[str] = None  # NAV 전일 대비
    nav_prdy_ctrt: Optional[str] = None  # NAV 전일 대비율
    nav_vrss_prpr: Optional[str] = None  # NAV 대비 현재가
    dprt: Optional[str] = None  # 괴리율
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    cntg_vol: Optional[str] = None  # 체결 거래량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NavComparisonTrend(SQLModel, table=True):
    """Output table for nav_comparison_trend"""
    __tablename__ = "kis_nav_comparison_trend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    stck_prpr: Optional[str] = None  # 주식 현재가
    prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    acml_vol: Optional[str] = None  # 누적 거래량
    acml_tr_pbmn: Optional[str] = None  # 누적 거래 대금
    stck_prdy_clpr: Optional[str] = None  # 주식 전일 종가
    stck_oprc: Optional[str] = None  # 주식 시가2
    stck_hgpr: Optional[str] = None  # 주식 최고가
    stck_lwpr: Optional[str] = None  # 주식 최저가
    stck_mxpr: Optional[str] = None  # 주식 상한가
    stck_llam: Optional[str] = None  # 주식 하한가
    nav: Optional[str] = None  # NAV
    nav_prdy_vrss_sign: Optional[str] = None  # NAV 전일 대비 부호
    nav_prdy_vrss: Optional[str] = None  # NAV 전일 대비
    nav_prdy_ctrt: Optional[str] = None  # NAV 전일 대비율
    prdy_clpr_nav: Optional[str] = None  # NAV전일종가
    oprc_nav: Optional[str] = None  # NAV시가
    hprc_nav: Optional[str] = None  # NAV고가
    lprc_nav: Optional[str] = None  # NAV저가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class AskingPrice(SQLModel, table=True):
    """Output table for asking_price"""
    __tablename__ = "kis_asking_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    symb: Optional[str] = None  # 종목코드
    zdiv: Optional[str] = None  # 소숫점자리수
    xymd: Optional[str] = None  # 현지일자
    xhms: Optional[str] = None  # 현지시간
    kymd: Optional[str] = None  # 한국일자
    khms: Optional[str] = None  # 한국시간
    bvol: Optional[str] = None  # 매수총잔량
    avol: Optional[str] = None  # 매도총잔량
    bdvl: Optional[str] = None  # 매수총잔량대비
    advl: Optional[str] = None  # 매도총잔량대비
    pbid1: Optional[str] = None  # 매수호가1
    pask1: Optional[str] = None  # 매도호가1
    vbid1: Optional[str] = None  # 매수잔량1
    vask1: Optional[str] = None  # 매도잔량1
    dbid1: Optional[str] = None  # 매수잔량대비1
    dask1: Optional[str] = None  # 매도잔량대비1
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Ccnl(SQLModel, table=True):
    """Output table for ccnl"""
    __tablename__ = "kis_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    series_cd: Optional[str] = None  # 종목코드
    bsns_date: Optional[str] = None  # 영업일자
    mrkt_open_date: Optional[str] = None  # 장개시일자
    mrkt_open_time: Optional[str] = None  # 장개시시각
    mrkt_close_date: Optional[str] = None  # 장종료일자
    mrkt_close_time: Optional[str] = None  # 장종료시각
    prev_price: Optional[str] = None  # 전일종가
    recv_date: Optional[str] = None  # 수신일자
    recv_time: Optional[str] = None  # 수신시각
    active_flag: Optional[str] = None  # 본장_전산장구분
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    prev_diff_price: Optional[str] = None  # 전일대비가
    prev_diff_rate: Optional[str] = None  # 등락률
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    vol: Optional[str] = None  # 누적거래량
    prev_sign: Optional[str] = None  # 전일대비부호
    quotsign: Optional[str] = None  # 체결구분
    recv_time2: Optional[str] = None  # 수신시각2 만분의일초
    psttl_price: Optional[str] = None  # 전일정산가
    psttl_sign: Optional[str] = None  # 전일정산가대비
    psttl_diff_price: Optional[str] = None  # 전일정산가대비가격
    psttl_diff_rate: Optional[str] = None  # 전일정산가대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DailyCcnl(SQLModel, table=True):
    """Output table for daily_ccnl"""
    __tablename__ = "kis_daily_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    tret_cnt: Optional[str] = None  # 자료개수
    last_n_cnt: Optional[str] = None  # N틱최종개수
    index_key: Optional[str] = None  # 이전조회KEY
    data_date: Optional[str] = None  # 일자
    data_time: Optional[str] = None  # 시각
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireCcld(SQLModel, table=True):
    """Output table for inquire_ccld"""
    __tablename__ = "kis_inquire_ccld"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cano: Optional[str] = None  # 종합계좌번호
    acnt_prdt_cd: Optional[str] = None  # 계좌상품코드
    ord_dt: Optional[str] = None  # 주문일자
    odno: Optional[str] = None  # 주문번호
    orgn_ord_dt: Optional[str] = None  # 원주문일자
    orgn_odno: Optional[str] = None  # 원주문번호
    ovrs_futr_fx_pdno: Optional[str] = None  # 해외선물FX상품번호
    rcit_dvsn_cd: Optional[str] = None  # 접수구분코드
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    trad_stgy_dvsn_cd: Optional[str] = None  # 매매전략구분코드
    bass_pric_type_cd: Optional[str] = None  # 기준가격유형코드
    ord_stat_cd: Optional[str] = None  # 주문상태코드
    fm_ord_qty: Optional[str] = None  # FM주문수량
    fm_ord_pric: Optional[str] = None  # FM주문가격
    fm_stop_ord_pric: Optional[str] = None  # FMSTOP주문가격
    rsvn_dvsn: Optional[str] = None  # 예약구분
    fm_ccld_qty: Optional[str] = None  # FM체결수량
    fm_ccld_pric: Optional[str] = None  # FM체결가격
    fm_ord_rmn_qty: Optional[str] = None  # FM주문잔여수량
    ord_grp_name: Optional[str] = None  # 주문그룹명
    erlm_dtl_dtime: Optional[str] = None  # 등록상세일시
    ccld_dtl_dtime: Optional[str] = None  # 체결상세일시
    ord_stfno: Optional[str] = None  # 주문직원번호
    rmks1: Optional[str] = None  # 비고1
    new_lqd_dvsn_cd: Optional[str] = None  # 신규청산구분코드
    fm_lqd_lmt_ord_pric: Optional[str] = None  # FM청산LIMIT주문가격
    fm_lqd_stop_pric: Optional[str] = None  # FM청산STOP가격
    ccld_cndt_cd: Optional[str] = None  # 체결조건코드
    noti_vald_dt: Optional[str] = None  # 게시유효일자
    acnt_type_cd: Optional[str] = None  # 계좌유형코드
    fuop_dvsn: Optional[str] = None  # 선물옵션구분
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDailyOrder(SQLModel, table=True):
    """Output table for inquire_daily_order"""
    __tablename__ = "kis_inquire_daily_order"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cano: Optional[str] = None  # 종합계좌번호
    acnt_prdt_cd: Optional[str] = None  # 계좌상품코드
    dt: Optional[str] = None  # 일자
    ord_dt: Optional[str] = None  # 주문일자
    odno: Optional[str] = None  # 주문번호
    orgn_ord_dt: Optional[str] = None  # 원주문일자
    orgn_odno: Optional[str] = None  # 원주문번호
    ovrs_futr_fx_pdno: Optional[str] = None  # 해외선물FX상품번호
    rvse_cncl_dvsn_cd: Optional[str] = None  # 정정취소구분코드
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    cplx_ord_dvsn_cd: Optional[str] = None  # 복합주문구분코드
    pric_dvsn_cd: Optional[str] = None  # 가격구분코드
    rcit_dvsn_cd: Optional[str] = None  # 접수구분코드
    fm_ord_qty: Optional[str] = None  # FM주문수량
    fm_ord_pric: Optional[str] = None  # FM주문가격
    fm_stop_ord_pric: Optional[str] = None  # FMSTOP주문가격
    ecis_rsvn_ord_yn: Optional[str] = None  # 행사예약주문여부
    fm_ccld_qty: Optional[str] = None  # FM체결수량
    fm_ccld_pric: Optional[str] = None  # FM체결가격
    fm_ord_rmn_qty: Optional[str] = None  # FM주문잔여수량
    ord_grp_name: Optional[str] = None  # 주문그룹명
    rcit_dtl_dtime: Optional[str] = None  # 접수상세일시
    ccld_dtl_dtime: Optional[str] = None  # 체결상세일시
    ordr_emp_no: Optional[str] = None  # 주문자사원번호
    rjct_rson_name: Optional[str] = None  # 거부사유명
    ccld_cndt_cd: Optional[str] = None  # 체결조건코드
    trad_end_dt: Optional[str] = None  # 매매종료일자
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePeriodCcld(SQLModel, table=True):
    """Output table for inquire_period_ccld"""
    __tablename__ = "kis_inquire_period_ccld"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cano: Optional[str] = None  # 종합계좌번호
    acnt_prdt_cd: Optional[str] = None  # 계좌상품코드
    crcy_cd: Optional[str] = None  # 통화코드
    fm_buy_qty: Optional[str] = None  # FM매수수량
    fm_sll_qty: Optional[str] = None  # FM매도수량
    fm_lqd_pfls_amt: Optional[str] = None  # FM청산손익금액
    fm_fee: Optional[str] = None  # FM수수료
    fm_net_pfls_amt: Optional[str] = None  # FM순손익금액
    fm_ustl_buy_qty: Optional[str] = None  # FM미결제매수수량
    fm_ustl_sll_qty: Optional[str] = None  # FM미결제매도수량
    fm_ustl_evlu_pfls_amt: Optional[str] = None  # FM미결제평가손익금액
    fm_ustl_evlu_pfls_amt2: Optional[str] = None  # FM미결제평가손익금액2
    fm_ustl_evlu_pfls_icdc_amt: Optional[str] = None  # FM미결제평가손익증감금액
    fm_ustl_agrm_amt: Optional[str] = None  # FM미결제약정금액
    fm_opt_lqd_amt: Optional[str] = None  # FM옵션청산금액
    ovrs_futr_fx_pdno: Optional[str] = None  # 해외선물FX상품번호
    fm_ccld_avg_pric: Optional[str] = None  # FM체결평균가격
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePeriodTrans(SQLModel, table=True):
    """Output table for inquire_period_trans"""
    __tablename__ = "kis_inquire_period_trans"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    trad_dt: Optional[str] = None  # 매매일자
    sttl_dt: Optional[str] = None  # 결제일자
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    sll_buy_dvsn_name: Optional[str] = None  # 
    pdno: Optional[str] = None  # 상품번호
    ovrs_item_name: Optional[str] = None  # 
    ccld_qty: Optional[str] = None  # 체결수량
    amt_unit_ccld_qty: Optional[str] = None  # 금액단위체결수량
    ft_ccld_unpr2: Optional[str] = None  # FT체결단가2
    ovrs_stck_ccld_unpr: Optional[str] = None  # 해외주식체결단가
    tr_frcr_amt2: Optional[str] = None  # 거래외화금액2
    tr_amt: Optional[str] = None  # 거래금액
    frcr_excc_amt_1: Optional[str] = None  # 외화정산금액1
    wcrc_excc_amt: Optional[str] = None  # 원화정산금액
    dmst_frcr_fee1: Optional[str] = None  # 국내외화수수료1
    frcr_fee1: Optional[str] = None  # 외화수수료1
    dmst_wcrc_fee: Optional[str] = None  # 국내원화수수료
    ovrs_wcrc_fee: Optional[str] = None  # 해외원화수수료
    crcy_cd: Optional[str] = None  # 통화코드
    std_pdno: Optional[str] = None  # 표준상품번호
    erlm_exrt: Optional[str] = None  # 등록환율
    loan_dvsn_cd: Optional[str] = None  # 대출구분코드
    loan_dvsn_name: Optional[str] = None  # 
    frcr_buy_amt_smtl: Optional[str] = None  # 외화매수금액합계
    frcr_sll_amt_smtl: Optional[str] = None  # 외화매도금액합계
    dmst_fee_smtl: Optional[str] = None  # 국내수수료합계
    ovrs_fee_smtl: Optional[str] = None  # 해외수수료합계
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePsamount(SQLModel, table=True):
    """Output table for inquire_psamount"""
    __tablename__ = "kis_inquire_psamount"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    tr_crcy_cd: Optional[str] = None  # 거래통화코드
    ord_psbl_frcr_amt: Optional[str] = None  # 주문가능외화금액
    sll_ruse_psbl_amt: Optional[str] = None  # 매도재사용가능금액
    ovrs_ord_psbl_amt: Optional[str] = None  # 해외주문가능금액
    max_ord_psbl_qty: Optional[str] = None  # 최대주문가능수량
    echm_af_ord_psbl_amt: Optional[str] = None  # 환전이후주문가능금액
    echm_af_ord_psbl_qty: Optional[str] = None  # 환전이후주문가능수량
    ord_psbl_qty: Optional[str] = None  # 주문가능수량
    exrt: Optional[str] = None  # 환율
    frcr_ord_psbl_amt1: Optional[str] = None  # 외화주문가능금액1
    ovrs_max_ord_psbl_qty: Optional[str] = None  # 해외최대주문가능수량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireTimeFuturechartprice(SQLModel, table=True):
    """Output table for inquire_time_futurechartprice"""
    __tablename__ = "kis_inquire_time_futurechartprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ret_cnt: Optional[str] = None  # 자료개수
    last_n_cnt: Optional[str] = None  # N틱최종개수
    index_key: Optional[str] = None  # 이전조회KEY
    data_date: Optional[str] = None  # 일자
    data_time: Optional[str] = None  # 시각
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireTimeOptchartprice(SQLModel, table=True):
    """Output table for inquire_time_optchartprice"""
    __tablename__ = "kis_inquire_time_optchartprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ret_cnt: Optional[str] = None  # 자료개수
    last_n_cnt: Optional[str] = None  # N틱최종개수
    index_key: Optional[str] = None  # 이전조회KEY
    data_date: Optional[str] = None  # 일자
    data_time: Optional[str] = None  # 시간
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireUnpd(SQLModel, table=True):
    """Output table for inquire_unpd"""
    __tablename__ = "kis_inquire_unpd"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cano: Optional[str] = None  # 종합계좌번호
    acnt_prdt_cd: Optional[str] = None  # 계좌상품코드
    ovrs_futr_fx_pdno: Optional[str] = None  # 해외선물FX상품번호
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    crcy_cd: Optional[str] = None  # 통화코드
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    fm_ustl_qty: Optional[str] = None  # FM미결제수량
    fm_ccld_avg_pric: Optional[str] = None  # FM체결평균가격
    fm_now_pric: Optional[str] = None  # FM현재가격
    fm_evlu_pfls_amt: Optional[str] = None  # FM평가손익금액
    fm_opt_evlu_amt: Optional[str] = None  # FM옵션평가금액
    fm_otp_evlu_pfls_amt: Optional[str] = None  # FM옵션평가손익금액
    fuop_dvsn: Optional[str] = None  # 선물옵션구분
    ecis_rsvn_ord_yn: Optional[str] = None  # 행사예약주문여부
    fm_lqd_psbl_qty: Optional[str] = None  # FM청산가능수량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InvestorUnpdTrend(SQLModel, table=True):
    """Output table for investor_unpd_trend"""
    __tablename__ = "kis_investor_unpd_trend"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    row_cnt: Optional[str] = None  # 응답레코드카운트
    prod_iscd: Optional[str] = None  # 상품
    cftc_iscd: Optional[str] = None  # CFTC코드
    bsop_date: Optional[str] = None  # 일자
    bidp_spec: Optional[str] = None  # 매수투기
    askp_spec: Optional[str] = None  # 매도투기
    spread_spec: Optional[str] = None  # 스프레드투기
    bidp_hedge: Optional[str] = None  # 매수헤지
    askp_hedge: Optional[str] = None  # 매도헤지
    hts_otst_smtn: Optional[str] = None  # 미결제합계
    bidp_missing: Optional[str] = None  # 매수누락
    askp_missing: Optional[str] = None  # 매도누락
    bidp_spec_cust: Optional[str] = None  # 매수투기고객
    askp_spec_cust: Optional[str] = None  # 매도투기고객
    spread_spec_cust: Optional[str] = None  # 스프레드투기고객
    bidp_hedge_cust: Optional[str] = None  # 매수헤지고객
    askp_hedge_cust: Optional[str] = None  # 매도헤지고객
    cust_smtn: Optional[str] = None  # 고객합계
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MarginDetail(SQLModel, table=True):
    """Output table for margin_detail"""
    __tablename__ = "kis_margin_detail"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cano: Optional[str] = None  # 종합계좌번호
    acnt_prdt_cd: Optional[str] = None  # 계좌상품코드
    crcy_cd: Optional[str] = None  # 통화코드
    resp_dt: Optional[str] = None  # 응답일자
    acnt_net_risk_mgna_aply_yn: Optional[str] = None  # 계좌순위험증거금적용여부
    fm_ord_psbl_amt: Optional[str] = None  # FM주문가능금액
    fm_add_mgn_amt: Optional[str] = None  # FM추가증거금액
    fm_brkg_mgn_amt: Optional[str] = None  # FM위탁증거금액
    fm_excc_brkg_mgn_amt: Optional[str] = None  # FM정산위탁증거금액
    fm_ustl_mgn_amt: Optional[str] = None  # FM미결제증거금액
    fm_mntn_mgn_amt: Optional[str] = None  # FM유지증거금액
    fm_ord_mgn_amt: Optional[str] = None  # FM주문증거금액
    fm_futr_ord_mgn_amt: Optional[str] = None  # FM선물주문증거금액
    fm_opt_buy_ord_amt: Optional[str] = None  # FM옵션매수주문금액
    fm_opt_sll_ord_mgn_amt: Optional[str] = None  # FM옵션매도주문증거금액
    fm_opt_buy_ord_mgn_amt: Optional[str] = None  # FM옵션매수주문증거금액
    fm_ecis_rsvn_mgn_amt: Optional[str] = None  # FM행사예약증거금액
    fm_span_brkg_mgn_amt: Optional[str] = None  # FMSPAN위탁증거금액
    fm_span_pric_altr_mgn_amt: Optional[str] = None  # FMSPAN가격변동증거금액
    fm_span_term_sprd_mgn_amt: Optional[str] = None  # FMSPAN기간스프레드증거금액
    fm_span_buy_opt_min_mgn_amt: Optional[str] = None  # FMSPAN옵션가격증거금액
    fm_span_opt_min_mgn_amt: Optional[str] = None  # FMSPAN옵션최소증거금액
    fm_span_tot_risk_mgn_amt: Optional[str] = None  # FMSPAN총위험증거금액
    fm_span_mntn_mgn_amt: Optional[str] = None  # FMSPAN유지증거금액
    fm_span_mntn_pric_altr_mgn_amt: Optional[str] = None  # FMSPAN유지가격변동증거금액
    fm_span_mntn_term_sprd_mgn_amt: Optional[str] = None  # FMSPAN유지기간스프레드증거금액
    fm_span_mntn_opt_pric_mgn_amt: Optional[str] = None  # FMSPAN유지옵션가격증거금액
    fm_span_mntn_opt_min_mgn_amt: Optional[str] = None  # FMSPAN유지옵션최소증거금액
    fm_span_mntn_tot_risk_mgn_amt: Optional[str] = None  # FMSPAN유지총위험증거금액
    fm_eurx_brkg_mgn_amt: Optional[str] = None  # FMEUREX위탁증거금액
    fm_eurx_pric_altr_mgn_amt: Optional[str] = None  # FMEUREX가격변동증거금액
    fm_eurx_term_sprd_mgn_amt: Optional[str] = None  # FMEUREX기간스프레드증거금액
    fm_eurx_opt_pric_mgn_amt: Optional[str] = None  # FMEUREX옵션가격증거금액
    fm_eurx_buy_opt_min_mgn_amt: Optional[str] = None  # FMEUREX매수옵션최소증거금액
    fm_eurx_tot_risk_mgn_amt: Optional[str] = None  # FMEUREX총위험증거금액
    fm_eurx_mntn_mgn_amt: Optional[str] = None  # FMEUREX유지증거금액
    fm_eurx_mntn_pric_altr_mgn_amt: Optional[str] = None  # FMEUREX유지가격변동증거금액
    fm_eurx_mntn_term_sprd_mgn_amt: Optional[str] = None  # FMEUREX기간스프레드증거금액
    fm_eurx_mntn_opt_pric_mgn_amt: Optional[str] = None  # FMEUREX유지옵션가격증거금액
    fm_eurx_mntn_tot_risk_mgn_amt: Optional[str] = None  # FMEUREX유지총위험증거금액
    fm_gnrl_brkg_mgn_amt: Optional[str] = None  # FM일반위탁증거금액
    fm_futr_ustl_mgn_amt: Optional[str] = None  # FM선물미결제증거금액
    fm_sll_opt_ustl_mgn_amt: Optional[str] = None  # FM매도옵션미결제증거금액
    fm_buy_opt_ustl_mgn_amt: Optional[str] = None  # FM매수옵션미결제증거금액
    fm_sprd_ustl_mgn_amt: Optional[str] = None  # FM스프레드미결제증거금액
    fm_avg_dsct_mgn_amt: Optional[str] = None  # FMAVG할인증거금액
    fm_gnrl_mntn_mgn_amt: Optional[str] = None  # FM일반유지증거금액
    fm_futr_mntn_mgn_amt: Optional[str] = None  # FM선물유지증거금액
    fm_opt_mntn_mgn_amt: Optional[str] = None  # FM옵션유지증거금액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MonthlyCcnl(SQLModel, table=True):
    """Output table for monthly_ccnl"""
    __tablename__ = "kis_monthly_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    tret_cnt: Optional[str] = None  # 자료개수
    last_n_cnt: Optional[str] = None  # N틱최종개수
    index_key: Optional[str] = None  # 이전조회KEY
    data_date: Optional[str] = None  # 일자
    data_time: Optional[str] = None  # 시각
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OptAskingPrice(SQLModel, table=True):
    """Output table for opt_asking_price"""
    __tablename__ = "kis_opt_asking_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    lowp_rice: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 현재가
    sttl_price: Optional[str] = None  # 정산가
    vol: Optional[str] = None  # 거래량
    prev_diff_price: Optional[str] = None  # 전일대비가
    prev_diff_rate: Optional[str] = None  # 전일대비율
    quot_date: Optional[str] = None  # 호가수신일자
    quot_time: Optional[str] = None  # 호가수신시각
    bid_qntt: Optional[str] = None  # 매수수량
    bid_num: Optional[str] = None  # 매수번호
    bid_price: Optional[str] = None  # 매수호가
    ask_qntt: Optional[str] = None  # 매도수량
    ask_num: Optional[str] = None  # 매도번호
    ask_price: Optional[str] = None  # 매도호가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OptDailyCcnl(SQLModel, table=True):
    """Output table for opt_daily_ccnl"""
    __tablename__ = "kis_opt_daily_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ret_cnt: Optional[str] = None  # 자료개수
    last_n_cnt: Optional[str] = None  # N틱최종개수
    index_key: Optional[str] = None  # 이전조회KEY
    data_date: Optional[str] = None  # 일자
    data_time: Optional[str] = None  # 시간
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OptDetail(SQLModel, table=True):
    """Output table for opt_detail"""
    __tablename__ = "kis_opt_detail"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    exch_cd: Optional[str] = None  # 거래소코드
    clas_cd: Optional[str] = None  # 품목종류
    crc_cd: Optional[str] = None  # 거래통화
    sttl_price: Optional[str] = None  # 전일종가
    sttl_date: Optional[str] = None  # 정산일
    trst_mgn: Optional[str] = None  # 증거금
    disp_digit: Optional[str] = None  # 가격표시진법
    tick_sz: Optional[str] = None  # 틱사이즈
    tick_val: Optional[str] = None  # 틱가치
    mrkt_open_date: Optional[str] = None  # 장개시일자
    mrkt_open_time: Optional[str] = None  # 장개시시각
    mrkt_close_date: Optional[str] = None  # 장마감일자
    mrkt_close_time: Optional[str] = None  # 장마감시각
    trd_fr_date: Optional[str] = None  # 상장일
    expr_date: Optional[str] = None  # 만기일
    trd_to_date: Optional[str] = None  # 최종거래일
    remn_cnt: Optional[str] = None  # 잔존일수
    stat_tp: Optional[str] = None  # 매매여부
    ctrt_size: Optional[str] = None  # 계약크기
    stl_tp: Optional[str] = None  # 최종결제구분
    frst_noti_date: Optional[str] = None  # 최초식별일
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OptMonthlyCcnl(SQLModel, table=True):
    """Output table for opt_monthly_ccnl"""
    __tablename__ = "kis_opt_monthly_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ret_cnt: Optional[str] = None  # 자료개수
    last_n_cnt: Optional[str] = None  # N틱최종개수
    index_key: Optional[str] = None  # 이전조회KEY
    data_date: Optional[str] = None  # 일자
    data_time: Optional[str] = None  # 시각
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OptPrice(SQLModel, table=True):
    """Output table for opt_price"""
    __tablename__ = "kis_opt_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    proc_date: Optional[str] = None  # 최종처리일자
    proc_time: Optional[str] = None  # 최종처리시각
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 현재가
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    bid_qntt: Optional[str] = None  # 매수1수량
    bid_price: Optional[str] = None  # 매수1호가
    ask_qntt: Optional[str] = None  # 매도1수량
    ask_price: Optional[str] = None  # 매도1호가
    trst_mgn: Optional[str] = None  # 증거금
    exch_cd: Optional[str] = None  # 거래소코드
    crc_cd: Optional[str] = None  # 거래통화
    trd_fr_date: Optional[str] = None  # 상장일
    expr_date: Optional[str] = None  # 만기일
    trd_to_date: Optional[str] = None  # 최종거래일
    remn_cnt: Optional[str] = None  # 잔존일수
    last_qntt: Optional[str] = None  # 체결량
    tot_ask_qntt: Optional[str] = None  # 총매도잔량
    tot_bid_qntt: Optional[str] = None  # 총매수잔량
    tick_size: Optional[str] = None  # 틱사이즈
    open_date: Optional[str] = None  # 장개시일자
    open_time: Optional[str] = None  # 장개시시각
    close_date: Optional[str] = None  # 장종료일자
    close_time: Optional[str] = None  # 장종료시각
    sbsnsdate: Optional[str] = None  # 영업일자
    sttl_price: Optional[str] = None  # 정산가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OptTickCcnl(SQLModel, table=True):
    """Output table for opt_tick_ccnl"""
    __tablename__ = "kis_opt_tick_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ret_cnt: Optional[str] = None  # 자료개수
    last_n_cnt: Optional[str] = None  # N틱최종개수
    index_key: Optional[str] = None  # 이전조회KEY
    data_date: Optional[str] = None  # 일자
    data_time: Optional[str] = None  # 시간
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OptWeeklyCcnl(SQLModel, table=True):
    """Output table for opt_weekly_ccnl"""
    __tablename__ = "kis_opt_weekly_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ret_cnt: Optional[str] = None  # 자료개수
    last_n_cnt: Optional[str] = None  # N틱최종개수
    index_key: Optional[str] = None  # 이전조회KEY
    data_date: Optional[str] = None  # 일자
    data_time: Optional[str] = None  # 시간
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OrderNotice(SQLModel, table=True):
    """Output table for order_notice"""
    __tablename__ = "kis_order_notice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    acct_no: Optional[str] = None  # 계좌번호
    ord_dt: Optional[str] = None  # 주문일자
    odno: Optional[str] = None  # 주문번호
    orgn_ord_dt: Optional[str] = None  # 원주문일자
    orgn_odno: Optional[str] = None  # 원주문번호
    series: Optional[str] = None  # 종목명
    rvse_cncl_dvsn_cd: Optional[str] = None  # 정정취소구분코드
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    cplx_ord_dvsn_cd: Optional[str] = None  # 복합주문구분코드
    prce_tp: Optional[str] = None  # 가격구분코드
    fm_excg_rcit_dvsn_cd: Optional[str] = None  # FM거래소접수구분코드
    ord_qty: Optional[str] = None  # 주문수량
    fm_lmt_pric: Optional[str] = None  # FMLIMIT가격
    fm_stop_ord_pric: Optional[str] = None  # FMSTOP주문가격
    tot_ccld_qty: Optional[str] = None  # 총체결수량
    tot_ccld_uv: Optional[str] = None  # 총체결단가
    ord_remq: Optional[str] = None  # 잔량
    fm_ord_grp_dt: Optional[str] = None  # FM주문그룹일자
    ord_grp_stno: Optional[str] = None  # 주문그룹번호
    ord_dtl_dtime: Optional[str] = None  # 주문상세일시
    oprt_dtl_dtime: Optional[str] = None  # 조작상세일시
    work_empl: Optional[str] = None  # 주문자
    crcy_cd: Optional[str] = None  # 통화코드
    lqd_yn: Optional[str] = None  # 청산여부(Y/N)
    lqd_lmt_pric: Optional[str] = None  # 청산LIMIT가격
    lqd_stop_pric: Optional[str] = None  # 청산STOP가격
    trd_cond: Optional[str] = None  # 체결조건코드
    term_ord_vald_dtime: Optional[str] = None  # 기간주문유효상세일시
    spec_tp: Optional[str] = None  # 계좌청산유형구분코드
    ecis_rsvn_ord_yn: Optional[str] = None  # 행사예약주문여부
    fuop_item_dvsn_cd: Optional[str] = None  # 선물옵션종목구분코드
    auto_ord_dvsn_cd: Optional[str] = None  # 자동주문 전략구분
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SearchContractDetail(SQLModel, table=True):
    """Output table for search_contract_detail"""
    __tablename__ = "kis_search_contract_detail"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    exch_cd: Optional[str] = None  # 거래소코드
    clas_cd: Optional[str] = None  # 품목종류
    crc_cd: Optional[str] = None  # 거래통화
    sttl_price: Optional[str] = None  # 정산가
    sttl_date: Optional[str] = None  # 정산일
    trst_mgn: Optional[str] = None  # 증거금
    disp_digit: Optional[str] = None  # 가격표시진법
    tick_sz: Optional[str] = None  # 틱사이즈
    tick_val: Optional[str] = None  # 틱가치
    mrkt_open_date: Optional[str] = None  # 장개시일자
    mrkt_open_time: Optional[str] = None  # 장개시시각
    mrkt_close_date: Optional[str] = None  # 장마감일자
    mrkt_close_time: Optional[str] = None  # 장마감시각
    trd_fr_date: Optional[str] = None  # 상장일
    expr_date: Optional[str] = None  # 만기일
    trd_to_date: Optional[str] = None  # 최종거래일
    remn_cnt: Optional[str] = None  # 잔존일수
    stat_tp: Optional[str] = None  # 매매여부
    ctrt_size: Optional[str] = None  # 계약크기
    stl_tp: Optional[str] = None  # 최종결제구분
    frst_noti_date: Optional[str] = None  # 최초식별일
    sub_exch_nm: Optional[str] = None  # 서브거래소코드
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SearchOptDetail(SQLModel, table=True):
    """Output table for search_opt_detail"""
    __tablename__ = "kis_search_opt_detail"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    exch_cd: Optional[str] = None  # 거래소코드
    clas_cd: Optional[str] = None  # 품목종류
    crc_cd: Optional[str] = None  # 거래통화
    sttl_price: Optional[str] = None  # 정산가
    sttl_date: Optional[str] = None  # 정산일
    trst_mgn: Optional[str] = None  # 증거금
    disp_digit: Optional[str] = None  # 가격표시진법
    tick_sz: Optional[str] = None  # 틱사이즈
    tick_val: Optional[str] = None  # 틱가치
    mrkt_open_date: Optional[str] = None  # 장개시일자
    mrkt_open_time: Optional[str] = None  # 장개시시각
    mrkt_close_date: Optional[str] = None  # 장마감일자
    mrkt_close_time: Optional[str] = None  # 장마감시각
    trd_fr_date: Optional[str] = None  # 상장일
    expr_date: Optional[str] = None  # 만기일
    trd_to_date: Optional[str] = None  # 최종거래일
    remn_cnt: Optional[str] = None  # 잔존일수
    stat_tp: Optional[str] = None  # 매매여부
    ctrt_size: Optional[str] = None  # 계약크기
    stl_tp: Optional[str] = None  # 최종결제구분
    frst_noti_date: Optional[str] = None  # 최초식별일
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class StockDetail(SQLModel, table=True):
    """Output table for stock_detail"""
    __tablename__ = "kis_stock_detail"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    exch_cd: Optional[str] = None  # 거래소코드
    tick_sz: Optional[str] = None  # 틱사이즈
    disp_digit: Optional[str] = None  # 가격표시진법
    trst_mgn: Optional[str] = None  # 증거금
    sttl_date: Optional[str] = None  # 정산일
    prev_price: Optional[str] = None  # 전일종가
    crc_cd: Optional[str] = None  # 거래통화
    clas_cd: Optional[str] = None  # 품목종류
    tick_val: Optional[str] = None  # 틱가치
    mrkt_open_date: Optional[str] = None  # 장개시일자
    mrkt_open_time: Optional[str] = None  # 장개시시각
    mrkt_close_date: Optional[str] = None  # 장마감일자
    mrkt_close_time: Optional[str] = None  # 장마감시각
    trd_fr_date: Optional[str] = None  # 상장일
    expr_date: Optional[str] = None  # 만기일
    trd_to_date: Optional[str] = None  # 최종거래일
    remn_cnt: Optional[str] = None  # 잔존일수
    stat_tp: Optional[str] = None  # 매매여부
    ctrt_size: Optional[str] = None  # 계약크기
    stl_tp: Optional[str] = None  # 최종결제구분
    frst_noti_date: Optional[str] = None  # 최초식별일
    sprd_srs_cd1: Optional[str] = None  # 스프레드 종목 #1
    sprd_srs_cd2: Optional[str] = None  # 스프레드 종목 #2
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TickCcnl(SQLModel, table=True):
    """Output table for tick_ccnl"""
    __tablename__ = "kis_tick_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    tret_cnt: Optional[str] = None  # 자료개수
    last_n_cnt: Optional[str] = None  # N틱최종개수
    index_key: Optional[str] = None  # 이전조회KEY
    data_date: Optional[str] = None  # 일자
    data_time: Optional[str] = None  # 시각
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class WeeklyCcnl(SQLModel, table=True):
    """Output table for weekly_ccnl"""
    __tablename__ = "kis_weekly_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ret_cnt: Optional[str] = None  # 자료개수
    last_n_cnt: Optional[str] = None  # N틱최종개수
    index_key: Optional[str] = None  # 이전조회KEY
    data_date: Optional[str] = None  # 일자
    data_time: Optional[str] = None  # 시각
    open_price: Optional[str] = None  # 시가
    high_price: Optional[str] = None  # 고가
    low_price: Optional[str] = None  # 저가
    last_price: Optional[str] = None  # 체결가격
    last_qntt: Optional[str] = None  # 체결수량
    vol: Optional[str] = None  # 누적거래수량
    prev_diff_flag: Optional[str] = None  # 전일대비구분
    prev_diff_price: Optional[str] = None  # 전일대비가격
    prev_diff_rate: Optional[str] = None  # 전일대비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class AlgoOrdno(SQLModel, table=True):
    """Output table for algo_ordno"""
    __tablename__ = "kis_algo_ordno"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ODNO: Optional[str] = None  # 주문번호
    TRAD_DVSN_NAME: Optional[str] = None  # 매매구분명
    PDNO: Optional[str] = None  # 상품번호
    ITEM_NAME: Optional[str] = None  # 종목명
    FT_ORD_QTY: Optional[str] = None  # FT주문수량
    FT_ORD_UNPR3: Optional[str] = None  # FT주문단가
    SPLT_BUY_ATTR_NAME: Optional[str] = None  # 분할매수속성명
    FT_CCLD_QTY: Optional[str] = None  # FT체결수량
    ORD_GNO_BRNO: Optional[str] = None  # 주문채번지점번호
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class BrknewsTitle(SQLModel, table=True):
    """Output table for brknews_title"""
    __tablename__ = "kis_brknews_title"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cntt_usiq_srno: Optional[str] = None  # 내용조회용일련번호
    news_ofer_entp_code: Optional[str] = None  # 뉴스제공업체코드
    data_dt: Optional[str] = None  # 작성일자
    data_tm: Optional[str] = None  # 작성시간
    hts_pbnt_titl_cntt: Optional[str] = None  # HTS공시제목내용
    news_lrdv_code: Optional[str] = None  # 뉴스대구분
    dorg: Optional[str] = None  # 자료원
    iscd1: Optional[str] = None  # 종목코드1
    iscd2: Optional[str] = None  # 종목코드2
    iscd3: Optional[str] = None  # 종목코드3
    iscd4: Optional[str] = None  # 종목코드4
    iscd5: Optional[str] = None  # 종목코드5
    iscd6: Optional[str] = None  # 종목코드6
    iscd7: Optional[str] = None  # 종목코드7
    iscd8: Optional[str] = None  # 종목코드8
    iscd9: Optional[str] = None  # 종목코드9
    iscd10: Optional[str] = None  # 종목코드10
    kor_isnm1: Optional[str] = None  # 한글종목명1
    kor_isnm2: Optional[str] = None  # 한글종목명2
    kor_isnm3: Optional[str] = None  # 한글종목명3
    kor_isnm4: Optional[str] = None  # 한글종목명4
    kor_isnm5: Optional[str] = None  # 한글종목명5
    kor_isnm6: Optional[str] = None  # 한글종목명6
    kor_isnm7: Optional[str] = None  # 한글종목명7
    kor_isnm8: Optional[str] = None  # 한글종목명8
    kor_isnm9: Optional[str] = None  # 한글종목명9
    kor_isnm10: Optional[str] = None  # 한글종목명10
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ColableByCompany(SQLModel, table=True):
    """Output table for colable_by_company"""
    __tablename__ = "kis_colable_by_company"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pdno: Optional[str] = None  # 상품번호
    ovrs_item_name: Optional[str] = None  # 해외종목명
    loan_rt: Optional[str] = None  # 대출비율
    mgge_mntn_rt: Optional[str] = None  # 담보유지비율
    mgge_ensu_rt: Optional[str] = None  # 담보확보비율
    loan_exec_psbl_yn: Optional[str] = None  # 대출실행가능여부
    stff_name: Optional[str] = None  # 직원명
    erlm_dt: Optional[str] = None  # 등록일자
    tr_mket_name: Optional[str] = None  # 거래시장명
    crcy_cd: Optional[str] = None  # 통화코드
    natn_kor_name: Optional[str] = None  # 국가한글명
    ovrs_excg_cd: Optional[str] = None  # 해외거래소코드
    loan_psbl_item_num: Optional[str] = None  # 대출가능종목수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CountriesHoliday(SQLModel, table=True):
    """Output table for countries_holiday"""
    __tablename__ = "kis_countries_holiday"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    tr_natn_cd: Optional[str] = None  # 거래국가코드
    natn_eng_abrv_cd: Optional[str] = None  # 국가영문약어코드
    tr_mket_cd: Optional[str] = None  # 거래시장코드
    tr_mket_name: Optional[str] = None  # 거래시장명
    acpl_sttl_dt: Optional[str] = None  # 현지결제일자
    dmst_sttl_dt: Optional[str] = None  # 국내결제일자
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Dailyprice(SQLModel, table=True):
    """Output table for dailyprice"""
    __tablename__ = "kis_dailyprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    rsym: Optional[str] = None  # 실시간조회종목코드
    zdiv: Optional[str] = None  # 소수점자리수
    nrec: Optional[str] = None  # 전일종가
    xymd: Optional[str] = None  # 일자(YYYYMMDD)
    clos: Optional[str] = None  # 종가
    sign: Optional[str] = None  # 대비기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    open: Optional[str] = None  # 시가
    high: Optional[str] = None  # 고가
    low: Optional[str] = None  # 저가
    tvol: Optional[str] = None  # 거래량
    tamt: Optional[str] = None  # 거래대금
    pbid: Optional[str] = None  # 매수호가
    vbid: Optional[str] = None  # 매수호가잔량
    pask: Optional[str] = None  # 매도호가
    vask: Optional[str] = None  # 매도호가잔량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DaytimeOrder(SQLModel, table=True):
    """Output table for daytime_order"""
    __tablename__ = "kis_daytime_order"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    KRX_FWDG_ORD_ORGNO: Optional[str] = None  # 한국거래소전송주문조직번호
    ODNO: Optional[str] = None  # 주문번호
    ORD_TMD: Optional[str] = None  # 주문시각
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DaytimeOrderRvsecncl(SQLModel, table=True):
    """Output table for daytime_order_rvsecncl"""
    __tablename__ = "kis_daytime_order_rvsecncl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    Output1: Optional[str] = None  # 응답상세
    KRX_FWDG_ORD_ORGNO: Optional[str] = None  # 한국거래소전송주문조직번호
    ODNO: Optional[str] = None  # 주문번호
    ORD_TMD: Optional[str] = None  # 주문시각
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DelayedAskingPriceAsia(SQLModel, table=True):
    """Output table for delayed_asking_price_asia"""
    __tablename__ = "kis_delayed_asking_price_asia"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    symb: Optional[str] = None  # 종목코드
    zdiv: Optional[str] = None  # 소숫점자리수
    xymd: Optional[str] = None  # 현지일자
    xhms: Optional[str] = None  # 현지시간
    kymd: Optional[str] = None  # 한국일자
    khms: Optional[str] = None  # 한국시간
    bvol: Optional[str] = None  # 매수총잔량
    avol: Optional[str] = None  # 매도총잔량
    bdvl: Optional[str] = None  # 매수총잔량대비
    advl: Optional[str] = None  # 매도총잔량대비
    pbid1: Optional[str] = None  # 매수호가1
    pask1: Optional[str] = None  # 매도호가1
    vbid1: Optional[str] = None  # 매수잔량1
    vask1: Optional[str] = None  # 매도잔량1
    dbid1: Optional[str] = None  # 매수잔량대비1
    dask1: Optional[str] = None  # 매도잔량대비1
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DelayedCcnl(SQLModel, table=True):
    """Output table for delayed_ccnl"""
    __tablename__ = "kis_delayed_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    SYMB: Optional[str] = None  # 종목코드
    ZDIV: Optional[str] = None  # 수수점자리수
    TYMD: Optional[str] = None  # 현지영업일자
    XYMD: Optional[str] = None  # 현지일자
    XHMS: Optional[str] = None  # 현지시간
    KYMD: Optional[str] = None  # 한국일자
    KHMS: Optional[str] = None  # 한국시간
    OPEN: Optional[str] = None  # 시가
    HIGH: Optional[str] = None  # 고가
    LOW: Optional[str] = None  # 저가
    LAST: Optional[str] = None  # 현재가
    SIGN: Optional[str] = None  # 대비구분
    DIFF: Optional[str] = None  # 전일대비
    RATE: Optional[str] = None  # 등락율
    PBID: Optional[str] = None  # 매수호가
    PASK: Optional[str] = None  # 매도호가
    VBID: Optional[str] = None  # 매수잔량
    VASK: Optional[str] = None  # 매도잔량
    EVOL: Optional[str] = None  # 체결량
    TVOL: Optional[str] = None  # 거래량
    TAMT: Optional[str] = None  # 거래대금
    BIVL: Optional[str] = None  # 매도체결량
    ASVL: Optional[str] = None  # 매수체결량
    STRN: Optional[str] = None  # 체결강도
    MTYP: Optional[str] = None  # 시장구분
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ForeignMargin(SQLModel, table=True):
    """Output table for foreign_margin"""
    __tablename__ = "kis_foreign_margin"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    natn_name: Optional[str] = None  # 국가명
    frcr_dncl_amt1: Optional[str] = None  # 외화예수금액
    ustl_buy_amt: Optional[str] = None  # 미결제매수금액
    ustl_sll_amt: Optional[str] = None  # 미결제매도금액
    frcr_rcvb_amt: Optional[str] = None  # 외화미수금액
    frcr_mgn_amt: Optional[str] = None  # 외화증거금액
    frcr_gnrl_ord_psbl_amt: Optional[str] = None  # 외화일반주문가능금액
    frcr_ord_psbl_amt1: Optional[str] = None  # 외화주문가능금액
    itgr_ord_psbl_amt: Optional[str] = None  # 통합주문가능금액
    bass_exrt: Optional[str] = None  # 기준환율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndustryPrice(SQLModel, table=True):
    """Output table for industry_price"""
    __tablename__ = "kis_industry_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    nrec: Optional[str] = None  # RecordCount
    icod: Optional[str] = None  # 업종코드
    name: Optional[str] = None  # 업종명
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class IndustryTheme(SQLModel, table=True):
    """Output table for industry_theme"""
    __tablename__ = "kis_industry_theme"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태정보
    crec: Optional[str] = None  # 현재조회종목수
    trec: Optional[str] = None  # 전체조회종목수
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    tvol: Optional[str] = None  # 거래량
    vask: Optional[str] = None  # 매도잔량
    pask: Optional[str] = None  # 매도호가
    pbid: Optional[str] = None  # 매수호가
    vbid: Optional[str] = None  # 매수잔량
    seqn: Optional[str] = None  # 순위
    ename: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireAlgoCcnl(SQLModel, table=True):
    """Output table for inquire_algo_ccnl"""
    __tablename__ = "kis_inquire_algo_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    CCLD_SEQ: Optional[str] = None  # 체결순번
    CCLD_BTWN: Optional[str] = None  # 체결시간
    PDNO: Optional[str] = None  # 상품번호
    ITEM_NAME: Optional[str] = None  # 종목명
    FT_CCLD_QTY: Optional[str] = None  # FT체결수량
    FT_CCLD_UNPR3: Optional[str] = None  # FT체결단가
    FT_CCLD_AMT3: Optional[str] = None  # FT체결금액
    ODNO: Optional[str] = None  # 주문번호
    TRAD_DVSN_NAME: Optional[str] = None  # 매매구분명
    FT_ORD_QTY: Optional[str] = None  # FT주문수량
    FT_ORD_UNPR3: Optional[str] = None  # FT주문단가
    ORD_TMD: Optional[str] = None  # 주문시각
    SPLT_BUY_ATTR_NAME: Optional[str] = None  # 분할매수속성명
    TR_CRCY: Optional[str] = None  # 거래통화
    CCLD_CNT: Optional[str] = None  # 체결건수
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireDailyChartprice(SQLModel, table=True):
    """Output table for inquire_daily_chartprice"""
    __tablename__ = "kis_inquire_daily_chartprice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ovrs_nmix_prdy_vrss: Optional[str] = None  # 전일 대비
    prdy_vrss_sign: Optional[str] = None  # 전일 대비 부호
    prdy_ctrt: Optional[str] = None  # 전일 대비율
    ovrs_nmix_prdy_clpr: Optional[str] = None  # 전일 종가
    acml_vol: Optional[str] = None  # 누적 거래량
    hts_kor_isnm: Optional[str] = None  # HTS 한글 종목명
    ovrs_nmix_prpr: Optional[str] = None  # 현재가
    stck_shrn_iscd: Optional[str] = None  # 단축 종목코드
    prdy_vol: Optional[str] = None  # 전일 거래량
    ovrs_prod_oprc: Optional[str] = None  # 시가
    ovrs_prod_hgpr: Optional[str] = None  # 최고가
    ovrs_prod_lwpr: Optional[str] = None  # 최저가
    stck_bsop_date: Optional[str] = None  # 영업 일자
    ovrs_nmix_oprc: Optional[str] = None  # 시가
    ovrs_nmix_hgpr: Optional[str] = None  # 최고가
    ovrs_nmix_lwpr: Optional[str] = None  # 최저가
    mod_yn: Optional[str] = None  # 변경 여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireNccs(SQLModel, table=True):
    """Output table for inquire_nccs"""
    __tablename__ = "kis_inquire_nccs"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    ord_dt: Optional[str] = None  # 주문일자
    ord_gno_brno: Optional[str] = None  # 주문채번지점번호
    odno: Optional[str] = None  # 주문번호
    orgn_odno: Optional[str] = None  # 원주문번호
    pdno: Optional[str] = None  # 상품번호
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    rvse_cncl_dvsn_cd: Optional[str] = None  # 정정취소구분코드
    rjct_rson: Optional[str] = None  # 거부사유
    ord_tmd: Optional[str] = None  # 주문시각
    tr_crcy_cd: Optional[str] = None  # 거래통화코드
    natn_cd: Optional[str] = None  # 국가코드
    ft_ord_qty: Optional[str] = None  # FT주문수량
    ft_ccld_qty: Optional[str] = None  # FT체결수량
    nccs_qty: Optional[str] = None  # 미체결수량
    ft_ord_unpr3: Optional[str] = None  # FT주문단가3
    ft_ccld_unpr3: Optional[str] = None  # FT체결단가3
    ft_ccld_amt3: Optional[str] = None  # FT체결금액3
    ovrs_excg_cd: Optional[str] = None  # 해외거래소코드
    loan_type_cd: Optional[str] = None  # 대출유형코드
    loan_dt: Optional[str] = None  # 대출일자
    usa_amk_exts_rqst_yn: Optional[str] = None  # 미국애프터마켓연장신청여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePaymtStdrBalance(SQLModel, table=True):
    """Output table for inquire_paymt_stdr_balance"""
    __tablename__ = "kis_inquire_paymt_stdr_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    pdno: Optional[str] = None  # 상품번호
    prdt_name: Optional[str] = None  # 상품명
    cblc_qty13: Optional[str] = None  # 잔고수량13
    ord_psbl_qty1: Optional[str] = None  # 주문가능수량1
    avg_unpr3: Optional[str] = None  # 평균단가3
    ovrs_now_pric1: Optional[str] = None  # 해외현재가격1
    frcr_pchs_amt: Optional[str] = None  # 외화매입금액
    frcr_evlu_amt2: Optional[str] = None  # 외화평가금액2
    evlu_pfls_amt2: Optional[str] = None  # 평가손익금액2
    bass_exrt: Optional[str] = None  # 기준환율
    oprt_dtl_dtime: Optional[str] = None  # 조작상세일시
    buy_crcy_cd: Optional[str] = None  # 매수통화코드
    thdt_sll_ccld_qty1: Optional[str] = None  # 당일매도체결수량1
    thdt_buy_ccld_qty1: Optional[str] = None  # 당일매수체결수량1
    evlu_pfls_rt1: Optional[str] = None  # 평가손익율1
    tr_mket_name: Optional[str] = None  # 거래시장명
    natn_kor_name: Optional[str] = None  # 국가한글명
    std_pdno: Optional[str] = None  # 표준상품번호
    mgge_qty: Optional[str] = None  # 담보수량
    loan_rmnd: Optional[str] = None  # 대출잔액
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    ovrs_excg_cd: Optional[str] = None  # 해외거래소코드
    scts_dvsn_name: Optional[str] = None  # 유가증권구분명
    ldng_cblc_qty: Optional[str] = None  # 대여잔고수량
    crcy_cd: Optional[str] = None  # 통화코드
    crcy_cd_name: Optional[str] = None  # 통화코드명
    frcr_dncl_amt_2: Optional[str] = None  # 외화예수금액2
    frst_bltn_exrt: Optional[str] = None  # 최초고시환율
    pchs_amt_smtl_amt: Optional[str] = None  # 매입금액합계금액
    tot_evlu_pfls_amt: Optional[str] = None  # 총평가손익금액
    evlu_erng_rt1: Optional[str] = None  # 평가수익율1
    tot_dncl_amt: Optional[str] = None  # 총예수금액
    wcrc_evlu_amt_smtl: Optional[str] = None  # 원화평가금액합계
    tot_asst_amt2: Optional[str] = None  # 총자산금액2
    frcr_cblc_wcrc_evlu_amt_smtl: Optional[str] = None  # 외화잔고원화평가금액합계
    tot_loan_amt: Optional[str] = None  # 총대출금액
    tot_ldng_evlu_amt: Optional[str] = None  # 총대여평가금액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquirePresentBalance(SQLModel, table=True):
    """Output table for inquire_present_balance"""
    __tablename__ = "kis_inquire_present_balance"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cblc_qty13: Optional[str] = None  # 잔고수량13
    thdt_buy_ccld_qty1: Optional[str] = None  # 당일매수체결수량1
    thdt_sll_ccld_qty1: Optional[str] = None  # 당일매도체결수량1
    ccld_qty_smtl1: Optional[str] = None  # 체결수량합계1
    ord_psbl_qty1: Optional[str] = None  # 주문가능수량1
    frcr_pchs_amt: Optional[str] = None  # 외화매입금액
    frcr_evlu_amt2: Optional[str] = None  # 출금가능원화금액
    evlu_pfls_amt2: Optional[str] = None  # 평가손익금액2
    evlu_pfls_rt1: Optional[str] = None  # 평가손익율1
    pdno: Optional[str] = None  # 상품번호
    bass_exrt: Optional[str] = None  # 기준환율
    buy_crcy_cd: Optional[str] = None  # 매수통화코드
    ovrs_now_pric1: Optional[str] = None  # 해외현재가격1
    avg_unpr3: Optional[str] = None  # 평균단가3
    tr_mket_name: Optional[str] = None  # 거래시장명
    natn_kor_name: Optional[str] = None  # 국가한글명
    pchs_rmnd_wcrc_amt: Optional[str] = None  # 매입잔액원화금액
    thdt_buy_ccld_frcr_amt: Optional[str] = None  # 당일매수체결외화금액
    thdt_sll_ccld_frcr_amt: Optional[str] = None  # 당일매도체결외화금액
    unit_amt: Optional[str] = None  # 단위금액
    std_pdno: Optional[str] = None  # 표준상품번호
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    loan_rmnd: Optional[str] = None  # 대출잔액
    loan_dt: Optional[str] = None  # 대출일자
    loan_expd_dt: Optional[str] = None  # 대출만기일자
    ovrs_excg_cd: Optional[str] = None  # 해외거래소코드
    item_lnkg_excg_cd: Optional[str] = None  # 종목연동거래소코드
    crcy_cd: Optional[str] = None  # 통화코드
    frcr_buy_amt_smtl: Optional[str] = None  # 외화매수금액합계
    frcr_sll_amt_smtl: Optional[str] = None  # 외화매도금액합계
    frcr_dncl_amt_2: Optional[str] = None  # 외화예수금액2
    frst_bltn_exrt: Optional[str] = None  # 최초고시환율
    frcr_buy_mgn_amt: Optional[str] = None  # 외화매수증거금액
    frcr_etc_mgna: Optional[str] = None  # 외화기타증거금
    frcr_drwg_psbl_amt_1: Optional[str] = None  # 외화출금가능금액1
    acpl_cstd_crcy_yn: Optional[str] = None  # 현지보관통화여부
    nxdy_frcr_drwg_psbl_amt: Optional[str] = None  # 익일외화출금가능금액
    output3: Optional[str] = None  # 응답상세3
    pchs_amt_smtl: Optional[str] = None  # 매입금액합계
    evlu_amt_smtl: Optional[str] = None  # 평가금액합계
    evlu_pfls_amt_smtl: Optional[str] = None  # 평가손익금액합계
    dncl_amt: Optional[str] = None  # 예수금액
    cma_evlu_amt: Optional[str] = None  # CMA평가금액
    tot_dncl_amt: Optional[str] = None  # 총예수금액
    etc_mgna: Optional[str] = None  # 기타증거금
    wdrw_psbl_tot_amt: Optional[str] = None  # 인출가능총금액
    frcr_evlu_tota: Optional[str] = None  # 외화평가총액
    evlu_erng_rt1: Optional[str] = None  # 평가수익율1
    pchs_amt_smtl_amt: Optional[str] = None  # 매입금액합계금액
    evlu_amt_smtl_amt: Optional[str] = None  # 평가금액합계금액
    tot_evlu_pfls_amt: Optional[str] = None  # 총평가손익금액
    tot_asst_amt: Optional[str] = None  # 총자산금액
    buy_mgn_amt: Optional[str] = None  # 매수증거금액
    mgna_tota: Optional[str] = None  # 증거금총액
    frcr_use_psbl_amt: Optional[str] = None  # 외화사용가능금액
    ustl_sll_amt_smtl: Optional[str] = None  # 미결제매도금액합계
    ustl_buy_amt_smtl: Optional[str] = None  # 미결제매수금액합계
    tot_frcr_cblc_smtl: Optional[str] = None  # 총외화잔고합계
    tot_loan_amt: Optional[str] = None  # 총대출금액
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InquireSearch(SQLModel, table=True):
    """Output table for inquire_search"""
    __tablename__ = "kis_inquire_search"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태정보
    crec: Optional[str] = None  # 현재조회종목수
    trec: Optional[str] = None  # 전체조회종목수
    nrec: Optional[str] = None  # Record Count
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    last: Optional[str] = None  # 현재가
    shar: Optional[str] = None  # 발행주식
    valx: Optional[str] = None  # 시가총액
    plow: Optional[str] = None  # 저가
    phigh: Optional[str] = None  # 고가
    popen: Optional[str] = None  # 시가
    tvol: Optional[str] = None  # 거래량
    rate: Optional[str] = None  # 등락율
    diff: Optional[str] = None  # 대비
    sign: Optional[str] = None  # 기호
    avol: Optional[str] = None  # 거래대금
    eps: Optional[str] = None  # EPS
    per: Optional[str] = None  # PER
    rank: Optional[str] = None  # 순위
    e_ordyn: Optional[str] = None  # 매매가능
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NewHighlow(SQLModel, table=True):
    """Output table for new_highlow"""
    __tablename__ = "kis_new_highlow"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태정보
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    tvol: Optional[str] = None  # 거래량
    pask: Optional[str] = None  # 매도호가
    pbid: Optional[str] = None  # 매수호가
    n_base: Optional[str] = None  # 기준가
    n_diff: Optional[str] = None  # 기준가대비
    n_rate: Optional[str] = None  # 기준가대비율
    ename: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    tamt: Optional[str] = None  # 거래대금
    nhgh: Optional[str] = None  # 신고가
    nlow: Optional[str] = None  # 신저가
    rank: Optional[str] = None  # 순위
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OrderResvList(SQLModel, table=True):
    """Output table for order_resv_list"""
    __tablename__ = "kis_order_resv_list"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    cncl_yn: Optional[str] = None  # 취소여부
    rsvn_ord_rcit_dt: Optional[str] = None  # 예약주문접수일자
    ovrs_rsvn_odno: Optional[str] = None  # 해외예약주문번호
    ord_dt: Optional[str] = None  # 주문일자
    ord_gno_brno: Optional[str] = None  # 주문채번지점번호
    odno: Optional[str] = None  # 주문번호
    sll_buy_dvsn_cd: Optional[str] = None  # 매도매수구분코드
    sll_buy_dvsn_cd_name: Optional[str] = None  # 매도매수구분명
    ovrs_rsvn_ord_stat_cd: Optional[str] = None  # 해외예약주문상태코드
    ovrs_rsvn_ord_stat_cd_name: Optional[str] = None  # 해외예약주문상태코드명
    pdno: Optional[str] = None  # 상품번호
    prdt_type_cd: Optional[str] = None  # 상품유형코드
    prdt_name: Optional[str] = None  # 상품명
    ord_rcit_tmd: Optional[str] = None  # 주문접수시각
    ord_fwdg_tmd: Optional[str] = None  # 주문전송시각
    tr_dvsn_name: Optional[str] = None  # 거래구분명
    ovrs_excg_cd: Optional[str] = None  # 해외거래소코드
    tr_mket_name: Optional[str] = None  # 거래시장명
    ord_stfno: Optional[str] = None  # 주문직원번호
    ft_ord_qty: Optional[str] = None  # FT주문수량
    ft_ord_unpr3: Optional[str] = None  # FT주문단가3
    ft_ccld_qty: Optional[str] = None  # FT체결수량
    nprc_rson_text: Optional[str] = None  # 미처리사유내용
    splt_buy_attr_name: Optional[str] = None  # 분할매수속성명
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Price(SQLModel, table=True):
    """Output table for price"""
    __tablename__ = "kis_price"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    rsym: Optional[str] = None  # 실시간조회종목코드
    zdiv: Optional[str] = None  # 소수점자리수
    base: Optional[str] = None  # 전일종가
    pvol: Optional[str] = None  # 전일거래량
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 대비기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    tvol: Optional[str] = None  # 거래량
    tamt: Optional[str] = None  # 거래대금
    ordy: Optional[str] = None  # 매수가능여부
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PriceDetail(SQLModel, table=True):
    """Output table for price_detail"""
    __tablename__ = "kis_price_detail"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    rsym: Optional[str] = None  # 실시간조회종목코드
    pvol: Optional[str] = None  # 전일거래량
    open: Optional[str] = None  # 시가
    high: Optional[str] = None  # 고가
    low: Optional[str] = None  # 저가
    last: Optional[str] = None  # 현재가
    base: Optional[str] = None  # 전일종가
    tomv: Optional[str] = None  # 시가총액
    pamt: Optional[str] = None  # 전일거래대금
    uplp: Optional[str] = None  # 상한가
    dnlp: Optional[str] = None  # 하한가
    h52p: Optional[str] = None  # 52주최고가
    h52d: Optional[str] = None  # 52주최고일자
    l52p: Optional[str] = None  # 52주최저가
    l52d: Optional[str] = None  # 52주최저일자
    perx: Optional[str] = None  # PER
    pbrx: Optional[str] = None  # PBR
    epsx: Optional[str] = None  # EPS
    bpsx: Optional[str] = None  # BPS
    shar: Optional[str] = None  # 상장주수
    mcap: Optional[str] = None  # 자본금
    curr: Optional[str] = None  # 통화
    zdiv: Optional[str] = None  # 소수점자리수
    vnit: Optional[str] = None  # 매매단위
    t_xprc: Optional[str] = None  # 원환산당일가격
    t_xdif: Optional[str] = None  # 원환산당일대비
    t_xrat: Optional[str] = None  # 원환산당일등락
    p_xprc: Optional[str] = None  # 원환산전일가격
    p_xdif: Optional[str] = None  # 원환산전일대비
    p_xrat: Optional[str] = None  # 원환산전일등락
    t_rate: Optional[str] = None  # 당일환율
    p_rate: Optional[str] = None  # 전일환율
    t_xsgn: Optional[str] = None  # 원환산당일기호
    p_xsng: Optional[str] = None  # 원환산전일기호
    e_ordyn: Optional[str] = None  # 거래가능여부
    e_hogau: Optional[str] = None  # 호가단위
    e_icod: Optional[str] = None  # 업종(섹터)
    e_parp: Optional[str] = None  # 액면가
    tvol: Optional[str] = None  # 거래량
    tamt: Optional[str] = None  # 거래대금
    etyp_nm: Optional[str] = None  # ETP 분류명
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PriceFluct(SQLModel, table=True):
    """Output table for price_fluct"""
    __tablename__ = "kis_price_fluct"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    knam: Optional[str] = None  # 종목명
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    tvol: Optional[str] = None  # 거래량
    pask: Optional[str] = None  # 매도호가
    pbid: Optional[str] = None  # 매수호가
    n_base: Optional[str] = None  # 기준가격
    n_diff: Optional[str] = None  # 기준가격대비
    n_rate: Optional[str] = None  # 기준가격대비율
    enam: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    tamt: Optional[str] = None  # 거래대금
    n_last: Optional[str] = None  # 기준현재가
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class QuotInquireCcnl(SQLModel, table=True):
    """Output table for quot_inquire_ccnl"""
    __tablename__ = "kis_quot_inquire_ccnl"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    vpow: Optional[str] = None  # 체결강도
    evol: Optional[str] = None  # 체결량
    khms: Optional[str] = None  # 한국기준시간
    tvol: Optional[str] = None  # 거래량
    last: Optional[str] = None  # 체결가
    mtyp: Optional[str] = None  # 시장구분
    sign: Optional[str] = None  # 기호
    pbid: Optional[str] = None  # 매수호가
    diff: Optional[str] = None  # 대비
    pask: Optional[str] = None  # 매도호가
    rate: Optional[str] = None  # 등락율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class RightsByIce(SQLModel, table=True):
    """Output table for rights_by_ice"""
    __tablename__ = "kis_rights_by_ice"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    anno_dt: Optional[str] = None  # ICE공시일
    ca_title: Optional[str] = None  # 권리유형
    div_lock_dt: Optional[str] = None  # 배당락일
    pay_dt: Optional[str] = None  # 지급일
    record_dt: Optional[str] = None  # 기준일
    validity_dt: Optional[str] = None  # 효력일자
    local_end_dt: Optional[str] = None  # 현지지시마감일
    lock_dt: Optional[str] = None  # 권리락일
    delist_dt: Optional[str] = None  # 상장폐지일
    redempt_dt: Optional[str] = None  # 상환일자
    early_redempt_dt: Optional[str] = None  # 조기상환일자
    effective_dt: Optional[str] = None  # 적용일
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TradeGrowth(SQLModel, table=True):
    """Output table for trade_growth"""
    __tablename__ = "kis_trade_growth"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태정보
    crec: Optional[str] = None  # 현재조회종목수
    trec: Optional[str] = None  # 전체조회종목수
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    pask: Optional[str] = None  # 매도호가
    pbid: Optional[str] = None  # 매수호가
    tvol: Optional[str] = None  # 거래량
    n_tvol: Optional[str] = None  # 평균거래량
    n_rate: Optional[str] = None  # 증가율
    rank: Optional[str] = None  # 순위
    ename: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    tamt: Optional[str] = None  # 거래대금
    n_diff: Optional[str] = None  # 증가량
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TradePbmn(SQLModel, table=True):
    """Output table for trade_pbmn"""
    __tablename__ = "kis_trade_pbmn"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태정보
    crec: Optional[str] = None  # 현재조회종목수
    trec: Optional[str] = None  # 전체조회종목수
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    pask: Optional[str] = None  # 매도호가
    pbid: Optional[str] = None  # 매수호가
    tvol: Optional[str] = None  # 거래량
    tamt: Optional[str] = None  # 거래대금
    a_tamt: Optional[str] = None  # 평균거래대금
    rank: Optional[str] = None  # 순위
    ename: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TradeTurnover(SQLModel, table=True):
    """Output table for trade_turnover"""
    __tablename__ = "kis_trade_turnover"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태정보
    crec: Optional[str] = None  # 현재조회종목수
    trec: Optional[str] = None  # 전체조회종목수
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    tvol: Optional[str] = None  # 거래량
    pask: Optional[str] = None  # 매도호가
    pbid: Optional[str] = None  # 매수호가
    n_tvol: Optional[str] = None  # 평균거래량
    shar: Optional[str] = None  # 상장주식수
    tover: Optional[str] = None  # 회전율
    rank: Optional[str] = None  # 순위
    ename: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    tamt: Optional[str] = None  # 거래대금
    trat: Optional[str] = None  # 회전율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TradeVol(SQLModel, table=True):
    """Output table for trade_vol"""
    __tablename__ = "kis_trade_vol"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태정보
    crec: Optional[str] = None  # 현재조회종목수
    trec: Optional[str] = None  # 전체조회종목수
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    pask: Optional[str] = None  # 매도호가
    pbid: Optional[str] = None  # 매수호가
    tvol: Optional[str] = None  # 거래량
    tamt: Optional[str] = None  # 거래대금
    a_tvol: Optional[str] = None  # 평균거래량
    rank: Optional[str] = None  # 순위
    ename: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class VolumeSurge(SQLModel, table=True):
    """Output table for volume_surge"""
    __tablename__ = "kis_volume_surge"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    api_name: str = Field(index=True)
    
    zdiv: Optional[str] = None  # 소수점자리수
    stat: Optional[str] = None  # 거래상태
    nrec: Optional[str] = None  # RecordCount
    rsym: Optional[str] = None  # 실시간조회심볼
    excd: Optional[str] = None  # 거래소코드
    symb: Optional[str] = None  # 종목코드
    knam: Optional[str] = None  # 종목명
    name: Optional[str] = None  # 종목명
    last: Optional[str] = None  # 현재가
    sign: Optional[str] = None  # 기호
    diff: Optional[str] = None  # 대비
    rate: Optional[str] = None  # 등락율
    tvol: Optional[str] = None  # 거래량
    pask: Optional[str] = None  # 매도호가
    pbid: Optional[str] = None  # 매수호가
    n_tvol: Optional[str] = None  # 기준거래량
    n_diff: Optional[str] = None  # 증가량
    n_rate: Optional[str] = None  # 증가율
    enam: Optional[str] = None  # 영문종목명
    e_ordyn: Optional[str] = None  # 매매가능
    tamt: Optional[str] = None  # 거래대금
    trat: Optional[str] = None  # 거래량비율
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


# ===== Master Data Tables =====

class DomFutureMst(SQLModel, table=True):
    """국내 지수선물옵션 종목 마스터 테이블"""
    __tablename__ = "kis_dom_future_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # 마스터 데이터 필드 (fo_idx_code_mts.mst)
    product_type: Optional[str] = Field(default=None, description="상품종류")
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, description="한글종목명")
    atm_division: Optional[str] = Field(default=None, description="ATM구분")
    strike_price: Optional[str] = Field(default=None, description="행사가")
    month_code: Optional[str] = Field(default=None, description="월물구분코드")
    underlying_short_code: Optional[str] = Field(default=None, description="기초자산단축코드")
    underlying_name: Optional[str] = Field(default=None, description="기초자산명")
    
    # 관리 필드
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OverFutureMst(SQLModel, table=True):
    """해외선물옵션 종목 마스터 테이블"""
    __tablename__ = "kis_over_future_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # 마스터 데이터 필드 (ffcode.mst)
    symbol_code: Optional[str] = Field(default=None, description="종목코드", index=True)
    auto_order_yn: Optional[str] = Field(default=None, description="서버자동주문가능종목여부")
    twap_order_yn: Optional[str] = Field(default=None, description="서버자동주문TWAP가능종목여부")
    econ_order_yn: Optional[str] = Field(default=None, description="서버자동경제지표주문가능종목여부")
    filler: Optional[str] = Field(default=None, description="필러")
    kor_name: Optional[str] = Field(default=None, description="종목한글명")
    exchange_code: Optional[str] = Field(default=None, description="거래소코드", index=True)
    item_code: Optional[str] = Field(default=None, description="품목코드")
    item_type: Optional[str] = Field(default=None, description="품목종류")
    display_decimal: Optional[str] = Field(default=None, description="출력소수점")
    calc_decimal: Optional[str] = Field(default=None, description="계산소수점")
    tick_size: Optional[str] = Field(default=None, description="틱사이즈")
    tick_value: Optional[str] = Field(default=None, description="틱가치")
    contract_size: Optional[str] = Field(default=None, description="계약크기")
    price_notation: Optional[str] = Field(default=None, description="가격표시진법")
    conversion_multiplier: Optional[str] = Field(default=None, description="환산승수")
    most_active_yn: Optional[str] = Field(default=None, description="최다월물여부")
    nearest_month_yn: Optional[str] = Field(default=None, description="최근월물여부")
    spread_yn: Optional[str] = Field(default=None, description="스프레드여부")
    spread_leg1_yn: Optional[str] = Field(default=None, description="스프레드기준종목LEG1여부")
    sub_exchange_code: Optional[str] = Field(default=None, description="서브거래소코드")
    
    # 관리 필드
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomStockFutureMst(SQLModel, table=True):
    """국내 주식선물옵션 종목 마스터 테이블"""
    __tablename__ = "kis_dom_stock_future_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # 마스터 데이터 필드 (fo_stk_code_mts.mst)
    product_type: Optional[str] = Field(default=None, description="상품종류")
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, description="한글종목명")
    atm_division: Optional[str] = Field(default=None, description="ATM구분")
    strike_price: Optional[str] = Field(default=None, description="행사가")
    month_code: Optional[str] = Field(default=None, description="월물구분코드")
    underlying_short_code: Optional[str] = Field(default=None, description="기초자산단축코드")
    underlying_name: Optional[str] = Field(default=None, description="기초자산명")
    
    # 관리 필드
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OverStockMst(SQLModel, table=True):
    """해외주식 종목 마스터 테이블"""
    __tablename__ = "kis_over_stock_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # 마스터 데이터 필드 (*mst.cod - 나스닥, 뉴욕, 아멕스, 상해, 심천, 도쿄, 홍콩, 하노이, 호치민 등)
    national_code: Optional[str] = Field(default=None, description="국가코드")
    exchange_id: Optional[str] = Field(default=None, description="거래소ID")
    exchange_code: Optional[str] = Field(default=None, description="거래소코드", index=True)
    exchange_name: Optional[str] = Field(default=None, description="거래소명")
    symbol: Optional[str] = Field(default=None, description="심볼", index=True)
    realtime_symbol: Optional[str] = Field(default=None, description="실시간심볼")
    korea_name: Optional[str] = Field(default=None, description="한글명")
    english_name: Optional[str] = Field(default=None, description="영문명")
    security_type: Optional[str] = Field(default=None, description="증권타입(1:지수,2:주식,3:ETP,4:워런트)")
    currency: Optional[str] = Field(default=None, description="통화")
    float_position: Optional[str] = Field(default=None, description="소수점자리")
    data_type: Optional[str] = Field(default=None, description="데이터타입")
    base_price: Optional[str] = Field(default=None, description="기준가")
    bid_order_size: Optional[str] = Field(default=None, description="매수호가수량")
    ask_order_size: Optional[str] = Field(default=None, description="매도호가수량")
    market_start_time: Optional[str] = Field(default=None, description="장시작시간(HHMM)")
    market_end_time: Optional[str] = Field(default=None, description="장종료시간(HHMM)")
    dr_yn: Optional[str] = Field(default=None, description="DR여부(Y/N)")
    dr_country_code: Optional[str] = Field(default=None, description="DR국가코드")
    industry_code: Optional[str] = Field(default=None, description="업종분류코드")
    index_constituent_yn: Optional[str] = Field(default=None, description="지수구성종목존재여부(0:없음,1:있음)")
    tick_size_type: Optional[str] = Field(default=None, description="틱사이즈타입")
    division_code: Optional[str] = Field(default=None, description="구분코드(001:ETF,002:ETN,003:ETC,004:Others,005:VIX_ETF,006:VIX_ETN)")
    tick_size_type_detail: Optional[str] = Field(default=None, description="틱사이즈타입상세")
    
    # 관리 필드
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomBondMst(SQLModel, table=True):
    """국내 채권 종목 마스터 테이블"""
    __tablename__ = "kis_dom_bond_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    bond_type: Optional[str] = Field(default=None, description="유형 (A0:장내소매채권, F9:주식관련사채/소액채권, C0:국고채권)")
    bond_cls_code: Optional[str] = Field(default=None, description="채권분류코드")
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, description="종목명")
    bond_int_cls_code: Optional[str] = Field(default=None, description="채권이자분류코드")
    listed_date: Optional[str] = Field(default=None, description="상장일")
    public_date: Optional[str] = Field(default=None, description="발행일")
    redemption_date: Optional[str] = Field(default=None, description="상환일")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomCmeFutureMst(SQLModel, table=True):
    """CME연계 야간선물 종목 마스터 테이블"""
    __tablename__ = "kis_dom_cme_future_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    product_type: Optional[str] = Field(default=None, description="상품종류")
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, description="한글종목명")
    strike_price: Optional[str] = Field(default=None, description="행사가")
    underlying_short_code: Optional[str] = Field(default=None, description="기초자산단축코드")
    underlying_name: Optional[str] = Field(default=None, description="기초자산명")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomComFutureMst(SQLModel, table=True):
    """상품선물옵션 종목 마스터 테이블"""
    __tablename__ = "kis_dom_com_future_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    product_class: Optional[str] = Field(default=None, description="상품구분")
    product_type: Optional[str] = Field(default=None, description="상품종류")
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, description="한글종목명")
    month_code: Optional[str] = Field(default=None, description="월물구분코드")
    underlying_short_code: Optional[str] = Field(default=None, description="기초자산단축코드")
    underlying_name: Optional[str] = Field(default=None, description="기초자산명")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomElwMst(SQLModel, table=True):
    """국내 ELW 종목 마스터 테이블"""
    __tablename__ = "kis_dom_elw_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, description="한글종목명")
    elw_right_type: Optional[str] = Field(default=None, description="ELW권리형태 (0:표준옵션, 1:디지털옵션, 2:조기종료옵션)")
    elw_early_end_price: Optional[str] = Field(default=None, description="ELW조기종료발생기준가격")
    basket_yn: Optional[str] = Field(default=None, description="바스켓여부")
    underlying_code1: Optional[str] = Field(default=None, description="기초자산코드1")
    underlying_code2: Optional[str] = Field(default=None, description="기초자산코드2")
    underlying_code3: Optional[str] = Field(default=None, description="기초자산코드3")
    underlying_code4: Optional[str] = Field(default=None, description="기초자산코드4")
    underlying_code5: Optional[str] = Field(default=None, description="기초자산코드5")
    issuer_name: Optional[str] = Field(default=None, description="발행사한글종목명")
    issuer_code: Optional[str] = Field(default=None, description="발행사코드")
    strike_price: Optional[str] = Field(default=None, description="행사가")
    last_trade_date: Optional[str] = Field(default=None, description="최종거래일")
    remain_days: Optional[str] = Field(default=None, description="잔존일수")
    right_type_code: Optional[str] = Field(default=None, description="권리유형구분코드")
    payment_date: Optional[str] = Field(default=None, description="지급일")
    prev_market_cap: Optional[str] = Field(default=None, description="전일시가총액")
    listed_shares: Optional[str] = Field(default=None, description="상장주수")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomEurexOptionMst(SQLModel, table=True):
    """EUREX연계 야간옵션 종목 마스터 테이블"""
    __tablename__ = "kis_dom_eurex_option_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    product_type: Optional[str] = Field(default=None, description="상품종류")
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, description="한글종목명")
    atm_division: Optional[str] = Field(default=None, description="ATM구분")
    strike_price: Optional[str] = Field(default=None, description="행사가")
    underlying_short_code: Optional[str] = Field(default=None, description="기초자산단축코드")
    underlying_name: Optional[str] = Field(default=None, description="기초자산명")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomKonexMst(SQLModel, table=True):
    """코넥스 종목 마스터 테이블"""
    __tablename__ = "kis_dom_konex_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, description="종목명")
    group_code: Optional[str] = Field(default=None, description="증권그룹구분코드 (KN:코넥스)")
    base_price: Optional[str] = Field(default=None, description="주식기준가")
    
    # 추가 주요 컬럼
    listed_date: Optional[str] = Field(default=None, description="상장일자")
    listed_shares: Optional[str] = Field(default=None, description="상장주수")
    capital: Optional[str] = Field(default=None, description="자본금")
    face_value: Optional[str] = Field(default=None, description="액면가")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomKosdaqMst(SQLModel, table=True):
    """코스닥 종목 마스터 테이블"""
    __tablename__ = "kis_dom_kosdaq_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, description="한글종목명")
    group_code: Optional[str] = Field(default=None, description="증권그룹구분코드 (ST:주권, MF:증권투자회사, RT:부동산투자회사, SC:선박투자회사, IF:사회간접자본투융자회사, DR:주식예탁증서, EW:ELW, EF:ETF, SW:신주인수권증권, SR:신주인수권증서, BC:수익증권, FE:해외ETF, FS:외국주권)")
    market_cap_scale: Optional[str] = Field(default=None, description="시가총액규모")
    industry_code_l: Optional[str] = Field(default=None, description="지수업종대분류")
    industry_code_m: Optional[str] = Field(default=None, description="지수업종중분류")
    industry_code_s: Optional[str] = Field(default=None, description="지수업종소분류")
    
    # 추가 주요 컬럼
    base_price: Optional[str] = Field(default=None, description="기준가")
    listed_date: Optional[str] = Field(default=None, description="상장일자")
    listed_shares: Optional[str] = Field(default=None, description="상장주수")
    capital: Optional[str] = Field(default=None, description="자본금")
    face_value: Optional[str] = Field(default=None, description="액면가")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomKospiMst(SQLModel, table=True):
    """코스피 종목 마스터 테이블"""
    __tablename__ = "kis_dom_kospi_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, description="한글명")
    group_code: Optional[str] = Field(default=None, description="증권그룹구분코드 (ST:주권, MF:증권투자회사, RT:부동산투자회사, SC:선박투자회사, IF:사회간접자본투융자회사, DR:주식예탁증서, EW:ELW, EF:ETF, SW:신주인수권증권, SR:신주인수권증서, BC:수익증권, FE:해외ETF, FS:외국주권)")
    market_cap_scale: Optional[str] = Field(default=None, description="시가총액규모")
    industry_code_l: Optional[str] = Field(default=None, description="지수업종대분류")
    industry_code_m: Optional[str] = Field(default=None, description="지수업종중분류")
    industry_code_s: Optional[str] = Field(default=None, description="지수업종소분류")
    
    # 추가 주요 컬럼
    base_price: Optional[str] = Field(default=None, description="기준가")
    listed_date: Optional[str] = Field(default=None, description="상장일자")
    listed_shares: Optional[str] = Field(default=None, description="상장주수")
    capital: Optional[str] = Field(default=None, description="자본금")
    face_value: Optional[str] = Field(default=None, description="액면가")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MemberCodeMst(SQLModel, table=True):
    """회원사 코드 마스터 테이블"""
    __tablename__ = "kis_member_code_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    member_code: Optional[str] = Field(default=None, description="회원사코드", index=True)
    member_name: Optional[str] = Field(default=None, description="회원사명")
    region_code: Optional[str] = Field(default=None, description="구분 (0:국내, 1:외국)")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OverIndexMst(SQLModel, table=True):
    """해외주식 지수 마스터 테이블"""
    __tablename__ = "kis_over_index_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    division_code: Optional[str] = Field(default=None, description="구분코드 (W:세계주요지수, P:미국지수, Q:미국종목, H:세계주요종목, D:미국상장국내기업, G:유럽상장국내기업, F:CME선물, M:반도체, X:환율, C:상품선물, R:국내금리, L:리보금리, B:주요국정부채)")
    symbol: Optional[str] = Field(default=None, description="심볼", index=True)
    eng_name: Optional[str] = Field(default=None, description="영문명")
    kor_name: Optional[str] = Field(default=None, description="한글명")
    industry_code: Optional[str] = Field(default=None, description="종목업종코드")
    dow30_yn: Optional[str] = Field(default=None, description="다우30편입여부")
    nasdaq100_yn: Optional[str] = Field(default=None, description="나스닥100편입여부")
    sp500_yn: Optional[str] = Field(default=None, description="S&P500편입여부")
    exchange_code: Optional[str] = Field(default=None, description="거래소코드")
    nation_code: Optional[str] = Field(default=None, description="국가구분코드")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class SectorMst(SQLModel, table=True):
    """업종 코드 마스터 테이블"""
    __tablename__ = "kis_sector_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    sector_code: Optional[str] = Field(default=None, description="업종코드", index=True)
    sector_name: Optional[str] = Field(default=None, description="업종명")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ThemeMst(SQLModel, table=True):
    """테마 코드 마스터 테이블"""
    __tablename__ = "kis_theme_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    theme_code: Optional[str] = Field(default=None, description="테마코드", index=True)
    theme_name: Optional[str] = Field(default=None, description="테마명")
    stock_code: Optional[str] = Field(default=None, description="종목코드")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MetaTableMst(SQLModel, table=True):
    """테이블 메타데이터 (설명) 저장"""
    __tablename__ = "kis_meta_table_mst"
    
    table_name: str = Field(primary_key=True, description="테이블 이름")
    description: Optional[str] = Field(default=None, description="테이블 설명")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MetaColumnMst(SQLModel, table=True):
    """컬럼 메타데이터 (설명) 저장"""
    __tablename__ = "kis_meta_column_mst"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    table_name: str = Field(index=True, description="테이블 이름")
    column_name: str = Field(index=True, description="컬럼 이름")
    description: Optional[str] = Field(default=None, description="컬럼 설명")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
