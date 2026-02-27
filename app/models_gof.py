"""
Auto-generated SQLModel classes from Oracle DDL.
"""

from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

class AfterHourBalance(SQLModel, table=True):
    __tablename__ = "after_hour_balance"

    id: int = Field(primary_key=True)
    api_name: str
    stck_shrn_iscd: Optional[str] = Field(default=None)
    data_rank: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    ovtm_total_askp_rsqn: Optional[str] = Field(default=None)
    ovtm_total_bidp_rsqn: Optional[str] = Field(default=None)
    mkob_otcp_vol: Optional[str] = Field(default=None)
    mkfa_otcp_vol: Optional[str] = Field(default=None)
    created_at: datetime


class AlgoOrdno(SQLModel, table=True):
    __tablename__ = "algo_ordno"

    id: int = Field(primary_key=True)
    api_name: str
    odno: Optional[str] = Field(default=None)
    trad_dvsn_name: Optional[str] = Field(default=None)
    pdno: Optional[str] = Field(default=None)
    item_name: Optional[str] = Field(default=None)
    ft_ord_qty: Optional[str] = Field(default=None)
    ft_ord_unpr3: Optional[str] = Field(default=None)
    splt_buy_attr_name: Optional[str] = Field(default=None)
    ft_ccld_qty: Optional[str] = Field(default=None)
    ord_gno_brno: Optional[str] = Field(default=None)
    created_at: datetime


class ApiMst(SQLModel, table=True):
    __tablename__ = "api_mst"

    api_name: str = Field(primary_key=True)
    api_url: str
    tr_id: str
    tr_cont: str
    request_type: str
    description: Optional[str] = Field(default=None)
    output_table_name: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class ApiParam(SQLModel, table=True):
    __tablename__ = "api_param"

    id: int = Field(primary_key=True)
    api_name: str
    param_name: str
    param_type: str
    is_required: int
    default_value: Optional[str] = Field(default=None)
    min_length: Optional[int] = Field(default=None)
    max_length: Optional[int] = Field(default=None)
    allowed_values: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    created_at: datetime


class AskingPrice(SQLModel, table=True):
    __tablename__ = "asking_price"

    id: int = Field(primary_key=True)
    api_name: str
    symb: Optional[str] = Field(default=None)
    zdiv: Optional[str] = Field(default=None)
    xymd: Optional[str] = Field(default=None)
    xhms: Optional[str] = Field(default=None)
    kymd: Optional[str] = Field(default=None)
    khms: Optional[str] = Field(default=None)
    bvol: Optional[str] = Field(default=None)
    avol: Optional[str] = Field(default=None)
    bdvl: Optional[str] = Field(default=None)
    advl: Optional[str] = Field(default=None)
    pbid1: Optional[str] = Field(default=None)
    pask1: Optional[str] = Field(default=None)
    vbid1: Optional[str] = Field(default=None)
    vask1: Optional[str] = Field(default=None)
    dbid1: Optional[str] = Field(default=None)
    dask1: Optional[str] = Field(default=None)
    created_at: datetime


class AskingPriceKrx(SQLModel, table=True):
    __tablename__ = "asking_price_krx"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    bsop_hour: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    askp2: Optional[str] = Field(default=None)
    askp3: Optional[str] = Field(default=None)
    askp4: Optional[str] = Field(default=None)
    askp5: Optional[str] = Field(default=None)
    askp6: Optional[str] = Field(default=None)
    askp7: Optional[str] = Field(default=None)
    askp8: Optional[str] = Field(default=None)
    askp9: Optional[str] = Field(default=None)
    askp10: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    bidp2: Optional[str] = Field(default=None)
    bidp3: Optional[str] = Field(default=None)
    bidp4: Optional[str] = Field(default=None)
    bidp5: Optional[str] = Field(default=None)
    bidp6: Optional[str] = Field(default=None)
    bidp7: Optional[str] = Field(default=None)
    bidp8: Optional[str] = Field(default=None)
    bidp9: Optional[str] = Field(default=None)
    bidp10: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    askp_rsqn2: Optional[str] = Field(default=None)
    askp_rsqn3: Optional[str] = Field(default=None)
    askp_rsqn4: Optional[str] = Field(default=None)
    askp_rsqn5: Optional[str] = Field(default=None)
    askp_rsqn6: Optional[str] = Field(default=None)
    askp_rsqn7: Optional[str] = Field(default=None)
    askp_rsqn8: Optional[str] = Field(default=None)
    askp_rsqn9: Optional[str] = Field(default=None)
    askp_rsqn10: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn2: Optional[str] = Field(default=None)
    bidp_rsqn3: Optional[str] = Field(default=None)
    bidp_rsqn4: Optional[str] = Field(default=None)
    bidp_rsqn5: Optional[str] = Field(default=None)
    bidp_rsqn6: Optional[str] = Field(default=None)
    bidp_rsqn7: Optional[str] = Field(default=None)
    bidp_rsqn8: Optional[str] = Field(default=None)
    bidp_rsqn9: Optional[str] = Field(default=None)
    bidp_rsqn10: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    ovtm_total_askp_rsqn: Optional[str] = Field(default=None)
    ovtm_total_bidp_rsqn: Optional[str] = Field(default=None)
    antc_cnpr: Optional[str] = Field(default=None)
    antc_cnqn: Optional[str] = Field(default=None)
    antc_vol: Optional[str] = Field(default=None)
    antc_cntg_vrss: Optional[str] = Field(default=None)
    antc_cntg_vrss_sign: Optional[str] = Field(default=None)
    antc_cntg_prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    total_askp_rsqn_icdc: Optional[str] = Field(default=None)
    total_bidp_rsqn_icdc: Optional[str] = Field(default=None)
    ovtm_total_askp_icdc: Optional[str] = Field(default=None)
    ovtm_total_bidp_icdc: Optional[str] = Field(default=None)
    stck_deal_cls_code: Optional[str] = Field(default=None)
    created_at: datetime


class AskingPriceNxt(SQLModel, table=True):
    __tablename__ = "asking_price_nxt"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    bsop_hour: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    askp2: Optional[str] = Field(default=None)
    askp3: Optional[str] = Field(default=None)
    askp4: Optional[str] = Field(default=None)
    askp5: Optional[str] = Field(default=None)
    askp6: Optional[str] = Field(default=None)
    askp7: Optional[str] = Field(default=None)
    askp8: Optional[str] = Field(default=None)
    askp9: Optional[str] = Field(default=None)
    askp10: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    bidp2: Optional[str] = Field(default=None)
    bidp3: Optional[str] = Field(default=None)
    bidp4: Optional[str] = Field(default=None)
    bidp5: Optional[str] = Field(default=None)
    bidp6: Optional[str] = Field(default=None)
    bidp7: Optional[str] = Field(default=None)
    bidp8: Optional[str] = Field(default=None)
    bidp9: Optional[str] = Field(default=None)
    bidp10: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    askp_rsqn2: Optional[str] = Field(default=None)
    askp_rsqn3: Optional[str] = Field(default=None)
    askp_rsqn4: Optional[str] = Field(default=None)
    askp_rsqn5: Optional[str] = Field(default=None)
    askp_rsqn6: Optional[str] = Field(default=None)
    askp_rsqn7: Optional[str] = Field(default=None)
    askp_rsqn8: Optional[str] = Field(default=None)
    askp_rsqn9: Optional[str] = Field(default=None)
    askp_rsqn10: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn2: Optional[str] = Field(default=None)
    bidp_rsqn3: Optional[str] = Field(default=None)
    bidp_rsqn4: Optional[str] = Field(default=None)
    bidp_rsqn5: Optional[str] = Field(default=None)
    bidp_rsqn6: Optional[str] = Field(default=None)
    bidp_rsqn7: Optional[str] = Field(default=None)
    bidp_rsqn8: Optional[str] = Field(default=None)
    bidp_rsqn9: Optional[str] = Field(default=None)
    bidp_rsqn10: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    ovtm_total_askp_rsqn: Optional[str] = Field(default=None)
    ovtm_total_bidp_rsqn: Optional[str] = Field(default=None)
    antc_cnpr: Optional[str] = Field(default=None)
    antc_cnqn: Optional[str] = Field(default=None)
    antc_vol: Optional[str] = Field(default=None)
    antc_cntg_vrss: Optional[str] = Field(default=None)
    antc_cntg_vrss_sign: Optional[str] = Field(default=None)
    antc_cntg_prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    total_askp_rsqn_icdc: Optional[str] = Field(default=None)
    total_bidp_rsqn_icdc: Optional[str] = Field(default=None)
    ovtm_total_askp_icdc: Optional[str] = Field(default=None)
    ovtm_total_bidp_icdc: Optional[str] = Field(default=None)
    stck_deal_cls_code: Optional[str] = Field(default=None)
    kmid_prc: Optional[str] = Field(default=None)
    kmid_total_rsqn: Optional[str] = Field(default=None)
    kmid_cls_code: Optional[str] = Field(default=None)
    nmid_prc: Optional[str] = Field(default=None)
    nmid_total_rsqn: Optional[str] = Field(default=None)
    nmid_cls_code: Optional[str] = Field(default=None)
    created_at: datetime


class AskingPriceTotal(SQLModel, table=True):
    __tablename__ = "asking_price_total"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    bsop_hour: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    askp2: Optional[str] = Field(default=None)
    askp3: Optional[str] = Field(default=None)
    askp4: Optional[str] = Field(default=None)
    askp5: Optional[str] = Field(default=None)
    askp6: Optional[str] = Field(default=None)
    askp7: Optional[str] = Field(default=None)
    askp8: Optional[str] = Field(default=None)
    askp9: Optional[str] = Field(default=None)
    askp10: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    bidp2: Optional[str] = Field(default=None)
    bidp3: Optional[str] = Field(default=None)
    bidp4: Optional[str] = Field(default=None)
    bidp5: Optional[str] = Field(default=None)
    bidp6: Optional[str] = Field(default=None)
    bidp7: Optional[str] = Field(default=None)
    bidp8: Optional[str] = Field(default=None)
    bidp9: Optional[str] = Field(default=None)
    bidp10: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    askp_rsqn2: Optional[str] = Field(default=None)
    askp_rsqn3: Optional[str] = Field(default=None)
    askp_rsqn4: Optional[str] = Field(default=None)
    askp_rsqn5: Optional[str] = Field(default=None)
    askp_rsqn6: Optional[str] = Field(default=None)
    askp_rsqn7: Optional[str] = Field(default=None)
    askp_rsqn8: Optional[str] = Field(default=None)
    askp_rsqn9: Optional[str] = Field(default=None)
    askp_rsqn10: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn2: Optional[str] = Field(default=None)
    bidp_rsqn3: Optional[str] = Field(default=None)
    bidp_rsqn4: Optional[str] = Field(default=None)
    bidp_rsqn5: Optional[str] = Field(default=None)
    bidp_rsqn6: Optional[str] = Field(default=None)
    bidp_rsqn7: Optional[str] = Field(default=None)
    bidp_rsqn8: Optional[str] = Field(default=None)
    bidp_rsqn9: Optional[str] = Field(default=None)
    bidp_rsqn10: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    ovtm_total_askp_rsqn: Optional[str] = Field(default=None)
    ovtm_total_bidp_rsqn: Optional[str] = Field(default=None)
    antc_cnpr: Optional[str] = Field(default=None)
    antc_cnqn: Optional[str] = Field(default=None)
    antc_vol: Optional[str] = Field(default=None)
    antc_cntg_vrss: Optional[str] = Field(default=None)
    antc_cntg_vrss_sign: Optional[str] = Field(default=None)
    antc_cntg_prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    total_askp_rsqn_icdc: Optional[str] = Field(default=None)
    total_bidp_rsqn_icdc: Optional[str] = Field(default=None)
    ovtm_total_askp_icdc: Optional[str] = Field(default=None)
    ovtm_total_bidp_icdc: Optional[str] = Field(default=None)
    stck_deal_cls_code: Optional[str] = Field(default=None)
    kmid_prc: Optional[str] = Field(default=None)
    kmid_total_rsqn: Optional[str] = Field(default=None)
    kmid_cls_code: Optional[str] = Field(default=None)
    nmid_prc: Optional[str] = Field(default=None)
    nmid_total_rsqn: Optional[str] = Field(default=None)
    nmid_cls_code: Optional[str] = Field(default=None)
    created_at: datetime


class AvgUnit(SQLModel, table=True):
    __tablename__ = "avg_unit"

    id: int = Field(primary_key=True)
    api_name: str
    evlu_dt: Optional[str] = Field(default=None)
    pdno: Optional[str] = Field(default=None)
    prdt_type_cd: Optional[str] = Field(default=None)
    kis_unpr: Optional[str] = Field(default=None)
    kbp_unpr: Optional[str] = Field(default=None)
    nice_evlu_unpr: Optional[str] = Field(default=None)
    fnp_unpr: Optional[str] = Field(default=None)
    avg_evlu_unpr: Optional[str] = Field(default=None)
    kis_crdt_grad_text: Optional[str] = Field(default=None)
    kbp_crdt_grad_text: Optional[str] = Field(default=None)
    nice_crdt_grad_text: Optional[str] = Field(default=None)
    fnp_crdt_grad_text: Optional[str] = Field(default=None)
    chng_yn: Optional[str] = Field(default=None)
    kis_erng_rt: Optional[str] = Field(default=None)
    kbp_erng_rt: Optional[str] = Field(default=None)
    nice_evlu_erng_rt: Optional[str] = Field(default=None)
    fnp_erng_rt: Optional[str] = Field(default=None)
    avg_evlu_erng_rt: Optional[str] = Field(default=None)
    kis_rf_unpr: Optional[str] = Field(default=None)
    kbp_rf_unpr: Optional[str] = Field(default=None)
    nice_evlu_rf_unpr: Optional[str] = Field(default=None)
    avg_evlu_rf_unpr: Optional[str] = Field(default=None)
    kis_evlu_amt: Optional[str] = Field(default=None)
    kbp_evlu_amt: Optional[str] = Field(default=None)
    nice_evlu_amt: Optional[str] = Field(default=None)
    fnp_evlu_amt: Optional[str] = Field(default=None)
    avg_evlu_amt: Optional[str] = Field(default=None)
    output3: Optional[str] = Field(default=None)
    kis_crcy_cd: Optional[str] = Field(default=None)
    kis_evlu_unit_pric: Optional[str] = Field(default=None)
    kis_evlu_pric: Optional[str] = Field(default=None)
    kbp_crcy_cd: Optional[str] = Field(default=None)
    kbp_evlu_unit_pric: Optional[str] = Field(default=None)
    kbp_evlu_pric: Optional[str] = Field(default=None)
    nice_crcy_cd: Optional[str] = Field(default=None)
    nice_evlu_unit_pric: Optional[str] = Field(default=None)
    nice_evlu_pric: Optional[str] = Field(default=None)
    avg_evlu_unit_pric: Optional[str] = Field(default=None)
    avg_evlu_pric: Optional[str] = Field(default=None)
    created_at: datetime


class BondAskingPrice(SQLModel, table=True):
    __tablename__ = "bond_asking_price"

    id: int = Field(primary_key=True)
    api_name: str
    stnd_iscd: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    askp_ert1: Optional[str] = Field(default=None)
    bidp_ert1: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    askp_ert2: Optional[str] = Field(default=None)
    bidp_ert2: Optional[str] = Field(default=None)
    askp2: Optional[str] = Field(default=None)
    bidp2: Optional[str] = Field(default=None)
    askp_rsqn2: Optional[str] = Field(default=None)
    bidp_rsqn2: Optional[str] = Field(default=None)
    askp_ert3: Optional[str] = Field(default=None)
    bidp_ert3: Optional[str] = Field(default=None)
    askp3: Optional[str] = Field(default=None)
    bidp3: Optional[str] = Field(default=None)
    askp_rsqn3: Optional[str] = Field(default=None)
    bidp_rsqn3: Optional[str] = Field(default=None)
    askp_ert4: Optional[str] = Field(default=None)
    bidp_ert4: Optional[str] = Field(default=None)
    askp4: Optional[str] = Field(default=None)
    bidp4: Optional[str] = Field(default=None)
    askp_rsqn4: Optional[str] = Field(default=None)
    bidp_rsqn4: Optional[str] = Field(default=None)
    askp_ert5: Optional[str] = Field(default=None)
    bidp_ert5: Optional[str] = Field(default=None)
    askp5: Optional[str] = Field(default=None)
    bidp5: Optional[str] = Field(default=None)
    askp_rsqn52: Optional[str] = Field(default=None)
    bidp_rsqn53: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    created_at: datetime


class BondCcnl(SQLModel, table=True):
    __tablename__ = "bond_ccnl"

    id: int = Field(primary_key=True)
    api_name: str
    stnd_iscd: Optional[str] = Field(default=None)
    bond_isnm: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    cntg_vol: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    stck_prdy_clpr: Optional[str] = Field(default=None)
    bond_cntg_ert: Optional[str] = Field(default=None)
    oprc_ert: Optional[str] = Field(default=None)
    hgpr_ert: Optional[str] = Field(default=None)
    lwpr_ert: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    prdy_vol: Optional[str] = Field(default=None)
    cntg_type_cls_code: Optional[str] = Field(default=None)
    created_at: datetime


class BondIndexCcnl(SQLModel, table=True):
    __tablename__ = "bond_index_ccnl"

    id: int = Field(primary_key=True)
    api_name: str
    nmix_id: Optional[str] = Field(default=None)
    stnd_date1: Optional[str] = Field(default=None)
    trnm_hour: Optional[str] = Field(default=None)
    totl_ernn_nmix_oprc: Optional[str] = Field(default=None)
    totl_ernn_nmix_hgpr: Optional[str] = Field(default=None)
    totl_ernn_nmix_lwpr: Optional[str] = Field(default=None)
    totl_ernn_nmix: Optional[str] = Field(default=None)
    prdy_totl_ernn_nmix: Optional[str] = Field(default=None)
    totl_ernn_nmix_prdy_vrss: Optional[str] = Field(default=None)
    totl_ernn_nmix_prdy_vrss_sign: Optional[str] = Field(default=None)
    totl_ernn_nmix_prdy_ctrt: Optional[str] = Field(default=None)
    clen_prc_nmix: Optional[str] = Field(default=None)
    mrkt_prc_nmix: Optional[str] = Field(default=None)
    bond_call_rnvs_nmix: Optional[str] = Field(default=None)
    bond_zero_rnvs_nmix: Optional[str] = Field(default=None)
    bond_futs_thpr: Optional[str] = Field(default=None)
    bond_avrg_drtn_val: Optional[str] = Field(default=None)
    bond_avrg_cnvx_val: Optional[str] = Field(default=None)
    bond_avrg_ytm_val: Optional[str] = Field(default=None)
    bond_avrg_frdl_ytm_val: Optional[str] = Field(default=None)
    created_at: datetime


class BrknewsTitle(SQLModel, table=True):
    __tablename__ = "brknews_title"

    id: int = Field(primary_key=True)
    api_name: str
    cntt_usiq_srno: Optional[str] = Field(default=None)
    news_ofer_entp_code: Optional[str] = Field(default=None)
    data_dt: Optional[str] = Field(default=None)
    data_tm: Optional[str] = Field(default=None)
    hts_pbnt_titl_cntt: Optional[str] = Field(default=None)
    news_lrdv_code: Optional[str] = Field(default=None)
    dorg: Optional[str] = Field(default=None)
    iscd1: Optional[str] = Field(default=None)
    iscd2: Optional[str] = Field(default=None)
    iscd3: Optional[str] = Field(default=None)
    iscd4: Optional[str] = Field(default=None)
    iscd5: Optional[str] = Field(default=None)
    iscd6: Optional[str] = Field(default=None)
    iscd7: Optional[str] = Field(default=None)
    iscd8: Optional[str] = Field(default=None)
    iscd9: Optional[str] = Field(default=None)
    iscd10: Optional[str] = Field(default=None)
    kor_isnm1: Optional[str] = Field(default=None)
    kor_isnm2: Optional[str] = Field(default=None)
    kor_isnm3: Optional[str] = Field(default=None)
    kor_isnm4: Optional[str] = Field(default=None)
    kor_isnm5: Optional[str] = Field(default=None)
    kor_isnm6: Optional[str] = Field(default=None)
    kor_isnm7: Optional[str] = Field(default=None)
    kor_isnm8: Optional[str] = Field(default=None)
    kor_isnm9: Optional[str] = Field(default=None)
    kor_isnm10: Optional[str] = Field(default=None)
    created_at: datetime


class BulkTransNum(SQLModel, table=True):
    __tablename__ = "bulk_trans_num"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    data_rank: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    shnu_cntg_csnu: Optional[str] = Field(default=None)
    seln_cntg_csnu: Optional[str] = Field(default=None)
    ntby_cnqn: Optional[str] = Field(default=None)
    created_at: datetime


class Buy(SQLModel, table=True):
    __tablename__ = "buy"

    id: int = Field(primary_key=True)
    api_name: str
    krx_fwdg_ord_orgno: Optional[str] = Field(default=None)
    odno: Optional[str] = Field(default=None)
    ord_tmd: Optional[str] = Field(default=None)
    created_at: datetime


class CaptureUplowprice(SQLModel, table=True):
    __tablename__ = "capture_uplowprice"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    prdy_vol: Optional[str] = Field(default=None)
    seln_cnqn: Optional[str] = Field(default=None)
    shnu_cnqn: Optional[str] = Field(default=None)
    stck_llam: Optional[str] = Field(default=None)
    stck_mxpr: Optional[str] = Field(default=None)
    prdy_vrss_vol_rate: Optional[str] = Field(default=None)
    created_at: datetime


class Ccnl(SQLModel, table=True):
    __tablename__ = "ccnl"

    id: int = Field(primary_key=True)
    api_name: str
    series_cd: Optional[str] = Field(default=None)
    bsns_date: Optional[str] = Field(default=None)
    mrkt_open_date: Optional[str] = Field(default=None)
    mrkt_open_time: Optional[str] = Field(default=None)
    mrkt_close_date: Optional[str] = Field(default=None)
    mrkt_close_time: Optional[str] = Field(default=None)
    prev_price: Optional[str] = Field(default=None)
    recv_date: Optional[str] = Field(default=None)
    recv_time: Optional[str] = Field(default=None)
    active_flag: Optional[str] = Field(default=None)
    last_price: Optional[str] = Field(default=None)
    last_qntt: Optional[str] = Field(default=None)
    prev_diff_price: Optional[str] = Field(default=None)
    prev_diff_rate: Optional[str] = Field(default=None)
    open_price: Optional[str] = Field(default=None)
    high_price: Optional[str] = Field(default=None)
    low_price: Optional[str] = Field(default=None)
    vol: Optional[str] = Field(default=None)
    prev_sign: Optional[str] = Field(default=None)
    quotsign: Optional[str] = Field(default=None)
    recv_time2: Optional[str] = Field(default=None)
    psttl_price: Optional[str] = Field(default=None)
    psttl_sign: Optional[str] = Field(default=None)
    psttl_diff_price: Optional[str] = Field(default=None)
    psttl_diff_rate: Optional[str] = Field(default=None)
    created_at: datetime


class CcnlKrx(SQLModel, table=True):
    __tablename__ = "ccnl_krx"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    wghn_avrg_stck_prc: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    cntg_vol: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    seln_cntg_csnu: Optional[str] = Field(default=None)
    shnu_cntg_csnu: Optional[str] = Field(default=None)
    ntby_cntg_csnu: Optional[str] = Field(default=None)
    cttr: Optional[str] = Field(default=None)
    seln_cntg_smtn: Optional[str] = Field(default=None)
    shnu_cntg_smtn: Optional[str] = Field(default=None)
    ccld_dvsn: Optional[str] = Field(default=None)
    shnu_rate: Optional[str] = Field(default=None)
    prdy_vol_vrss_acml_vol_rate: Optional[str] = Field(default=None)
    oprc_hour: Optional[str] = Field(default=None)
    oprc_vrss_prpr_sign: Optional[str] = Field(default=None)
    oprc_vrss_prpr: Optional[str] = Field(default=None)
    hgpr_hour: Optional[str] = Field(default=None)
    hgpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    hgpr_vrss_prpr: Optional[str] = Field(default=None)
    lwpr_hour: Optional[str] = Field(default=None)
    lwpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    lwpr_vrss_prpr: Optional[str] = Field(default=None)
    bsop_date: Optional[str] = Field(default=None)
    new_mkop_cls_code: Optional[str] = Field(default=None)
    trht_yn: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    vol_tnrt: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol_rate: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    mrkt_trtm_cls_code: Optional[str] = Field(default=None)
    vi_stnd_prc: Optional[str] = Field(default=None)
    created_at: datetime


class CcnlNotice(SQLModel, table=True):
    __tablename__ = "ccnl_notice"

    id: int = Field(primary_key=True)
    api_name: str
    cust_id: Optional[str] = Field(default=None)
    acnt_no: Optional[str] = Field(default=None)
    oder_no: Optional[str] = Field(default=None)
    ooder_no: Optional[str] = Field(default=None)
    seln_byov_cls: Optional[str] = Field(default=None)
    rctf_cls: Optional[str] = Field(default=None)
    oder_kind2: Optional[str] = Field(default=None)
    stck_shrn_iscd: Optional[str] = Field(default=None)
    cntg_qty: Optional[str] = Field(default=None)
    cntg_unpr: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    rfus_yn: Optional[str] = Field(default=None)
    cntg_yn: Optional[str] = Field(default=None)
    acpt_yn: Optional[str] = Field(default=None)
    brnc_no: Optional[str] = Field(default=None)
    oder_qty: Optional[str] = Field(default=None)
    acnt_name: Optional[str] = Field(default=None)
    cntg_isnm: Optional[str] = Field(default=None)
    oder_cond: Optional[str] = Field(default=None)
    debt_gb: Optional[str] = Field(default=None)
    debt_date: Optional[str] = Field(default=None)
    start_tm: Optional[str] = Field(default=None)
    end_tm: Optional[str] = Field(default=None)
    tm_div_tp: Optional[str] = Field(default=None)
    created_at: datetime


class CcnlNxt(SQLModel, table=True):
    __tablename__ = "ccnl_nxt"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    wghn_avrg_stck_prc: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    cntg_vol: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    seln_cntg_csnu: Optional[str] = Field(default=None)
    shnu_cntg_csnu: Optional[str] = Field(default=None)
    ntby_cntg_csnu: Optional[str] = Field(default=None)
    cttr: Optional[str] = Field(default=None)
    seln_cntg_smtn: Optional[str] = Field(default=None)
    shnu_cntg_smtn: Optional[str] = Field(default=None)
    cntg_cls_code: Optional[str] = Field(default=None)
    shnu_rate: Optional[str] = Field(default=None)
    prdy_vol_vrss_acml_vol_rate: Optional[str] = Field(default=None)
    oprc_hour: Optional[str] = Field(default=None)
    oprc_vrss_prpr_sign: Optional[str] = Field(default=None)
    oprc_vrss_prpr: Optional[str] = Field(default=None)
    hgpr_hour: Optional[str] = Field(default=None)
    hgpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    hgpr_vrss_prpr: Optional[str] = Field(default=None)
    lwpr_hour: Optional[str] = Field(default=None)
    lwpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    lwpr_vrss_prpr: Optional[str] = Field(default=None)
    bsop_date: Optional[str] = Field(default=None)
    new_mkop_cls_code: Optional[str] = Field(default=None)
    trht_yn: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    vol_tnrt: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol_rate: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    mrkt_trtm_cls_code: Optional[str] = Field(default=None)
    vi_stnd_prc: Optional[str] = Field(default=None)
    created_at: datetime


class CcnlTotal(SQLModel, table=True):
    __tablename__ = "ccnl_total"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    wghn_avrg_stck_prc: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    cntg_vol: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    seln_cntg_csnu: Optional[str] = Field(default=None)
    shnu_cntg_csnu: Optional[str] = Field(default=None)
    ntby_cntg_csnu: Optional[str] = Field(default=None)
    cttr: Optional[str] = Field(default=None)
    seln_cntg_smtn: Optional[str] = Field(default=None)
    shnu_cntg_smtn: Optional[str] = Field(default=None)
    cntg_cls_code: Optional[str] = Field(default=None)
    shnu_rate: Optional[str] = Field(default=None)
    prdy_vol_vrss_acml_vol_rate: Optional[str] = Field(default=None)
    oprc_hour: Optional[str] = Field(default=None)
    oprc_vrss_prpr_sign: Optional[str] = Field(default=None)
    oprc_vrss_prpr: Optional[str] = Field(default=None)
    hgpr_hour: Optional[str] = Field(default=None)
    hgpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    hgpr_vrss_prpr: Optional[str] = Field(default=None)
    lwpr_hour: Optional[str] = Field(default=None)
    lwpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    lwpr_vrss_prpr: Optional[str] = Field(default=None)
    bsop_date: Optional[str] = Field(default=None)
    new_mkop_cls_code: Optional[str] = Field(default=None)
    trht_yn: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    vol_tnrt: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol_rate: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    mrkt_trtm_cls_code: Optional[str] = Field(default=None)
    vi_stnd_prc: Optional[str] = Field(default=None)
    created_at: datetime


class ChkHoliday(SQLModel, table=True):
    __tablename__ = "chk_holiday"

    id: int = Field(primary_key=True)
    api_name: str
    bass_dt: Optional[str] = Field(default=None)
    wday_dvsn_cd: Optional[str] = Field(default=None)
    bzdy_yn: Optional[str] = Field(default=None)
    tr_day_yn: Optional[str] = Field(default=None)
    opnd_yn: Optional[str] = Field(default=None)
    sttl_day_yn: Optional[str] = Field(default=None)
    created_at: datetime


class ColableByCompany(SQLModel, table=True):
    __tablename__ = "colable_by_company"

    id: int = Field(primary_key=True)
    api_name: str
    pdno: Optional[str] = Field(default=None)
    ovrs_item_name: Optional[str] = Field(default=None)
    loan_rt: Optional[str] = Field(default=None)
    mgge_mntn_rt: Optional[str] = Field(default=None)
    mgge_ensu_rt: Optional[str] = Field(default=None)
    loan_exec_psbl_yn: Optional[str] = Field(default=None)
    stff_name: Optional[str] = Field(default=None)
    erlm_dt: Optional[str] = Field(default=None)
    tr_mket_name: Optional[str] = Field(default=None)
    crcy_cd: Optional[str] = Field(default=None)
    natn_kor_name: Optional[str] = Field(default=None)
    ovrs_excg_cd: Optional[str] = Field(default=None)
    loan_psbl_item_num: Optional[str] = Field(default=None)
    created_at: datetime


class CommodityFuturesRealtimeConclusion(SQLModel, table=True):
    __tablename__ = "commodity_futures_realtime_conclusion"

    id: int = Field(primary_key=True)
    api_name: str
    futs_shrn_iscd: Optional[str] = Field(default=None)
    bsop_hour: Optional[str] = Field(default=None)
    futs_prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    futs_prdy_ctrt: Optional[str] = Field(default=None)
    futs_prpr: Optional[str] = Field(default=None)
    futs_oprc: Optional[str] = Field(default=None)
    futs_hgpr: Optional[str] = Field(default=None)
    futs_lwpr: Optional[str] = Field(default=None)
    last_cnqn: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    hts_thpr: Optional[str] = Field(default=None)
    mrkt_basis: Optional[str] = Field(default=None)
    dprt: Optional[str] = Field(default=None)
    nmsc_fctn_stpl_prc: Optional[str] = Field(default=None)
    fmsc_fctn_stpl_prc: Optional[str] = Field(default=None)
    spead_prc: Optional[str] = Field(default=None)
    hts_otst_stpl_qty: Optional[str] = Field(default=None)
    otst_stpl_qty_icdc: Optional[str] = Field(default=None)
    oprc_hour: Optional[str] = Field(default=None)
    oprc_vrss_prpr_sign: Optional[str] = Field(default=None)
    oprc_vrss_nmix_prpr: Optional[str] = Field(default=None)
    hgpr_hour: Optional[str] = Field(default=None)
    hgpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    hgpr_vrss_nmix_prpr: Optional[str] = Field(default=None)
    lwpr_hour: Optional[str] = Field(default=None)
    lwpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    lwpr_vrss_nmix_prpr: Optional[str] = Field(default=None)
    shnu_rate: Optional[str] = Field(default=None)
    cttr: Optional[str] = Field(default=None)
    esdg: Optional[str] = Field(default=None)
    otst_stpl_rgbf_qty_icdc: Optional[str] = Field(default=None)
    thpr_basis: Optional[str] = Field(default=None)
    futs_askp1: Optional[str] = Field(default=None)
    futs_bidp1: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    seln_cntg_csnu: Optional[str] = Field(default=None)
    shnu_cntg_csnu: Optional[str] = Field(default=None)
    ntby_cntg_csnu: Optional[str] = Field(default=None)
    seln_cntg_smtn: Optional[str] = Field(default=None)
    shnu_cntg_smtn: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    prdy_vol_vrss_acml_vol_rate: Optional[str] = Field(default=None)
    dscs_bltr_acml_qty: Optional[str] = Field(default=None)
    dynm_mxpr: Optional[str] = Field(default=None)
    dynm_llam: Optional[str] = Field(default=None)
    dynm_prc_limt_yn: Optional[str] = Field(default=None)
    created_at: datetime


class CommodityFuturesRealtimeQuote(SQLModel, table=True):
    __tablename__ = "commodity_futures_realtime_quote"

    id: int = Field(primary_key=True)
    api_name: str
    futs_shrn_iscd: Optional[str] = Field(default=None)
    bsop_hour: Optional[str] = Field(default=None)
    futs_askp1: Optional[str] = Field(default=None)
    futs_askp2: Optional[str] = Field(default=None)
    futs_askp3: Optional[str] = Field(default=None)
    futs_askp4: Optional[str] = Field(default=None)
    futs_askp5: Optional[str] = Field(default=None)
    futs_bidp1: Optional[str] = Field(default=None)
    futs_bidp2: Optional[str] = Field(default=None)
    futs_bidp3: Optional[str] = Field(default=None)
    futs_bidp4: Optional[str] = Field(default=None)
    futs_bidp5: Optional[str] = Field(default=None)
    askp_csnu1: Optional[str] = Field(default=None)
    askp_csnu2: Optional[str] = Field(default=None)
    askp_csnu3: Optional[str] = Field(default=None)
    askp_csnu4: Optional[str] = Field(default=None)
    askp_csnu5: Optional[str] = Field(default=None)
    bidp_csnu1: Optional[str] = Field(default=None)
    bidp_csnu2: Optional[str] = Field(default=None)
    bidp_csnu3: Optional[str] = Field(default=None)
    bidp_csnu4: Optional[str] = Field(default=None)
    bidp_csnu5: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    askp_rsqn2: Optional[str] = Field(default=None)
    askp_rsqn3: Optional[str] = Field(default=None)
    askp_rsqn4: Optional[str] = Field(default=None)
    askp_rsqn5: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn2: Optional[str] = Field(default=None)
    bidp_rsqn3: Optional[str] = Field(default=None)
    bidp_rsqn4: Optional[str] = Field(default=None)
    bidp_rsqn5: Optional[str] = Field(default=None)
    total_askp_csnu: Optional[str] = Field(default=None)
    total_bidp_csnu: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    total_askp_rsqn_icdc: Optional[str] = Field(default=None)
    total_bidp_rsqn_icdc: Optional[str] = Field(default=None)
    created_at: datetime


class CompareStocks(SQLModel, table=True):
    __tablename__ = "compare_stocks"

    id: int = Field(primary_key=True)
    api_name: str
    elw_shrn_iscd: Optional[str] = Field(default=None)
    elw_kor_isnm: Optional[str] = Field(default=None)
    created_at: datetime


class CompInterest(SQLModel, table=True):
    __tablename__ = "comp_interest"

    id: int = Field(primary_key=True)
    api_name: str
    bcdt_code: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    bond_mnrt_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    bond_mnrt_prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    stck_bsop_date: Optional[str] = Field(default=None)
    bstp_nmix_prdy_ctrt: Optional[str] = Field(default=None)
    created_at: datetime


class CompProgramTradeDaily(SQLModel, table=True):
    __tablename__ = "comp_program_trade_daily"

    id: int = Field(primary_key=True)
    api_name: str
    stck_bsop_date: Optional[str] = Field(default=None)
    nabt_entm_seln_tr_pbmn: Optional[str] = Field(default=None)
    nabt_onsl_seln_vol: Optional[str] = Field(default=None)
    whol_onsl_seln_tr_pbmn: Optional[str] = Field(default=None)
    arbt_smtn_shnu_vol: Optional[str] = Field(default=None)
    nabt_smtn_shnu_tr_pbmn: Optional[str] = Field(default=None)
    arbt_entm_ntby_qty: Optional[str] = Field(default=None)
    nabt_entm_ntby_tr_pbmn: Optional[str] = Field(default=None)
    arbt_entm_seln_vol: Optional[str] = Field(default=None)
    nabt_entm_seln_vol_rate: Optional[str] = Field(default=None)
    nabt_onsl_seln_vol_rate: Optional[str] = Field(default=None)
    whol_onsl_seln_tr_pbmn_rate: Optional[str] = Field(default=None)
    arbt_smtm_shun_vol_rate: Optional[str] = Field(default=None)
    nabt_smtm_shun_tr_pbmn_rate: Optional[str] = Field(default=None)
    arbt_entm_ntby_qty_rate: Optional[str] = Field(default=None)
    nabt_entm_ntby_tr_pbmn_rate: Optional[str] = Field(default=None)
    arbt_entm_seln_vol_rate: Optional[str] = Field(default=None)
    nabt_entm_seln_tr_pbmn_rate: Optional[str] = Field(default=None)
    nabt_onsl_seln_tr_pbmn: Optional[str] = Field(default=None)
    whol_smtn_seln_vol: Optional[str] = Field(default=None)
    arbt_smtn_shnu_tr_pbmn: Optional[str] = Field(default=None)
    whol_entm_shnu_vol: Optional[str] = Field(default=None)
    arbt_entm_ntby_tr_pbmn: Optional[str] = Field(default=None)
    nabt_onsl_ntby_qty: Optional[str] = Field(default=None)
    arbt_entm_seln_tr_pbmn: Optional[str] = Field(default=None)
    whol_seln_vol_rate: Optional[str] = Field(default=None)
    whol_entm_shnu_vol_rate: Optional[str] = Field(default=None)
    whol_entm_seln_tr_pbmn: Optional[str] = Field(default=None)
    nabt_smtm_seln_vol: Optional[str] = Field(default=None)
    arbt_entm_shnu_vol: Optional[str] = Field(default=None)
    nabt_entm_shnu_tr_pbmn: Optional[str] = Field(default=None)
    whol_onsl_shnu_vol: Optional[str] = Field(default=None)
    arbt_onsl_ntby_tr_pbmn: Optional[str] = Field(default=None)
    nabt_smtn_ntby_qty: Optional[str] = Field(default=None)
    arbt_onsl_seln_vol: Optional[str] = Field(default=None)
    whol_entm_ntby_qty: Optional[str] = Field(default=None)
    nabt_onsl_ntby_tr_pbmn: Optional[str] = Field(default=None)
    arbt_onsl_seln_tr_pbmn: Optional[str] = Field(default=None)
    nabt_smtm_seln_tr_pbmn_rate: Optional[str] = Field(default=None)
    arbt_entm_shnu_vol_rate: Optional[str] = Field(default=None)
    nabt_entm_shnu_tr_pbmn_rate: Optional[str] = Field(default=None)
    whol_onsl_shnu_tr_pbmn: Optional[str] = Field(default=None)
    arbt_onsl_ntby_tr_pbmn_rate: Optional[str] = Field(default=None)
    nabt_smtm_ntby_qty_rate: Optional[str] = Field(default=None)
    arbt_onsl_seln_vol_rate: Optional[str] = Field(default=None)
    whol_entm_seln_vol: Optional[str] = Field(default=None)
    arbt_entm_shnu_tr_pbmn: Optional[str] = Field(default=None)
    nabt_onsl_shnu_vol: Optional[str] = Field(default=None)
    whol_smtn_shnu_vol: Optional[str] = Field(default=None)
    arbt_smtn_ntby_tr_pbmn: Optional[str] = Field(default=None)
    arbt_smtn_seln_vol: Optional[str] = Field(default=None)
    whol_entm_seln_tr_pbmn_rate: Optional[str] = Field(default=None)
    arbt_onsl_shnu_vol_rate: Optional[str] = Field(default=None)
    nabt_smtm_shun_vol_rate: Optional[str] = Field(default=None)
    whol_shun_tr_pbmn_rate: Optional[str] = Field(default=None)
    nabt_entm_ntby_qty_rate: Optional[str] = Field(default=None)
    arbt_smtm_seln_tr_pbmn_rate: Optional[str] = Field(default=None)
    arbt_onsl_shnu_vol: Optional[str] = Field(default=None)
    nabt_onsl_shnu_tr_pbmn: Optional[str] = Field(default=None)
    nabt_smtn_shnu_vol: Optional[str] = Field(default=None)
    whol_smtn_shnu_tr_pbmn: Optional[str] = Field(default=None)
    arbt_smtm_ntby_qty: Optional[str] = Field(default=None)
    nabt_smtn_ntby_tr_pbmn: Optional[str] = Field(default=None)
    arbt_smtn_seln_tr_pbmn: Optional[str] = Field(default=None)
    arbt_onsl_shnu_tr_pbmn_rate: Optional[str] = Field(default=None)
    whol_shun_vol_rate: Optional[str] = Field(default=None)
    arbt_smtm_ntby_tr_pbmn_rate: Optional[str] = Field(default=None)
    whol_entm_ntby_qty_rate: Optional[str] = Field(default=None)
    created_at: datetime


class CompProgramTradeToday(SQLModel, table=True):
    __tablename__ = "comp_program_trade_today"

    id: int = Field(primary_key=True)
    api_name: str
    stck_bsop_date: Optional[str] = Field(default=None)
    stck_clpr: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    whol_smtn_seln_vol: Optional[str] = Field(default=None)
    whol_smtn_shnu_vol: Optional[str] = Field(default=None)
    whol_smtn_ntby_qty: Optional[str] = Field(default=None)
    whol_smtn_seln_tr_pbmn: Optional[str] = Field(default=None)
    whol_smtn_shnu_tr_pbmn: Optional[str] = Field(default=None)
    whol_smtn_ntby_tr_pbmn: Optional[str] = Field(default=None)
    whol_ntby_vol_icdc: Optional[str] = Field(default=None)
    whol_ntby_tr_pbmn_icdc2: Optional[str] = Field(default=None)
    created_at: datetime


class CondSearch(SQLModel, table=True):
    __tablename__ = "cond_search"

    id: int = Field(primary_key=True)
    api_name: str
    bond_shrn_iscd: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    rght_type_name: Optional[str] = Field(default=None)
    elw_prpr: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acpr: Optional[str] = Field(default=None)
    stck_cnvr_rate: Optional[str] = Field(default=None)
    stck_lstn_date: Optional[str] = Field(default=None)
    stck_last_tr_date: Optional[str] = Field(default=None)
    hts_rmnn_dynu: Optional[str] = Field(default=None)
    unas_isnm: Optional[str] = Field(default=None)
    unas_prpr: Optional[str] = Field(default=None)
    unas_prdy_vrss: Optional[str] = Field(default=None)
    unas_prdy_vrss_sign: Optional[str] = Field(default=None)
    unas_prdy_ctrt: Optional[str] = Field(default=None)
    unas_acml_vol: Optional[str] = Field(default=None)
    moneyness: Optional[str] = Field(default=None)
    atm_cls_name: Optional[str] = Field(default=None)
    prit: Optional[str] = Field(default=None)
    delta_val: Optional[str] = Field(default=None)
    hts_ints_vltl: Optional[str] = Field(default=None)
    tmvl_val: Optional[str] = Field(default=None)
    gear: Optional[str] = Field(default=None)
    lvrg_val: Optional[str] = Field(default=None)
    prls_qryr_rate: Optional[str] = Field(default=None)
    cfp: Optional[str] = Field(default=None)
    lstn_stcn: Optional[str] = Field(default=None)
    pblc_co_name: Optional[str] = Field(default=None)
    lp_mbcr_name: Optional[str] = Field(default=None)
    lp_hldn_rate: Optional[str] = Field(default=None)
    elw_rght_form: Optional[str] = Field(default=None)
    elw_ko_barrier: Optional[str] = Field(default=None)
    apprch_rate: Optional[str] = Field(default=None)
    unas_shrn_iscd: Optional[str] = Field(default=None)
    mtrt_date: Optional[str] = Field(default=None)
    prmm_val: Optional[str] = Field(default=None)
    stck_lp_fin_date: Optional[str] = Field(default=None)
    tick_conv_prc: Optional[str] = Field(default=None)
    prls_qryr_stpr_prc: Optional[str] = Field(default=None)
    lp_hvol: Optional[str] = Field(default=None)
    created_at: datetime


class CountriesHoliday(SQLModel, table=True):
    __tablename__ = "countries_holiday"

    id: int = Field(primary_key=True)
    api_name: str
    prdt_type_cd: Optional[str] = Field(default=None)
    tr_natn_cd: Optional[str] = Field(default=None)
    natn_eng_abrv_cd: Optional[str] = Field(default=None)
    tr_mket_cd: Optional[str] = Field(default=None)
    tr_mket_name: Optional[str] = Field(default=None)
    acpl_sttl_dt: Optional[str] = Field(default=None)
    dmst_sttl_dt: Optional[str] = Field(default=None)
    created_at: datetime


class CreditBalance(SQLModel, table=True):
    __tablename__ = "credit_balance"

    id: int = Field(primary_key=True)
    api_name: str
    bstp_cls_code: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    stnd_date1: Optional[str] = Field(default=None)
    stnd_date2: Optional[str] = Field(default=None)
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    whol_loan_rmnd_stcn: Optional[str] = Field(default=None)
    whol_loan_rmnd_amt: Optional[str] = Field(default=None)
    whol_loan_rmnd_rate: Optional[str] = Field(default=None)
    whol_stln_rmnd_stcn: Optional[str] = Field(default=None)
    whol_stln_rmnd_amt: Optional[str] = Field(default=None)
    whol_stln_rmnd_rate: Optional[str] = Field(default=None)
    nday_vrss_loan_rmnd_inrt: Optional[str] = Field(default=None)
    nday_vrss_stln_rmnd_inrt: Optional[str] = Field(default=None)
    created_at: datetime


class CreditByCompany(SQLModel, table=True):
    __tablename__ = "credit_by_company"

    id: int = Field(primary_key=True)
    api_name: str
    stck_shrn_iscd: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    crdt_rate: Optional[str] = Field(default=None)
    created_at: datetime


class Dailyprice(SQLModel, table=True):
    __tablename__ = "dailyprice"

    id: int = Field(primary_key=True)
    api_name: str
    rsym: Optional[str] = Field(default=None)
    zdiv: Optional[str] = Field(default=None)
    nrec: Optional[str] = Field(default=None)
    xymd: Optional[str] = Field(default=None)
    clos: Optional[str] = Field(default=None)
    sign: Optional[str] = Field(default=None)
    diff: Optional[str] = Field(default=None)
    rate: Optional[str] = Field(default=None)
    open: Optional[str] = Field(default=None)
    high: Optional[str] = Field(default=None)
    low: Optional[str] = Field(default=None)
    tvol: Optional[str] = Field(default=None)
    tamt: Optional[str] = Field(default=None)
    pbid: Optional[str] = Field(default=None)
    vbid: Optional[str] = Field(default=None)
    pask: Optional[str] = Field(default=None)
    vask: Optional[str] = Field(default=None)
    created_at: datetime


class DailyCcnl(SQLModel, table=True):
    __tablename__ = "daily_ccnl"

    id: int = Field(primary_key=True)
    api_name: str
    tret_cnt: Optional[str] = Field(default=None)
    last_n_cnt: Optional[str] = Field(default=None)
    index_key: Optional[str] = Field(default=None)
    data_date: Optional[str] = Field(default=None)
    data_time: Optional[str] = Field(default=None)
    open_price: Optional[str] = Field(default=None)
    high_price: Optional[str] = Field(default=None)
    low_price: Optional[str] = Field(default=None)
    last_price: Optional[str] = Field(default=None)
    last_qntt: Optional[str] = Field(default=None)
    vol: Optional[str] = Field(default=None)
    prev_diff_flag: Optional[str] = Field(default=None)
    prev_diff_price: Optional[str] = Field(default=None)
    prev_diff_rate: Optional[str] = Field(default=None)
    created_at: datetime


class DailyCreditBalance(SQLModel, table=True):
    __tablename__ = "daily_credit_balance"

    id: int = Field(primary_key=True)
    api_name: str
    deal_date: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    stlm_date: Optional[str] = Field(default=None)
    whol_loan_new_stcn: Optional[str] = Field(default=None)
    whol_loan_rdmp_stcn: Optional[str] = Field(default=None)
    whol_loan_rmnd_stcn: Optional[str] = Field(default=None)
    whol_loan_new_amt: Optional[str] = Field(default=None)
    whol_loan_rdmp_amt: Optional[str] = Field(default=None)
    whol_loan_rmnd_amt: Optional[str] = Field(default=None)
    whol_loan_rmnd_rate: Optional[str] = Field(default=None)
    whol_loan_gvrt: Optional[str] = Field(default=None)
    whol_stln_new_stcn: Optional[str] = Field(default=None)
    whol_stln_rdmp_stcn: Optional[str] = Field(default=None)
    whol_stln_rmnd_stcn: Optional[str] = Field(default=None)
    whol_stln_new_amt: Optional[str] = Field(default=None)
    whol_stln_rdmp_amt: Optional[str] = Field(default=None)
    whol_stln_rmnd_amt: Optional[str] = Field(default=None)
    whol_stln_rmnd_rate: Optional[str] = Field(default=None)
    whol_stln_gvrt: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    created_at: datetime


class DailyLoanTrans(SQLModel, table=True):
    __tablename__ = "daily_loan_trans"

    id: int = Field(primary_key=True)
    api_name: str
    bsop_date: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    new_stcn: Optional[str] = Field(default=None)
    rdmp_stcn: Optional[str] = Field(default=None)
    prdy_rmnd_vrss: Optional[str] = Field(default=None)
    rmnd_stcn: Optional[str] = Field(default=None)
    rmnd_amt: Optional[str] = Field(default=None)
    created_at: datetime


class DailyPrice(SQLModel, table=True):
    __tablename__ = "daily_price"

    id: int = Field(primary_key=True)
    api_name: str
    stck_bsop_date: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    stck_clpr: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    prdy_vrss_vol_rate: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    hts_frgn_ehrt: Optional[str] = Field(default=None)
    frgn_ntby_qty: Optional[str] = Field(default=None)
    flng_cls_code: Optional[str] = Field(default=None)
    acml_prtt_rate: Optional[str] = Field(default=None)
    created_at: datetime


class DailyShortSale(SQLModel, table=True):
    __tablename__ = "daily_short_sale"

    id: int = Field(primary_key=True)
    api_name: str
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    prdy_vol: Optional[str] = Field(default=None)
    stck_bsop_date: Optional[str] = Field(default=None)
    stck_clpr: Optional[str] = Field(default=None)
    stnd_vol_smtn: Optional[str] = Field(default=None)
    ssts_cntg_qty: Optional[str] = Field(default=None)
    ssts_vol_rlim: Optional[str] = Field(default=None)
    acml_ssts_cntg_qty: Optional[str] = Field(default=None)
    acml_ssts_cntg_qty_rlim: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    stnd_tr_pbmn_smtn: Optional[str] = Field(default=None)
    ssts_tr_pbmn: Optional[str] = Field(default=None)
    ssts_tr_pbmn_rlim: Optional[str] = Field(default=None)
    acml_ssts_tr_pbmn: Optional[str] = Field(default=None)
    acml_ssts_tr_pbmn_rlim: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    avrg_prc: Optional[str] = Field(default=None)
    created_at: datetime


class DaytimeOrder(SQLModel, table=True):
    __tablename__ = "daytime_order"

    id: int = Field(primary_key=True)
    api_name: str
    krx_fwdg_ord_orgno: Optional[str] = Field(default=None)
    odno: Optional[str] = Field(default=None)
    ord_tmd: Optional[str] = Field(default=None)
    created_at: datetime


class DaytimeOrderRvsecncl(SQLModel, table=True):
    __tablename__ = "daytime_order_rvsecncl"

    id: int = Field(primary_key=True)
    api_name: str
    output1: Optional[str] = Field(default=None)
    krx_fwdg_ord_orgno: Optional[str] = Field(default=None)
    odno: Optional[str] = Field(default=None)
    ord_tmd: Optional[str] = Field(default=None)
    created_at: datetime


class Dbtools$executionHistory(SQLModel, table=True):
    __tablename__ = "dbtools$execution_history"

    id: float = Field(primary_key=True)
    hash: Optional[str] = Field(default=None)
    created_by: Optional[str] = Field(default=None)
    created_on: Optional[datetime] = Field(default=None)
    updated_by: Optional[str] = Field(default=None)
    updated_on: Optional[datetime] = Field(default=None)
    statement: Optional[str] = Field(default=None)
    times: Optional[float] = Field(default=None)


class DelayedAskingPriceAsia(SQLModel, table=True):
    __tablename__ = "delayed_asking_price_asia"

    id: int = Field(primary_key=True)
    api_name: str
    symb: Optional[str] = Field(default=None)
    zdiv: Optional[str] = Field(default=None)
    xymd: Optional[str] = Field(default=None)
    xhms: Optional[str] = Field(default=None)
    kymd: Optional[str] = Field(default=None)
    khms: Optional[str] = Field(default=None)
    bvol: Optional[str] = Field(default=None)
    avol: Optional[str] = Field(default=None)
    bdvl: Optional[str] = Field(default=None)
    advl: Optional[str] = Field(default=None)
    pbid1: Optional[str] = Field(default=None)
    pask1: Optional[str] = Field(default=None)
    vbid1: Optional[str] = Field(default=None)
    vask1: Optional[str] = Field(default=None)
    dbid1: Optional[str] = Field(default=None)
    dask1: Optional[str] = Field(default=None)
    created_at: datetime


class DelayedCcnl(SQLModel, table=True):
    __tablename__ = "delayed_ccnl"

    id: int = Field(primary_key=True)
    api_name: str
    symb: Optional[str] = Field(default=None)
    zdiv: Optional[str] = Field(default=None)
    tymd: Optional[str] = Field(default=None)
    xymd: Optional[str] = Field(default=None)
    xhms: Optional[str] = Field(default=None)
    kymd: Optional[str] = Field(default=None)
    khms: Optional[str] = Field(default=None)
    open: Optional[str] = Field(default=None)
    high: Optional[str] = Field(default=None)
    low: Optional[str] = Field(default=None)
    last: Optional[str] = Field(default=None)
    sign: Optional[str] = Field(default=None)
    diff: Optional[str] = Field(default=None)
    rate: Optional[str] = Field(default=None)
    pbid: Optional[str] = Field(default=None)
    pask: Optional[str] = Field(default=None)
    vbid: Optional[str] = Field(default=None)
    vask: Optional[str] = Field(default=None)
    evol: Optional[str] = Field(default=None)
    tvol: Optional[str] = Field(default=None)
    tamt: Optional[str] = Field(default=None)
    bivl: Optional[str] = Field(default=None)
    asvl: Optional[str] = Field(default=None)
    strn: Optional[str] = Field(default=None)
    mtyp: Optional[str] = Field(default=None)
    created_at: datetime


class Disparity(SQLModel, table=True):
    __tablename__ = "disparity"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    data_rank: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    d5_dsrt: Optional[str] = Field(default=None)
    d10_dsrt: Optional[str] = Field(default=None)
    d20_dsrt: Optional[str] = Field(default=None)
    d60_dsrt: Optional[str] = Field(default=None)
    d120_dsrt: Optional[str] = Field(default=None)
    created_at: datetime


class DisplayBoardCallput(SQLModel, table=True):
    __tablename__ = "display_board_callput"

    id: int = Field(primary_key=True)
    api_name: str
    acpr: Optional[str] = Field(default=None)
    unch_prpr: Optional[str] = Field(default=None)
    optn_shrn_iscd: Optional[str] = Field(default=None)
    optn_prpr: Optional[str] = Field(default=None)
    optn_prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    optn_prdy_ctrt: Optional[str] = Field(default=None)
    optn_bidp: Optional[str] = Field(default=None)
    optn_askp: Optional[str] = Field(default=None)
    tmvl_val: Optional[str] = Field(default=None)
    nmix_sdpr: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    seln_rsqn: Optional[str] = Field(default=None)
    shnu_rsqn: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    hts_otst_stpl_qty: Optional[str] = Field(default=None)
    otst_stpl_qty_icdc: Optional[str] = Field(default=None)
    delta_val: Optional[str] = Field(default=None)
    gama: Optional[str] = Field(default=None)
    vega: Optional[str] = Field(default=None)
    theta: Optional[str] = Field(default=None)
    rho: Optional[str] = Field(default=None)
    hts_ints_vltl: Optional[str] = Field(default=None)
    invl_val: Optional[str] = Field(default=None)
    esdg: Optional[str] = Field(default=None)
    dprt: Optional[str] = Field(default=None)
    hist_vltl: Optional[str] = Field(default=None)
    hts_thpr: Optional[str] = Field(default=None)
    optn_oprc: Optional[str] = Field(default=None)
    optn_hgpr: Optional[str] = Field(default=None)
    optn_lwpr: Optional[str] = Field(default=None)
    optn_mxpr: Optional[str] = Field(default=None)
    optn_llam: Optional[str] = Field(default=None)
    atm_cls_name: Optional[str] = Field(default=None)
    rgbf_vrss_icdc: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    futs_antc_cnpr: Optional[str] = Field(default=None)
    futs_antc_cntg_vrss: Optional[str] = Field(default=None)
    antc_cntg_vrss_sign: Optional[str] = Field(default=None)
    antc_cntg_prdy_ctrt: Optional[str] = Field(default=None)
    created_at: datetime


class DisplayBoardFutures(SQLModel, table=True):
    __tablename__ = "display_board_futures"

    id: int = Field(primary_key=True)
    api_name: str
    futs_shrn_iscd: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    futs_prpr: Optional[str] = Field(default=None)
    futs_prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    futs_prdy_ctrt: Optional[str] = Field(default=None)
    hts_thpr: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    futs_askp: Optional[str] = Field(default=None)
    futs_bidp: Optional[str] = Field(default=None)
    hts_otst_stpl_qty: Optional[str] = Field(default=None)
    futs_hgpr: Optional[str] = Field(default=None)
    futs_lwpr: Optional[str] = Field(default=None)
    hts_rmnn_dynu: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    futs_antc_cnpr: Optional[str] = Field(default=None)
    futs_antc_cntg_vrss: Optional[str] = Field(default=None)
    antc_cntg_vrss_sign: Optional[str] = Field(default=None)
    antc_cntg_prdy_ctrt: Optional[str] = Field(default=None)
    created_at: datetime


class DisplayBoardOptionList(SQLModel, table=True):
    __tablename__ = "display_board_option_list"

    id: int = Field(primary_key=True)
    api_name: str
    mtrt_yymm_code: Optional[str] = Field(default=None)
    mtrt_yymm: Optional[str] = Field(default=None)
    created_at: datetime


class DisplayBoardTop(SQLModel, table=True):
    __tablename__ = "display_board_top"

    id: int = Field(primary_key=True)
    api_name: str
    unas_prpr: Optional[str] = Field(default=None)
    unas_prdy_vrss: Optional[str] = Field(default=None)
    unas_prdy_vrss_sign: Optional[str] = Field(default=None)
    unas_prdy_ctrt: Optional[str] = Field(default=None)
    unas_acml_vol: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    futs_prpr: Optional[str] = Field(default=None)
    futs_prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    futs_prdy_ctrt: Optional[str] = Field(default=None)
    hts_rmnn_dynu: Optional[str] = Field(default=None)
    created_at: datetime


class DividendRate(SQLModel, table=True):
    __tablename__ = "dividend_rate"

    id: int = Field(primary_key=True)
    api_name: str
    rank: Optional[str] = Field(default=None)
    sht_cd: Optional[str] = Field(default=None)
    record_date: Optional[str] = Field(default=None)
    per_sto_divi_amt: Optional[str] = Field(default=None)
    divi_rate: Optional[str] = Field(default=None)
    divi_kind: Optional[str] = Field(default=None)
    created_at: datetime


class DomBondMst(SQLModel, table=True):
    __tablename__ = "dom_bond_mst"

    id: int = Field(primary_key=True)
    bond_type: Optional[str] = Field(default=None)
    bond_cls_code: Optional[str] = Field(default=None)
    standard_code: Optional[str] = Field(default=None)
    kor_name: Optional[str] = Field(default=None)
    bond_int_cls_code: Optional[str] = Field(default=None)
    listed_date: Optional[str] = Field(default=None)
    public_date: Optional[str] = Field(default=None)
    redemption_date: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class DomCmeFutureMst(SQLModel, table=True):
    __tablename__ = "dom_cme_future_mst"

    id: int = Field(primary_key=True)
    product_type: Optional[str] = Field(default=None)
    short_code: Optional[str] = Field(default=None)
    standard_code: Optional[str] = Field(default=None)
    kor_name: Optional[str] = Field(default=None)
    strike_price: Optional[str] = Field(default=None)
    underlying_short_code: Optional[str] = Field(default=None)
    underlying_name: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class DomComFutureMst(SQLModel, table=True):
    __tablename__ = "dom_com_future_mst"

    id: int = Field(primary_key=True)
    product_class: Optional[str] = Field(default=None)
    product_type: Optional[str] = Field(default=None)
    short_code: Optional[str] = Field(default=None)
    standard_code: Optional[str] = Field(default=None)
    kor_name: Optional[str] = Field(default=None)
    month_code: Optional[str] = Field(default=None)
    underlying_short_code: Optional[str] = Field(default=None)
    underlying_name: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class DomElwMst(SQLModel, table=True):
    __tablename__ = "dom_elw_mst"

    id: int = Field(primary_key=True)
    short_code: Optional[str] = Field(default=None)
    standard_code: Optional[str] = Field(default=None)
    kor_name: Optional[str] = Field(default=None)
    elw_right_type: Optional[str] = Field(default=None)
    elw_early_end_price: Optional[str] = Field(default=None)
    basket_yn: Optional[str] = Field(default=None)
    underlying_code1: Optional[str] = Field(default=None)
    underlying_code2: Optional[str] = Field(default=None)
    underlying_code3: Optional[str] = Field(default=None)
    underlying_code4: Optional[str] = Field(default=None)
    underlying_code5: Optional[str] = Field(default=None)
    issuer_name: Optional[str] = Field(default=None)
    issuer_code: Optional[str] = Field(default=None)
    strike_price: Optional[str] = Field(default=None)
    last_trade_date: Optional[str] = Field(default=None)
    remain_days: Optional[str] = Field(default=None)
    right_type_code: Optional[str] = Field(default=None)
    payment_date: Optional[str] = Field(default=None)
    prev_market_cap: Optional[str] = Field(default=None)
    listed_shares: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class DomEurexOptionMst(SQLModel, table=True):
    __tablename__ = "dom_eurex_option_mst"

    id: int = Field(primary_key=True)
    product_type: Optional[str] = Field(default=None)
    short_code: Optional[str] = Field(default=None)
    standard_code: Optional[str] = Field(default=None)
    kor_name: Optional[str] = Field(default=None)
    atm_division: Optional[str] = Field(default=None)
    strike_price: Optional[str] = Field(default=None)
    underlying_short_code: Optional[str] = Field(default=None)
    underlying_name: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class DomFutureMst(SQLModel, table=True):
    __tablename__ = "dom_future_mst"

    id: int = Field(primary_key=True)
    product_type: Optional[str] = Field(default=None)
    short_code: Optional[str] = Field(default=None)
    standard_code: Optional[str] = Field(default=None)
    kor_name: Optional[str] = Field(default=None)
    atm_division: Optional[str] = Field(default=None)
    strike_price: Optional[str] = Field(default=None)
    month_code: Optional[str] = Field(default=None)
    underlying_short_code: Optional[str] = Field(default=None)
    underlying_name: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class DomKonexMst(SQLModel, table=True):
    __tablename__ = "dom_konex_mst"

    id: int = Field(primary_key=True)
    short_code: Optional[str] = Field(default=None)
    standard_code: Optional[str] = Field(default=None)
    kor_name: Optional[str] = Field(default=None)
    group_code: Optional[str] = Field(default=None)
    base_price: Optional[str] = Field(default=None)
    listed_date: Optional[str] = Field(default=None)
    listed_shares: Optional[str] = Field(default=None)
    capital: Optional[str] = Field(default=None)
    face_value: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class DomKosdaqMst(SQLModel, table=True):
    __tablename__ = "dom_kosdaq_mst"

    id: int = Field(primary_key=True)
    short_code: Optional[str] = Field(default=None)
    standard_code: Optional[str] = Field(default=None)
    kor_name: Optional[str] = Field(default=None)
    group_code: Optional[str] = Field(default=None)
    market_cap_scale: Optional[str] = Field(default=None)
    industry_code_l: Optional[str] = Field(default=None)
    industry_code_m: Optional[str] = Field(default=None)
    industry_code_s: Optional[str] = Field(default=None)
    base_price: Optional[str] = Field(default=None)
    listed_date: Optional[str] = Field(default=None)
    listed_shares: Optional[str] = Field(default=None)
    capital: Optional[str] = Field(default=None)
    face_value: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class DomKospiMst(SQLModel, table=True):
    __tablename__ = "dom_kospi_mst"

    id: int = Field(primary_key=True)
    short_code: Optional[str] = Field(default=None)
    standard_code: Optional[str] = Field(default=None)
    kor_name: Optional[str] = Field(default=None)
    group_code: Optional[str] = Field(default=None)
    market_cap_scale: Optional[str] = Field(default=None)
    industry_code_l: Optional[str] = Field(default=None)
    industry_code_m: Optional[str] = Field(default=None)
    industry_code_s: Optional[str] = Field(default=None)
    base_price: Optional[str] = Field(default=None)
    listed_date: Optional[str] = Field(default=None)
    listed_shares: Optional[str] = Field(default=None)
    capital: Optional[str] = Field(default=None)
    face_value: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class DomStockFutureMst(SQLModel, table=True):
    __tablename__ = "dom_stock_future_mst"

    id: int = Field(primary_key=True)
    product_type: Optional[str] = Field(default=None)
    short_code: Optional[str] = Field(default=None)
    standard_code: Optional[str] = Field(default=None)
    kor_name: Optional[str] = Field(default=None)
    atm_division: Optional[str] = Field(default=None)
    strike_price: Optional[str] = Field(default=None)
    month_code: Optional[str] = Field(default=None)
    underlying_short_code: Optional[str] = Field(default=None)
    underlying_name: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class ElwAskingPrice(SQLModel, table=True):
    __tablename__ = "elw_asking_price"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    bsop_hour: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    askp2: Optional[str] = Field(default=None)
    askp3: Optional[str] = Field(default=None)
    askp4: Optional[str] = Field(default=None)
    askp5: Optional[str] = Field(default=None)
    askp6: Optional[str] = Field(default=None)
    askp7: Optional[str] = Field(default=None)
    askp8: Optional[str] = Field(default=None)
    askp9: Optional[str] = Field(default=None)
    askp10: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    bidp2: Optional[str] = Field(default=None)
    bidp3: Optional[str] = Field(default=None)
    bidp4: Optional[str] = Field(default=None)
    bidp5: Optional[str] = Field(default=None)
    bidp6: Optional[str] = Field(default=None)
    bidp7: Optional[str] = Field(default=None)
    bidp8: Optional[str] = Field(default=None)
    bidp9: Optional[str] = Field(default=None)
    bidp10: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    askp_rsqn2: Optional[str] = Field(default=None)
    askp_rsqn3: Optional[str] = Field(default=None)
    askp_rsqn4: Optional[str] = Field(default=None)
    askp_rsqn5: Optional[str] = Field(default=None)
    askp_rsqn6: Optional[str] = Field(default=None)
    askp_rsqn7: Optional[str] = Field(default=None)
    askp_rsqn8: Optional[str] = Field(default=None)
    askp_rsqn9: Optional[str] = Field(default=None)
    askp_rsqn10: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn2: Optional[str] = Field(default=None)
    bidp_rsqn3: Optional[str] = Field(default=None)
    bidp_rsqn4: Optional[str] = Field(default=None)
    bidp_rsqn5: Optional[str] = Field(default=None)
    bidp_rsqn6: Optional[str] = Field(default=None)
    bidp_rsqn7: Optional[str] = Field(default=None)
    bidp_rsqn8: Optional[str] = Field(default=None)
    bidp_rsqn9: Optional[str] = Field(default=None)
    bidp_rsqn10: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    antc_cnpr: Optional[str] = Field(default=None)
    antc_cnqn: Optional[str] = Field(default=None)
    antc_cntg_vrss_sign: Optional[str] = Field(default=None)
    antc_cntg_vrss: Optional[str] = Field(default=None)
    antc_cntg_prdy_ctrt: Optional[str] = Field(default=None)
    lp_askp_rsqn1: Optional[str] = Field(default=None)
    lp_askp_rsqn2: Optional[str] = Field(default=None)
    lp_askp_rsqn3: Optional[str] = Field(default=None)
    lp_bidp_rsqn4: Optional[str] = Field(default=None)
    lp_askp_rsqn4: Optional[str] = Field(default=None)
    lp_bidp_rsqn5: Optional[str] = Field(default=None)
    lp_askp_rsqn5: Optional[str] = Field(default=None)
    lp_bidp_rsqn6: Optional[str] = Field(default=None)
    lp_askp_rsqn6: Optional[str] = Field(default=None)
    lp_bidp_rsqn7: Optional[str] = Field(default=None)
    lp_askp_rsqn7: Optional[str] = Field(default=None)
    lp_askp_rsqn8: Optional[str] = Field(default=None)
    lp_bidp_rsqn8: Optional[str] = Field(default=None)
    lp_askp_rsqn9: Optional[str] = Field(default=None)
    lp_bidp_rsqn9: Optional[str] = Field(default=None)
    lp_askp_rsqn10: Optional[str] = Field(default=None)
    lp_bidp_rsqn10: Optional[str] = Field(default=None)
    lp_bidp_rsqn1: Optional[str] = Field(default=None)
    lp_total_askp_rsqn: Optional[str] = Field(default=None)
    lp_bidp_rsqn2: Optional[str] = Field(default=None)
    lp_total_bidp_rsqn: Optional[str] = Field(default=None)
    lp_bidp_rsqn3: Optional[str] = Field(default=None)
    antc_vol: Optional[str] = Field(default=None)
    created_at: datetime


class ElwCcnl(SQLModel, table=True):
    __tablename__ = "elw_ccnl"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    wghn_avrg_stck_prc: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    cntg_vol: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    seln_cntg_csnu: Optional[str] = Field(default=None)
    shnu_cntg_csnu: Optional[str] = Field(default=None)
    ntby_cntg_csnu: Optional[str] = Field(default=None)
    cttr: Optional[str] = Field(default=None)
    seln_cntg_smtn: Optional[str] = Field(default=None)
    shnu_cntg_smtn: Optional[str] = Field(default=None)
    cntg_cls_code: Optional[str] = Field(default=None)
    shnu_rate: Optional[str] = Field(default=None)
    prdy_vol_vrss_acml_vol_rate: Optional[str] = Field(default=None)
    oprc_hour: Optional[str] = Field(default=None)
    oprc_vrss_prpr_sign: Optional[str] = Field(default=None)
    oprc_vrss_prpr: Optional[str] = Field(default=None)
    hgpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    hgpr_vrss_prpr: Optional[str] = Field(default=None)
    lwpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    lwpr_vrss_prpr: Optional[str] = Field(default=None)
    bsop_date: Optional[str] = Field(default=None)
    new_mkop_cls_code: Optional[str] = Field(default=None)
    trht_yn: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    vol_rate: Optional[str] = Field(default=None)
    prdy_vrss_vol_rate: Optional[str] = Field(default=None)
    askp_rsqn_icdc: Optional[str] = Field(default=None)
    bidp_rsqn_icdc: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    mrkt_trtm_cls_code: Optional[str] = Field(default=None)
    vi_cls_code: Optional[str] = Field(default=None)
    timr_val: Optional[str] = Field(default=None)
    parity: Optional[str] = Field(default=None)
    prm_val: Optional[str] = Field(default=None)
    gear: Optional[str] = Field(default=None)
    bep_rate: Optional[str] = Field(default=None)
    itmv_val: Optional[str] = Field(default=None)
    prm_rate: Optional[str] = Field(default=None)
    sppt_pnt: Optional[str] = Field(default=None)
    lvrg_val: Optional[str] = Field(default=None)
    delta: Optional[str] = Field(default=None)
    gamma: Optional[str] = Field(default=None)
    vega: Optional[str] = Field(default=None)
    theta: Optional[str] = Field(default=None)
    rho: Optional[str] = Field(default=None)
    hts_antc_vol: Optional[str] = Field(default=None)
    hts_theo_prc: Optional[str] = Field(default=None)
    vol_tnrt: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol_rate: Optional[str] = Field(default=None)
    apprch_rate: Optional[str] = Field(default=None)
    lp_hvol: Optional[str] = Field(default=None)
    lp_hldn_rate: Optional[str] = Field(default=None)
    lp_ntby_qty: Optional[str] = Field(default=None)
    created_at: datetime


class ElwExpCcnl(SQLModel, table=True):
    __tablename__ = "elw_exp_ccnl"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    wghn_avrg_stck_prc: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    cntg_vol: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    seln_cntg_csnu: Optional[str] = Field(default=None)
    shnu_cntg_csnu: Optional[str] = Field(default=None)
    ntby_cntg_csnu: Optional[str] = Field(default=None)
    cttr: Optional[str] = Field(default=None)
    seln_cntg_smtn: Optional[str] = Field(default=None)
    shnu_cntg_smtn: Optional[str] = Field(default=None)
    cntg_cls_code: Optional[str] = Field(default=None)
    shnu_rate: Optional[str] = Field(default=None)
    prdy_vol_vrss_acml_vol_rate: Optional[str] = Field(default=None)
    oprc_hour: Optional[str] = Field(default=None)
    oprc_vrss_prpr_sign: Optional[str] = Field(default=None)
    oprc_vrss_prpr: Optional[str] = Field(default=None)
    hgpr_hour: Optional[str] = Field(default=None)
    hgpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    hgpr_vrss_prpr: Optional[str] = Field(default=None)
    lwpr_hour: Optional[str] = Field(default=None)
    lwpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    lwpr_vrss_prpr: Optional[str] = Field(default=None)
    bsop_date: Optional[str] = Field(default=None)
    new_mkop_cls_code: Optional[str] = Field(default=None)
    trht_yn: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    tmvl_val: Optional[str] = Field(default=None)
    prit: Optional[str] = Field(default=None)
    prmm_val: Optional[str] = Field(default=None)
    gear: Optional[str] = Field(default=None)
    prls_qryr_rate: Optional[str] = Field(default=None)
    invl_val: Optional[str] = Field(default=None)
    prmm_rate: Optional[str] = Field(default=None)
    cfp: Optional[str] = Field(default=None)
    lvrg_val: Optional[str] = Field(default=None)
    delta: Optional[str] = Field(default=None)
    gama: Optional[str] = Field(default=None)
    vega: Optional[str] = Field(default=None)
    theta: Optional[str] = Field(default=None)
    rho: Optional[str] = Field(default=None)
    hts_ints_vltl: Optional[str] = Field(default=None)
    hts_thpr: Optional[str] = Field(default=None)
    vol_tnrt: Optional[str] = Field(default=None)
    lp_hvol: Optional[str] = Field(default=None)
    lp_hldn_rate: Optional[str] = Field(default=None)
    created_at: datetime


class EstimatePerform(SQLModel, table=True):
    __tablename__ = "estimate_perform"

    id: int = Field(primary_key=True)
    api_name: str
    sht_cd: Optional[str] = Field(default=None)
    item_kor_nm: Optional[str] = Field(default=None)
    estdate: Optional[str] = Field(default=None)
    capital: Optional[str] = Field(default=None)
    forn_item_lmtrt: Optional[str] = Field(default=None)
    data1: Optional[str] = Field(default=None)
    data2: Optional[str] = Field(default=None)
    data3: Optional[str] = Field(default=None)
    data4: Optional[str] = Field(default=None)
    data5: Optional[str] = Field(default=None)
    output3: Optional[str] = Field(default=None)
    output4: Optional[str] = Field(default=None)
    dt: Optional[str] = Field(default=None)
    created_at: datetime


class EtfNavTrend(SQLModel, table=True):
    __tablename__ = "etf_nav_trend"

    id: int = Field(primary_key=True)
    api_name: str
    rt_cd: Optional[str] = Field(default=None)
    msg_cd: Optional[str] = Field(default=None)
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    nav: Optional[str] = Field(default=None)
    nav_prdy_vrss_sign: Optional[str] = Field(default=None)
    nav_prdy_vrss: Optional[str] = Field(default=None)
    nav_prdy_ctrt: Optional[str] = Field(default=None)
    oprc_nav: Optional[str] = Field(default=None)
    hprc_nav: Optional[str] = Field(default=None)
    lprc_nav: Optional[str] = Field(default=None)
    created_at: datetime


class ExpirationStocks(SQLModel, table=True):
    __tablename__ = "expiration_stocks"

    id: int = Field(primary_key=True)
    api_name: str
    elw_shrn_iscd: Optional[str] = Field(default=None)
    elw_kor_isnm: Optional[str] = Field(default=None)
    unas_isnm: Optional[str] = Field(default=None)
    unas_prpr: Optional[str] = Field(default=None)
    acpr: Optional[str] = Field(default=None)
    stck_cnvr_rate: Optional[str] = Field(default=None)
    elw_prpr: Optional[str] = Field(default=None)
    stck_lstn_date: Optional[str] = Field(default=None)
    stck_last_tr_date: Optional[str] = Field(default=None)
    total_rdmp_amt: Optional[str] = Field(default=None)
    rdmp_amt: Optional[str] = Field(default=None)
    lstn_stcn: Optional[str] = Field(default=None)
    lp_hvol: Optional[str] = Field(default=None)
    ccls_paym_prc: Optional[str] = Field(default=None)
    mtrt_vltn_amt: Optional[str] = Field(default=None)
    evnt_prd_fin_date: Optional[str] = Field(default=None)
    stlm_date: Optional[str] = Field(default=None)
    pblc_prc: Optional[str] = Field(default=None)
    unas_shrn_iscd: Optional[str] = Field(default=None)
    stnd_iscd: Optional[str] = Field(default=None)
    rdmp_ask_amt: Optional[str] = Field(default=None)
    created_at: datetime


class ExpCcnlKrx(SQLModel, table=True):
    __tablename__ = "exp_ccnl_krx"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    wghn_avrg_stck_prc: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    cntg_vol: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    seln_cntg_csnu: Optional[str] = Field(default=None)
    shnu_cntg_csnu: Optional[str] = Field(default=None)
    ntby_cntg_csnu: Optional[str] = Field(default=None)
    cttr: Optional[str] = Field(default=None)
    seln_cntg_smtn: Optional[str] = Field(default=None)
    shnu_cntg_smtn: Optional[str] = Field(default=None)
    cntg_cls_code: Optional[str] = Field(default=None)
    shnu_rate: Optional[str] = Field(default=None)
    prdy_vol_vrss_acml_vol_rate: Optional[str] = Field(default=None)
    oprc_hour: Optional[str] = Field(default=None)
    oprc_vrss_prpr_sign: Optional[str] = Field(default=None)
    oprc_vrss_prpr: Optional[str] = Field(default=None)
    hgpr_hour: Optional[str] = Field(default=None)
    hgpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    hgpr_vrss_prpr: Optional[str] = Field(default=None)
    lwpr_hour: Optional[str] = Field(default=None)
    lwpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    lwpr_vrss_prpr: Optional[str] = Field(default=None)
    bsop_date: Optional[str] = Field(default=None)
    new_mkop_cls_code: Optional[str] = Field(default=None)
    trht_yn: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    vol_tnrt: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol_rate: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    mrkt_trtm_cls_code: Optional[str] = Field(default=None)
    created_at: datetime


class ExpCcnlNxt(SQLModel, table=True):
    __tablename__ = "exp_ccnl_nxt"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    wghn_avrg_stck_prc: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    cntg_vol: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    seln_cntg_csnu: Optional[str] = Field(default=None)
    shnu_cntg_csnu: Optional[str] = Field(default=None)
    ntby_cntg_csnu: Optional[str] = Field(default=None)
    cttr: Optional[str] = Field(default=None)
    seln_cntg_smtn: Optional[str] = Field(default=None)
    shnu_cntg_smtn: Optional[str] = Field(default=None)
    cntg_cls_code: Optional[str] = Field(default=None)
    shnu_rate: Optional[str] = Field(default=None)
    prdy_vol_vrss_acml_vol_rate: Optional[str] = Field(default=None)
    oprc_hour: Optional[str] = Field(default=None)
    oprc_vrss_prpr_sign: Optional[str] = Field(default=None)
    oprc_vrss_prpr: Optional[str] = Field(default=None)
    hgpr_hour: Optional[str] = Field(default=None)
    hgpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    hgpr_vrss_prpr: Optional[str] = Field(default=None)
    lwpr_hour: Optional[str] = Field(default=None)
    lwpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    lwpr_vrss_prpr: Optional[str] = Field(default=None)
    bsop_date: Optional[str] = Field(default=None)
    new_mkop_cls_code: Optional[str] = Field(default=None)
    trht_yn: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    vol_tnrt: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol_rate: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    mrkt_trtm_cls_code: Optional[str] = Field(default=None)
    vi_stnd_prc: Optional[str] = Field(default=None)
    created_at: datetime


class ExpCcnlTotal(SQLModel, table=True):
    __tablename__ = "exp_ccnl_total"

    id: int = Field(primary_key=True)
    api_name: str
    mksc_shrn_iscd: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    wghn_avrg_stck_prc: Optional[str] = Field(default=None)
    stck_oprc: Optional[str] = Field(default=None)
    stck_hgpr: Optional[str] = Field(default=None)
    stck_lwpr: Optional[str] = Field(default=None)
    askp1: Optional[str] = Field(default=None)
    bidp1: Optional[str] = Field(default=None)
    cntg_vol: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    seln_cntg_csnu: Optional[str] = Field(default=None)
    shnu_cntg_csnu: Optional[str] = Field(default=None)
    ntby_cntg_csnu: Optional[str] = Field(default=None)
    cttr: Optional[str] = Field(default=None)
    seln_cntg_smtn: Optional[str] = Field(default=None)
    shnu_cntg_smtn: Optional[str] = Field(default=None)
    cntg_cls_code: Optional[str] = Field(default=None)
    shnu_rate: Optional[str] = Field(default=None)
    prdy_vol_vrss_acml_vol_rate: Optional[str] = Field(default=None)
    oprc_hour: Optional[str] = Field(default=None)
    oprc_vrss_prpr_sign: Optional[str] = Field(default=None)
    oprc_vrss_prpr: Optional[str] = Field(default=None)
    hgpr_hour: Optional[str] = Field(default=None)
    hgpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    hgpr_vrss_prpr: Optional[str] = Field(default=None)
    lwpr_hour: Optional[str] = Field(default=None)
    lwpr_vrss_prpr_sign: Optional[str] = Field(default=None)
    lwpr_vrss_prpr: Optional[str] = Field(default=None)
    bsop_date: Optional[str] = Field(default=None)
    new_mkop_cls_code: Optional[str] = Field(default=None)
    trht_yn: Optional[str] = Field(default=None)
    askp_rsqn1: Optional[str] = Field(default=None)
    bidp_rsqn1: Optional[str] = Field(default=None)
    total_askp_rsqn: Optional[str] = Field(default=None)
    total_bidp_rsqn: Optional[str] = Field(default=None)
    vol_tnrt: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol: Optional[str] = Field(default=None)
    prdy_smns_hour_acml_vol_rate: Optional[str] = Field(default=None)
    hour_cls_code: Optional[str] = Field(default=None)
    mrkt_trtm_cls_code: Optional[str] = Field(default=None)
    vi_stnd_prc: Optional[str] = Field(default=None)
    created_at: datetime


class ExpClosingPrice(SQLModel, table=True):
    __tablename__ = "exp_closing_price"

    id: int = Field(primary_key=True)
    api_name: str
    stck_shrn_iscd: Optional[str] = Field(default=None)
    hts_kor_isnm: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    sdpr_vrss_prpr: Optional[str] = Field(default=None)
    sdpr_vrss_prpr_rate: Optional[str] = Field(default=None)
    cntg_vol: Optional[str] = Field(default=None)
    created_at: datetime


class ExpIndexTrend(SQLModel, table=True):
    __tablename__ = "exp_index_trend"

    id: int = Field(primary_key=True)
    api_name: str
    stck_cntg_hour: Optional[str] = Field(default=None)
    bstp_nmix_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    bstp_nmix_prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    acml_tr_pbmn: Optional[str] = Field(default=None)
    created_at: datetime


class ExpPriceTrend(SQLModel, table=True):
    __tablename__ = "exp_price_trend"

    id: int = Field(primary_key=True)
    api_name: str
    rprs_mrkt_kor_name: Optional[str] = Field(default=None)
    antc_cnpr: Optional[str] = Field(default=None)
    antc_cntg_vrss_sign: Optional[str] = Field(default=None)
    antc_cntg_vrss: Optional[str] = Field(default=None)
    antc_cntg_prdy_ctrt: Optional[str] = Field(default=None)
    antc_vol: Optional[str] = Field(default=None)
    antc_tr_pbmn: Optional[str] = Field(default=None)
    stck_bsop_date: Optional[str] = Field(default=None)
    stck_cntg_hour: Optional[str] = Field(default=None)
    stck_prpr: Optional[str] = Field(default=None)
    prdy_vrss_sign: Optional[str] = Field(default=None)
    prdy_vrss: Optional[str] = Field(default=None)
    prdy_ctrt: Optional[str] = Field(default=None)
    acml_vol: Optional[str] = Field(default=None)
    created_at: datetime


