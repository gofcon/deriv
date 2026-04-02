"""
models_kis.py - KIS API 관련 SQLModel 클래스 정의

KIS(한국투자증권) API 출력 테이블 및 마스터 데이터 테이블.
인프라/워크플로우 테이블(ApiMst, BrowserMst 등)은 models_gofcon.py 참조.
"""

from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime, func, Integer, Identity

try:
    from . import oracle_mapping  # noqa: F401
except ImportError:
    import oracle_mapping  # noqa: F401


# ===== KIS API 출력 테이블 =====

class KrxIsinMst(SQLModel, table=True):
    """Output table for KRX ISIN data"""
    __tablename__ = "krx_isin_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))
    api_name: str = Field(index=True)

    isin_code: Optional[str] = Field(default=None, max_length=100)
    item_name: Optional[str] = Field(default=None, max_length=200)



class StockPrice(SQLModel, table=True):
    """Output table for stock_price"""
    __tablename__ = "kis_stock_price"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))
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

    updated_at: Optional[datetime] = Field(default=None,
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()))


class DailyPrice(SQLModel, table=True):
    """Output table for daily_price"""
    __tablename__ = "kis_daily_price"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))
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

    updated_at: Optional[datetime] = Field(default=None,
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()))


class DisplayBoardTop(SQLModel, table=True):
    """Output table for display_board_top"""
    __tablename__ = "kis_display_board_top"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))
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

    updated_at: Optional[datetime] = Field(default=None,
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()))


# ===== Master Data Tables =====

class DomFutureMst(SQLModel, table=True):
    """국내 지수선물옵션 종목 마스터 테이블"""
    __tablename__ = "kis_dom_future_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    product_type: Optional[str] = Field(default=None, max_length=100, description="상품종류")
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, max_length=100, description="한글종목명")
    atm_division: Optional[str] = Field(default=None, max_length=100, description="ATM구분")
    strike_price: Optional[str] = Field(default=None, max_length=100, description="행사가")
    month_code: Optional[str] = Field(default=None, max_length=100, description="월물구분코드")
    underlying_short_code: Optional[str] = Field(default=None, max_length=100, description="기초자산단축코드")
    underlying_name: Optional[str] = Field(default=None, max_length=100, description="기초자산명")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OverFutureMst(SQLModel, table=True):
    """해외선물옵션 종목 마스터 테이블"""
    __tablename__ = "kis_over_future_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    symbol_code: Optional[str] = Field(default=None, description="종목코드", index=True)
    auto_order_yn: Optional[str] = Field(default=None, max_length=100, description="서버자동주문가능종목여부")
    twap_order_yn: Optional[str] = Field(default=None, max_length=100, description="서버자동주문TWAP가능종목여부")
    econ_order_yn: Optional[str] = Field(default=None, max_length=100, description="서버자동경제지표주문가능종목여부")
    filler: Optional[str] = Field(default=None, max_length=100, description="필러")
    kor_name: Optional[str] = Field(default=None, max_length=100, description="종목한글명")
    exchange_code: Optional[str] = Field(default=None, description="거래소코드", index=True)
    item_code: Optional[str] = Field(default=None, max_length=100, description="품목코드")
    item_type: Optional[str] = Field(default=None, max_length=100, description="품목종류")
    display_decimal: Optional[str] = Field(default=None, max_length=100, description="출력소수점")
    calc_decimal: Optional[str] = Field(default=None, max_length=100, description="계산소수점")
    tick_size: Optional[str] = Field(default=None, max_length=100, description="틱사이즈")
    tick_value: Optional[str] = Field(default=None, max_length=100, description="틱가치")
    contract_size: Optional[str] = Field(default=None, max_length=100, description="계약크기")
    price_notation: Optional[str] = Field(default=None, max_length=100, description="가격표시진법")
    conversion_multiplier: Optional[str] = Field(default=None, max_length=100, description="환산승수")
    most_active_yn: Optional[str] = Field(default=None, max_length=100, description="최다월물여부")
    nearest_month_yn: Optional[str] = Field(default=None, max_length=100, description="최근월물여부")
    spread_yn: Optional[str] = Field(default=None, max_length=100, description="스프레드여부")
    spread_leg1_yn: Optional[str] = Field(default=None, max_length=100, description="스프레드기준종목LEG1여부")
    sub_exchange_code: Optional[str] = Field(default=None, max_length=100, description="서브거래소코드")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomStockFutureMst(SQLModel, table=True):
    """국내 주식선물옵션 종목 마스터 테이블"""
    __tablename__ = "kis_dom_stock_future_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    product_type: Optional[str] = Field(default=None, max_length=100, description="상품종류")
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, max_length=100, description="한글종목명")
    atm_division: Optional[str] = Field(default=None, max_length=100, description="ATM구분")
    strike_price: Optional[str] = Field(default=None, max_length=100, description="행사가")
    month_code: Optional[str] = Field(default=None, max_length=100, description="월물구분코드")
    underlying_short_code: Optional[str] = Field(default=None, max_length=100, description="기초자산단축코드")
    underlying_name: Optional[str] = Field(default=None, max_length=100, description="기초자산명")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OverStockMst(SQLModel, table=True):
    """해외주식 종목 마스터 테이블"""
    __tablename__ = "kis_over_stock_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    national_code: Optional[str] = Field(default=None, max_length=100, description="국가코드")
    exchange_id: Optional[str] = Field(default=None, max_length=100, description="거래소ID")
    exchange_code: Optional[str] = Field(default=None, description="거래소코드", index=True)
    exchange_name: Optional[str] = Field(default=None, max_length=100, description="거래소명")
    symbol: Optional[str] = Field(default=None, description="심볼", index=True)
    realtime_symbol: Optional[str] = Field(default=None, max_length=100, description="실시간심볼")
    korea_name: Optional[str] = Field(default=None, max_length=100, description="한글명")
    english_name: Optional[str] = Field(default=None, max_length=100, description="영문명")
    security_type: Optional[str] = Field(default=None, max_length=100, description="증권타입(1:지수,2:주식,3:ETP,4:워런트)")
    currency: Optional[str] = Field(default=None, max_length=100, description="통화")
    float_position: Optional[str] = Field(default=None, max_length=100, description="소수점자리")
    data_type: Optional[str] = Field(default=None, max_length=100, description="데이터타입")
    base_price: Optional[str] = Field(default=None, max_length=100, description="기준가")
    bid_order_size: Optional[str] = Field(default=None, max_length=100, description="매수호가수량")
    ask_order_size: Optional[str] = Field(default=None, max_length=100, description="매도호가수량")
    market_start_time: Optional[str] = Field(default=None, max_length=100, description="장시작시간(HHMM)")
    market_end_time: Optional[str] = Field(default=None, max_length=100, description="장종료시간(HHMM)")
    dr_yn: Optional[str] = Field(default=None, max_length=100, description="DR여부(Y/N)")
    dr_country_code: Optional[str] = Field(default=None, max_length=100, description="DR국가코드")
    industry_code: Optional[str] = Field(default=None, max_length=100, description="업종분류코드")
    index_constituent_yn: Optional[str] = Field(default=None, max_length=100, description="지수구성종목존재여부(0:없음,1:있음)")
    tick_size_type: Optional[str] = Field(default=None, max_length=100, description="틱사이즈타입")
    division_code: Optional[str] = Field(default=None, max_length=100, description="구분코드(001:ETF,002:ETN,003:ETC,004:Others,005:VIX_ETF,006:VIX_ETN)")
    tick_size_type_detail: Optional[str] = Field(default=None, max_length=100, description="틱사이즈타입상세")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomBondMst(SQLModel, table=True):
    """국내 채권 종목 마스터 테이블"""
    __tablename__ = "kis_dom_bond_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    bond_type: Optional[str] = Field(default=None, max_length=100, description="유형 (A0:장내소매채권, F9:주식관련사채/소액채권, C0:국고채권)")
    bond_cls_code: Optional[str] = Field(default=None, max_length=100, description="채권분류코드")
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, max_length=100, description="종목명")
    bond_int_cls_code: Optional[str] = Field(default=None, max_length=100, description="채권이자분류코드")
    listed_date: Optional[str] = Field(default=None, max_length=100, description="상장일")
    public_date: Optional[str] = Field(default=None, max_length=100, description="발행일")
    redemption_date: Optional[str] = Field(default=None, max_length=100, description="상환일")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomCmeFutureMst(SQLModel, table=True):
    """CME연계 야간선물 종목 마스터 테이블"""
    __tablename__ = "kis_dom_cme_future_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    product_type: Optional[str] = Field(default=None, max_length=100, description="상품종류")
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, max_length=100, description="한글종목명")
    strike_price: Optional[str] = Field(default=None, max_length=100, description="행사가")
    underlying_short_code: Optional[str] = Field(default=None, max_length=100, description="기초자산단축코드")
    underlying_name: Optional[str] = Field(default=None, max_length=100, description="기초자산명")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomComFutureMst(SQLModel, table=True):
    """상품선물옵션 종목 마스터 테이블"""
    __tablename__ = "kis_dom_com_future_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    product_class: Optional[str] = Field(default=None, max_length=100, description="상품구분")
    product_type: Optional[str] = Field(default=None, max_length=100, description="상품종류")
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, max_length=100, description="한글종목명")
    month_code: Optional[str] = Field(default=None, max_length=100, description="월물구분코드")
    underlying_short_code: Optional[str] = Field(default=None, max_length=100, description="기초자산단축코드")
    underlying_name: Optional[str] = Field(default=None, max_length=100, description="기초자산명")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomElwMst(SQLModel, table=True):
    """국내 ELW 종목 마스터 테이블"""
    __tablename__ = "kis_dom_elw_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, max_length=100, description="한글종목명")
    elw_right_type: Optional[str] = Field(default=None, max_length=100, description="ELW권리형태 (0:표준옵션, 1:디지털옵션, 2:조기종료옵션)")
    elw_early_end_price: Optional[str] = Field(default=None, max_length=100, description="ELW조기종료발생기준가격")
    basket_yn: Optional[str] = Field(default=None, max_length=100, description="바스켓여부")
    underlying_code1: Optional[str] = Field(default=None, max_length=100, description="기초자산코드1")
    underlying_code2: Optional[str] = Field(default=None, max_length=100, description="기초자산코드2")
    underlying_code3: Optional[str] = Field(default=None, max_length=100, description="기초자산코드3")
    underlying_code4: Optional[str] = Field(default=None, max_length=100, description="기초자산코드4")
    underlying_code5: Optional[str] = Field(default=None, max_length=100, description="기초자산코드5")
    issuer_name: Optional[str] = Field(default=None, max_length=100, description="발행사한글종목명")
    issuer_code: Optional[str] = Field(default=None, max_length=100, description="발행사코드")
    strike_price: Optional[str] = Field(default=None, max_length=100, description="행사가")
    last_trade_date: Optional[str] = Field(default=None, max_length=100, description="최종거래일")
    remain_days: Optional[str] = Field(default=None, max_length=100, description="잔존일수")
    right_type_code: Optional[str] = Field(default=None, max_length=100, description="권리유형구분코드")
    payment_date: Optional[str] = Field(default=None, max_length=100, description="지급일")
    prev_market_cap: Optional[str] = Field(default=None, max_length=100, description="전일시가총액")
    listed_shares: Optional[str] = Field(default=None, max_length=100, description="상장주수")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomEurexOptionMst(SQLModel, table=True):
    """EUREX연계 야간옵션 종목 마스터 테이블"""
    __tablename__ = "kis_dom_eurex_option_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    product_type: Optional[str] = Field(default=None, max_length=100, description="상품종류")
    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, max_length=100, description="한글종목명")
    atm_division: Optional[str] = Field(default=None, max_length=100, description="ATM구분")
    strike_price: Optional[str] = Field(default=None, max_length=100, description="행사가")
    underlying_short_code: Optional[str] = Field(default=None, max_length=100, description="기초자산단축코드")
    underlying_name: Optional[str] = Field(default=None, max_length=100, description="기초자산명")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomKonexMst(SQLModel, table=True):
    """코넥스 종목 마스터 테이블"""
    __tablename__ = "kis_dom_konex_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, max_length=100, description="종목명")
    group_code: Optional[str] = Field(default=None, max_length=100, description="증권그룹구분코드 (KN:코넥스)")
    base_price: Optional[str] = Field(default=None, max_length=100, description="주식기준가")
    listed_date: Optional[str] = Field(default=None, max_length=100, description="상장일자")
    listed_shares: Optional[str] = Field(default=None, max_length=100, description="상장주수")
    capital: Optional[str] = Field(default=None, max_length=100, description="자본금")
    face_value: Optional[str] = Field(default=None, max_length=100, description="액면가")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomKosdaqMst(SQLModel, table=True):
    """코스닥 종목 마스터 테이블"""
    __tablename__ = "kis_dom_kosdaq_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, max_length=100, description="한글종목명")
    group_code: Optional[str] = Field(default=None, max_length=100, description="증권그룹구분코드")
    market_cap_scale: Optional[str] = Field(default=None, max_length=100, description="시가총액규모")
    industry_code_l: Optional[str] = Field(default=None, max_length=100, description="지수업종대분류")
    industry_code_m: Optional[str] = Field(default=None, max_length=100, description="지수업종중분류")
    industry_code_s: Optional[str] = Field(default=None, max_length=100, description="지수업종소분류")
    base_price: Optional[str] = Field(default=None, max_length=100, description="기준가")
    listed_date: Optional[str] = Field(default=None, max_length=100, description="상장일자")
    listed_shares: Optional[str] = Field(default=None, max_length=100, description="상장주수")
    capital: Optional[str] = Field(default=None, max_length=100, description="자본금")
    face_value: Optional[str] = Field(default=None, max_length=100, description="액면가")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DomKospiMst(SQLModel, table=True):
    """코스피 종목 마스터 테이블"""
    __tablename__ = "kis_dom_kospi_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    short_code: Optional[str] = Field(default=None, description="단축코드", index=True)
    standard_code: Optional[str] = Field(default=None, description="표준코드", index=True)
    kor_name: Optional[str] = Field(default=None, max_length=100, description="한글명")
    group_code: Optional[str] = Field(default=None, max_length=100, description="증권그룹구분코드")
    market_cap_scale: Optional[str] = Field(default=None, max_length=100, description="시가총액규모")
    industry_code_l: Optional[str] = Field(default=None, max_length=100, description="지수업종대분류")
    industry_code_m: Optional[str] = Field(default=None, max_length=100, description="지수업종중분류")
    industry_code_s: Optional[str] = Field(default=None, max_length=100, description="지수업종소분류")
    base_price: Optional[str] = Field(default=None, max_length=100, description="기준가")
    listed_date: Optional[str] = Field(default=None, max_length=100, description="상장일자")
    listed_shares: Optional[str] = Field(default=None, max_length=100, description="상장주수")
    capital: Optional[str] = Field(default=None, max_length=100, description="자본금")
    face_value: Optional[str] = Field(default=None, max_length=100, description="액면가")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MemberCodeMst(SQLModel, table=True):
    """회원사 코드 마스터 테이블"""
    __tablename__ = "kis_member_code_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    member_code: Optional[str] = Field(default=None, description="회원사코드", index=True)
    member_name: Optional[str] = Field(default=None, max_length=100, description="회원사명")
    region_code: Optional[str] = Field(default=None, max_length=100, description="구분 (0:국내, 1:외국)")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OverIndexMst(SQLModel, table=True):
    """해외주식 지수 마스터 테이블"""
    __tablename__ = "kis_over_index_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    division_code: Optional[str] = Field(default=None, max_length=100, description="구분코드")
    symbol: Optional[str] = Field(default=None, description="심볼", index=True)
    eng_name: Optional[str] = Field(default=None, max_length=100, description="영문명")
    kor_name: Optional[str] = Field(default=None, max_length=100, description="한글명")
    industry_code: Optional[str] = Field(default=None, max_length=100, description="종목업종코드")
    dow30_yn: Optional[str] = Field(default=None, max_length=100, description="다우30편입여부")
    nasdaq100_yn: Optional[str] = Field(default=None, max_length=100, description="나스닥100편입여부")
    sp500_yn: Optional[str] = Field(default=None, max_length=100, description="S&P500편입여부")
    exchange_code: Optional[str] = Field(default=None, max_length=100, description="거래소코드")
    nation_code: Optional[str] = Field(default=None, max_length=100, description="국가구분코드")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class SectorMst(SQLModel, table=True):
    """업종 코드 마스터 테이블"""
    __tablename__ = "kis_sector_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    sector_code: Optional[str] = Field(default=None, description="업종코드", index=True)
    sector_name: Optional[str] = Field(default=None, max_length=100, description="업종명")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ThemeMst(SQLModel, table=True):
    """테마 코드 마스터 테이블"""
    __tablename__ = "kis_theme_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))

    theme_code: Optional[str] = Field(default=None, description="테마코드", index=True)
    theme_name: Optional[str] = Field(default=None, max_length=100, description="테마명")
    stock_code: Optional[str] = Field(default=None, max_length=100, description="종목코드")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MetaTableMst(SQLModel, table=True):
    """테이블 메타데이터 (설명) 저장"""
    __tablename__ = "kis_meta_table_mst"

    table_name: str = Field(primary_key=True, description="테이블 이름")
    description: Optional[str] = Field(default=None, max_length=500, description="테이블 설명")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MetaColumnMst(SQLModel, table=True):
    """컬럼 메타데이터 (설명) 저장"""
    __tablename__ = "kis_meta_column_mst"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1), primary_key=True))
    table_name: str = Field(index=True, description="테이블 이름")
    column_name: str = Field(index=True, description="컬럼 이름")
    description: Optional[str] = Field(default=None, max_length=500, description="컬럼 설명")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
