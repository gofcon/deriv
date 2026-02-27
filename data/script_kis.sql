create table DBTOOLS$EXECUTION_HISTORY
(
    ID         NUMBER not null
        constraint DBTOOLS$EXECUTION_HISTORY_PK
            primary key,
    HASH       CLOB,
    CREATED_BY VARCHAR2(255),
    CREATED_ON TIMESTAMP(6) WITH TIME ZONE,
    UPDATED_BY VARCHAR2(255),
    UPDATED_ON TIMESTAMP(6) WITH TIME ZONE,
    STATEMENT  CLOB,
    TIMES      NUMBER
)
/

create table API_MST
(
    API_NAME          VARCHAR2(4000) not null
        primary key,
    API_URL           VARCHAR2(4000) not null,
    TR_ID             VARCHAR2(4000) not null,
    TR_CONT           VARCHAR2(4000) not null,
    REQUEST_TYPE      VARCHAR2(4000) not null,
    DESCRIPTION       VARCHAR2(4000),
    OUTPUT_TABLE_NAME VARCHAR2(4000),
    CREATED_AT        DATE           not null,
    UPDATED_AT        DATE           not null
)
/

create table STOCK_PRICE
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    ISCD_STAT_CLS_CODE       VARCHAR2(4000),
    MARG_RATE                VARCHAR2(4000),
    RPRS_MRKT_KOR_NAME       VARCHAR2(4000),
    NEW_HGPR_LWPR_CLS_CODE   VARCHAR2(4000),
    BSTP_KOR_ISNM            VARCHAR2(4000),
    TEMP_STOP_YN             VARCHAR2(4000),
    OPRC_RANG_CONT_YN        VARCHAR2(4000),
    CLPR_RANG_CONT_YN        VARCHAR2(4000),
    CRDT_ABLE_YN             VARCHAR2(4000),
    GRMN_RATE_CLS_CODE       VARCHAR2(4000),
    ELW_PBLC_YN              VARCHAR2(4000),
    STCK_PRPR                VARCHAR2(4000),
    PRDY_VRSS                VARCHAR2(4000),
    PRDY_VRSS_SIGN           VARCHAR2(4000),
    PRDY_CTRT                VARCHAR2(4000),
    ACML_TR_PBMN             VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    PRDY_VRSS_VOL_RATE       VARCHAR2(4000),
    STCK_OPRC                VARCHAR2(4000),
    STCK_HGPR                VARCHAR2(4000),
    STCK_LWPR                VARCHAR2(4000),
    STCK_MXPR                VARCHAR2(4000),
    STCK_LLAM                VARCHAR2(4000),
    STCK_SDPR                VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC       VARCHAR2(4000),
    HTS_FRGN_EHRT            VARCHAR2(4000),
    FRGN_NTBY_QTY            VARCHAR2(4000),
    PGTR_NTBY_QTY            VARCHAR2(4000),
    PVT_SCND_DMRS_PRC        VARCHAR2(4000),
    PVT_FRST_DMRS_PRC        VARCHAR2(4000),
    PVT_PONT_VAL             VARCHAR2(4000),
    PVT_FRST_DMSP_PRC        VARCHAR2(4000),
    PVT_SCND_DMSP_PRC        VARCHAR2(4000),
    DMRS_VAL                 VARCHAR2(4000),
    DMSP_VAL                 VARCHAR2(4000),
    CPFN                     VARCHAR2(4000),
    RSTC_WDTH_PRC            VARCHAR2(4000),
    STCK_FCAM                VARCHAR2(4000),
    STCK_SSPR                VARCHAR2(4000),
    ASPR_UNIT                VARCHAR2(4000),
    HTS_DEAL_QTY_UNIT_VAL    VARCHAR2(4000),
    LSTN_STCN                VARCHAR2(4000),
    HTS_AVLS                 VARCHAR2(4000),
    PER                      VARCHAR2(4000),
    PBR                      VARCHAR2(4000),
    STAC_MONTH               VARCHAR2(4000),
    VOL_TNRT                 VARCHAR2(4000),
    EPS                      VARCHAR2(4000),
    BPS                      VARCHAR2(4000),
    D250_HGPR                VARCHAR2(4000),
    D250_HGPR_DATE           VARCHAR2(4000),
    D250_HGPR_VRSS_PRPR_RATE VARCHAR2(4000),
    D250_LWPR                VARCHAR2(4000),
    D250_LWPR_DATE           VARCHAR2(4000),
    D250_LWPR_VRSS_PRPR_RATE VARCHAR2(4000),
    STCK_DRYY_HGPR           VARCHAR2(4000),
    DRYY_HGPR_VRSS_PRPR_RATE VARCHAR2(4000),
    DRYY_HGPR_DATE           VARCHAR2(4000),
    STCK_DRYY_LWPR           VARCHAR2(4000),
    DRYY_LWPR_VRSS_PRPR_RATE VARCHAR2(4000),
    DRYY_LWPR_DATE           VARCHAR2(4000),
    W52_HGPR                 VARCHAR2(4000),
    W52_HGPR_VRSS_PRPR_CTRT  VARCHAR2(4000),
    W52_HGPR_DATE            VARCHAR2(4000),
    W52_LWPR                 VARCHAR2(4000),
    W52_LWPR_VRSS_PRPR_CTRT  VARCHAR2(4000),
    W52_LWPR_DATE            VARCHAR2(4000),
    WHOL_LOAN_RMND_RATE      VARCHAR2(4000),
    SSTS_YN                  VARCHAR2(4000),
    STCK_SHRN_ISCD           VARCHAR2(4000),
    FCAM_CNNM                VARCHAR2(4000),
    CPFN_CNNM                VARCHAR2(4000),
    APPRCH_RATE              VARCHAR2(4000),
    FRGN_HLDN_QTY            VARCHAR2(4000),
    VI_CLS_CODE              VARCHAR2(4000),
    OVTM_VI_CLS_CODE         VARCHAR2(4000),
    LAST_SSTS_CNTG_QTY       VARCHAR2(4000),
    INVT_CAFUL_YN            VARCHAR2(4000),
    MRKT_WARN_CLS_CODE       VARCHAR2(4000),
    SHORT_OVER_YN            VARCHAR2(4000),
    SLTR_YN                  VARCHAR2(4000),
    MANG_ISSU_CLS_CODE       VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_STOCK_PRICE_API_NAME
    on STOCK_PRICE (API_NAME)
/

create table DAILY_PRICE
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    STCK_BSOP_DATE     VARCHAR2(4000),
    STCK_OPRC          VARCHAR2(4000),
    STCK_HGPR          VARCHAR2(4000),
    STCK_LWPR          VARCHAR2(4000),
    STCK_CLPR          VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    PRDY_VRSS_VOL_RATE VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    HTS_FRGN_EHRT      VARCHAR2(4000),
    FRGN_NTBY_QTY      VARCHAR2(4000),
    FLNG_CLS_CODE      VARCHAR2(4000),
    ACML_PRTT_RATE     VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_DAILY_PRICE_API_NAME
    on DAILY_PRICE (API_NAME)
/

create table DISPLAY_BOARD_TOP
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    UNAS_PRPR           VARCHAR2(4000),
    UNAS_PRDY_VRSS      VARCHAR2(4000),
    UNAS_PRDY_VRSS_SIGN VARCHAR2(4000),
    UNAS_PRDY_CTRT      VARCHAR2(4000),
    UNAS_ACML_VOL       VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    FUTS_PRPR           VARCHAR2(4000),
    FUTS_PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    FUTS_PRDY_CTRT      VARCHAR2(4000),
    HTS_RMNN_DYNU       VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_DISPLAY_BOARD_TOP_API_NAME
    on DISPLAY_BOARD_TOP (API_NAME)
/

create table AVG_UNIT
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    EVLU_DT             VARCHAR2(4000),
    PDNO                VARCHAR2(4000),
    PRDT_TYPE_CD        VARCHAR2(4000),
    KIS_UNPR            VARCHAR2(4000),
    KBP_UNPR            VARCHAR2(4000),
    NICE_EVLU_UNPR      VARCHAR2(4000),
    FNP_UNPR            VARCHAR2(4000),
    AVG_EVLU_UNPR       VARCHAR2(4000),
    KIS_CRDT_GRAD_TEXT  VARCHAR2(4000),
    KBP_CRDT_GRAD_TEXT  VARCHAR2(4000),
    NICE_CRDT_GRAD_TEXT VARCHAR2(4000),
    FNP_CRDT_GRAD_TEXT  VARCHAR2(4000),
    CHNG_YN             VARCHAR2(4000),
    KIS_ERNG_RT         VARCHAR2(4000),
    KBP_ERNG_RT         VARCHAR2(4000),
    NICE_EVLU_ERNG_RT   VARCHAR2(4000),
    FNP_ERNG_RT         VARCHAR2(4000),
    AVG_EVLU_ERNG_RT    VARCHAR2(4000),
    KIS_RF_UNPR         VARCHAR2(4000),
    KBP_RF_UNPR         VARCHAR2(4000),
    NICE_EVLU_RF_UNPR   VARCHAR2(4000),
    AVG_EVLU_RF_UNPR    VARCHAR2(4000),
    KIS_EVLU_AMT        VARCHAR2(4000),
    KBP_EVLU_AMT        VARCHAR2(4000),
    NICE_EVLU_AMT       VARCHAR2(4000),
    FNP_EVLU_AMT        VARCHAR2(4000),
    AVG_EVLU_AMT        VARCHAR2(4000),
    OUTPUT3             VARCHAR2(4000),
    KIS_CRCY_CD         VARCHAR2(4000),
    KIS_EVLU_UNIT_PRIC  VARCHAR2(4000),
    KIS_EVLU_PRIC       VARCHAR2(4000),
    KBP_CRCY_CD         VARCHAR2(4000),
    KBP_EVLU_UNIT_PRIC  VARCHAR2(4000),
    KBP_EVLU_PRIC       VARCHAR2(4000),
    NICE_CRCY_CD        VARCHAR2(4000),
    NICE_EVLU_UNIT_PRIC VARCHAR2(4000),
    NICE_EVLU_PRIC      VARCHAR2(4000),
    AVG_EVLU_UNIT_PRIC  VARCHAR2(4000),
    AVG_EVLU_PRIC       VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_AVG_UNIT_API_NAME
    on AVG_UNIT (API_NAME)
/

create table BOND_ASKING_PRICE
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    STND_ISCD       VARCHAR2(4000),
    STCK_CNTG_HOUR  VARCHAR2(4000),
    ASKP_ERT1       VARCHAR2(4000),
    BIDP_ERT1       VARCHAR2(4000),
    ASKP1           VARCHAR2(4000),
    BIDP1           VARCHAR2(4000),
    ASKP_RSQN1      VARCHAR2(4000),
    BIDP_RSQN1      VARCHAR2(4000),
    ASKP_ERT2       VARCHAR2(4000),
    BIDP_ERT2       VARCHAR2(4000),
    ASKP2           VARCHAR2(4000),
    BIDP2           VARCHAR2(4000),
    ASKP_RSQN2      VARCHAR2(4000),
    BIDP_RSQN2      VARCHAR2(4000),
    ASKP_ERT3       VARCHAR2(4000),
    BIDP_ERT3       VARCHAR2(4000),
    ASKP3           VARCHAR2(4000),
    BIDP3           VARCHAR2(4000),
    ASKP_RSQN3      VARCHAR2(4000),
    BIDP_RSQN3      VARCHAR2(4000),
    ASKP_ERT4       VARCHAR2(4000),
    BIDP_ERT4       VARCHAR2(4000),
    ASKP4           VARCHAR2(4000),
    BIDP4           VARCHAR2(4000),
    ASKP_RSQN4      VARCHAR2(4000),
    BIDP_RSQN4      VARCHAR2(4000),
    ASKP_ERT5       VARCHAR2(4000),
    BIDP_ERT5       VARCHAR2(4000),
    ASKP5           VARCHAR2(4000),
    BIDP5           VARCHAR2(4000),
    ASKP_RSQN52     VARCHAR2(4000),
    BIDP_RSQN53     VARCHAR2(4000),
    TOTAL_ASKP_RSQN VARCHAR2(4000),
    TOTAL_BIDP_RSQN VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_BOND_ASKING_PRICE_API_NAME
    on BOND_ASKING_PRICE (API_NAME)
/

create table BOND_CCNL
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    STND_ISCD          VARCHAR2(4000),
    BOND_ISNM          VARCHAR2(4000),
    STCK_CNTG_HOUR     VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    STCK_PRPR          VARCHAR2(4000),
    CNTG_VOL           VARCHAR2(4000),
    STCK_OPRC          VARCHAR2(4000),
    STCK_HGPR          VARCHAR2(4000),
    STCK_LWPR          VARCHAR2(4000),
    STCK_PRDY_CLPR     VARCHAR2(4000),
    BOND_CNTG_ERT      VARCHAR2(4000),
    OPRC_ERT           VARCHAR2(4000),
    HGPR_ERT           VARCHAR2(4000),
    LWPR_ERT           VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    PRDY_VOL           VARCHAR2(4000),
    CNTG_TYPE_CLS_CODE VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_BOND_CCNL_API_NAME
    on BOND_CCNL (API_NAME)
/

create table BOND_INDEX_CCNL
(
    ID                            NUMBER         not null
        primary key,
    API_NAME                      VARCHAR2(4000) not null,
    NMIX_ID                       VARCHAR2(4000),
    STND_DATE1                    VARCHAR2(4000),
    TRNM_HOUR                     VARCHAR2(4000),
    TOTL_ERNN_NMIX_OPRC           VARCHAR2(4000),
    TOTL_ERNN_NMIX_HGPR           VARCHAR2(4000),
    TOTL_ERNN_NMIX_LWPR           VARCHAR2(4000),
    TOTL_ERNN_NMIX                VARCHAR2(4000),
    PRDY_TOTL_ERNN_NMIX           VARCHAR2(4000),
    TOTL_ERNN_NMIX_PRDY_VRSS      VARCHAR2(4000),
    TOTL_ERNN_NMIX_PRDY_VRSS_SIGN VARCHAR2(4000),
    TOTL_ERNN_NMIX_PRDY_CTRT      VARCHAR2(4000),
    CLEN_PRC_NMIX                 VARCHAR2(4000),
    MRKT_PRC_NMIX                 VARCHAR2(4000),
    BOND_CALL_RNVS_NMIX           VARCHAR2(4000),
    BOND_ZERO_RNVS_NMIX           VARCHAR2(4000),
    BOND_FUTS_THPR                VARCHAR2(4000),
    BOND_AVRG_DRTN_VAL            VARCHAR2(4000),
    BOND_AVRG_CNVX_VAL            VARCHAR2(4000),
    BOND_AVRG_YTM_VAL             VARCHAR2(4000),
    BOND_AVRG_FRDL_YTM_VAL        VARCHAR2(4000),
    CREATED_AT                    DATE           not null
)
/

create index IX_BOND_INDEX_CCNL_API_NAME
    on BOND_INDEX_CCNL (API_NAME)
/

create table BUY
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    KRX_FWDG_ORD_ORGNO VARCHAR2(4000),
    ODNO               VARCHAR2(4000),
    ORD_TMD            VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_BUY_API_NAME
    on BUY (API_NAME)
/

create table INQUIRE_ASKING_PRICE
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    RSYM       VARCHAR2(4000),
    ZDIV       VARCHAR2(4000),
    CURR       VARCHAR2(4000),
    BASE       VARCHAR2(4000),
    OPEN       VARCHAR2(4000),
    HIGH       VARCHAR2(4000),
    LOW        VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    DYMD       VARCHAR2(4000),
    DHMS       VARCHAR2(4000),
    BVOL       VARCHAR2(4000),
    AVOL       VARCHAR2(4000),
    BDVL       VARCHAR2(4000),
    ADVL       VARCHAR2(4000),
    CODE       VARCHAR2(4000),
    ROPEN      VARCHAR2(4000),
    RHIGH      VARCHAR2(4000),
    RLOW       VARCHAR2(4000),
    RCLOSE     VARCHAR2(4000),
    PBID1      VARCHAR2(4000),
    PASK1      VARCHAR2(4000),
    VBID1      VARCHAR2(4000),
    VASK1      VARCHAR2(4000),
    DBID1      VARCHAR2(4000),
    DASK1      VARCHAR2(4000),
    VSTM       VARCHAR2(4000),
    VETM       VARCHAR2(4000),
    CSBP       VARCHAR2(4000),
    CSHI       VARCHAR2(4000),
    CSLO       VARCHAR2(4000),
    IEP        VARCHAR2(4000),
    IEV        VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_INQUIRE_ASKING_PRICE_API_NAME
    on INQUIRE_ASKING_PRICE (API_NAME)
/

create table INQUIRE_BALANCE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    CANO                VARCHAR2(4000),
    ACNT_PRDT_CD        VARCHAR2(4000),
    PRDT_TYPE_CD        VARCHAR2(4000),
    OVRS_PDNO           VARCHAR2(4000),
    FRCR_EVLU_PFLS_AMT  VARCHAR2(4000),
    EVLU_PFLS_RT        VARCHAR2(4000),
    PCHS_AVG_PRIC       VARCHAR2(4000),
    OVRS_CBLC_QTY       VARCHAR2(4000),
    ORD_PSBL_QTY        VARCHAR2(4000),
    FRCR_PCHS_AMT1      VARCHAR2(4000),
    OVRS_STCK_EVLU_AMT  VARCHAR2(4000),
    NOW_PRIC2           VARCHAR2(4000),
    TR_CRCY_CD          VARCHAR2(4000),
    OVRS_EXCG_CD        VARCHAR2(4000),
    LOAN_TYPE_CD        VARCHAR2(4000),
    LOAN_DT             VARCHAR2(4000),
    EXPD_DT             VARCHAR2(4000),
    OVRS_RLZT_PFLS_AMT  VARCHAR2(4000),
    OVRS_TOT_PFLS       VARCHAR2(4000),
    RLZT_ERNG_RT        VARCHAR2(4000),
    TOT_EVLU_PFLS_AMT   VARCHAR2(4000),
    TOT_PFTRT           VARCHAR2(4000),
    FRCR_BUY_AMT_SMTL1  VARCHAR2(4000),
    OVRS_RLZT_PFLS_AMT2 VARCHAR2(4000),
    FRCR_BUY_AMT_SMTL2  VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_INQUIRE_BALANCE_API_NAME
    on INQUIRE_BALANCE (API_NAME)
/

create table INQUIRE_CCNL
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    ORD_DT               VARCHAR2(4000),
    ORD_GNO_BRNO         VARCHAR2(4000),
    ODNO                 VARCHAR2(4000),
    ORGN_ODNO            VARCHAR2(4000),
    SLL_BUY_DVSN_CD      VARCHAR2(4000),
    SLL_BUY_DVSN_CD_NAME VARCHAR2(4000),
    RVSE_CNCL_DVSN       VARCHAR2(4000),
    RVSE_CNCL_DVSN_NAME  VARCHAR2(4000),
    PDNO                 VARCHAR2(4000),
    PRDT_NAME            VARCHAR2(4000),
    FT_ORD_QTY           VARCHAR2(4000),
    FT_ORD_UNPR3         VARCHAR2(4000),
    FT_CCLD_QTY          VARCHAR2(4000),
    FT_CCLD_UNPR3        VARCHAR2(4000),
    FT_CCLD_AMT3         VARCHAR2(4000),
    NCCS_QTY             VARCHAR2(4000),
    PRCS_STAT_NAME       VARCHAR2(4000),
    RJCT_RSON            VARCHAR2(4000),
    RJCT_RSON_NAME       VARCHAR2(4000),
    ORD_TMD              VARCHAR2(4000),
    TR_MKET_NAME         VARCHAR2(4000),
    TR_CRCY_CD           VARCHAR2(4000),
    TR_NATN              VARCHAR2(4000),
    OVRS_EXCG_CD         VARCHAR2(4000),
    TR_NATN_NAME         VARCHAR2(4000),
    DMST_ORD_DT          VARCHAR2(4000),
    THCO_ORD_TMD         VARCHAR2(4000),
    LOAN_TYPE_CD         VARCHAR2(4000),
    LOAN_DT              VARCHAR2(4000),
    MDIA_DVSN_NAME       VARCHAR2(4000),
    USA_AMK_EXTS_RQST_YN VARCHAR2(4000),
    SPLT_BUY_ATTR_NAME   VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_INQUIRE_CCNL_API_NAME
    on INQUIRE_CCNL (API_NAME)
/

create table INQUIRE_DAILY_CCLD
(
    ID                    NUMBER         not null
        primary key,
    API_NAME              VARCHAR2(4000) not null,
    FM_TOT_CCLD_QTY       VARCHAR2(4000),
    FM_TOT_FUTR_AGRM_AMT  VARCHAR2(4000),
    FM_TOT_OPT_AGRM_AMT   VARCHAR2(4000),
    FM_FEE_SMTL           VARCHAR2(4000),
    DT                    VARCHAR2(4000),
    CCNO                  VARCHAR2(4000),
    OVRS_FUTR_FX_PDNO     VARCHAR2(4000),
    SLL_BUY_DVSN_CD       VARCHAR2(4000),
    FM_CCLD_QTY           VARCHAR2(4000),
    FM_CCLD_AMT           VARCHAR2(4000),
    FM_FUTR_CCLD_AMT      VARCHAR2(4000),
    FM_OPT_CCLD_AMT       VARCHAR2(4000),
    CRCY_CD               VARCHAR2(4000),
    FM_FEE                VARCHAR2(4000),
    FM_FUTR_PURE_AGRM_AMT VARCHAR2(4000),
    FM_OPT_PURE_AGRM_AMT  VARCHAR2(4000),
    CCLD_DTL_DTIME        VARCHAR2(4000),
    ORD_DT                VARCHAR2(4000),
    ODNO                  VARCHAR2(4000),
    ORD_MDIA_DVSN_NAME    VARCHAR2(4000),
    CREATED_AT            DATE           not null
)
/

create index IX_INQUIRE_DAILY_CCLD_API_NAME
    on INQUIRE_DAILY_CCLD (API_NAME)
/

create table INQUIRE_DAILY_ITEMCHARTPRICE
(
    ID                      NUMBER         not null
        primary key,
    API_NAME                VARCHAR2(4000) not null,
    PRDY_VRSS               VARCHAR2(4000),
    PRDY_VRSS_SIGN          VARCHAR2(4000),
    PRDY_CTRT               VARCHAR2(4000),
    STCK_PRDY_CLPR          VARCHAR2(4000),
    ACML_VOL                VARCHAR2(4000),
    ACML_TR_PBMN            VARCHAR2(4000),
    HTS_KOR_ISNM            VARCHAR2(4000),
    STCK_PRPR               VARCHAR2(4000),
    STCK_SHRN_ISCD          VARCHAR2(4000),
    PRDY_VOL                VARCHAR2(4000),
    STCK_MXPR               VARCHAR2(4000),
    STCK_LLAM               VARCHAR2(4000),
    STCK_OPRC               VARCHAR2(4000),
    STCK_HGPR               VARCHAR2(4000),
    STCK_LWPR               VARCHAR2(4000),
    STCK_PRDY_OPRC          VARCHAR2(4000),
    STCK_PRDY_HGPR          VARCHAR2(4000),
    STCK_PRDY_LWPR          VARCHAR2(4000),
    ASKP                    VARCHAR2(4000),
    BIDP                    VARCHAR2(4000),
    PRDY_VRSS_VOL           VARCHAR2(4000),
    VOL_TNRT                VARCHAR2(4000),
    STCK_FCAM               VARCHAR2(4000),
    LSTN_STCN               VARCHAR2(4000),
    CPFN                    VARCHAR2(4000),
    HTS_AVLS                VARCHAR2(4000),
    PER                     VARCHAR2(4000),
    EPS                     VARCHAR2(4000),
    PBR                     VARCHAR2(4000),
    ITEWHOL_LOAN_RMND_RATEM VARCHAR2(4000),
    STCK_BSOP_DATE          VARCHAR2(4000),
    STCK_CLPR               VARCHAR2(4000),
    FLNG_CLS_CODE           VARCHAR2(4000),
    PRTT_RATE               VARCHAR2(4000),
    MOD_YN                  VARCHAR2(4000),
    REVL_ISSU_REAS          VARCHAR2(4000),
    CREATED_AT              DATE           not null
)
/

create index IX_INQUIRE_DAILY_ITEMCHARTPRICE_API_NAME
    on INQUIRE_DAILY_ITEMCHARTPRICE (API_NAME)
/

create table INQUIRE_DAILY_PRICE
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    STCK_BSOP_DATE     VARCHAR2(4000),
    STCK_OPRC          VARCHAR2(4000),
    STCK_HGPR          VARCHAR2(4000),
    STCK_LWPR          VARCHAR2(4000),
    STCK_CLPR          VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    PRDY_VRSS_VOL_RATE VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    HTS_FRGN_EHRT      VARCHAR2(4000),
    FRGN_NTBY_QTY      VARCHAR2(4000),
    FLNG_CLS_CODE      VARCHAR2(4000),
    ACML_PRTT_RATE     VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_INQUIRE_DAILY_PRICE_API_NAME
    on INQUIRE_DAILY_PRICE (API_NAME)
/

create table INQUIRE_PRICE
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    PROC_DATE       VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    PROC_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    TRST_MGN        VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    BID_QNTT        VARCHAR2(4000),
    BID_PRICE       VARCHAR2(4000),
    ASK_QNTT        VARCHAR2(4000),
    ASK_PRICE       VARCHAR2(4000),
    PREV_PRICE      VARCHAR2(4000),
    EXCH_CD         VARCHAR2(4000),
    CRC_CD          VARCHAR2(4000),
    TRD_FR_DATE     VARCHAR2(4000),
    EXPR_DATE       VARCHAR2(4000),
    TRD_TO_DATE     VARCHAR2(4000),
    REMN_CNT        VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    TOT_ASK_QNTT    VARCHAR2(4000),
    TOT_BID_QNTT    VARCHAR2(4000),
    TICK_SIZE       VARCHAR2(4000),
    OPEN_DATE       VARCHAR2(4000),
    OPEN_TIME       VARCHAR2(4000),
    CLOSE_DATE      VARCHAR2(4000),
    CLOSE_TIME      VARCHAR2(4000),
    SBSNSDATE       VARCHAR2(4000),
    STTL_PRICE      VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_INQUIRE_PRICE_API_NAME
    on INQUIRE_PRICE (API_NAME)
/

create table INQUIRE_PSBL_ORDER
(
    ID                     NUMBER         not null
        primary key,
    API_NAME               VARCHAR2(4000) not null,
    ORD_PSBL_CASH          VARCHAR2(4000),
    ORD_PSBL_SBST          VARCHAR2(4000),
    RUSE_PSBL_AMT          VARCHAR2(4000),
    FUND_RPCH_CHGS         VARCHAR2(4000),
    PSBL_QTY_CALC_UNPR     VARCHAR2(4000),
    NRCVB_BUY_AMT          VARCHAR2(4000),
    NRCVB_BUY_QTY          VARCHAR2(4000),
    MAX_BUY_AMT            VARCHAR2(4000),
    MAX_BUY_QTY            VARCHAR2(4000),
    CMA_EVLU_AMT           VARCHAR2(4000),
    OVRS_RE_USE_AMT_WCRC   VARCHAR2(4000),
    ORD_PSBL_FRCR_AMT_WCRC VARCHAR2(4000),
    CREATED_AT             DATE           not null
)
/

create index IX_INQUIRE_PSBL_ORDER_API_NAME
    on INQUIRE_PSBL_ORDER (API_NAME)
/

create table INQUIRE_PSBL_RVSECNCL
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    ORD_GNO_BRNO        VARCHAR2(4000),
    ODNO                VARCHAR2(4000),
    ORGN_ODNO           VARCHAR2(4000),
    ORD_DVSN_NAME       VARCHAR2(4000),
    PDNO                VARCHAR2(4000),
    PRDT_NAME           VARCHAR2(4000),
    RVSE_CNCL_DVSN_NAME VARCHAR2(4000),
    ORD_QTY             VARCHAR2(4000),
    ORD_UNPR            VARCHAR2(4000),
    ORD_TMD             VARCHAR2(4000),
    TOT_CCLD_QTY        VARCHAR2(4000),
    TOT_CCLD_AMT        VARCHAR2(4000),
    PSBL_QTY            VARCHAR2(4000),
    SLL_BUY_DVSN_CD     VARCHAR2(4000),
    ORD_DVSN_CD         VARCHAR2(4000),
    MGCO_APTM_ODNO      VARCHAR2(4000),
    EXCG_DVSN_CD        VARCHAR2(4000),
    EXCG_ID_DVSN_CD     VARCHAR2(4000),
    EXCG_ID_DVSN_NAME   VARCHAR2(4000),
    STPM_CNDT_PRIC      VARCHAR2(4000),
    STPM_EFCT_OCCR_YN   VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_INQUIRE_PSBL_RVSECNCL_API_NAME
    on INQUIRE_PSBL_RVSECNCL (API_NAME)
/

create table ISSUE_INFO
(
    ID                         NUMBER         not null
        primary key,
    API_NAME                   VARCHAR2(4000) not null,
    PDNO                       VARCHAR2(4000),
    PRDT_TYPE_CD               VARCHAR2(4000),
    PRDT_NAME                  VARCHAR2(4000),
    PRDT_ENG_NAME              VARCHAR2(4000),
    IVST_HEED_PRDT_YN          VARCHAR2(4000),
    EXTS_YN                    VARCHAR2(4000),
    BOND_CLSF_CD               VARCHAR2(4000),
    BOND_CLSF_KOR_NAME         VARCHAR2(4000),
    PAPR                       VARCHAR2(4000),
    INT_MNED_DVSN_CD           VARCHAR2(4000),
    RVNU_SHAP_CD               VARCHAR2(4000),
    ISSU_AMT                   VARCHAR2(4000),
    LSTG_RMND                  VARCHAR2(4000),
    INT_DFRM_MCNT              VARCHAR2(4000),
    BOND_INT_DFRM_MTHD_CD      VARCHAR2(4000),
    SPLT_RDPT_RCNT             VARCHAR2(4000),
    PRCA_DFMT_TERM_MCNT        VARCHAR2(4000),
    INT_ANAP_DVSN_CD           VARCHAR2(4000),
    BOND_RGHT_DVSN_CD          VARCHAR2(4000),
    PRDT_PCLC_TEXT             VARCHAR2(4000),
    PRDT_ABRV_NAME             VARCHAR2(4000),
    PRDT_ENG_ABRV_NAME         VARCHAR2(4000),
    SPRX_PSBL_YN               VARCHAR2(4000),
    PBFF_PPLC_OFRG_MTHD_CD     VARCHAR2(4000),
    CMCO_CD                    VARCHAR2(4000),
    ISSU_ISTT_CD               VARCHAR2(4000),
    ISSU_ISTT_NAME             VARCHAR2(4000),
    PNIA_DFRM_AGCY_ISTT_CD     VARCHAR2(4000),
    DSCT_EC_RT                 VARCHAR2(4000),
    SRFC_INRT                  VARCHAR2(4000),
    EXPD_RDPT_RT               VARCHAR2(4000),
    EXPD_ASRC_ERNG_RT          VARCHAR2(4000),
    BOND_GRTE_ISTT_NAME        VARCHAR2(4000),
    INT_DFRM_DAY_TYPE_CD       VARCHAR2(4000),
    KSD_INT_CALC_UNIT_CD       VARCHAR2(4000),
    INT_WUNT_UDER_PRCS_DVSN_CD VARCHAR2(4000),
    RVNU_DT                    VARCHAR2(4000),
    ISSU_DT                    VARCHAR2(4000),
    LSTG_DT                    VARCHAR2(4000),
    EXPD_DT                    VARCHAR2(4000),
    RDPT_DT                    VARCHAR2(4000),
    SBST_PRIC                  VARCHAR2(4000),
    RGBF_INT_DFRM_DT           VARCHAR2(4000),
    NXTM_INT_DFRM_DT           VARCHAR2(4000),
    FRST_INT_DFRM_DT           VARCHAR2(4000),
    ECIS_PRIC                  VARCHAR2(4000),
    RGHT_STCK_STD_PDNO         VARCHAR2(4000),
    ECIS_OPNG_DT               VARCHAR2(4000),
    ECIS_END_DT                VARCHAR2(4000),
    BOND_RVNU_MTHD_CD          VARCHAR2(4000),
    OPRT_STFNO                 VARCHAR2(4000),
    OPRT_STFF_NAME             VARCHAR2(4000),
    RGBF_INT_DFRM_WDAY         VARCHAR2(4000),
    NXTM_INT_DFRM_WDAY         VARCHAR2(4000),
    KIS_CRDT_GRAD_TEXT         VARCHAR2(4000),
    KBP_CRDT_GRAD_TEXT         VARCHAR2(4000),
    NICE_CRDT_GRAD_TEXT        VARCHAR2(4000),
    FNP_CRDT_GRAD_TEXT         VARCHAR2(4000),
    DPSI_PSBL_YN               VARCHAR2(4000),
    PNIA_INT_CALC_UNPR         VARCHAR2(4000),
    PRCM_IDX_BOND_YN           VARCHAR2(4000),
    EXPD_EXTS_SRDP_RCNT        VARCHAR2(4000),
    EXPD_EXTS_SRDP_RT          VARCHAR2(4000),
    LOAN_PSBL_YN               VARCHAR2(4000),
    GRTE_DVSN_CD               VARCHAR2(4000),
    FNRR_RANK_DVSN_CD          VARCHAR2(4000),
    KRX_LSTG_ABOL_DVSN_CD      VARCHAR2(4000),
    ASST_RQDI_DVSN_CD          VARCHAR2(4000),
    OPCB_DVSN_CD               VARCHAR2(4000),
    CRFD_ITEM_YN               VARCHAR2(4000),
    CRFD_ITEM_RSTC_CCLC_DT     VARCHAR2(4000),
    BOND_NMPR_UNIT_PRIC        VARCHAR2(4000),
    IVST_HEED_BOND_DVSN_NAME   VARCHAR2(4000),
    ADD_ERNG_RT                VARCHAR2(4000),
    ADD_ERNG_RT_APLY_DT        VARCHAR2(4000),
    BOND_TR_STOP_DVSN_CD       VARCHAR2(4000),
    IVST_HEED_BOND_DVSN_CD     VARCHAR2(4000),
    PCLR_CNDT_TEXT             VARCHAR2(4000),
    HBBD_YN                    VARCHAR2(4000),
    CDTL_CPTL_SCTY_TYPE_CD     VARCHAR2(4000),
    ELEC_SCTY_YN               VARCHAR2(4000),
    SQ1_CLOP_ECIS_OPNG_DT      VARCHAR2(4000),
    FRST_ERLM_STFNO            VARCHAR2(4000),
    FRST_ERLM_DT               VARCHAR2(4000),
    FRST_ERLM_TMD              VARCHAR2(4000),
    TLG_RCVG_DTL_DTIME         VARCHAR2(4000),
    CREATED_AT                 DATE           not null
)
/

create index IX_ISSUE_INFO_API_NAME
    on ISSUE_INFO (API_NAME)
/

create table ORDER_RVSECNCL
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    KRX_FWDG_ORD_ORGNO VARCHAR2(4000),
    ODNO               VARCHAR2(4000),
    ORD_TMD            VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_ORDER_RVSECNCL_API_NAME
    on ORDER_RVSECNCL (API_NAME)
/

create table SEARCH_BOND_INFO
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    PDNO                         VARCHAR2(4000),
    PRDT_TYPE_CD                 VARCHAR2(4000),
    KSD_BOND_ITEM_NAME           VARCHAR2(4000),
    KSD_BOND_ITEM_ENG_NAME       VARCHAR2(4000),
    KSD_BOND_LSTG_TYPE_CD        VARCHAR2(4000),
    KSD_OFRG_DVSN_CD             VARCHAR2(4000),
    KSD_BOND_INT_DFRM_DVSN_CD    VARCHAR2(4000),
    ISSU_DT                      VARCHAR2(4000),
    RDPT_DT                      VARCHAR2(4000),
    RVNU_DT                      VARCHAR2(4000),
    ISO_CRCY_CD                  VARCHAR2(4000),
    MDWY_RDPT_DT                 VARCHAR2(4000),
    KSD_RCVG_BOND_DSCT_RT        VARCHAR2(4000),
    KSD_RCVG_BOND_SRFC_INRT      VARCHAR2(4000),
    BOND_EXPD_RDPT_RT            VARCHAR2(4000),
    KSD_PRCA_RDPT_MTHD_CD        VARCHAR2(4000),
    INT_CALTM_MCNT               VARCHAR2(4000),
    KSD_INT_CALC_UNIT_CD         VARCHAR2(4000),
    UVAL_CUT_DVSN_CD             VARCHAR2(4000),
    UVAL_CUT_DCPT_DGIT           VARCHAR2(4000),
    KSD_DYDV_CALTM_APLY_DVSN_CD  VARCHAR2(4000),
    DYDV_CALC_DCNT               VARCHAR2(4000),
    BOND_EXPD_ASRC_ERNG_RT       VARCHAR2(4000),
    PADF_PLAC_HDOF_NAME          VARCHAR2(4000),
    LSTG_DT                      VARCHAR2(4000),
    LSTG_ABOL_DT                 VARCHAR2(4000),
    KSD_BOND_ISSU_MTHD_CD        VARCHAR2(4000),
    LAPS_INDF_YN                 VARCHAR2(4000),
    KSD_LHDY_PNIA_DFRM_MTHD_CD   VARCHAR2(4000),
    FRST_INT_DFRM_DT             VARCHAR2(4000),
    KSD_PRCM_LNKG_GVBD_YN        VARCHAR2(4000),
    DPSI_END_DT                  VARCHAR2(4000),
    DPSI_STRT_DT                 VARCHAR2(4000),
    DPSI_PSBL_YN                 VARCHAR2(4000),
    ATYP_RDPT_BOND_ERLM_YN       VARCHAR2(4000),
    DSHN_OCCR_YN                 VARCHAR2(4000),
    EXPD_EXTS_YN                 VARCHAR2(4000),
    PCLR_PTCR_TEXT               VARCHAR2(4000),
    DPSI_PSBL_EXCP_STAT_CD       VARCHAR2(4000),
    EXPD_EXTS_SRDP_RCNT          VARCHAR2(4000),
    EXPD_EXTS_SRDP_RT            VARCHAR2(4000),
    EXPD_RDPT_RT                 VARCHAR2(4000),
    EXPD_ASRC_ERNG_RT            VARCHAR2(4000),
    BOND_INT_DFRM_MTHD_CD        VARCHAR2(4000),
    INT_DFRM_DAY_TYPE_CD         VARCHAR2(4000),
    PRCA_DFMT_TERM_MCNT          VARCHAR2(4000),
    SPLT_RDPT_RCNT               VARCHAR2(4000),
    RGBF_INT_DFRM_DT             VARCHAR2(4000),
    NXTM_INT_DFRM_DT             VARCHAR2(4000),
    SPRX_PSBL_YN                 VARCHAR2(4000),
    ICTX_RT_DVSN_CD              VARCHAR2(4000),
    BOND_CLSF_CD                 VARCHAR2(4000),
    BOND_CLSF_KOR_NAME           VARCHAR2(4000),
    INT_MNED_DVSN_CD             VARCHAR2(4000),
    PNIA_INT_CALC_UNPR           VARCHAR2(4000),
    FRN_INTR                     VARCHAR2(4000),
    APLY_DAY_PRCM_IDX_LNKG_CEFC  VARCHAR2(4000),
    KSD_EXPD_DYDV_CALC_BASS_CD   VARCHAR2(4000),
    EXPD_DYDV_CALC_DCNT          VARCHAR2(4000),
    KSD_CBBW_DVSN_CD             VARCHAR2(4000),
    CRFD_ITEM_YN                 VARCHAR2(4000),
    PNIA_BANK_OFDY_DFRM_MTHD_CD  VARCHAR2(4000),
    QIB_YN                       VARCHAR2(4000),
    QIB_CCLC_DT                  VARCHAR2(4000),
    CSBD_YN                      VARCHAR2(4000),
    CSBD_CCLC_DT                 VARCHAR2(4000),
    KSD_OPCB_YN                  VARCHAR2(4000),
    KSD_SODN_YN                  VARCHAR2(4000),
    KSD_RQDI_SCTY_YN             VARCHAR2(4000),
    ELEC_SCTY_YN                 VARCHAR2(4000),
    RGHT_ECIS_MBDY_DVSN_CD       VARCHAR2(4000),
    INT_RKNG_MTHD_DVSN_CD        VARCHAR2(4000),
    OFRG_DVSN_CD                 VARCHAR2(4000),
    KSD_TOT_ISSU_AMT             VARCHAR2(4000),
    NEXT_INDF_CHK_ECLS_YN        VARCHAR2(4000),
    KSD_BOND_INTR_DVSN_CD        VARCHAR2(4000),
    KSD_INRT_APLY_DVSN_CD        VARCHAR2(4000),
    KRX_ISSU_ISTT_CD             VARCHAR2(4000),
    KSD_INDF_FRQC_UDER_CALC_CD   VARCHAR2(4000),
    KSD_INDF_FRQC_UDER_CALC_DCNT VARCHAR2(4000),
    TLG_RCVG_DTL_DTIME           VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_SEARCH_BOND_INFO_API_NAME
    on SEARCH_BOND_INFO (API_NAME)
/

create table SELL
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    KRX_FWDG_ORD_ORGNO VARCHAR2(4000),
    ODNO               VARCHAR2(4000),
    ORD_TMD            VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_SELL_API_NAME
    on SELL (API_NAME)
/

create table COMMODITY_FUTURES_REALTIME_CONCLUSION
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    FUTS_SHRN_ISCD              VARCHAR2(4000),
    BSOP_HOUR                   VARCHAR2(4000),
    FUTS_PRDY_VRSS              VARCHAR2(4000),
    PRDY_VRSS_SIGN              VARCHAR2(4000),
    FUTS_PRDY_CTRT              VARCHAR2(4000),
    FUTS_PRPR                   VARCHAR2(4000),
    FUTS_OPRC                   VARCHAR2(4000),
    FUTS_HGPR                   VARCHAR2(4000),
    FUTS_LWPR                   VARCHAR2(4000),
    LAST_CNQN                   VARCHAR2(4000),
    ACML_VOL                    VARCHAR2(4000),
    ACML_TR_PBMN                VARCHAR2(4000),
    HTS_THPR                    VARCHAR2(4000),
    MRKT_BASIS                  VARCHAR2(4000),
    DPRT                        VARCHAR2(4000),
    NMSC_FCTN_STPL_PRC          VARCHAR2(4000),
    FMSC_FCTN_STPL_PRC          VARCHAR2(4000),
    SPEAD_PRC                   VARCHAR2(4000),
    HTS_OTST_STPL_QTY           VARCHAR2(4000),
    OTST_STPL_QTY_ICDC          VARCHAR2(4000),
    OPRC_HOUR                   VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN         VARCHAR2(4000),
    OPRC_VRSS_NMIX_PRPR         VARCHAR2(4000),
    HGPR_HOUR                   VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    HGPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    LWPR_HOUR                   VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    LWPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    SHNU_RATE                   VARCHAR2(4000),
    CTTR                        VARCHAR2(4000),
    ESDG                        VARCHAR2(4000),
    OTST_STPL_RGBF_QTY_ICDC     VARCHAR2(4000),
    THPR_BASIS                  VARCHAR2(4000),
    FUTS_ASKP1                  VARCHAR2(4000),
    FUTS_BIDP1                  VARCHAR2(4000),
    ASKP_RSQN1                  VARCHAR2(4000),
    BIDP_RSQN1                  VARCHAR2(4000),
    SELN_CNTG_CSNU              VARCHAR2(4000),
    SHNU_CNTG_CSNU              VARCHAR2(4000),
    NTBY_CNTG_CSNU              VARCHAR2(4000),
    SELN_CNTG_SMTN              VARCHAR2(4000),
    SHNU_CNTG_SMTN              VARCHAR2(4000),
    TOTAL_ASKP_RSQN             VARCHAR2(4000),
    TOTAL_BIDP_RSQN             VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE VARCHAR2(4000),
    DSCS_BLTR_ACML_QTY          VARCHAR2(4000),
    DYNM_MXPR                   VARCHAR2(4000),
    DYNM_LLAM                   VARCHAR2(4000),
    DYNM_PRC_LIMT_YN            VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_COMMODITY_FUTURES_REALTIME_CONCLUSION_API_NAME
    on COMMODITY_FUTURES_REALTIME_CONCLUSION (API_NAME)
/

create table COMMODITY_FUTURES_REALTIME_QUOTE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    FUTS_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    FUTS_ASKP1           VARCHAR2(4000),
    FUTS_ASKP2           VARCHAR2(4000),
    FUTS_ASKP3           VARCHAR2(4000),
    FUTS_ASKP4           VARCHAR2(4000),
    FUTS_ASKP5           VARCHAR2(4000),
    FUTS_BIDP1           VARCHAR2(4000),
    FUTS_BIDP2           VARCHAR2(4000),
    FUTS_BIDP3           VARCHAR2(4000),
    FUTS_BIDP4           VARCHAR2(4000),
    FUTS_BIDP5           VARCHAR2(4000),
    ASKP_CSNU1           VARCHAR2(4000),
    ASKP_CSNU2           VARCHAR2(4000),
    ASKP_CSNU3           VARCHAR2(4000),
    ASKP_CSNU4           VARCHAR2(4000),
    ASKP_CSNU5           VARCHAR2(4000),
    BIDP_CSNU1           VARCHAR2(4000),
    BIDP_CSNU2           VARCHAR2(4000),
    BIDP_CSNU3           VARCHAR2(4000),
    BIDP_CSNU4           VARCHAR2(4000),
    BIDP_CSNU5           VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    TOTAL_ASKP_CSNU      VARCHAR2(4000),
    TOTAL_BIDP_CSNU      VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_COMMODITY_FUTURES_REALTIME_QUOTE_API_NAME
    on COMMODITY_FUTURES_REALTIME_QUOTE (API_NAME)
/

create table DISPLAY_BOARD_CALLPUT
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    ACPR                VARCHAR2(4000),
    UNCH_PRPR           VARCHAR2(4000),
    OPTN_SHRN_ISCD      VARCHAR2(4000),
    OPTN_PRPR           VARCHAR2(4000),
    OPTN_PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    OPTN_PRDY_CTRT      VARCHAR2(4000),
    OPTN_BIDP           VARCHAR2(4000),
    OPTN_ASKP           VARCHAR2(4000),
    TMVL_VAL            VARCHAR2(4000),
    NMIX_SDPR           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    SELN_RSQN           VARCHAR2(4000),
    SHNU_RSQN           VARCHAR2(4000),
    ACML_TR_PBMN        VARCHAR2(4000),
    HTS_OTST_STPL_QTY   VARCHAR2(4000),
    OTST_STPL_QTY_ICDC  VARCHAR2(4000),
    DELTA_VAL           VARCHAR2(4000),
    GAMA                VARCHAR2(4000),
    VEGA                VARCHAR2(4000),
    THETA               VARCHAR2(4000),
    RHO                 VARCHAR2(4000),
    HTS_INTS_VLTL       VARCHAR2(4000),
    INVL_VAL            VARCHAR2(4000),
    ESDG                VARCHAR2(4000),
    DPRT                VARCHAR2(4000),
    HIST_VLTL           VARCHAR2(4000),
    HTS_THPR            VARCHAR2(4000),
    OPTN_OPRC           VARCHAR2(4000),
    OPTN_HGPR           VARCHAR2(4000),
    OPTN_LWPR           VARCHAR2(4000),
    OPTN_MXPR           VARCHAR2(4000),
    OPTN_LLAM           VARCHAR2(4000),
    ATM_CLS_NAME        VARCHAR2(4000),
    RGBF_VRSS_ICDC      VARCHAR2(4000),
    TOTAL_ASKP_RSQN     VARCHAR2(4000),
    TOTAL_BIDP_RSQN     VARCHAR2(4000),
    FUTS_ANTC_CNPR      VARCHAR2(4000),
    FUTS_ANTC_CNTG_VRSS VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_DISPLAY_BOARD_CALLPUT_API_NAME
    on DISPLAY_BOARD_CALLPUT (API_NAME)
/

create table DISPLAY_BOARD_FUTURES
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    FUTS_SHRN_ISCD      VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    FUTS_PRPR           VARCHAR2(4000),
    FUTS_PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    FUTS_PRDY_CTRT      VARCHAR2(4000),
    HTS_THPR            VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    FUTS_ASKP           VARCHAR2(4000),
    FUTS_BIDP           VARCHAR2(4000),
    HTS_OTST_STPL_QTY   VARCHAR2(4000),
    FUTS_HGPR           VARCHAR2(4000),
    FUTS_LWPR           VARCHAR2(4000),
    HTS_RMNN_DYNU       VARCHAR2(4000),
    TOTAL_ASKP_RSQN     VARCHAR2(4000),
    TOTAL_BIDP_RSQN     VARCHAR2(4000),
    FUTS_ANTC_CNPR      VARCHAR2(4000),
    FUTS_ANTC_CNTG_VRSS VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_DISPLAY_BOARD_FUTURES_API_NAME
    on DISPLAY_BOARD_FUTURES (API_NAME)
/

create table DISPLAY_BOARD_OPTION_LIST
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    MTRT_YYMM_CODE VARCHAR2(4000),
    MTRT_YYMM      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_DISPLAY_BOARD_OPTION_LIST_API_NAME
    on DISPLAY_BOARD_OPTION_LIST (API_NAME)
/

create table EXP_PRICE_TREND
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    RPRS_MRKT_KOR_NAME  VARCHAR2(4000),
    ANTC_CNPR           VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    ANTC_CNTG_VRSS      VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT VARCHAR2(4000),
    ANTC_VOL            VARCHAR2(4000),
    ANTC_TR_PBMN        VARCHAR2(4000),
    STCK_BSOP_DATE      VARCHAR2(4000),
    STCK_CNTG_HOUR      VARCHAR2(4000),
    STCK_PRPR           VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_EXP_PRICE_TREND_API_NAME
    on EXP_PRICE_TREND (API_NAME)
/

create table FUOPT_CCNL_NOTICE
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    CUST_ID        VARCHAR2(4000),
    ACNT_NO        VARCHAR2(4000),
    ODER_NO        VARCHAR2(4000),
    OODER_NO       VARCHAR2(4000),
    SELN_BYOV_CLS  VARCHAR2(4000),
    RCTF_CLS       VARCHAR2(4000),
    ODER_KIND2     VARCHAR2(4000),
    STCK_SHRN_ISCD VARCHAR2(4000),
    CNTG_QTY       VARCHAR2(4000),
    CNTG_UNPR      VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    RFUS_YN        VARCHAR2(4000),
    CNTG_YN        VARCHAR2(4000),
    ACPT_YN        VARCHAR2(4000),
    BRNC_NO        VARCHAR2(4000),
    ODER_QTY       VARCHAR2(4000),
    ACNT_NAME      VARCHAR2(4000),
    CNTG_ISNM      VARCHAR2(4000),
    ODER_COND      VARCHAR2(4000),
    ORD_GRP        VARCHAR2(4000),
    ORD_GRPSEQ     VARCHAR2(4000),
    ORDER_PRC      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_FUOPT_CCNL_NOTICE_API_NAME
    on FUOPT_CCNL_NOTICE (API_NAME)
/

create table FUTURES_EXP_CCNL
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    FUTS_SHRN_ISCD      VARCHAR2(4000),
    BSOP_HOUR           VARCHAR2(4000),
    ANTC_CNPR           VARCHAR2(4000),
    ANTC_CNTG_VRSS      VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT VARCHAR2(4000),
    ANTC_MKOP_CLS_CODE  VARCHAR2(4000),
    ANTC_CNQN           VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_FUTURES_EXP_CCNL_API_NAME
    on FUTURES_EXP_CCNL (API_NAME)
/

create table INDEX_FUTURES_REALTIME_CONCLUSION
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    FUTS_SHRN_ISCD              VARCHAR2(4000),
    BSOP_HOUR                   VARCHAR2(4000),
    FUTS_PRDY_VRSS              VARCHAR2(4000),
    PRDY_VRSS_SIGN              VARCHAR2(4000),
    FUTS_PRDY_CTRT              VARCHAR2(4000),
    FUTS_PRPR                   VARCHAR2(4000),
    FUTS_OPRC                   VARCHAR2(4000),
    FUTS_HGPR                   VARCHAR2(4000),
    FUTS_LWPR                   VARCHAR2(4000),
    LAST_CNQN                   VARCHAR2(4000),
    ACML_VOL                    VARCHAR2(4000),
    ACML_TR_PBMN                VARCHAR2(4000),
    HTS_THPR                    VARCHAR2(4000),
    MRKT_BASIS                  VARCHAR2(4000),
    DPRT                        VARCHAR2(4000),
    NMSC_FCTN_STPL_PRC          VARCHAR2(4000),
    FMSC_FCTN_STPL_PRC          VARCHAR2(4000),
    SPEAD_PRC                   VARCHAR2(4000),
    HTS_OTST_STPL_QTY           VARCHAR2(4000),
    OTST_STPL_QTY_ICDC          VARCHAR2(4000),
    OPRC_HOUR                   VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN         VARCHAR2(4000),
    OPRC_VRSS_NMIX_PRPR         VARCHAR2(4000),
    HGPR_HOUR                   VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    HGPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    LWPR_HOUR                   VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    LWPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    SHNU_RATE                   VARCHAR2(4000),
    CTTR                        VARCHAR2(4000),
    ESDG                        VARCHAR2(4000),
    OTST_STPL_RGBF_QTY_ICDC     VARCHAR2(4000),
    THPR_BASIS                  VARCHAR2(4000),
    FUTS_ASKP1                  VARCHAR2(4000),
    FUTS_BIDP1                  VARCHAR2(4000),
    ASKP_RSQN1                  VARCHAR2(4000),
    BIDP_RSQN1                  VARCHAR2(4000),
    SELN_CNTG_CSNU              VARCHAR2(4000),
    SHNU_CNTG_CSNU              VARCHAR2(4000),
    NTBY_CNTG_CSNU              VARCHAR2(4000),
    SELN_CNTG_SMTN              VARCHAR2(4000),
    SHNU_CNTG_SMTN              VARCHAR2(4000),
    TOTAL_ASKP_RSQN             VARCHAR2(4000),
    TOTAL_BIDP_RSQN             VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE VARCHAR2(4000),
    DSCS_BLTR_ACML_QTY          VARCHAR2(4000),
    DYNM_MXPR                   VARCHAR2(4000),
    DYNM_LLAM                   VARCHAR2(4000),
    DYNM_PRC_LIMT_YN            VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_INDEX_FUTURES_REALTIME_CONCLUSION_API_NAME
    on INDEX_FUTURES_REALTIME_CONCLUSION (API_NAME)
/

create table INDEX_FUTURES_REALTIME_QUOTE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    FUTS_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    FUTS_ASKP1           VARCHAR2(4000),
    FUTS_ASKP2           VARCHAR2(4000),
    FUTS_ASKP3           VARCHAR2(4000),
    FUTS_ASKP4           VARCHAR2(4000),
    FUTS_ASKP5           VARCHAR2(4000),
    FUTS_BIDP1           VARCHAR2(4000),
    FUTS_BIDP2           VARCHAR2(4000),
    FUTS_BIDP3           VARCHAR2(4000),
    FUTS_BIDP4           VARCHAR2(4000),
    FUTS_BIDP5           VARCHAR2(4000),
    ASKP_CSNU1           VARCHAR2(4000),
    ASKP_CSNU2           VARCHAR2(4000),
    ASKP_CSNU3           VARCHAR2(4000),
    ASKP_CSNU4           VARCHAR2(4000),
    ASKP_CSNU5           VARCHAR2(4000),
    BIDP_CSNU1           VARCHAR2(4000),
    BIDP_CSNU2           VARCHAR2(4000),
    BIDP_CSNU3           VARCHAR2(4000),
    BIDP_CSNU4           VARCHAR2(4000),
    BIDP_CSNU5           VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    TOTAL_ASKP_CSNU      VARCHAR2(4000),
    TOTAL_BIDP_CSNU      VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_INDEX_FUTURES_REALTIME_QUOTE_API_NAME
    on INDEX_FUTURES_REALTIME_QUOTE (API_NAME)
/

create table INDEX_OPTION_REALTIME_CONCLUSION
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    OPTN_SHRN_ISCD              VARCHAR2(4000),
    BSOP_HOUR                   VARCHAR2(4000),
    OPTN_PRPR                   VARCHAR2(4000),
    PRDY_VRSS_SIGN              VARCHAR2(4000),
    OPTN_PRDY_VRSS              VARCHAR2(4000),
    PRDY_CTRT                   VARCHAR2(4000),
    OPTN_OPRC                   VARCHAR2(4000),
    OPTN_HGPR                   VARCHAR2(4000),
    OPTN_LWPR                   VARCHAR2(4000),
    LAST_CNQN                   VARCHAR2(4000),
    ACML_VOL                    VARCHAR2(4000),
    ACML_TR_PBMN                VARCHAR2(4000),
    HTS_THPR                    VARCHAR2(4000),
    HTS_OTST_STPL_QTY           VARCHAR2(4000),
    OTST_STPL_QTY_ICDC          VARCHAR2(4000),
    OPRC_HOUR                   VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN         VARCHAR2(4000),
    OPRC_VRSS_NMIX_PRPR         VARCHAR2(4000),
    HGPR_HOUR                   VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    HGPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    LWPR_HOUR                   VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    LWPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    SHNU_RATE                   VARCHAR2(4000),
    PRMM_VAL                    VARCHAR2(4000),
    INVL_VAL                    VARCHAR2(4000),
    TMVL_VAL                    VARCHAR2(4000),
    DELTA                       VARCHAR2(4000),
    GAMA                        VARCHAR2(4000),
    VEGA                        VARCHAR2(4000),
    THETA                       VARCHAR2(4000),
    RHO                         VARCHAR2(4000),
    HTS_INTS_VLTL               VARCHAR2(4000),
    ESDG                        VARCHAR2(4000),
    OTST_STPL_RGBF_QTY_ICDC     VARCHAR2(4000),
    THPR_BASIS                  VARCHAR2(4000),
    UNAS_HIST_VLTL              VARCHAR2(4000),
    CTTR                        VARCHAR2(4000),
    DPRT                        VARCHAR2(4000),
    MRKT_BASIS                  VARCHAR2(4000),
    OPTN_ASKP1                  VARCHAR2(4000),
    OPTN_BIDP1                  VARCHAR2(4000),
    ASKP_RSQN1                  VARCHAR2(4000),
    BIDP_RSQN1                  VARCHAR2(4000),
    SELN_CNTG_CSNU              VARCHAR2(4000),
    SHNU_CNTG_CSNU              VARCHAR2(4000),
    NTBY_CNTG_CSNU              VARCHAR2(4000),
    SELN_CNTG_SMTN              VARCHAR2(4000),
    SHNU_CNTG_SMTN              VARCHAR2(4000),
    TOTAL_ASKP_RSQN             VARCHAR2(4000),
    TOTAL_BIDP_RSQN             VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE VARCHAR2(4000),
    AVRG_VLTL                   VARCHAR2(4000),
    DSCS_LRQN_VOL               VARCHAR2(4000),
    DYNM_MXPR                   VARCHAR2(4000),
    DYNM_LLAM                   VARCHAR2(4000),
    DYNM_PRC_LIMT_YN            VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_INDEX_OPTION_REALTIME_CONCLUSION_API_NAME
    on INDEX_OPTION_REALTIME_CONCLUSION (API_NAME)
/

create table INDEX_OPTION_REALTIME_QUOTE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    OPTN_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    OPTN_ASKP1           VARCHAR2(4000),
    OPTN_ASKP2           VARCHAR2(4000),
    OPTN_ASKP3           VARCHAR2(4000),
    OPTN_ASKP4           VARCHAR2(4000),
    OPTN_ASKP5           VARCHAR2(4000),
    OPTN_BIDP1           VARCHAR2(4000),
    OPTN_BIDP2           VARCHAR2(4000),
    OPTN_BIDP3           VARCHAR2(4000),
    OPTN_BIDP4           VARCHAR2(4000),
    OPTN_BIDP5           VARCHAR2(4000),
    ASKP_CSNU1           VARCHAR2(4000),
    ASKP_CSNU2           VARCHAR2(4000),
    ASKP_CSNU3           VARCHAR2(4000),
    ASKP_CSNU4           VARCHAR2(4000),
    ASKP_CSNU5           VARCHAR2(4000),
    BIDP_CSNU1           VARCHAR2(4000),
    BIDP_CSNU2           VARCHAR2(4000),
    BIDP_CSNU3           VARCHAR2(4000),
    BIDP_CSNU4           VARCHAR2(4000),
    BIDP_CSNU5           VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    TOTAL_ASKP_CSNU      VARCHAR2(4000),
    TOTAL_BIDP_CSNU      VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_INDEX_OPTION_REALTIME_QUOTE_API_NAME
    on INDEX_OPTION_REALTIME_QUOTE (API_NAME)
/

create table INQUIRE_BALANCE_SETTLEMENT_PL
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    PDNO             VARCHAR2(4000),
    PRDT_NAME        VARCHAR2(4000),
    TRAD_DVSN_NAME   VARCHAR2(4000),
    BFDY_CBLC_QTY    VARCHAR2(4000),
    NEW_QTY          VARCHAR2(4000),
    MNPL_RPCH_QTY    VARCHAR2(4000),
    CBLC_QTY         VARCHAR2(4000),
    CBLC_AMT         VARCHAR2(4000),
    TRAD_PFLS_AMT    VARCHAR2(4000),
    EVLU_AMT         VARCHAR2(4000),
    EVLU_PFLS_AMT    VARCHAR2(4000),
    NXDY_DNCA        VARCHAR2(4000),
    MMGA_CASH        VARCHAR2(4000),
    BRKG_MGNA_CASH   VARCHAR2(4000),
    OPT_BUY_CHGS     VARCHAR2(4000),
    OPT_LQD_EVLU_AMT VARCHAR2(4000),
    DNCA_SBST        VARCHAR2(4000),
    MMGA_TOTA        VARCHAR2(4000),
    BRKG_MGNA_TOTA   VARCHAR2(4000),
    OPT_SLL_CHGS     VARCHAR2(4000),
    FEE              VARCHAR2(4000),
    THDT_DFPA        VARCHAR2(4000),
    RNWL_DFPA        VARCHAR2(4000),
    DNCA_CASH        VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_INQUIRE_BALANCE_SETTLEMENT_PL_API_NAME
    on INQUIRE_BALANCE_SETTLEMENT_PL (API_NAME)
/

create table INQUIRE_BALANCE_VALUATION_PL
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    CANO               VARCHAR2(4000),
    ACNT_PRDT_CD       VARCHAR2(4000),
    PDNO               VARCHAR2(4000),
    PRDT_TYPE_CD       VARCHAR2(4000),
    SHTN_PDNO          VARCHAR2(4000),
    PRDT_NAME          VARCHAR2(4000),
    SLL_BUY_DVSN_NAME  VARCHAR2(4000),
    CBLC_QTY1          VARCHAR2(4000),
    EXCC_UNPR          VARCHAR2(4000),
    CCLD_AVG_UNPR1     VARCHAR2(4000),
    IDX_CLPR           VARCHAR2(4000),
    PCHS_AMT           VARCHAR2(4000),
    EVLU_AMT           VARCHAR2(4000),
    EVLU_PFLS_AMT      VARCHAR2(4000),
    TRAD_PFLS_AMT      VARCHAR2(4000),
    LQD_PSBL_QTY       VARCHAR2(4000),
    DNCA_CASH          VARCHAR2(4000),
    FRCR_DNCL_AMT      VARCHAR2(4000),
    DNCA_SBST          VARCHAR2(4000),
    TOT_DNCL_AMT       VARCHAR2(4000),
    TOT_CCLD_AMT       VARCHAR2(4000),
    CASH_MGNA          VARCHAR2(4000),
    SBST_MGNA          VARCHAR2(4000),
    MGNA_TOTA          VARCHAR2(4000),
    OPT_DFPA           VARCHAR2(4000),
    THDT_DFPA          VARCHAR2(4000),
    RNWL_DFPA          VARCHAR2(4000),
    FEE                VARCHAR2(4000),
    NXDY_DNCA          VARCHAR2(4000),
    NXDY_DNCL_AMT      VARCHAR2(4000),
    PRSM_DPAST         VARCHAR2(4000),
    PRSM_DPAST_AMT     VARCHAR2(4000),
    PPRT_ORD_PSBL_CASH VARCHAR2(4000),
    ADD_MGNA_CASH      VARCHAR2(4000),
    ADD_MGNA_TOTA      VARCHAR2(4000),
    FUTR_TRAD_PFLS_AMT VARCHAR2(4000),
    OPT_TRAD_PFLS_AMT  VARCHAR2(4000),
    FUTR_EVLU_PFLS_AMT VARCHAR2(4000),
    OPT_EVLU_PFLS_AMT  VARCHAR2(4000),
    TRAD_PFLS_AMT_SMTL VARCHAR2(4000),
    EVLU_PFLS_AMT_SMTL VARCHAR2(4000),
    WDRW_PSBL_TOT_AMT  VARCHAR2(4000),
    ORD_PSBL_CASH      VARCHAR2(4000),
    ORD_PSBL_SBST      VARCHAR2(4000),
    ORD_PSBL_TOTA      VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_INQUIRE_BALANCE_VALUATION_PL_API_NAME
    on INQUIRE_BALANCE_VALUATION_PL (API_NAME)
/

create table INQUIRE_CCNL_BSTIME
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    PDNO              VARCHAR2(4000),
    PRDT_NAME         VARCHAR2(4000),
    ODNO              VARCHAR2(4000),
    TR_TYPE_NAME      VARCHAR2(4000),
    LAST_STTLDT       VARCHAR2(4000),
    CCLD_IDX          VARCHAR2(4000),
    CCLD_QTY          VARCHAR2(4000),
    TRAD_AMT          VARCHAR2(4000),
    FEE               VARCHAR2(4000),
    CCLD_BTWN         VARCHAR2(4000),
    TOT_CCLD_QTY_SMTL VARCHAR2(4000),
    TOT_CCLD_AMT_SMTL VARCHAR2(4000),
    FEE_ADJT          VARCHAR2(4000),
    FEE_SMTL          VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_INQUIRE_CCNL_BSTIME_API_NAME
    on INQUIRE_CCNL_BSTIME (API_NAME)
/

create table INQUIRE_DAILY_AMOUNT_FEE
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    ORD_DT             VARCHAR2(4000),
    PDNO               VARCHAR2(4000),
    ITEM_NAME          VARCHAR2(4000),
    SLL_AGRM_AMT       VARCHAR2(4000),
    SLL_FEE            VARCHAR2(4000),
    BUY_AGRM_AMT       VARCHAR2(4000),
    BUY_FEE            VARCHAR2(4000),
    TOT_FEE_SMTL       VARCHAR2(4000),
    TRAD_PFLS          VARCHAR2(4000),
    FUTR_AGRM          VARCHAR2(4000),
    FUTR_AGRM_AMT      VARCHAR2(4000),
    FUTR_AGRM_AMT_SMTL VARCHAR2(4000),
    FUTR_SLL_FEE_SMTL  VARCHAR2(4000),
    FUTR_BUY_FEE_SMTL  VARCHAR2(4000),
    FUTR_FEE_SMTL      VARCHAR2(4000),
    OPT_AGRM           VARCHAR2(4000),
    OPT_AGRM_AMT       VARCHAR2(4000),
    OPT_AGRM_AMT_SMTL  VARCHAR2(4000),
    OPT_SLL_FEE_SMTL   VARCHAR2(4000),
    OPT_BUY_FEE_SMTL   VARCHAR2(4000),
    OPT_FEE_SMTL       VARCHAR2(4000),
    PRDT_FUTR_AGRM     VARCHAR2(4000),
    PRDT_FUOP          VARCHAR2(4000),
    PRDT_FUTR_EVLU_AMT VARCHAR2(4000),
    FUTR_FEE           VARCHAR2(4000),
    OPT_FEE            VARCHAR2(4000),
    FEE                VARCHAR2(4000),
    AGRM_AMT_SMTL      VARCHAR2(4000),
    FEE_SMTL           VARCHAR2(4000),
    TRAD_PFLS_SMTL     VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_INQUIRE_DAILY_AMOUNT_FEE_API_NAME
    on INQUIRE_DAILY_AMOUNT_FEE (API_NAME)
/

create table INQUIRE_DAILY_FUOPCHARTPRICE
(
    ID                      NUMBER         not null
        primary key,
    API_NAME                VARCHAR2(4000) not null,
    FUTS_PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN          VARCHAR2(4000),
    FUTS_PRDY_CTRT          VARCHAR2(4000),
    FUTS_PRDY_CLPR          VARCHAR2(4000),
    ACML_VOL                VARCHAR2(4000),
    ACML_TR_PBMN            VARCHAR2(4000),
    HTS_KOR_ISNM            VARCHAR2(4000),
    FUTS_PRPR               VARCHAR2(4000),
    FUTS_SHRN_ISCD          VARCHAR2(4000),
    PRDY_VOL                VARCHAR2(4000),
    FUTS_MXPR               VARCHAR2(4000),
    FUTS_LLAM               VARCHAR2(4000),
    FUTS_OPRC               VARCHAR2(4000),
    FUTS_HGPR               VARCHAR2(4000),
    FUTS_LWPR               VARCHAR2(4000),
    FUTS_PRDY_OPRC          VARCHAR2(4000),
    FUTS_PRDY_HGPR          VARCHAR2(4000),
    FUTS_PRDY_LWPR          VARCHAR2(4000),
    FUTS_ASKP               VARCHAR2(4000),
    FUTS_BIDP               VARCHAR2(4000),
    BASIS                   VARCHAR2(4000),
    KOSPI200_NMIX           VARCHAR2(4000),
    KOSPI200_PRDY_VRSS      VARCHAR2(4000),
    KOSPI200_PRDY_CTRT      VARCHAR2(4000),
    KOSPI200_PRDY_VRSS_SIGN VARCHAR2(4000),
    HTS_OTST_STPL_QTY       VARCHAR2(4000),
    OTST_STPL_QTY_ICDC      VARCHAR2(4000),
    TDAY_RLTV               VARCHAR2(4000),
    HTS_THPR                VARCHAR2(4000),
    DPRT                    VARCHAR2(4000),
    STCK_BSOP_DATE          VARCHAR2(4000),
    MOD_YN                  VARCHAR2(4000),
    CREATED_AT              DATE           not null
)
/

create index IX_INQUIRE_DAILY_FUOPCHARTPRICE_API_NAME
    on INQUIRE_DAILY_FUOPCHARTPRICE (API_NAME)
/

create table INQUIRE_DEPOSIT
(
    ID                        NUMBER         not null
        primary key,
    API_NAME                  VARCHAR2(4000) not null,
    FM_NXDY_DNCL_AMT          VARCHAR2(4000),
    FM_TOT_ASST_EVLU_AMT      VARCHAR2(4000),
    CANO                      VARCHAR2(4000),
    ACNT_PRDT_CD              VARCHAR2(4000),
    CRCY_CD                   VARCHAR2(4000),
    RESP_DT                   VARCHAR2(4000),
    FM_DNCA_RMND              VARCHAR2(4000),
    FM_LQD_PFLS_AMT           VARCHAR2(4000),
    FM_FEE                    VARCHAR2(4000),
    FM_FUOP_EVLU_PFLS_AMT     VARCHAR2(4000),
    FM_RCVB_AMT               VARCHAR2(4000),
    FM_BRKG_MGN_AMT           VARCHAR2(4000),
    FM_MNTN_MGN_AMT           VARCHAR2(4000),
    FM_ADD_MGN_AMT            VARCHAR2(4000),
    FM_RISK_RT                VARCHAR2(4000),
    FM_ORD_PSBL_AMT           VARCHAR2(4000),
    FM_DRWG_PSBL_AMT          VARCHAR2(4000),
    FM_ECHM_RQRM_AMT          VARCHAR2(4000),
    FM_DRWG_PRAR_AMT          VARCHAR2(4000),
    FM_OPT_TR_CHGS            VARCHAR2(4000),
    FM_OPT_ICLD_ASST_EVLU_AMT VARCHAR2(4000),
    FM_OPT_EVLU_AMT           VARCHAR2(4000),
    FM_CRCY_SBST_AMT          VARCHAR2(4000),
    FM_CRCY_SBST_USE_AMT      VARCHAR2(4000),
    FM_CRCY_SBST_STUP_AMT     VARCHAR2(4000),
    CREATED_AT                DATE           not null
)
/

create index IX_INQUIRE_DEPOSIT_API_NAME
    on INQUIRE_DEPOSIT (API_NAME)
/

create table INQUIRE_NGT_BALANCE
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    CANO               VARCHAR2(4000),
    ACNT_PRDT_CD       VARCHAR2(4000),
    PDNO               VARCHAR2(4000),
    PRDT_TYPE_CD       VARCHAR2(4000),
    SHTN_PDNO          VARCHAR2(4000),
    PRDT_NAME          VARCHAR2(4000),
    SLL_BUY_DVSN_NAME  VARCHAR2(4000),
    SLL_BUY_DVSN_CD    VARCHAR2(4000),
    TRAD_DVSN_NAME     VARCHAR2(4000),
    CBLC_QTY           VARCHAR2(4000),
    EXCC_UNPR          VARCHAR2(4000),
    CCLD_AVG_UNPR1     VARCHAR2(4000),
    IDX_CLPR           VARCHAR2(4000),
    PCHS_AMT           VARCHAR2(4000),
    EVLU_AMT           VARCHAR2(4000),
    EVLU_PFLS_AMT      VARCHAR2(4000),
    TRAD_PFLS_AMT      VARCHAR2(4000),
    LQD_PSBL_QTY       VARCHAR2(4000),
    DNCA_CASH          VARCHAR2(4000),
    FRCR_DNCL_AMT      VARCHAR2(4000),
    DNCA_SBST          VARCHAR2(4000),
    TOT_DNCL_AMT       VARCHAR2(4000),
    CASH_MGNA          VARCHAR2(4000),
    SBST_MGNA          VARCHAR2(4000),
    MGNA_TOTA          VARCHAR2(4000),
    OPT_DFPA           VARCHAR2(4000),
    THDT_DFPA          VARCHAR2(4000),
    RNWL_DFPA          VARCHAR2(4000),
    FEE                VARCHAR2(4000),
    NXDY_DNCA          VARCHAR2(4000),
    NXDY_DNCL_AMT      VARCHAR2(4000),
    PRSM_DPAST         VARCHAR2(4000),
    PPRT_ORD_PSBL_CASH VARCHAR2(4000),
    ADD_MGNA_CASH      VARCHAR2(4000),
    ADD_MGNA_TOTA      VARCHAR2(4000),
    FUTR_TRAD_PFLS_AMT VARCHAR2(4000),
    OPT_TRAD_PFLS_AMT  VARCHAR2(4000),
    FUTR_EVLU_PFLS_AMT VARCHAR2(4000),
    OPT_EVLU_PFLS_AMT  VARCHAR2(4000),
    TRAD_PFLS_AMT_SMTL VARCHAR2(4000),
    EVLU_PFLS_AMT_SMTL VARCHAR2(4000),
    WDRW_PSBL_TOT_AMT  VARCHAR2(4000),
    ORD_PSBL_CASH      VARCHAR2(4000),
    ORD_PSBL_SBST      VARCHAR2(4000),
    ORD_PSBL_TOTA      VARCHAR2(4000),
    MMGA_TOT_AMT       VARCHAR2(4000),
    MMGA_CASH_AMT      VARCHAR2(4000),
    MTNC_RT            VARCHAR2(4000),
    ISFC_AMT           VARCHAR2(4000),
    PCHS_AMT_SMTL      VARCHAR2(4000),
    EVLU_AMT_SMTL      VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_INQUIRE_NGT_BALANCE_API_NAME
    on INQUIRE_NGT_BALANCE (API_NAME)
/

create table INQUIRE_NGT_CCNL
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    ORD_GNO_BRNO             VARCHAR2(4000),
    CANO                     VARCHAR2(4000),
    CSAC_NAME                VARCHAR2(4000),
    ACNT_PRDT_CD             VARCHAR2(4000),
    ORD_DT                   VARCHAR2(4000),
    ODNO                     VARCHAR2(4000),
    ORGN_ODNO                VARCHAR2(4000),
    SLL_BUY_DVSN_CD          VARCHAR2(4000),
    TRAD_DVSN_NAME           VARCHAR2(4000),
    NMPR_TYPE_NAME           VARCHAR2(4000),
    PDNO                     VARCHAR2(4000),
    PRDT_NAME                VARCHAR2(4000),
    PRDT_TYPE_CD             VARCHAR2(4000),
    ORD_QTY                  VARCHAR2(4000),
    ORD_IDX4                 VARCHAR2(4000),
    QTY                      VARCHAR2(4000),
    ORD_TMD                  VARCHAR2(4000),
    TOT_CCLD_QTY             VARCHAR2(4000),
    AVG_IDX                  VARCHAR2(4000),
    TOT_CCLD_AMT             VARCHAR2(4000),
    RJCT_QTY                 VARCHAR2(4000),
    INGR_TRAD_RJCT_RSON_CD   VARCHAR2(4000),
    INGR_TRAD_RJCT_RSON_NAME VARCHAR2(4000),
    ORD_STFNO                VARCHAR2(4000),
    SPRD_ITEM_YN             VARCHAR2(4000),
    ORD_IP_ADDR              VARCHAR2(4000),
    TOT_ORD_QTY              VARCHAR2(4000),
    "tot_ccld_qty_SMTL"      VARCHAR2(4000),
    "tot_ccld_amt_SMTL"      VARCHAR2(4000),
    FEE                      VARCHAR2(4000),
    CTAC_TLNO                VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_INQUIRE_NGT_CCNL_API_NAME
    on INQUIRE_NGT_CCNL (API_NAME)
/

create table INQUIRE_PSBL_NGT_ORDER
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    MAX_ORD_PSBL_QTY VARCHAR2(4000),
    TOT_PSBL_QTY     VARCHAR2(4000),
    LQD_PSBL_QTY     VARCHAR2(4000),
    LQD_PSBL_QTY_1   VARCHAR2(4000),
    ORD_PSBL_QTY     VARCHAR2(4000),
    BASS_IDX         VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_INQUIRE_PSBL_NGT_ORDER_API_NAME
    on INQUIRE_PSBL_NGT_ORDER (API_NAME)
/

create table INQUIRE_TIME_FUOPCHARTPRICE
(
    ID                      NUMBER         not null
        primary key,
    API_NAME                VARCHAR2(4000) not null,
    FUTS_PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN          VARCHAR2(4000),
    FUTS_PRDY_CTRT          VARCHAR2(4000),
    FUTS_PRDY_CLPR          VARCHAR2(4000),
    PRDY_NMIX               VARCHAR2(4000),
    ACML_VOL                VARCHAR2(4000),
    ACML_TR_PBMN            VARCHAR2(4000),
    HTS_KOR_ISNM            VARCHAR2(4000),
    FUTS_PRPR               VARCHAR2(4000),
    FUTS_SHRN_ISCD          VARCHAR2(4000),
    PRDY_VOL                VARCHAR2(4000),
    FUTS_MXPR               VARCHAR2(4000),
    FUTS_LLAM               VARCHAR2(4000),
    FUTS_OPRC               VARCHAR2(4000),
    FUTS_HGPR               VARCHAR2(4000),
    FUTS_LWPR               VARCHAR2(4000),
    FUTS_PRDY_OPRC          VARCHAR2(4000),
    FUTS_PRDY_HGPR          VARCHAR2(4000),
    FUTS_PRDY_LWPR          VARCHAR2(4000),
    FUTS_ASKP               VARCHAR2(4000),
    FUTS_BIDP               VARCHAR2(4000),
    BASIS                   VARCHAR2(4000),
    KOSPI200_NMIX           VARCHAR2(4000),
    KOSPI200_PRDY_VRSS      VARCHAR2(4000),
    KOSPI200_PRDY_CTRT      VARCHAR2(4000),
    KOSPI200_PRDY_VRSS_SIGN VARCHAR2(4000),
    HTS_OTST_STPL_QTY       VARCHAR2(4000),
    OTST_STPL_QTY_ICDC      VARCHAR2(4000),
    TDAY_RLTV               VARCHAR2(4000),
    HTS_THPR                VARCHAR2(4000),
    DPRT                    VARCHAR2(4000),
    STCK_BSOP_DATE          VARCHAR2(4000),
    STCK_CNTG_HOUR          VARCHAR2(4000),
    CNTG_VOL                VARCHAR2(4000),
    CREATED_AT              DATE           not null
)
/

create index IX_INQUIRE_TIME_FUOPCHARTPRICE_API_NAME
    on INQUIRE_TIME_FUOPCHARTPRICE (API_NAME)
/

create table KRX_NGT_FUTURES_ASKING_PRICE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    FUTS_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    FUTS_ASKP1           VARCHAR2(4000),
    FUTS_ASKP2           VARCHAR2(4000),
    FUTS_ASKP3           VARCHAR2(4000),
    FUTS_ASKP4           VARCHAR2(4000),
    FUTS_ASKP5           VARCHAR2(4000),
    FUTS_BIDP1           VARCHAR2(4000),
    FUTS_BIDP2           VARCHAR2(4000),
    FUTS_BIDP3           VARCHAR2(4000),
    FUTS_BIDP4           VARCHAR2(4000),
    FUTS_BIDP5           VARCHAR2(4000),
    ASKP_CSNU1           VARCHAR2(4000),
    ASKP_CSNU2           VARCHAR2(4000),
    ASKP_CSNU3           VARCHAR2(4000),
    ASKP_CSNU4           VARCHAR2(4000),
    ASKP_CSNU5           VARCHAR2(4000),
    BIDP_CSNU1           VARCHAR2(4000),
    BIDP_CSNU2           VARCHAR2(4000),
    BIDP_CSNU3           VARCHAR2(4000),
    BIDP_CSNU4           VARCHAR2(4000),
    BIDP_CSNU5           VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    TOTAL_ASKP_CSNU      VARCHAR2(4000),
    TOTAL_BIDP_CSNU      VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_KRX_NGT_FUTURES_ASKING_PRICE_API_NAME
    on KRX_NGT_FUTURES_ASKING_PRICE (API_NAME)
/

create table KRX_NGT_FUTURES_CCNL
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    FUTS_SHRN_ISCD              VARCHAR2(4000),
    BSOP_HOUR                   VARCHAR2(4000),
    FUTS_PRDY_VRSS              VARCHAR2(4000),
    PRDY_VRSS_SIGN              VARCHAR2(4000),
    FUTS_PRDY_CTRT              VARCHAR2(4000),
    FUTS_PRPR                   VARCHAR2(4000),
    FUTS_OPRC                   VARCHAR2(4000),
    FUTS_HGPR                   VARCHAR2(4000),
    FUTS_LWPR                   VARCHAR2(4000),
    LAST_CNQN                   VARCHAR2(4000),
    ACML_VOL                    VARCHAR2(4000),
    ACML_TR_PBMN                VARCHAR2(4000),
    HTS_THPR                    VARCHAR2(4000),
    MRKT_BASIS                  VARCHAR2(4000),
    DPRT                        VARCHAR2(4000),
    NMSC_FCTN_STPL_PRC          VARCHAR2(4000),
    FMSC_FCTN_STPL_PRC          VARCHAR2(4000),
    SPEAD_PRC                   VARCHAR2(4000),
    HTS_OTST_STPL_QTY           VARCHAR2(4000),
    OTST_STPL_QTY_ICDC          VARCHAR2(4000),
    OPRC_HOUR                   VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN         VARCHAR2(4000),
    OPRC_VRSS_NMIX_PRPR         VARCHAR2(4000),
    HGPR_HOUR                   VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    HGPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    LWPR_HOUR                   VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    LWPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    SHNU_RATE                   VARCHAR2(4000),
    CTTR                        VARCHAR2(4000),
    ESDG                        VARCHAR2(4000),
    OTST_STPL_RGBF_QTY_ICDC     VARCHAR2(4000),
    THPR_BASIS                  VARCHAR2(4000),
    FUTS_ASKP1                  VARCHAR2(4000),
    FUTS_BIDP1                  VARCHAR2(4000),
    ASKP_RSQN1                  VARCHAR2(4000),
    BIDP_RSQN1                  VARCHAR2(4000),
    SELN_CNTG_CSNU              VARCHAR2(4000),
    SHNU_CNTG_CSNU              VARCHAR2(4000),
    NTBY_CNTG_CSNU              VARCHAR2(4000),
    SELN_CNTG_SMTN              VARCHAR2(4000),
    SHNU_CNTG_SMTN              VARCHAR2(4000),
    TOTAL_ASKP_RSQN             VARCHAR2(4000),
    TOTAL_BIDP_RSQN             VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE VARCHAR2(4000),
    DYNM_MXPR                   VARCHAR2(4000),
    DYNM_LLAM                   VARCHAR2(4000),
    DYNM_PRC_LIMT_YN            VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_KRX_NGT_FUTURES_CCNL_API_NAME
    on KRX_NGT_FUTURES_CCNL (API_NAME)
/

create table KRX_NGT_FUTURES_CCNL_NOTICE
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    CUST_ID        VARCHAR2(4000),
    ACNT_NO        VARCHAR2(4000),
    ODER_NO        VARCHAR2(4000),
    OODER_NO       VARCHAR2(4000),
    SELN_BYOV_CLS  VARCHAR2(4000),
    RCTF_CLS       VARCHAR2(4000),
    ODER_KIND2     VARCHAR2(4000),
    STCK_SHRN_ISCD VARCHAR2(4000),
    CNTG_QTY       VARCHAR2(4000),
    CNTG_UNPR      VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    RFUS_YN        VARCHAR2(4000),
    CNTG_YN        VARCHAR2(4000),
    ACPT_YN        VARCHAR2(4000),
    BRNC_NO        VARCHAR2(4000),
    ODER_QTY       VARCHAR2(4000),
    ACNT_NAME      VARCHAR2(4000),
    CNTG_ISNM      VARCHAR2(4000),
    ODER_COND      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_KRX_NGT_FUTURES_CCNL_NOTICE_API_NAME
    on KRX_NGT_FUTURES_CCNL_NOTICE (API_NAME)
/

create table KRX_NGT_OPTION_ASKING_PRICE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    OPTN_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    OPTN_ASKP1           VARCHAR2(4000),
    OPTN_ASKP2           VARCHAR2(4000),
    OPTN_ASKP3           VARCHAR2(4000),
    OPTN_ASKP4           VARCHAR2(4000),
    OPTN_ASKP5           VARCHAR2(4000),
    OPTN_BIDP1           VARCHAR2(4000),
    OPTN_BIDP2           VARCHAR2(4000),
    OPTN_BIDP3           VARCHAR2(4000),
    OPTN_BIDP4           VARCHAR2(4000),
    OPTN_BIDP5           VARCHAR2(4000),
    ASKP_CSNU1           VARCHAR2(4000),
    ASKP_CSNU2           VARCHAR2(4000),
    ASKP_CSNU3           VARCHAR2(4000),
    ASKP_CSNU4           VARCHAR2(4000),
    ASKP_CSNU5           VARCHAR2(4000),
    BIDP_CSNU1           VARCHAR2(4000),
    BIDP_CSNU2           VARCHAR2(4000),
    BIDP_CSNU3           VARCHAR2(4000),
    BIDP_CSNU4           VARCHAR2(4000),
    BIDP_CSNU5           VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    TOTAL_ASKP_CSNU      VARCHAR2(4000),
    TOTAL_BIDP_CSNU      VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_KRX_NGT_OPTION_ASKING_PRICE_API_NAME
    on KRX_NGT_OPTION_ASKING_PRICE (API_NAME)
/

create table KRX_NGT_OPTION_CCNL
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    OPTN_SHRN_ISCD              VARCHAR2(4000),
    BSOP_HOUR                   VARCHAR2(4000),
    OPTN_PRPR                   VARCHAR2(4000),
    PRDY_VRSS_SIGN              VARCHAR2(4000),
    OPTN_PRDY_VRSS              VARCHAR2(4000),
    PRDY_CTRT                   VARCHAR2(4000),
    OPTN_OPRC                   VARCHAR2(4000),
    OPTN_HGPR                   VARCHAR2(4000),
    OPTN_LWPR                   VARCHAR2(4000),
    LAST_CNQN                   VARCHAR2(4000),
    ACML_VOL                    VARCHAR2(4000),
    ACML_TR_PBMN                VARCHAR2(4000),
    HTS_THPR                    VARCHAR2(4000),
    HTS_OTST_STPL_QTY           VARCHAR2(4000),
    OTST_STPL_QTY_ICDC          VARCHAR2(4000),
    OPRC_HOUR                   VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN         VARCHAR2(4000),
    OPRC_VRSS_NMIX_PRPR         VARCHAR2(4000),
    HGPR_HOUR                   VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    HGPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    LWPR_HOUR                   VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    LWPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    SHNU_RATE                   VARCHAR2(4000),
    PRMM_VAL                    VARCHAR2(4000),
    INVL_VAL                    VARCHAR2(4000),
    TMVL_VAL                    VARCHAR2(4000),
    DELTA                       VARCHAR2(4000),
    GAMA                        VARCHAR2(4000),
    VEGA                        VARCHAR2(4000),
    THETA                       VARCHAR2(4000),
    RHO                         VARCHAR2(4000),
    HTS_INTS_VLTL               VARCHAR2(4000),
    ESDG                        VARCHAR2(4000),
    OTST_STPL_RGBF_QTY_ICDC     VARCHAR2(4000),
    THPR_BASIS                  VARCHAR2(4000),
    UNAS_HIST_VLTL              VARCHAR2(4000),
    CTTR                        VARCHAR2(4000),
    DPRT                        VARCHAR2(4000),
    MRKT_BASIS                  VARCHAR2(4000),
    OPTN_ASKP1                  VARCHAR2(4000),
    OPTN_BIDP1                  VARCHAR2(4000),
    ASKP_RSQN1                  VARCHAR2(4000),
    BIDP_RSQN1                  VARCHAR2(4000),
    SELN_CNTG_CSNU              VARCHAR2(4000),
    SHNU_CNTG_CSNU              VARCHAR2(4000),
    NTBY_CNTG_CSNU              VARCHAR2(4000),
    SELN_CNTG_SMTN              VARCHAR2(4000),
    SHNU_CNTG_SMTN              VARCHAR2(4000),
    TOTAL_ASKP_RSQN             VARCHAR2(4000),
    TOTAL_BIDP_RSQN             VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE VARCHAR2(4000),
    DYNM_MXPR                   VARCHAR2(4000),
    DYNM_PRC_LIMT_YN            VARCHAR2(4000),
    DYNM_LLAM                   VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_KRX_NGT_OPTION_CCNL_API_NAME
    on KRX_NGT_OPTION_CCNL (API_NAME)
/

create table KRX_NGT_OPTION_EXP_CCNL
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    OPTN_SHRN_ISCD      VARCHAR2(4000),
    BSOP_HOUR           VARCHAR2(4000),
    ANTC_CNPR           VARCHAR2(4000),
    ANTC_CNTG_VRSS      VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT VARCHAR2(4000),
    ANTC_MKOP_CLS_CODE  VARCHAR2(4000),
    ANTC_CNQN           VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_KRX_NGT_OPTION_EXP_CCNL_API_NAME
    on KRX_NGT_OPTION_EXP_CCNL (API_NAME)
/

create table KRX_NGT_OPTION_NOTICE
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    CUST_ID        VARCHAR2(4000),
    ACNT_NO        VARCHAR2(4000),
    ODER_NO        VARCHAR2(4000),
    OODER_NO       VARCHAR2(4000),
    SELN_BYOV_CLS  VARCHAR2(4000),
    RCTF_CLS       VARCHAR2(4000),
    ODER_KIND2     VARCHAR2(4000),
    STCK_SHRN_ISCD VARCHAR2(4000),
    CNTG_QTY       VARCHAR2(4000),
    CNTG_UNPR      VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    RFUS_YN        VARCHAR2(4000),
    CNTG_YN        VARCHAR2(4000),
    ACPT_YN        VARCHAR2(4000),
    BRNC_NO        VARCHAR2(4000),
    ODER_QTY       VARCHAR2(4000),
    ACNT_NAME      VARCHAR2(4000),
    CNTG_ISNM      VARCHAR2(4000),
    ODER_COND      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_KRX_NGT_OPTION_NOTICE_API_NAME
    on KRX_NGT_OPTION_NOTICE (API_NAME)
/

create table NGT_MARGIN_DETAIL
(
    ID                         NUMBER         not null
        primary key,
    API_NAME                   VARCHAR2(4000) not null,
    FUTR_NEW_MGN_AMT           VARCHAR2(4000),
    FUTR_SPRD_ORD_MGNA         VARCHAR2(4000),
    OPT_SLL_NEW_MGN_AMT        VARCHAR2(4000),
    OPT_BUY_NEW_MGN_AMT        VARCHAR2(4000),
    NEW_MGN_AMT                VARCHAR2(4000),
    OPT_PRIC_MGNA              VARCHAR2(4000),
    FUOP_PRIC_ALTR_MGNA        VARCHAR2(4000),
    FUTR_SPRD_MGNA             VARCHAR2(4000),
    UWDL_MGNA                  VARCHAR2(4000),
    CTRT_PER_MIN_MGNA          VARCHAR2(4000),
    TOT_RISK_MGNA              VARCHAR2(4000),
    NETRISK_BRKG_MGNA          VARCHAR2(4000),
    OPT_SLL_CHGS               VARCHAR2(4000),
    OPT_BUY_CHGS               VARCHAR2(4000),
    FUTR_LOSS_AMT              VARCHAR2(4000),
    FUTR_PRFT_AMT              VARCHAR2(4000),
    THDT_CCLD_NET_LOSS_AMT     VARCHAR2(4000),
    BRKG_MGNA                  VARCHAR2(4000),
    DNCA_CASH                  VARCHAR2(4000),
    DNCA_SBST                  VARCHAR2(4000),
    DNCA_TOTA                  VARCHAR2(4000),
    WDRW_PSBL_CASH_AMT         VARCHAR2(4000),
    WDRW_PSBL_SBSA             VARCHAR2(4000),
    WDRW_PSBL_TOT_AMT          VARCHAR2(4000),
    ORD_PSBL_CASH_AMT          VARCHAR2(4000),
    ORD_PSBL_SBSA              VARCHAR2(4000),
    ORD_PSBL_TOT_AMT           VARCHAR2(4000),
    BRKG_MGNA_CASH_AMT         VARCHAR2(4000),
    BRKG_MGNA_SBST             VARCHAR2(4000),
    BRKG_MGNA_TOT_AMT          VARCHAR2(4000),
    ADD_MGNA_CASH_AMT          VARCHAR2(4000),
    ADD_MGNA_SBSA              VARCHAR2(4000),
    ADD_MGNA_TOT_AMT           VARCHAR2(4000),
    BFDY_SBST_SLL_SBST_AMT     VARCHAR2(4000),
    THDT_SBST_SLL_SBST_AMT     VARCHAR2(4000),
    BFDY_SBST_SLL_CCLD_AMT     VARCHAR2(4000),
    THDT_SBST_SLL_CCLD_AMT     VARCHAR2(4000),
    OPT_DFPA                   VARCHAR2(4000),
    EXCC_DFPA                  VARCHAR2(4000),
    FEE_AMT                    VARCHAR2(4000),
    NXDY_DNCL_AMT              VARCHAR2(4000),
    PRSM_DPAST_AMT             VARCHAR2(4000),
    OPT_BUY_EXUS_ACNT_YN       VARCHAR2(4000),
    BASE_DPSA_GDAT_GRAD_CD     VARCHAR2(4000),
    OPT_BASE_DPSA_GDAT_GRAD_CD VARCHAR2(4000),
    CREATED_AT                 DATE           not null
)
/

create index IX_NGT_MARGIN_DETAIL_API_NAME
    on NGT_MARGIN_DETAIL (API_NAME)
/

create table OPTION_EXP_CCNL
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    OPTN_SHRN_ISCD      VARCHAR2(4000),
    BSOP_HOUR           VARCHAR2(4000),
    ANTC_CNPR           VARCHAR2(4000),
    ANTC_CNTG_VRSS      VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT VARCHAR2(4000),
    ANTC_MKOP_CLS_CODE  VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_OPTION_EXP_CCNL_API_NAME
    on OPTION_EXP_CCNL (API_NAME)
/

create table "order"
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    KRX_FWDG_ORD_ORGNO VARCHAR2(4000),
    ODNO               VARCHAR2(4000),
    ORD_TMD            VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_ORDER_API_NAME
    on "order" (API_NAME)
/

create table STOCK_FUTURES_REALTIME_CONCLUSION
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    FUTS_SHRN_ISCD              VARCHAR2(4000),
    BSOP_HOUR                   VARCHAR2(4000),
    STCK_PRPR                   VARCHAR2(4000),
    PRDY_VRSS_SIGN              VARCHAR2(4000),
    PRDY_VRSS                   VARCHAR2(4000),
    FUTS_PRDY_CTRT              VARCHAR2(4000),
    STCK_OPRC                   VARCHAR2(4000),
    STCK_HGPR                   VARCHAR2(4000),
    STCK_LWPR                   VARCHAR2(4000),
    LAST_CNQN                   VARCHAR2(4000),
    ACML_VOL                    VARCHAR2(4000),
    ACML_TR_PBMN                VARCHAR2(4000),
    HTS_THPR                    VARCHAR2(4000),
    MRKT_BASIS                  VARCHAR2(4000),
    DPRT                        VARCHAR2(4000),
    NMSC_FCTN_STPL_PRC          VARCHAR2(4000),
    FMSC_FCTN_STPL_PRC          VARCHAR2(4000),
    SPEAD_PRC                   VARCHAR2(4000),
    HTS_OTST_STPL_QTY           VARCHAR2(4000),
    OTST_STPL_QTY_ICDC          VARCHAR2(4000),
    OPRC_HOUR                   VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN         VARCHAR2(4000),
    OPRC_VRSS_PRPR              VARCHAR2(4000),
    HGPR_HOUR                   VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    HGPR_VRSS_PRPR              VARCHAR2(4000),
    LWPR_HOUR                   VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    LWPR_VRSS_PRPR              VARCHAR2(4000),
    SHNU_RATE                   VARCHAR2(4000),
    CTTR                        VARCHAR2(4000),
    ESDG                        VARCHAR2(4000),
    OTST_STPL_RGBF_QTY_ICDC     VARCHAR2(4000),
    THPR_BASIS                  VARCHAR2(4000),
    ASKP1                       VARCHAR2(4000),
    BIDP1                       VARCHAR2(4000),
    ASKP_RSQN1                  VARCHAR2(4000),
    BIDP_RSQN1                  VARCHAR2(4000),
    SELN_CNTG_CSNU              VARCHAR2(4000),
    SHNU_CNTG_CSNU              VARCHAR2(4000),
    NTBY_CNTG_CSNU              VARCHAR2(4000),
    SELN_CNTG_SMTN              VARCHAR2(4000),
    SHNU_CNTG_SMTN              VARCHAR2(4000),
    TOTAL_ASKP_RSQN             VARCHAR2(4000),
    TOTAL_BIDP_RSQN             VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE VARCHAR2(4000),
    DYNM_MXPR                   VARCHAR2(4000),
    DYNM_LLAM                   VARCHAR2(4000),
    DYNM_PRC_LIMT_YN            VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_STOCK_FUTURES_REALTIME_CONCLUSION_API_NAME
    on STOCK_FUTURES_REALTIME_CONCLUSION (API_NAME)
/

create table STOCK_FUTURES_REALTIME_QUOTE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    FUTS_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    ASKP1                VARCHAR2(4000),
    ASKP2                VARCHAR2(4000),
    ASKP3                VARCHAR2(4000),
    ASKP4                VARCHAR2(4000),
    ASKP5                VARCHAR2(4000),
    ASKP6                VARCHAR2(4000),
    ASKP7                VARCHAR2(4000),
    ASKP8                VARCHAR2(4000),
    ASKP9                VARCHAR2(4000),
    ASKP10               VARCHAR2(4000),
    BIDP1                VARCHAR2(4000),
    BIDP2                VARCHAR2(4000),
    BIDP3                VARCHAR2(4000),
    BIDP4                VARCHAR2(4000),
    BIDP5                VARCHAR2(4000),
    BIDP6                VARCHAR2(4000),
    BIDP7                VARCHAR2(4000),
    BIDP8                VARCHAR2(4000),
    BIDP9                VARCHAR2(4000),
    BIDP10               VARCHAR2(4000),
    ASKP_CSNU1           VARCHAR2(4000),
    ASKP_CSNU2           VARCHAR2(4000),
    ASKP_CSNU3           VARCHAR2(4000),
    ASKP_CSNU4           VARCHAR2(4000),
    ASKP_CSNU5           VARCHAR2(4000),
    ASKP_CSNU6           VARCHAR2(4000),
    ASKP_CSNU7           VARCHAR2(4000),
    ASKP_CSNU8           VARCHAR2(4000),
    ASKP_CSNU9           VARCHAR2(4000),
    ASKP_CSNU10          VARCHAR2(4000),
    BIDP_CSNU1           VARCHAR2(4000),
    BIDP_CSNU2           VARCHAR2(4000),
    BIDP_CSNU3           VARCHAR2(4000),
    BIDP_CSNU4           VARCHAR2(4000),
    BIDP_CSNU5           VARCHAR2(4000),
    BIDP_CSNU6           VARCHAR2(4000),
    BIDP_CSNU7           VARCHAR2(4000),
    BIDP_CSNU8           VARCHAR2(4000),
    BIDP_CSNU9           VARCHAR2(4000),
    BIDP_CSNU10          VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    ASKP_RSQN6           VARCHAR2(4000),
    ASKP_RSQN7           VARCHAR2(4000),
    ASKP_RSQN8           VARCHAR2(4000),
    ASKP_RSQN9           VARCHAR2(4000),
    ASKP_RSQN10          VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN6           VARCHAR2(4000),
    BIDP_RSQN7           VARCHAR2(4000),
    BIDP_RSQN8           VARCHAR2(4000),
    BIDP_RSQN9           VARCHAR2(4000),
    BIDP_RSQN10          VARCHAR2(4000),
    TOTAL_ASKP_CSNU      VARCHAR2(4000),
    TOTAL_BIDP_CSNU      VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_STOCK_FUTURES_REALTIME_QUOTE_API_NAME
    on STOCK_FUTURES_REALTIME_QUOTE (API_NAME)
/

create table STOCK_OPTION_ASKING_PRICE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    OPTN_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    OPTN_ASKP1           VARCHAR2(4000),
    OPTN_ASKP2           VARCHAR2(4000),
    OPTN_ASKP3           VARCHAR2(4000),
    OPTN_ASKP4           VARCHAR2(4000),
    OPTN_ASKP5           VARCHAR2(4000),
    OPTN_BIDP1           VARCHAR2(4000),
    OPTN_BIDP2           VARCHAR2(4000),
    OPTN_BIDP3           VARCHAR2(4000),
    OPTN_BIDP4           VARCHAR2(4000),
    OPTN_BIDP5           VARCHAR2(4000),
    ASKP_CSNU1           VARCHAR2(4000),
    ASKP_CSNU2           VARCHAR2(4000),
    ASKP_CSNU3           VARCHAR2(4000),
    ASKP_CSNU4           VARCHAR2(4000),
    ASKP_CSNU5           VARCHAR2(4000),
    BIDP_CSNU1           VARCHAR2(4000),
    BIDP_CSNU2           VARCHAR2(4000),
    BIDP_CSNU3           VARCHAR2(4000),
    BIDP_CSNU4           VARCHAR2(4000),
    BIDP_CSNU5           VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    TOTAL_ASKP_CSNU      VARCHAR2(4000),
    TOTAL_BIDP_CSNU      VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    OPTN_ASKP6           VARCHAR2(4000),
    OPTN_ASKP7           VARCHAR2(4000),
    OPTN_ASKP8           VARCHAR2(4000),
    OPTN_ASKP9           VARCHAR2(4000),
    OPTN_ASKP10          VARCHAR2(4000),
    OPTN_BIDP6           VARCHAR2(4000),
    OPTN_BIDP7           VARCHAR2(4000),
    OPTN_BIDP8           VARCHAR2(4000),
    OPTN_BIDP9           VARCHAR2(4000),
    OPTN_BIDP10          VARCHAR2(4000),
    ASKP_CSNU6           VARCHAR2(4000),
    ASKP_CSNU7           VARCHAR2(4000),
    ASKP_CSNU8           VARCHAR2(4000),
    ASKP_CSNU9           VARCHAR2(4000),
    ASKP_CSNU10          VARCHAR2(4000),
    BIDP_CSNU6           VARCHAR2(4000),
    BIDP_CSNU7           VARCHAR2(4000),
    BIDP_CSNU8           VARCHAR2(4000),
    BIDP_CSNU9           VARCHAR2(4000),
    BIDP_CSNU10          VARCHAR2(4000),
    ASKP_RSQN6           VARCHAR2(4000),
    ASKP_RSQN7           VARCHAR2(4000),
    ASKP_RSQN8           VARCHAR2(4000),
    ASKP_RSQN9           VARCHAR2(4000),
    ASKP_RSQN10          VARCHAR2(4000),
    BIDP_RSQN6           VARCHAR2(4000),
    BIDP_RSQN7           VARCHAR2(4000),
    BIDP_RSQN8           VARCHAR2(4000),
    BIDP_RSQN9           VARCHAR2(4000),
    BIDP_RSQN10          VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_STOCK_OPTION_ASKING_PRICE_API_NAME
    on STOCK_OPTION_ASKING_PRICE (API_NAME)
/

create table STOCK_OPTION_CCNL
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    OPTN_SHRN_ISCD              VARCHAR2(4000),
    BSOP_HOUR                   VARCHAR2(4000),
    OPTN_PRPR                   VARCHAR2(4000),
    PRDY_VRSS_SIGN              VARCHAR2(4000),
    OPTN_PRDY_VRSS              VARCHAR2(4000),
    PRDY_CTRT                   VARCHAR2(4000),
    OPTN_OPRC                   VARCHAR2(4000),
    OPTN_HGPR                   VARCHAR2(4000),
    OPTN_LWPR                   VARCHAR2(4000),
    LAST_CNQN                   VARCHAR2(4000),
    ACML_VOL                    VARCHAR2(4000),
    ACML_TR_PBMN                VARCHAR2(4000),
    HTS_THPR                    VARCHAR2(4000),
    HTS_OTST_STPL_QTY           VARCHAR2(4000),
    OTST_STPL_QTY_ICDC          VARCHAR2(4000),
    OPRC_HOUR                   VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN         VARCHAR2(4000),
    OPRC_VRSS_NMIX_PRPR         VARCHAR2(4000),
    HGPR_HOUR                   VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    HGPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    LWPR_HOUR                   VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    LWPR_VRSS_NMIX_PRPR         VARCHAR2(4000),
    SHNU_RATE                   VARCHAR2(4000),
    PRMM_VAL                    VARCHAR2(4000),
    INVL_VAL                    VARCHAR2(4000),
    TMVL_VAL                    VARCHAR2(4000),
    DELTA                       VARCHAR2(4000),
    GAMA                        VARCHAR2(4000),
    VEGA                        VARCHAR2(4000),
    THETA                       VARCHAR2(4000),
    RHO                         VARCHAR2(4000),
    HTS_INTS_VLTL               VARCHAR2(4000),
    ESDG                        VARCHAR2(4000),
    OTST_STPL_RGBF_QTY_ICDC     VARCHAR2(4000),
    THPR_BASIS                  VARCHAR2(4000),
    UNAS_HIST_VLTL              VARCHAR2(4000),
    CTTR                        VARCHAR2(4000),
    DPRT                        VARCHAR2(4000),
    MRKT_BASIS                  VARCHAR2(4000),
    OPTN_ASKP1                  VARCHAR2(4000),
    OPTN_BIDP1                  VARCHAR2(4000),
    ASKP_RSQN1                  VARCHAR2(4000),
    BIDP_RSQN1                  VARCHAR2(4000),
    SELN_CNTG_CSNU              VARCHAR2(4000),
    SHNU_CNTG_CSNU              VARCHAR2(4000),
    NTBY_CNTG_CSNU              VARCHAR2(4000),
    SELN_CNTG_SMTN              VARCHAR2(4000),
    SHNU_CNTG_SMTN              VARCHAR2(4000),
    TOTAL_ASKP_RSQN             VARCHAR2(4000),
    TOTAL_BIDP_RSQN             VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_STOCK_OPTION_CCNL_API_NAME
    on STOCK_OPTION_CCNL (API_NAME)
/

create table AFTER_HOUR_BALANCE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    STCK_SHRN_ISCD       VARCHAR2(4000),
    DATA_RANK            VARCHAR2(4000),
    HTS_KOR_ISNM         VARCHAR2(4000),
    STCK_PRPR            VARCHAR2(4000),
    PRDY_VRSS            VARCHAR2(4000),
    PRDY_VRSS_SIGN       VARCHAR2(4000),
    PRDY_CTRT            VARCHAR2(4000),
    OVTM_TOTAL_ASKP_RSQN VARCHAR2(4000),
    OVTM_TOTAL_BIDP_RSQN VARCHAR2(4000),
    MKOB_OTCP_VOL        VARCHAR2(4000),
    MKFA_OTCP_VOL        VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_AFTER_HOUR_BALANCE_API_NAME
    on AFTER_HOUR_BALANCE (API_NAME)
/

create table ASKING_PRICE_KRX
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    HOUR_CLS_CODE        VARCHAR2(4000),
    ASKP1                VARCHAR2(4000),
    ASKP2                VARCHAR2(4000),
    ASKP3                VARCHAR2(4000),
    ASKP4                VARCHAR2(4000),
    ASKP5                VARCHAR2(4000),
    ASKP6                VARCHAR2(4000),
    ASKP7                VARCHAR2(4000),
    ASKP8                VARCHAR2(4000),
    ASKP9                VARCHAR2(4000),
    ASKP10               VARCHAR2(4000),
    BIDP1                VARCHAR2(4000),
    BIDP2                VARCHAR2(4000),
    BIDP3                VARCHAR2(4000),
    BIDP4                VARCHAR2(4000),
    BIDP5                VARCHAR2(4000),
    BIDP6                VARCHAR2(4000),
    BIDP7                VARCHAR2(4000),
    BIDP8                VARCHAR2(4000),
    BIDP9                VARCHAR2(4000),
    BIDP10               VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    ASKP_RSQN6           VARCHAR2(4000),
    ASKP_RSQN7           VARCHAR2(4000),
    ASKP_RSQN8           VARCHAR2(4000),
    ASKP_RSQN9           VARCHAR2(4000),
    ASKP_RSQN10          VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN6           VARCHAR2(4000),
    BIDP_RSQN7           VARCHAR2(4000),
    BIDP_RSQN8           VARCHAR2(4000),
    BIDP_RSQN9           VARCHAR2(4000),
    BIDP_RSQN10          VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    OVTM_TOTAL_ASKP_RSQN VARCHAR2(4000),
    OVTM_TOTAL_BIDP_RSQN VARCHAR2(4000),
    ANTC_CNPR            VARCHAR2(4000),
    ANTC_CNQN            VARCHAR2(4000),
    ANTC_VOL             VARCHAR2(4000),
    ANTC_CNTG_VRSS       VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN  VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT  VARCHAR2(4000),
    ACML_VOL             VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    OVTM_TOTAL_ASKP_ICDC VARCHAR2(4000),
    OVTM_TOTAL_BIDP_ICDC VARCHAR2(4000),
    STCK_DEAL_CLS_CODE   VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_ASKING_PRICE_KRX_API_NAME
    on ASKING_PRICE_KRX (API_NAME)
/

create table ASKING_PRICE_NXT
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    HOUR_CLS_CODE        VARCHAR2(4000),
    ASKP1                VARCHAR2(4000),
    ASKP2                VARCHAR2(4000),
    ASKP3                VARCHAR2(4000),
    ASKP4                VARCHAR2(4000),
    ASKP5                VARCHAR2(4000),
    ASKP6                VARCHAR2(4000),
    ASKP7                VARCHAR2(4000),
    ASKP8                VARCHAR2(4000),
    ASKP9                VARCHAR2(4000),
    ASKP10               VARCHAR2(4000),
    BIDP1                VARCHAR2(4000),
    BIDP2                VARCHAR2(4000),
    BIDP3                VARCHAR2(4000),
    BIDP4                VARCHAR2(4000),
    BIDP5                VARCHAR2(4000),
    BIDP6                VARCHAR2(4000),
    BIDP7                VARCHAR2(4000),
    BIDP8                VARCHAR2(4000),
    BIDP9                VARCHAR2(4000),
    BIDP10               VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    ASKP_RSQN6           VARCHAR2(4000),
    ASKP_RSQN7           VARCHAR2(4000),
    ASKP_RSQN8           VARCHAR2(4000),
    ASKP_RSQN9           VARCHAR2(4000),
    ASKP_RSQN10          VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN6           VARCHAR2(4000),
    BIDP_RSQN7           VARCHAR2(4000),
    BIDP_RSQN8           VARCHAR2(4000),
    BIDP_RSQN9           VARCHAR2(4000),
    BIDP_RSQN10          VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    OVTM_TOTAL_ASKP_RSQN VARCHAR2(4000),
    OVTM_TOTAL_BIDP_RSQN VARCHAR2(4000),
    ANTC_CNPR            VARCHAR2(4000),
    ANTC_CNQN            VARCHAR2(4000),
    ANTC_VOL             VARCHAR2(4000),
    ANTC_CNTG_VRSS       VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN  VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT  VARCHAR2(4000),
    ACML_VOL             VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    OVTM_TOTAL_ASKP_ICDC VARCHAR2(4000),
    OVTM_TOTAL_BIDP_ICDC VARCHAR2(4000),
    STCK_DEAL_CLS_CODE   VARCHAR2(4000),
    KMID_PRC             VARCHAR2(4000),
    KMID_TOTAL_RSQN      VARCHAR2(4000),
    KMID_CLS_CODE        VARCHAR2(4000),
    NMID_PRC             VARCHAR2(4000),
    NMID_TOTAL_RSQN      VARCHAR2(4000),
    NMID_CLS_CODE        VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_ASKING_PRICE_NXT_API_NAME
    on ASKING_PRICE_NXT (API_NAME)
/

create table ASKING_PRICE_TOTAL
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    HOUR_CLS_CODE        VARCHAR2(4000),
    ASKP1                VARCHAR2(4000),
    ASKP2                VARCHAR2(4000),
    ASKP3                VARCHAR2(4000),
    ASKP4                VARCHAR2(4000),
    ASKP5                VARCHAR2(4000),
    ASKP6                VARCHAR2(4000),
    ASKP7                VARCHAR2(4000),
    ASKP8                VARCHAR2(4000),
    ASKP9                VARCHAR2(4000),
    ASKP10               VARCHAR2(4000),
    BIDP1                VARCHAR2(4000),
    BIDP2                VARCHAR2(4000),
    BIDP3                VARCHAR2(4000),
    BIDP4                VARCHAR2(4000),
    BIDP5                VARCHAR2(4000),
    BIDP6                VARCHAR2(4000),
    BIDP7                VARCHAR2(4000),
    BIDP8                VARCHAR2(4000),
    BIDP9                VARCHAR2(4000),
    BIDP10               VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    ASKP_RSQN6           VARCHAR2(4000),
    ASKP_RSQN7           VARCHAR2(4000),
    ASKP_RSQN8           VARCHAR2(4000),
    ASKP_RSQN9           VARCHAR2(4000),
    ASKP_RSQN10          VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN6           VARCHAR2(4000),
    BIDP_RSQN7           VARCHAR2(4000),
    BIDP_RSQN8           VARCHAR2(4000),
    BIDP_RSQN9           VARCHAR2(4000),
    BIDP_RSQN10          VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    OVTM_TOTAL_ASKP_RSQN VARCHAR2(4000),
    OVTM_TOTAL_BIDP_RSQN VARCHAR2(4000),
    ANTC_CNPR            VARCHAR2(4000),
    ANTC_CNQN            VARCHAR2(4000),
    ANTC_VOL             VARCHAR2(4000),
    ANTC_CNTG_VRSS       VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN  VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT  VARCHAR2(4000),
    ACML_VOL             VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    OVTM_TOTAL_ASKP_ICDC VARCHAR2(4000),
    OVTM_TOTAL_BIDP_ICDC VARCHAR2(4000),
    STCK_DEAL_CLS_CODE   VARCHAR2(4000),
    KMID_PRC             VARCHAR2(4000),
    KMID_TOTAL_RSQN      VARCHAR2(4000),
    KMID_CLS_CODE        VARCHAR2(4000),
    NMID_PRC             VARCHAR2(4000),
    NMID_TOTAL_RSQN      VARCHAR2(4000),
    NMID_CLS_CODE        VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_ASKING_PRICE_TOTAL_API_NAME
    on ASKING_PRICE_TOTAL (API_NAME)
/

create table BULK_TRANS_NUM
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD VARCHAR2(4000),
    DATA_RANK      VARCHAR2(4000),
    HTS_KOR_ISNM   VARCHAR2(4000),
    STCK_PRPR      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    SHNU_CNTG_CSNU VARCHAR2(4000),
    SELN_CNTG_CSNU VARCHAR2(4000),
    NTBY_CNQN      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_BULK_TRANS_NUM_API_NAME
    on BULK_TRANS_NUM (API_NAME)
/

create table CAPTURE_UPLOWPRICE
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD     VARCHAR2(4000),
    HTS_KOR_ISNM       VARCHAR2(4000),
    STCK_PRPR          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    TOTAL_ASKP_RSQN    VARCHAR2(4000),
    TOTAL_BIDP_RSQN    VARCHAR2(4000),
    ASKP_RSQN1         VARCHAR2(4000),
    BIDP_RSQN1         VARCHAR2(4000),
    PRDY_VOL           VARCHAR2(4000),
    SELN_CNQN          VARCHAR2(4000),
    SHNU_CNQN          VARCHAR2(4000),
    STCK_LLAM          VARCHAR2(4000),
    STCK_MXPR          VARCHAR2(4000),
    PRDY_VRSS_VOL_RATE VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_CAPTURE_UPLOWPRICE_API_NAME
    on CAPTURE_UPLOWPRICE (API_NAME)
/

create table CCNL_KRX
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD               VARCHAR2(4000),
    STCK_CNTG_HOUR               VARCHAR2(4000),
    STCK_PRPR                    VARCHAR2(4000),
    PRDY_VRSS_SIGN               VARCHAR2(4000),
    PRDY_VRSS                    VARCHAR2(4000),
    PRDY_CTRT                    VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC           VARCHAR2(4000),
    STCK_OPRC                    VARCHAR2(4000),
    STCK_HGPR                    VARCHAR2(4000),
    STCK_LWPR                    VARCHAR2(4000),
    ASKP1                        VARCHAR2(4000),
    BIDP1                        VARCHAR2(4000),
    CNTG_VOL                     VARCHAR2(4000),
    ACML_VOL                     VARCHAR2(4000),
    ACML_TR_PBMN                 VARCHAR2(4000),
    SELN_CNTG_CSNU               VARCHAR2(4000),
    SHNU_CNTG_CSNU               VARCHAR2(4000),
    NTBY_CNTG_CSNU               VARCHAR2(4000),
    CTTR                         VARCHAR2(4000),
    SELN_CNTG_SMTN               VARCHAR2(4000),
    SHNU_CNTG_SMTN               VARCHAR2(4000),
    CCLD_DVSN                    VARCHAR2(4000),
    SHNU_RATE                    VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE  VARCHAR2(4000),
    OPRC_HOUR                    VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN          VARCHAR2(4000),
    OPRC_VRSS_PRPR               VARCHAR2(4000),
    HGPR_HOUR                    VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    HGPR_VRSS_PRPR               VARCHAR2(4000),
    LWPR_HOUR                    VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    LWPR_VRSS_PRPR               VARCHAR2(4000),
    BSOP_DATE                    VARCHAR2(4000),
    NEW_MKOP_CLS_CODE            VARCHAR2(4000),
    TRHT_YN                      VARCHAR2(4000),
    ASKP_RSQN1                   VARCHAR2(4000),
    BIDP_RSQN1                   VARCHAR2(4000),
    TOTAL_ASKP_RSQN              VARCHAR2(4000),
    TOTAL_BIDP_RSQN              VARCHAR2(4000),
    VOL_TNRT                     VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL      VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL_RATE VARCHAR2(4000),
    HOUR_CLS_CODE                VARCHAR2(4000),
    MRKT_TRTM_CLS_CODE           VARCHAR2(4000),
    VI_STND_PRC                  VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_CCNL_KRX_API_NAME
    on CCNL_KRX (API_NAME)
/

create table CCNL_NOTICE
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    CUST_ID        VARCHAR2(4000),
    ACNT_NO        VARCHAR2(4000),
    ODER_NO        VARCHAR2(4000),
    OODER_NO       VARCHAR2(4000),
    SELN_BYOV_CLS  VARCHAR2(4000),
    RCTF_CLS       VARCHAR2(4000),
    ODER_KIND2     VARCHAR2(4000),
    STCK_SHRN_ISCD VARCHAR2(4000),
    CNTG_QTY       VARCHAR2(4000),
    CNTG_UNPR      VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    RFUS_YN        VARCHAR2(4000),
    CNTG_YN        VARCHAR2(4000),
    ACPT_YN        VARCHAR2(4000),
    BRNC_NO        VARCHAR2(4000),
    ODER_QTY       VARCHAR2(4000),
    ACNT_NAME      VARCHAR2(4000),
    CNTG_ISNM      VARCHAR2(4000),
    ODER_COND      VARCHAR2(4000),
    DEBT_GB        VARCHAR2(4000),
    DEBT_DATE      VARCHAR2(4000),
    START_TM       VARCHAR2(4000),
    END_TM         VARCHAR2(4000),
    TM_DIV_TP      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_CCNL_NOTICE_API_NAME
    on CCNL_NOTICE (API_NAME)
/

create table CCNL_NXT
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD               VARCHAR2(4000),
    STCK_CNTG_HOUR               VARCHAR2(4000),
    STCK_PRPR                    VARCHAR2(4000),
    PRDY_VRSS_SIGN               VARCHAR2(4000),
    PRDY_VRSS                    VARCHAR2(4000),
    PRDY_CTRT                    VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC           VARCHAR2(4000),
    STCK_OPRC                    VARCHAR2(4000),
    STCK_HGPR                    VARCHAR2(4000),
    STCK_LWPR                    VARCHAR2(4000),
    ASKP1                        VARCHAR2(4000),
    BIDP1                        VARCHAR2(4000),
    CNTG_VOL                     VARCHAR2(4000),
    ACML_VOL                     VARCHAR2(4000),
    ACML_TR_PBMN                 VARCHAR2(4000),
    SELN_CNTG_CSNU               VARCHAR2(4000),
    SHNU_CNTG_CSNU               VARCHAR2(4000),
    NTBY_CNTG_CSNU               VARCHAR2(4000),
    CTTR                         VARCHAR2(4000),
    SELN_CNTG_SMTN               VARCHAR2(4000),
    SHNU_CNTG_SMTN               VARCHAR2(4000),
    CNTG_CLS_CODE                VARCHAR2(4000),
    SHNU_RATE                    VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE  VARCHAR2(4000),
    OPRC_HOUR                    VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN          VARCHAR2(4000),
    OPRC_VRSS_PRPR               VARCHAR2(4000),
    HGPR_HOUR                    VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    HGPR_VRSS_PRPR               VARCHAR2(4000),
    LWPR_HOUR                    VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    LWPR_VRSS_PRPR               VARCHAR2(4000),
    BSOP_DATE                    VARCHAR2(4000),
    NEW_MKOP_CLS_CODE            VARCHAR2(4000),
    TRHT_YN                      VARCHAR2(4000),
    ASKP_RSQN1                   VARCHAR2(4000),
    BIDP_RSQN1                   VARCHAR2(4000),
    TOTAL_ASKP_RSQN              VARCHAR2(4000),
    TOTAL_BIDP_RSQN              VARCHAR2(4000),
    VOL_TNRT                     VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL      VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL_RATE VARCHAR2(4000),
    HOUR_CLS_CODE                VARCHAR2(4000),
    MRKT_TRTM_CLS_CODE           VARCHAR2(4000),
    VI_STND_PRC                  VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_CCNL_NXT_API_NAME
    on CCNL_NXT (API_NAME)
/

create table CCNL_TOTAL
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD               VARCHAR2(4000),
    STCK_CNTG_HOUR               VARCHAR2(4000),
    STCK_PRPR                    VARCHAR2(4000),
    PRDY_VRSS_SIGN               VARCHAR2(4000),
    PRDY_VRSS                    VARCHAR2(4000),
    PRDY_CTRT                    VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC           VARCHAR2(4000),
    STCK_OPRC                    VARCHAR2(4000),
    STCK_HGPR                    VARCHAR2(4000),
    STCK_LWPR                    VARCHAR2(4000),
    ASKP1                        VARCHAR2(4000),
    BIDP1                        VARCHAR2(4000),
    CNTG_VOL                     VARCHAR2(4000),
    ACML_VOL                     VARCHAR2(4000),
    ACML_TR_PBMN                 VARCHAR2(4000),
    SELN_CNTG_CSNU               VARCHAR2(4000),
    SHNU_CNTG_CSNU               VARCHAR2(4000),
    NTBY_CNTG_CSNU               VARCHAR2(4000),
    CTTR                         VARCHAR2(4000),
    SELN_CNTG_SMTN               VARCHAR2(4000),
    SHNU_CNTG_SMTN               VARCHAR2(4000),
    CNTG_CLS_CODE                VARCHAR2(4000),
    SHNU_RATE                    VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE  VARCHAR2(4000),
    OPRC_HOUR                    VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN          VARCHAR2(4000),
    OPRC_VRSS_PRPR               VARCHAR2(4000),
    HGPR_HOUR                    VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    HGPR_VRSS_PRPR               VARCHAR2(4000),
    LWPR_HOUR                    VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    LWPR_VRSS_PRPR               VARCHAR2(4000),
    BSOP_DATE                    VARCHAR2(4000),
    NEW_MKOP_CLS_CODE            VARCHAR2(4000),
    TRHT_YN                      VARCHAR2(4000),
    ASKP_RSQN1                   VARCHAR2(4000),
    BIDP_RSQN1                   VARCHAR2(4000),
    TOTAL_ASKP_RSQN              VARCHAR2(4000),
    TOTAL_BIDP_RSQN              VARCHAR2(4000),
    VOL_TNRT                     VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL      VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL_RATE VARCHAR2(4000),
    HOUR_CLS_CODE                VARCHAR2(4000),
    MRKT_TRTM_CLS_CODE           VARCHAR2(4000),
    VI_STND_PRC                  VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_CCNL_TOTAL_API_NAME
    on CCNL_TOTAL (API_NAME)
/

create table CHK_HOLIDAY
(
    ID           NUMBER         not null
        primary key,
    API_NAME     VARCHAR2(4000) not null,
    BASS_DT      VARCHAR2(4000),
    WDAY_DVSN_CD VARCHAR2(4000),
    BZDY_YN      VARCHAR2(4000),
    TR_DAY_YN    VARCHAR2(4000),
    OPND_YN      VARCHAR2(4000),
    STTL_DAY_YN  VARCHAR2(4000),
    CREATED_AT   DATE           not null
)
/

create index IX_CHK_HOLIDAY_API_NAME
    on CHK_HOLIDAY (API_NAME)
/

create table COMP_INTEREST
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    BCDT_CODE           VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    BOND_MNRT_PRPR      VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    BOND_MNRT_PRDY_VRSS VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    STCK_BSOP_DATE      VARCHAR2(4000),
    BSTP_NMIX_PRDY_CTRT VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_COMP_INTEREST_API_NAME
    on COMP_INTEREST (API_NAME)
/

create table COMP_PROGRAM_TRADE_DAILY
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    STCK_BSOP_DATE              VARCHAR2(4000),
    NABT_ENTM_SELN_TR_PBMN      VARCHAR2(4000),
    NABT_ONSL_SELN_VOL          VARCHAR2(4000),
    WHOL_ONSL_SELN_TR_PBMN      VARCHAR2(4000),
    ARBT_SMTN_SHNU_VOL          VARCHAR2(4000),
    NABT_SMTN_SHNU_TR_PBMN      VARCHAR2(4000),
    ARBT_ENTM_NTBY_QTY          VARCHAR2(4000),
    NABT_ENTM_NTBY_TR_PBMN      VARCHAR2(4000),
    ARBT_ENTM_SELN_VOL          VARCHAR2(4000),
    NABT_ENTM_SELN_VOL_RATE     VARCHAR2(4000),
    NABT_ONSL_SELN_VOL_RATE     VARCHAR2(4000),
    WHOL_ONSL_SELN_TR_PBMN_RATE VARCHAR2(4000),
    ARBT_SMTM_SHUN_VOL_RATE     VARCHAR2(4000),
    NABT_SMTM_SHUN_TR_PBMN_RATE VARCHAR2(4000),
    ARBT_ENTM_NTBY_QTY_RATE     VARCHAR2(4000),
    NABT_ENTM_NTBY_TR_PBMN_RATE VARCHAR2(4000),
    ARBT_ENTM_SELN_VOL_RATE     VARCHAR2(4000),
    NABT_ENTM_SELN_TR_PBMN_RATE VARCHAR2(4000),
    NABT_ONSL_SELN_TR_PBMN      VARCHAR2(4000),
    WHOL_SMTN_SELN_VOL          VARCHAR2(4000),
    ARBT_SMTN_SHNU_TR_PBMN      VARCHAR2(4000),
    WHOL_ENTM_SHNU_VOL          VARCHAR2(4000),
    ARBT_ENTM_NTBY_TR_PBMN      VARCHAR2(4000),
    NABT_ONSL_NTBY_QTY          VARCHAR2(4000),
    ARBT_ENTM_SELN_TR_PBMN      VARCHAR2(4000),
    WHOL_SELN_VOL_RATE          VARCHAR2(4000),
    WHOL_ENTM_SHNU_VOL_RATE     VARCHAR2(4000),
    WHOL_ENTM_SELN_TR_PBMN      VARCHAR2(4000),
    NABT_SMTM_SELN_VOL          VARCHAR2(4000),
    ARBT_ENTM_SHNU_VOL          VARCHAR2(4000),
    NABT_ENTM_SHNU_TR_PBMN      VARCHAR2(4000),
    WHOL_ONSL_SHNU_VOL          VARCHAR2(4000),
    ARBT_ONSL_NTBY_TR_PBMN      VARCHAR2(4000),
    NABT_SMTN_NTBY_QTY          VARCHAR2(4000),
    ARBT_ONSL_SELN_VOL          VARCHAR2(4000),
    WHOL_ENTM_NTBY_QTY          VARCHAR2(4000),
    NABT_ONSL_NTBY_TR_PBMN      VARCHAR2(4000),
    ARBT_ONSL_SELN_TR_PBMN      VARCHAR2(4000),
    NABT_SMTM_SELN_TR_PBMN_RATE VARCHAR2(4000),
    ARBT_ENTM_SHNU_VOL_RATE     VARCHAR2(4000),
    NABT_ENTM_SHNU_TR_PBMN_RATE VARCHAR2(4000),
    WHOL_ONSL_SHNU_TR_PBMN      VARCHAR2(4000),
    ARBT_ONSL_NTBY_TR_PBMN_RATE VARCHAR2(4000),
    NABT_SMTM_NTBY_QTY_RATE     VARCHAR2(4000),
    ARBT_ONSL_SELN_VOL_RATE     VARCHAR2(4000),
    WHOL_ENTM_SELN_VOL          VARCHAR2(4000),
    ARBT_ENTM_SHNU_TR_PBMN      VARCHAR2(4000),
    NABT_ONSL_SHNU_VOL          VARCHAR2(4000),
    WHOL_SMTN_SHNU_VOL          VARCHAR2(4000),
    ARBT_SMTN_NTBY_TR_PBMN      VARCHAR2(4000),
    ARBT_SMTN_SELN_VOL          VARCHAR2(4000),
    WHOL_ENTM_SELN_TR_PBMN_RATE VARCHAR2(4000),
    ARBT_ONSL_SHNU_VOL_RATE     VARCHAR2(4000),
    NABT_SMTM_SHUN_VOL_RATE     VARCHAR2(4000),
    WHOL_SHUN_TR_PBMN_RATE      VARCHAR2(4000),
    NABT_ENTM_NTBY_QTY_RATE     VARCHAR2(4000),
    ARBT_SMTM_SELN_TR_PBMN_RATE VARCHAR2(4000),
    ARBT_ONSL_SHNU_VOL          VARCHAR2(4000),
    NABT_ONSL_SHNU_TR_PBMN      VARCHAR2(4000),
    NABT_SMTN_SHNU_VOL          VARCHAR2(4000),
    WHOL_SMTN_SHNU_TR_PBMN      VARCHAR2(4000),
    ARBT_SMTM_NTBY_QTY          VARCHAR2(4000),
    NABT_SMTN_NTBY_TR_PBMN      VARCHAR2(4000),
    ARBT_SMTN_SELN_TR_PBMN      VARCHAR2(4000),
    ARBT_ONSL_SHNU_TR_PBMN_RATE VARCHAR2(4000),
    WHOL_SHUN_VOL_RATE          VARCHAR2(4000),
    ARBT_SMTM_NTBY_TR_PBMN_RATE VARCHAR2(4000),
    WHOL_ENTM_NTBY_QTY_RATE     VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_COMP_PROGRAM_TRADE_DAILY_API_NAME
    on COMP_PROGRAM_TRADE_DAILY (API_NAME)
/

create table COMP_PROGRAM_TRADE_TODAY
(
    ID                      NUMBER         not null
        primary key,
    API_NAME                VARCHAR2(4000) not null,
    STCK_BSOP_DATE          VARCHAR2(4000),
    STCK_CLPR               VARCHAR2(4000),
    PRDY_VRSS               VARCHAR2(4000),
    PRDY_VRSS_SIGN          VARCHAR2(4000),
    PRDY_CTRT               VARCHAR2(4000),
    ACML_VOL                VARCHAR2(4000),
    ACML_TR_PBMN            VARCHAR2(4000),
    WHOL_SMTN_SELN_VOL      VARCHAR2(4000),
    WHOL_SMTN_SHNU_VOL      VARCHAR2(4000),
    WHOL_SMTN_NTBY_QTY      VARCHAR2(4000),
    WHOL_SMTN_SELN_TR_PBMN  VARCHAR2(4000),
    WHOL_SMTN_SHNU_TR_PBMN  VARCHAR2(4000),
    WHOL_SMTN_NTBY_TR_PBMN  VARCHAR2(4000),
    WHOL_NTBY_VOL_ICDC      VARCHAR2(4000),
    WHOL_NTBY_TR_PBMN_ICDC2 VARCHAR2(4000),
    CREATED_AT              DATE           not null
)
/

create index IX_COMP_PROGRAM_TRADE_TODAY_API_NAME
    on COMP_PROGRAM_TRADE_TODAY (API_NAME)
/

create table CREDIT_BALANCE
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    BSTP_CLS_CODE            VARCHAR2(4000),
    HTS_KOR_ISNM             VARCHAR2(4000),
    STND_DATE1               VARCHAR2(4000),
    STND_DATE2               VARCHAR2(4000),
    MKSC_SHRN_ISCD           VARCHAR2(4000),
    STCK_PRPR                VARCHAR2(4000),
    PRDY_VRSS                VARCHAR2(4000),
    PRDY_VRSS_SIGN           VARCHAR2(4000),
    PRDY_CTRT                VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    WHOL_LOAN_RMND_STCN      VARCHAR2(4000),
    WHOL_LOAN_RMND_AMT       VARCHAR2(4000),
    WHOL_LOAN_RMND_RATE      VARCHAR2(4000),
    WHOL_STLN_RMND_STCN      VARCHAR2(4000),
    WHOL_STLN_RMND_AMT       VARCHAR2(4000),
    WHOL_STLN_RMND_RATE      VARCHAR2(4000),
    NDAY_VRSS_LOAN_RMND_INRT VARCHAR2(4000),
    NDAY_VRSS_STLN_RMND_INRT VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_CREDIT_BALANCE_API_NAME
    on CREDIT_BALANCE (API_NAME)
/

create table CREDIT_BY_COMPANY
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STCK_SHRN_ISCD VARCHAR2(4000),
    HTS_KOR_ISNM   VARCHAR2(4000),
    CRDT_RATE      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_CREDIT_BY_COMPANY_API_NAME
    on CREDIT_BY_COMPANY (API_NAME)
/

create table DAILY_CREDIT_BALANCE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    DEAL_DATE           VARCHAR2(4000),
    STCK_PRPR           VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    STLM_DATE           VARCHAR2(4000),
    WHOL_LOAN_NEW_STCN  VARCHAR2(4000),
    WHOL_LOAN_RDMP_STCN VARCHAR2(4000),
    WHOL_LOAN_RMND_STCN VARCHAR2(4000),
    WHOL_LOAN_NEW_AMT   VARCHAR2(4000),
    WHOL_LOAN_RDMP_AMT  VARCHAR2(4000),
    WHOL_LOAN_RMND_AMT  VARCHAR2(4000),
    WHOL_LOAN_RMND_RATE VARCHAR2(4000),
    WHOL_LOAN_GVRT      VARCHAR2(4000),
    WHOL_STLN_NEW_STCN  VARCHAR2(4000),
    WHOL_STLN_RDMP_STCN VARCHAR2(4000),
    WHOL_STLN_RMND_STCN VARCHAR2(4000),
    WHOL_STLN_NEW_AMT   VARCHAR2(4000),
    WHOL_STLN_RDMP_AMT  VARCHAR2(4000),
    WHOL_STLN_RMND_AMT  VARCHAR2(4000),
    WHOL_STLN_RMND_RATE VARCHAR2(4000),
    WHOL_STLN_GVRT      VARCHAR2(4000),
    STCK_OPRC           VARCHAR2(4000),
    STCK_HGPR           VARCHAR2(4000),
    STCK_LWPR           VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_DAILY_CREDIT_BALANCE_API_NAME
    on DAILY_CREDIT_BALANCE (API_NAME)
/

create table DAILY_LOAN_TRANS
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    BSOP_DATE      VARCHAR2(4000),
    STCK_PRPR      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    NEW_STCN       VARCHAR2(4000),
    RDMP_STCN      VARCHAR2(4000),
    PRDY_RMND_VRSS VARCHAR2(4000),
    RMND_STCN      VARCHAR2(4000),
    RMND_AMT       VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_DAILY_LOAN_TRANS_API_NAME
    on DAILY_LOAN_TRANS (API_NAME)
/

create table DAILY_SHORT_SALE
(
    ID                      NUMBER         not null
        primary key,
    API_NAME                VARCHAR2(4000) not null,
    STCK_PRPR               VARCHAR2(4000),
    PRDY_VRSS               VARCHAR2(4000),
    PRDY_VRSS_SIGN          VARCHAR2(4000),
    PRDY_CTRT               VARCHAR2(4000),
    ACML_VOL                VARCHAR2(4000),
    PRDY_VOL                VARCHAR2(4000),
    STCK_BSOP_DATE          VARCHAR2(4000),
    STCK_CLPR               VARCHAR2(4000),
    STND_VOL_SMTN           VARCHAR2(4000),
    SSTS_CNTG_QTY           VARCHAR2(4000),
    SSTS_VOL_RLIM           VARCHAR2(4000),
    ACML_SSTS_CNTG_QTY      VARCHAR2(4000),
    ACML_SSTS_CNTG_QTY_RLIM VARCHAR2(4000),
    ACML_TR_PBMN            VARCHAR2(4000),
    STND_TR_PBMN_SMTN       VARCHAR2(4000),
    SSTS_TR_PBMN            VARCHAR2(4000),
    SSTS_TR_PBMN_RLIM       VARCHAR2(4000),
    ACML_SSTS_TR_PBMN       VARCHAR2(4000),
    ACML_SSTS_TR_PBMN_RLIM  VARCHAR2(4000),
    STCK_OPRC               VARCHAR2(4000),
    STCK_HGPR               VARCHAR2(4000),
    STCK_LWPR               VARCHAR2(4000),
    AVRG_PRC                VARCHAR2(4000),
    CREATED_AT              DATE           not null
)
/

create index IX_DAILY_SHORT_SALE_API_NAME
    on DAILY_SHORT_SALE (API_NAME)
/

create table DISPARITY
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD VARCHAR2(4000),
    DATA_RANK      VARCHAR2(4000),
    HTS_KOR_ISNM   VARCHAR2(4000),
    STCK_PRPR      VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    D5_DSRT        VARCHAR2(4000),
    D10_DSRT       VARCHAR2(4000),
    D20_DSRT       VARCHAR2(4000),
    D60_DSRT       VARCHAR2(4000),
    D120_DSRT      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_DISPARITY_API_NAME
    on DISPARITY (API_NAME)
/

create table DIVIDEND_RATE
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    RANK             VARCHAR2(4000),
    SHT_CD           VARCHAR2(4000),
    RECORD_DATE      VARCHAR2(4000),
    PER_STO_DIVI_AMT VARCHAR2(4000),
    DIVI_RATE        VARCHAR2(4000),
    DIVI_KIND        VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_DIVIDEND_RATE_API_NAME
    on DIVIDEND_RATE (API_NAME)
/

create table ESTIMATE_PERFORM
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    SHT_CD          VARCHAR2(4000),
    ITEM_KOR_NM     VARCHAR2(4000),
    ESTDATE         VARCHAR2(4000),
    CAPITAL         VARCHAR2(4000),
    FORN_ITEM_LMTRT VARCHAR2(4000),
    DATA1           VARCHAR2(4000),
    DATA2           VARCHAR2(4000),
    DATA3           VARCHAR2(4000),
    DATA4           VARCHAR2(4000),
    DATA5           VARCHAR2(4000),
    OUTPUT3         VARCHAR2(4000),
    OUTPUT4         VARCHAR2(4000),
    DT              VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_ESTIMATE_PERFORM_API_NAME
    on ESTIMATE_PERFORM (API_NAME)
/

create table EXP_CCNL_KRX
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD               VARCHAR2(4000),
    STCK_CNTG_HOUR               VARCHAR2(4000),
    STCK_PRPR                    VARCHAR2(4000),
    PRDY_VRSS_SIGN               VARCHAR2(4000),
    PRDY_VRSS                    VARCHAR2(4000),
    PRDY_CTRT                    VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC           VARCHAR2(4000),
    STCK_OPRC                    VARCHAR2(4000),
    STCK_HGPR                    VARCHAR2(4000),
    STCK_LWPR                    VARCHAR2(4000),
    ASKP1                        VARCHAR2(4000),
    BIDP1                        VARCHAR2(4000),
    CNTG_VOL                     VARCHAR2(4000),
    ACML_VOL                     VARCHAR2(4000),
    ACML_TR_PBMN                 VARCHAR2(4000),
    SELN_CNTG_CSNU               VARCHAR2(4000),
    SHNU_CNTG_CSNU               VARCHAR2(4000),
    NTBY_CNTG_CSNU               VARCHAR2(4000),
    CTTR                         VARCHAR2(4000),
    SELN_CNTG_SMTN               VARCHAR2(4000),
    SHNU_CNTG_SMTN               VARCHAR2(4000),
    CNTG_CLS_CODE                VARCHAR2(4000),
    SHNU_RATE                    VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE  VARCHAR2(4000),
    OPRC_HOUR                    VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN          VARCHAR2(4000),
    OPRC_VRSS_PRPR               VARCHAR2(4000),
    HGPR_HOUR                    VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    HGPR_VRSS_PRPR               VARCHAR2(4000),
    LWPR_HOUR                    VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    LWPR_VRSS_PRPR               VARCHAR2(4000),
    BSOP_DATE                    VARCHAR2(4000),
    NEW_MKOP_CLS_CODE            VARCHAR2(4000),
    TRHT_YN                      VARCHAR2(4000),
    ASKP_RSQN1                   VARCHAR2(4000),
    BIDP_RSQN1                   VARCHAR2(4000),
    TOTAL_ASKP_RSQN              VARCHAR2(4000),
    TOTAL_BIDP_RSQN              VARCHAR2(4000),
    VOL_TNRT                     VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL      VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL_RATE VARCHAR2(4000),
    HOUR_CLS_CODE                VARCHAR2(4000),
    MRKT_TRTM_CLS_CODE           VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_EXP_CCNL_KRX_API_NAME
    on EXP_CCNL_KRX (API_NAME)
/

create table EXP_CCNL_NXT
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD               VARCHAR2(4000),
    STCK_CNTG_HOUR               VARCHAR2(4000),
    STCK_PRPR                    VARCHAR2(4000),
    PRDY_VRSS_SIGN               VARCHAR2(4000),
    PRDY_VRSS                    VARCHAR2(4000),
    PRDY_CTRT                    VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC           VARCHAR2(4000),
    STCK_OPRC                    VARCHAR2(4000),
    STCK_HGPR                    VARCHAR2(4000),
    STCK_LWPR                    VARCHAR2(4000),
    ASKP1                        VARCHAR2(4000),
    BIDP1                        VARCHAR2(4000),
    CNTG_VOL                     VARCHAR2(4000),
    ACML_VOL                     VARCHAR2(4000),
    ACML_TR_PBMN                 VARCHAR2(4000),
    SELN_CNTG_CSNU               VARCHAR2(4000),
    SHNU_CNTG_CSNU               VARCHAR2(4000),
    NTBY_CNTG_CSNU               VARCHAR2(4000),
    CTTR                         VARCHAR2(4000),
    SELN_CNTG_SMTN               VARCHAR2(4000),
    SHNU_CNTG_SMTN               VARCHAR2(4000),
    CNTG_CLS_CODE                VARCHAR2(4000),
    SHNU_RATE                    VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE  VARCHAR2(4000),
    OPRC_HOUR                    VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN          VARCHAR2(4000),
    OPRC_VRSS_PRPR               VARCHAR2(4000),
    HGPR_HOUR                    VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    HGPR_VRSS_PRPR               VARCHAR2(4000),
    LWPR_HOUR                    VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    LWPR_VRSS_PRPR               VARCHAR2(4000),
    BSOP_DATE                    VARCHAR2(4000),
    NEW_MKOP_CLS_CODE            VARCHAR2(4000),
    TRHT_YN                      VARCHAR2(4000),
    ASKP_RSQN1                   VARCHAR2(4000),
    BIDP_RSQN1                   VARCHAR2(4000),
    TOTAL_ASKP_RSQN              VARCHAR2(4000),
    TOTAL_BIDP_RSQN              VARCHAR2(4000),
    VOL_TNRT                     VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL      VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL_RATE VARCHAR2(4000),
    HOUR_CLS_CODE                VARCHAR2(4000),
    MRKT_TRTM_CLS_CODE           VARCHAR2(4000),
    VI_STND_PRC                  VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_EXP_CCNL_NXT_API_NAME
    on EXP_CCNL_NXT (API_NAME)
/

create table EXP_CCNL_TOTAL
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD               VARCHAR2(4000),
    STCK_CNTG_HOUR               VARCHAR2(4000),
    STCK_PRPR                    VARCHAR2(4000),
    PRDY_VRSS_SIGN               VARCHAR2(4000),
    PRDY_VRSS                    VARCHAR2(4000),
    PRDY_CTRT                    VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC           VARCHAR2(4000),
    STCK_OPRC                    VARCHAR2(4000),
    STCK_HGPR                    VARCHAR2(4000),
    STCK_LWPR                    VARCHAR2(4000),
    ASKP1                        VARCHAR2(4000),
    BIDP1                        VARCHAR2(4000),
    CNTG_VOL                     VARCHAR2(4000),
    ACML_VOL                     VARCHAR2(4000),
    ACML_TR_PBMN                 VARCHAR2(4000),
    SELN_CNTG_CSNU               VARCHAR2(4000),
    SHNU_CNTG_CSNU               VARCHAR2(4000),
    NTBY_CNTG_CSNU               VARCHAR2(4000),
    CTTR                         VARCHAR2(4000),
    SELN_CNTG_SMTN               VARCHAR2(4000),
    SHNU_CNTG_SMTN               VARCHAR2(4000),
    CNTG_CLS_CODE                VARCHAR2(4000),
    SHNU_RATE                    VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE  VARCHAR2(4000),
    OPRC_HOUR                    VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN          VARCHAR2(4000),
    OPRC_VRSS_PRPR               VARCHAR2(4000),
    HGPR_HOUR                    VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    HGPR_VRSS_PRPR               VARCHAR2(4000),
    LWPR_HOUR                    VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    LWPR_VRSS_PRPR               VARCHAR2(4000),
    BSOP_DATE                    VARCHAR2(4000),
    NEW_MKOP_CLS_CODE            VARCHAR2(4000),
    TRHT_YN                      VARCHAR2(4000),
    ASKP_RSQN1                   VARCHAR2(4000),
    BIDP_RSQN1                   VARCHAR2(4000),
    TOTAL_ASKP_RSQN              VARCHAR2(4000),
    TOTAL_BIDP_RSQN              VARCHAR2(4000),
    VOL_TNRT                     VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL      VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL_RATE VARCHAR2(4000),
    HOUR_CLS_CODE                VARCHAR2(4000),
    MRKT_TRTM_CLS_CODE           VARCHAR2(4000),
    VI_STND_PRC                  VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_EXP_CCNL_TOTAL_API_NAME
    on EXP_CCNL_TOTAL (API_NAME)
/

create table EXP_CLOSING_PRICE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    STCK_SHRN_ISCD      VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    STCK_PRPR           VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    SDPR_VRSS_PRPR      VARCHAR2(4000),
    SDPR_VRSS_PRPR_RATE VARCHAR2(4000),
    CNTG_VOL            VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_EXP_CLOSING_PRICE_API_NAME
    on EXP_CLOSING_PRICE (API_NAME)
/

create table EXP_INDEX_TREND
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    STCK_CNTG_HOUR      VARCHAR2(4000),
    BSTP_NMIX_PRPR      VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    ACML_TR_PBMN        VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_EXP_INDEX_TREND_API_NAME
    on EXP_INDEX_TREND (API_NAME)
/

create table EXP_TOTAL_INDEX
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    BSTP_NMIX_PRPR      VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    ASCN_ISSU_CNT       VARCHAR2(4000),
    DOWN_ISSU_CNT       VARCHAR2(4000),
    STNR_ISSU_CNT       VARCHAR2(4000),
    BSTP_CLS_CODE       VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    BSTP_NMIX_PRDY_CTRT VARCHAR2(4000),
    NMIX_SDPR           VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_EXP_TOTAL_INDEX_API_NAME
    on EXP_TOTAL_INDEX (API_NAME)
/

create table EXP_TRANS_UPDOWN
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    STCK_SHRN_ISCD  VARCHAR2(4000),
    HTS_KOR_ISNM    VARCHAR2(4000),
    STCK_PRPR       VARCHAR2(4000),
    PRDY_VRSS       VARCHAR2(4000),
    PRDY_VRSS_SIGN  VARCHAR2(4000),
    PRDY_CTRT       VARCHAR2(4000),
    STCK_SDPR       VARCHAR2(4000),
    SELN_RSQN       VARCHAR2(4000),
    ASKP            VARCHAR2(4000),
    BIDP            VARCHAR2(4000),
    SHNU_RSQN       VARCHAR2(4000),
    CNTG_VOL        VARCHAR2(4000),
    ANTC_TR_PBMN    VARCHAR2(4000),
    TOTAL_ASKP_RSQN VARCHAR2(4000),
    TOTAL_BIDP_RSQN VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_EXP_TRANS_UPDOWN_API_NAME
    on EXP_TRANS_UPDOWN (API_NAME)
/

create table FINANCE_BALANCE_SHEET
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    STAC_YYMM  VARCHAR2(4000),
    CRAS       VARCHAR2(4000),
    FXAS       VARCHAR2(4000),
    TOTAL_ASET VARCHAR2(4000),
    FLOW_LBLT  VARCHAR2(4000),
    FIX_LBLT   VARCHAR2(4000),
    TOTAL_LBLT VARCHAR2(4000),
    CPFN       VARCHAR2(4000),
    CFP_SURP   VARCHAR2(4000),
    PRFI_SURP  VARCHAR2(4000),
    TOTAL_CPTL VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_FINANCE_BALANCE_SHEET_API_NAME
    on FINANCE_BALANCE_SHEET (API_NAME)
/

create table FINANCE_FINANCIAL_RATIO
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STAC_YYMM      VARCHAR2(4000),
    GRS            VARCHAR2(4000),
    BSOP_PRFI_INRT VARCHAR2(4000),
    NTIN_INRT      VARCHAR2(4000),
    ROE_VAL        VARCHAR2(4000),
    EPS            VARCHAR2(4000),
    SPS            VARCHAR2(4000),
    BPS            VARCHAR2(4000),
    RSRV_RATE      VARCHAR2(4000),
    LBLT_RATE      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_FINANCE_FINANCIAL_RATIO_API_NAME
    on FINANCE_FINANCIAL_RATIO (API_NAME)
/

create table FINANCE_GROWTH_RATIO
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STAC_YYMM      VARCHAR2(4000),
    GRS            VARCHAR2(4000),
    BSOP_PRFI_INRT VARCHAR2(4000),
    EQUT_INRT      VARCHAR2(4000),
    TOTL_ASET_INRT VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_FINANCE_GROWTH_RATIO_API_NAME
    on FINANCE_GROWTH_RATIO (API_NAME)
/

create table FINANCE_INCOME_STATEMENT
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STAC_YYMM      VARCHAR2(4000),
    SALE_ACCOUNT   VARCHAR2(4000),
    SALE_COST      VARCHAR2(4000),
    SALE_TOTL_PRFI VARCHAR2(4000),
    DEPR_COST      VARCHAR2(4000),
    SELL_MANG      VARCHAR2(4000),
    BSOP_PRTI      VARCHAR2(4000),
    BSOP_NON_ERNN  VARCHAR2(4000),
    BSOP_NON_EXPN  VARCHAR2(4000),
    OP_PRFI        VARCHAR2(4000),
    SPEC_PRFI      VARCHAR2(4000),
    SPEC_LOSS      VARCHAR2(4000),
    THTR_NTIN      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_FINANCE_INCOME_STATEMENT_API_NAME
    on FINANCE_INCOME_STATEMENT (API_NAME)
/

create table FINANCE_OTHER_MAJOR_RATIOS
(
    ID          NUMBER         not null
        primary key,
    API_NAME    VARCHAR2(4000) not null,
    STAC_YYMM   VARCHAR2(4000),
    PAYOUT_RATE VARCHAR2(4000),
    EVA         VARCHAR2(4000),
    EBITDA      VARCHAR2(4000),
    EV_EBITDA   VARCHAR2(4000),
    CREATED_AT  DATE           not null
)
/

create index IX_FINANCE_OTHER_MAJOR_RATIOS_API_NAME
    on FINANCE_OTHER_MAJOR_RATIOS (API_NAME)
/

create table FINANCE_PROFIT_RATIO
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    STAC_YYMM           VARCHAR2(4000),
    CPTL_NTIN_RATE      VARCHAR2(4000),
    SELF_CPTL_NTIN_INRT VARCHAR2(4000),
    SALE_NTIN_RATE      VARCHAR2(4000),
    SALE_TOTL_RATE      VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_FINANCE_PROFIT_RATIO_API_NAME
    on FINANCE_PROFIT_RATIO (API_NAME)
/

create table FINANCE_RATIO
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    DATA_RANK           VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    MKSC_SHRN_ISCD      VARCHAR2(4000),
    STCK_PRPR           VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    CPTL_OP_PRFI        VARCHAR2(4000),
    CPTL_NTIN_RATE      VARCHAR2(4000),
    SALE_TOTL_RATE      VARCHAR2(4000),
    SALE_NTIN_RATE      VARCHAR2(4000),
    BIS                 VARCHAR2(4000),
    LBLT_RATE           VARCHAR2(4000),
    BRAM_DEPN           VARCHAR2(4000),
    RSRV_RATE           VARCHAR2(4000),
    GRS                 VARCHAR2(4000),
    OP_PRFI_INRT        VARCHAR2(4000),
    BSOP_PRFI_INRT      VARCHAR2(4000),
    NTIN_INRT           VARCHAR2(4000),
    EQUT_INRT           VARCHAR2(4000),
    CPTL_TNRT           VARCHAR2(4000),
    SALE_BOND_TNRT      VARCHAR2(4000),
    TOTL_ASET_INRT      VARCHAR2(4000),
    STAC_MONTH          VARCHAR2(4000),
    STAC_MONTH_CLS_CODE VARCHAR2(4000),
    IQRY_CSNU           VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_FINANCE_RATIO_API_NAME
    on FINANCE_RATIO (API_NAME)
/

create table FINANCE_STABILITY_RATIO
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    STAC_YYMM  VARCHAR2(4000),
    LBLT_RATE  VARCHAR2(4000),
    BRAM_DEPN  VARCHAR2(4000),
    CRNT_RATE  VARCHAR2(4000),
    QUCK_RATE  VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_FINANCE_STABILITY_RATIO_API_NAME
    on FINANCE_STABILITY_RATIO (API_NAME)
/

create table FLUCTUATION
(
    ID                            NUMBER         not null
        primary key,
    API_NAME                      VARCHAR2(4000) not null,
    STCK_SHRN_ISCD                VARCHAR2(4000),
    DATA_RANK                     VARCHAR2(4000),
    HTS_KOR_ISNM                  VARCHAR2(4000),
    STCK_PRPR                     VARCHAR2(4000),
    PRDY_VRSS                     VARCHAR2(4000),
    PRDY_VRSS_SIGN                VARCHAR2(4000),
    PRDY_CTRT                     VARCHAR2(4000),
    ACML_VOL                      VARCHAR2(4000),
    STCK_HGPR                     VARCHAR2(4000),
    HGPR_HOUR                     VARCHAR2(4000),
    ACML_HGPR_DATE                VARCHAR2(4000),
    STCK_LWPR                     VARCHAR2(4000),
    LWPR_HOUR                     VARCHAR2(4000),
    ACML_LWPR_DATE                VARCHAR2(4000),
    LWPR_VRSS_PRPR_RATE           VARCHAR2(4000),
    DSGT_DATE_CLPR_VRSS_PRPR_RATE VARCHAR2(4000),
    CNNT_ASCN_DYNU                VARCHAR2(4000),
    HGPR_VRSS_PRPR_RATE           VARCHAR2(4000),
    CNNT_DOWN_DYNU                VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN           VARCHAR2(4000),
    OPRC_VRSS_PRPR                VARCHAR2(4000),
    OPRC_VRSS_PRPR_RATE           VARCHAR2(4000),
    PRD_RSFL                      VARCHAR2(4000),
    PRD_RSFL_RATE                 VARCHAR2(4000),
    CREATED_AT                    DATE           not null
)
/

create index IX_FLUCTUATION_API_NAME
    on FLUCTUATION (API_NAME)
/

create table FOREIGN_INSTITUTION_TOTAL
(
    ID                    NUMBER         not null
        primary key,
    API_NAME              VARCHAR2(4000) not null,
    HTS_KOR_ISNM          VARCHAR2(4000),
    MKSC_SHRN_ISCD        VARCHAR2(4000),
    NTBY_QTY              VARCHAR2(4000),
    STCK_PRPR             VARCHAR2(4000),
    PRDY_VRSS_SIGN        VARCHAR2(4000),
    PRDY_VRSS             VARCHAR2(4000),
    PRDY_CTRT             VARCHAR2(4000),
    ACML_VOL              VARCHAR2(4000),
    FRGN_NTBY_QTY         VARCHAR2(4000),
    ORGN_NTBY_QTY         VARCHAR2(4000),
    IVTR_NTBY_QTY         VARCHAR2(4000),
    BANK_NTBY_QTY         VARCHAR2(4000),
    INSU_NTBY_QTY         VARCHAR2(4000),
    MRBN_NTBY_QTY         VARCHAR2(4000),
    FUND_NTBY_QTY         VARCHAR2(4000),
    ETC_ORGT_NTBY_VOL     VARCHAR2(4000),
    ETC_CORP_NTBY_VOL     VARCHAR2(4000),
    FRGN_NTBY_TR_PBMN     VARCHAR2(4000),
    ORGN_NTBY_TR_PBMN     VARCHAR2(4000),
    IVTR_NTBY_TR_PBMN     VARCHAR2(4000),
    BANK_NTBY_TR_PBMN     VARCHAR2(4000),
    INSU_NTBY_TR_PBMN     VARCHAR2(4000),
    MRBN_NTBY_TR_PBMN     VARCHAR2(4000),
    FUND_NTBY_TR_PBMN     VARCHAR2(4000),
    ETC_ORGT_NTBY_TR_PBMN VARCHAR2(4000),
    ETC_CORP_NTBY_TR_PBMN VARCHAR2(4000),
    CREATED_AT            DATE           not null
)
/

create index IX_FOREIGN_INSTITUTION_TOTAL_API_NAME
    on FOREIGN_INSTITUTION_TOTAL (API_NAME)
/

create table FRGNMEM_PCHS_TREND
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    BSOP_HOUR          VARCHAR2(4000),
    STCK_PRPR          VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    FRGN_SELN_VOL      VARCHAR2(4000),
    FRGN_SHNU_VOL      VARCHAR2(4000),
    GLOB_NTBY_QTY      VARCHAR2(4000),
    FRGN_NTBY_QTY_ICDC VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_FRGNMEM_PCHS_TREND_API_NAME
    on FRGNMEM_PCHS_TREND (API_NAME)
/

create table FRGNMEM_TRADE_ESTIMATE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    STCK_SHRN_ISCD      VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    GLOB_NTSL_QTY       VARCHAR2(4000),
    STCK_PRPR           VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    GLOB_TOTAL_SELN_QTY VARCHAR2(4000),
    GLOB_TOTAL_SHNU_QTY VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_FRGNMEM_TRADE_ESTIMATE_API_NAME
    on FRGNMEM_TRADE_ESTIMATE (API_NAME)
/

create table FRGNMEM_TRADE_TREND
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    TOTAL_SELN_QTY     VARCHAR2(4000),
    TOTAL_SHNU_QTY     VARCHAR2(4000),
    BSOP_HOUR          VARCHAR2(4000),
    HTS_KOR_ISNM       VARCHAR2(4000),
    STCK_PRPR          VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    CNTG_VOL           VARCHAR2(4000),
    ACML_NTBY_QTY      VARCHAR2(4000),
    GLOB_NTBY_QTY      VARCHAR2(4000),
    FRGN_NTBY_QTY_ICDC VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_FRGNMEM_TRADE_TREND_API_NAME
    on FRGNMEM_TRADE_TREND (API_NAME)
/

create table HTS_TOP_VIEW
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    OUTPUT1           VARCHAR2(4000),
    MRKT_DIV_CLS_CODE VARCHAR2(4000),
    MKSC_SHRN_ISCD    VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_HTS_TOP_VIEW_API_NAME
    on HTS_TOP_VIEW (API_NAME)
/

create table INDEX_CCNL
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    BSTP_CLS_CODE            VARCHAR2(4000),
    BSOP_HOUR                VARCHAR2(4000),
    PRPR_NMIX                VARCHAR2(4000),
    PRDY_VRSS_SIGN           VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS      VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    ACML_TR_PBMN             VARCHAR2(4000),
    PCAS_VOL                 VARCHAR2(4000),
    PCAS_TR_PBMN             VARCHAR2(4000),
    PRDY_CTRT                VARCHAR2(4000),
    OPRC_NMIX                VARCHAR2(4000),
    NMIX_HGPR                VARCHAR2(4000),
    NMIX_LWPR                VARCHAR2(4000),
    OPRC_VRSS_NMIX_PRPR      VARCHAR2(4000),
    OPRC_VRSS_NMIX_SIGN      VARCHAR2(4000),
    HGPR_VRSS_NMIX_PRPR      VARCHAR2(4000),
    HGPR_VRSS_NMIX_SIGN      VARCHAR2(4000),
    LWPR_VRSS_NMIX_PRPR      VARCHAR2(4000),
    LWPR_VRSS_NMIX_SIGN      VARCHAR2(4000),
    PRDY_CLPR_VRSS_OPRC_RATE VARCHAR2(4000),
    PRDY_CLPR_VRSS_HGPR_RATE VARCHAR2(4000),
    PRDY_CLPR_VRSS_LWPR_RATE VARCHAR2(4000),
    UPLM_ISSU_CNT            VARCHAR2(4000),
    ASCN_ISSU_CNT            VARCHAR2(4000),
    STNR_ISSU_CNT            VARCHAR2(4000),
    DOWN_ISSU_CNT            VARCHAR2(4000),
    LSLM_ISSU_CNT            VARCHAR2(4000),
    QTQT_ASCN_ISSU_CNT       VARCHAR2(4000),
    QTQT_DOWN_ISSU_CNT       VARCHAR2(4000),
    TICK_VRSS                VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_INDEX_CCNL_API_NAME
    on INDEX_CCNL (API_NAME)
/

create table INDEX_EXP_CCNL
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    BSTP_CLS_CODE            VARCHAR2(4000),
    BSOP_HOUR                VARCHAR2(4000),
    PRPR_NMIX                VARCHAR2(4000),
    PRDY_VRSS_SIGN           VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS      VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    ACML_TR_PBMN             VARCHAR2(4000),
    PCAS_VOL                 VARCHAR2(4000),
    PCAS_TR_PBMN             VARCHAR2(4000),
    PRDY_CTRT                VARCHAR2(4000),
    OPRC_NMIX                VARCHAR2(4000),
    NMIX_HGPR                VARCHAR2(4000),
    NMIX_LWPR                VARCHAR2(4000),
    OPRC_VRSS_NMIX_PRPR      VARCHAR2(4000),
    OPRC_VRSS_NMIX_SIGN      VARCHAR2(4000),
    HGPR_VRSS_NMIX_PRPR      VARCHAR2(4000),
    HGPR_VRSS_NMIX_SIGN      VARCHAR2(4000),
    LWPR_VRSS_NMIX_PRPR      VARCHAR2(4000),
    LWPR_VRSS_NMIX_SIGN      VARCHAR2(4000),
    PRDY_CLPR_VRSS_OPRC_RATE VARCHAR2(4000),
    PRDY_CLPR_VRSS_HGPR_RATE VARCHAR2(4000),
    PRDY_CLPR_VRSS_LWPR_RATE VARCHAR2(4000),
    UPLM_ISSU_CNT            VARCHAR2(4000),
    ASCN_ISSU_CNT            VARCHAR2(4000),
    STNR_ISSU_CNT            VARCHAR2(4000),
    DOWN_ISSU_CNT            VARCHAR2(4000),
    LSLM_ISSU_CNT            VARCHAR2(4000),
    QTQT_ASCN_ISSU_CNT       VARCHAR2(4000),
    QTQT_DOWN_ISSU_CNT       VARCHAR2(4000),
    TICK_VRSS                VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_INDEX_EXP_CCNL_API_NAME
    on INDEX_EXP_CCNL (API_NAME)
/

create table INDEX_PROGRAM_TRADE
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    BSTP_CLS_CODE               VARCHAR2(4000),
    BSOP_HOUR                   VARCHAR2(4000),
    ARBT_SELN_ENTM_CNQN         VARCHAR2(4000),
    ARBT_SELN_ONSL_CNQN         VARCHAR2(4000),
    ARBT_SHNU_ENTM_CNQN         VARCHAR2(4000),
    ARBT_SHNU_ONSL_CNQN         VARCHAR2(4000),
    NABT_SELN_ENTM_CNQN         VARCHAR2(4000),
    NABT_SELN_ONSL_CNQN         VARCHAR2(4000),
    NABT_SHNU_ENTM_CNQN         VARCHAR2(4000),
    NABT_SHNU_ONSL_CNQN         VARCHAR2(4000),
    ARBT_SELN_ENTM_CNTG_AMT     VARCHAR2(4000),
    ARBT_SELN_ONSL_CNTG_AMT     VARCHAR2(4000),
    ARBT_SHNU_ENTM_CNTG_AMT     VARCHAR2(4000),
    ARBT_SHNU_ONSL_CNTG_AMT     VARCHAR2(4000),
    NABT_SELN_ENTM_CNTG_AMT     VARCHAR2(4000),
    NABT_SELN_ONSL_CNTG_AMT     VARCHAR2(4000),
    NABT_SHNU_ENTM_CNTG_AMT     VARCHAR2(4000),
    NABT_SHNU_ONSL_CNTG_AMT     VARCHAR2(4000),
    ARBT_SMTN_SELN_VOL          VARCHAR2(4000),
    ARBT_SMTM_SELN_VOL_RATE     VARCHAR2(4000),
    ARBT_SMTN_SELN_TR_PBMN      VARCHAR2(4000),
    ARBT_SMTM_SELN_TR_PBMN_RATE VARCHAR2(4000),
    ARBT_SMTN_SHNU_VOL          VARCHAR2(4000),
    ARBT_SMTM_SHNU_VOL_RATE     VARCHAR2(4000),
    ARBT_SMTN_SHNU_TR_PBMN      VARCHAR2(4000),
    ARBT_SMTM_SHNU_TR_PBMN_RATE VARCHAR2(4000),
    ARBT_SMTN_NTBY_QTY          VARCHAR2(4000),
    ARBT_SMTM_NTBY_QTY_RATE     VARCHAR2(4000),
    ARBT_SMTN_NTBY_TR_PBMN      VARCHAR2(4000),
    ARBT_SMTM_NTBY_TR_PBMN_RATE VARCHAR2(4000),
    NABT_SMTN_SELN_VOL          VARCHAR2(4000),
    NABT_SMTM_SELN_VOL_RATE     VARCHAR2(4000),
    NABT_SMTN_SELN_TR_PBMN      VARCHAR2(4000),
    NABT_SMTM_SELN_TR_PBMN_RATE VARCHAR2(4000),
    NABT_SMTN_SHNU_VOL          VARCHAR2(4000),
    NABT_SMTM_SHNU_VOL_RATE     VARCHAR2(4000),
    NABT_SMTN_SHNU_TR_PBMN      VARCHAR2(4000),
    NABT_SMTM_SHNU_TR_PBMN_RATE VARCHAR2(4000),
    NABT_SMTN_NTBY_QTY          VARCHAR2(4000),
    NABT_SMTM_NTBY_QTY_RATE     VARCHAR2(4000),
    NABT_SMTN_NTBY_TR_PBMN      VARCHAR2(4000),
    NABT_SMTM_NTBY_TR_PBMN_RATE VARCHAR2(4000),
    WHOL_ENTM_SELN_VOL          VARCHAR2(4000),
    ENTM_SELN_VOL_RATE          VARCHAR2(4000),
    WHOL_ENTM_SELN_TR_PBMN      VARCHAR2(4000),
    ENTM_SELN_TR_PBMN_RATE      VARCHAR2(4000),
    WHOL_ENTM_SHNU_VOL          VARCHAR2(4000),
    ENTM_SHNU_VOL_RATE          VARCHAR2(4000),
    WHOL_ENTM_SHNU_TR_PBMN      VARCHAR2(4000),
    ENTM_SHNU_TR_PBMN_RATE      VARCHAR2(4000),
    WHOL_ENTM_NTBY_QT           VARCHAR2(4000),
    ENTM_NTBY_QTY_RAT           VARCHAR2(4000),
    WHOL_ENTM_NTBY_TR_PBMN      VARCHAR2(4000),
    ENTM_NTBY_TR_PBMN_RATE      VARCHAR2(4000),
    WHOL_ONSL_SELN_VOL          VARCHAR2(4000),
    ONSL_SELN_VOL_RATE          VARCHAR2(4000),
    WHOL_ONSL_SELN_TR_PBMN      VARCHAR2(4000),
    ONSL_SELN_TR_PBMN_RATE      VARCHAR2(4000),
    WHOL_ONSL_SHNU_VOL          VARCHAR2(4000),
    ONSL_SHNU_VOL_RATE          VARCHAR2(4000),
    WHOL_ONSL_SHNU_TR_PBMN      VARCHAR2(4000),
    ONSL_SHNU_TR_PBMN_RATE      VARCHAR2(4000),
    WHOL_ONSL_NTBY_QTY          VARCHAR2(4000),
    ONSL_NTBY_QTY_RATE          VARCHAR2(4000),
    WHOL_ONSL_NTBY_TR_PBMN      VARCHAR2(4000),
    ONSL_NTBY_TR_PBMN_RATE      VARCHAR2(4000),
    TOTAL_SELN_QTY              VARCHAR2(4000),
    WHOL_SELN_VOL_RATE          VARCHAR2(4000),
    TOTAL_SELN_TR_PBMN          VARCHAR2(4000),
    WHOL_SELN_TR_PBMN_RATE      VARCHAR2(4000),
    SHNU_CNTG_SMTN              VARCHAR2(4000),
    WHOL_SHUN_VOL_RATE          VARCHAR2(4000),
    TOTAL_SHNU_TR_PBMN          VARCHAR2(4000),
    WHOL_SHUN_TR_PBMN_RATE      VARCHAR2(4000),
    WHOL_NTBY_QTY               VARCHAR2(4000),
    WHOL_SMTM_NTBY_QTY_RATE     VARCHAR2(4000),
    WHOL_NTBY_TR_PBMN           VARCHAR2(4000),
    WHOL_NTBY_TR_PBMN_RATE      VARCHAR2(4000),
    ARBT_ENTM_NTBY_QTY          VARCHAR2(4000),
    ARBT_ENTM_NTBY_TR_PBMN      VARCHAR2(4000),
    ARBT_ONSL_NTBY_QTY          VARCHAR2(4000),
    ARBT_ONSL_NTBY_TR_PBMN      VARCHAR2(4000),
    NABT_ENTM_NTBY_QTY          VARCHAR2(4000),
    NABT_ENTM_NTBY_TR_PBMN      VARCHAR2(4000),
    NABT_ONSL_NTBY_QTY          VARCHAR2(4000),
    NABT_ONSL_NTBY_TR_PBMN      VARCHAR2(4000),
    ACML_VOL                    VARCHAR2(4000),
    ACML_TR_PBMN                VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_INDEX_PROGRAM_TRADE_API_NAME
    on INDEX_PROGRAM_TRADE (API_NAME)
/

create table INQUIRE_ACCOUNT_BALANCE
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    PCHS_AMT                    VARCHAR2(4000),
    EVLU_AMT                    VARCHAR2(4000),
    EVLU_PFLS_AMT               VARCHAR2(4000),
    CRDT_LND_AMT                VARCHAR2(4000),
    REAL_NASS_AMT               VARCHAR2(4000),
    WHOL_WEIT_RT                VARCHAR2(4000),
    PCHS_AMT_SMTL               VARCHAR2(4000),
    NASS_TOT_AMT                VARCHAR2(4000),
    LOAN_AMT_SMTL               VARCHAR2(4000),
    EVLU_PFLS_AMT_SMTL          VARCHAR2(4000),
    EVLU_AMT_SMTL               VARCHAR2(4000),
    TOT_ASST_AMT                VARCHAR2(4000),
    TOT_LNDA_TOT_ULST_LNDA      VARCHAR2(4000),
    CMA_AUTO_LOAN_AMT           VARCHAR2(4000),
    TOT_MGLN_AMT                VARCHAR2(4000),
    STLN_EVLU_AMT               VARCHAR2(4000),
    CRDT_FNCG_AMT               VARCHAR2(4000),
    OCL_APL_LOAN_AMT            VARCHAR2(4000),
    PLDG_STUP_AMT               VARCHAR2(4000),
    FRCR_EVLU_TOTA              VARCHAR2(4000),
    TOT_DNCL_AMT                VARCHAR2(4000),
    CMA_EVLU_AMT                VARCHAR2(4000),
    DNCL_AMT                    VARCHAR2(4000),
    TOT_SBST_AMT                VARCHAR2(4000),
    THDT_RCVB_AMT               VARCHAR2(4000),
    OVRS_STCK_EVLU_AMT1         VARCHAR2(4000),
    OVRS_BOND_EVLU_AMT          VARCHAR2(4000),
    MMF_CMA_MGGE_LOAN_AMT       VARCHAR2(4000),
    SBSC_DNCL_AMT               VARCHAR2(4000),
    PBST_SBSC_FNDS_LOAN_USE_AMT VARCHAR2(4000),
    ETPR_CRDT_GRNT_LOAN_AMT     VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_INQUIRE_ACCOUNT_BALANCE_API_NAME
    on INQUIRE_ACCOUNT_BALANCE (API_NAME)
/

create table INQUIRE_ASKING_PRICE_EXP_CCN
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    ASPR_ACPT_HOUR       VARCHAR2(4000),
    ASKP1                VARCHAR2(4000),
    ASKP2                VARCHAR2(4000),
    ASKP3                VARCHAR2(4000),
    ASKP4                VARCHAR2(4000),
    ASKP5                VARCHAR2(4000),
    ASKP6                VARCHAR2(4000),
    ASKP7                VARCHAR2(4000),
    ASKP8                VARCHAR2(4000),
    ASKP9                VARCHAR2(4000),
    ASKP10               VARCHAR2(4000),
    BIDP1                VARCHAR2(4000),
    BIDP2                VARCHAR2(4000),
    BIDP3                VARCHAR2(4000),
    BIDP4                VARCHAR2(4000),
    BIDP5                VARCHAR2(4000),
    BIDP6                VARCHAR2(4000),
    BIDP7                VARCHAR2(4000),
    BIDP8                VARCHAR2(4000),
    BIDP9                VARCHAR2(4000),
    BIDP10               VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    ASKP_RSQN6           VARCHAR2(4000),
    ASKP_RSQN7           VARCHAR2(4000),
    ASKP_RSQN8           VARCHAR2(4000),
    ASKP_RSQN9           VARCHAR2(4000),
    ASKP_RSQN10          VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN6           VARCHAR2(4000),
    BIDP_RSQN7           VARCHAR2(4000),
    BIDP_RSQN8           VARCHAR2(4000),
    BIDP_RSQN9           VARCHAR2(4000),
    BIDP_RSQN10          VARCHAR2(4000),
    ASKP_RSQN_ICDC1      VARCHAR2(4000),
    ASKP_RSQN_ICDC2      VARCHAR2(4000),
    ASKP_RSQN_ICDC3      VARCHAR2(4000),
    ASKP_RSQN_ICDC4      VARCHAR2(4000),
    ASKP_RSQN_ICDC5      VARCHAR2(4000),
    ASKP_RSQN_ICDC6      VARCHAR2(4000),
    ASKP_RSQN_ICDC7      VARCHAR2(4000),
    ASKP_RSQN_ICDC8      VARCHAR2(4000),
    ASKP_RSQN_ICDC9      VARCHAR2(4000),
    ASKP_RSQN_ICDC10     VARCHAR2(4000),
    BIDP_RSQN_ICDC1      VARCHAR2(4000),
    BIDP_RSQN_ICDC2      VARCHAR2(4000),
    BIDP_RSQN_ICDC3      VARCHAR2(4000),
    BIDP_RSQN_ICDC4      VARCHAR2(4000),
    BIDP_RSQN_ICDC5      VARCHAR2(4000),
    BIDP_RSQN_ICDC6      VARCHAR2(4000),
    BIDP_RSQN_ICDC7      VARCHAR2(4000),
    BIDP_RSQN_ICDC8      VARCHAR2(4000),
    BIDP_RSQN_ICDC9      VARCHAR2(4000),
    BIDP_RSQN_ICDC10     VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    OVTM_TOTAL_ASKP_ICDC VARCHAR2(4000),
    OVTM_TOTAL_BIDP_ICDC VARCHAR2(4000),
    OVTM_TOTAL_ASKP_RSQN VARCHAR2(4000),
    OVTM_TOTAL_BIDP_RSQN VARCHAR2(4000),
    NTBY_ASPR_RSQN       VARCHAR2(4000),
    NEW_MKOP_CLS_CODE    VARCHAR2(4000),
    ANTC_MKOP_CLS_CODE   VARCHAR2(4000),
    STCK_PRPR            VARCHAR2(4000),
    STCK_OPRC            VARCHAR2(4000),
    STCK_HGPR            VARCHAR2(4000),
    STCK_LWPR            VARCHAR2(4000),
    STCK_SDPR            VARCHAR2(4000),
    ANTC_CNPR            VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN  VARCHAR2(4000),
    ANTC_CNTG_VRSS       VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT  VARCHAR2(4000),
    ANTC_VOL             VARCHAR2(4000),
    STCK_SHRN_ISCD       VARCHAR2(4000),
    VI_CLS_CODE          VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_INQUIRE_ASKING_PRICE_EXP_CCN_API_NAME
    on INQUIRE_ASKING_PRICE_EXP_CCN (API_NAME)
/

create table INQUIRE_BALANCE_RLZ_PL
(
    ID                     NUMBER         not null
        primary key,
    API_NAME               VARCHAR2(4000) not null,
    PDNO                   VARCHAR2(4000),
    PRDT_NAME              VARCHAR2(4000),
    TRAD_DVSN_NAME         VARCHAR2(4000),
    BFDY_BUY_QTY           VARCHAR2(4000),
    BFDY_SLL_QTY           VARCHAR2(4000),
    THDT_BUYQTY            VARCHAR2(4000),
    THDT_SLL_QTY           VARCHAR2(4000),
    HLDG_QTY               VARCHAR2(4000),
    ORD_PSBL_QTY           VARCHAR2(4000),
    PCHS_AVG_PRIC          VARCHAR2(4000),
    PCHS_AMT               VARCHAR2(4000),
    PRPR                   VARCHAR2(4000),
    EVLU_AMT               VARCHAR2(4000),
    EVLU_PFLS_AMT          VARCHAR2(4000),
    EVLU_PFLS_RT           VARCHAR2(4000),
    EVLU_ERNG_RT           VARCHAR2(4000),
    LOAN_DT                VARCHAR2(4000),
    LOAN_AMT               VARCHAR2(4000),
    STLN_SLNG_CHGS         VARCHAR2(4000),
    EXPD_DT                VARCHAR2(4000),
    STCK_LOAN_UNPR         VARCHAR2(4000),
    BFDY_CPRS_ICDC         VARCHAR2(4000),
    FLTT_RT                VARCHAR2(4000),
    DNCA_TOT_AMT           VARCHAR2(4000),
    NXDY_EXCC_AMT          VARCHAR2(4000),
    PRVS_RCDL_EXCC_AMT     VARCHAR2(4000),
    CMA_EVLU_AMT           VARCHAR2(4000),
    BFDY_BUY_AMT           VARCHAR2(4000),
    THDT_BUY_AMT           VARCHAR2(4000),
    NXDY_AUTO_RDPT_AMT     VARCHAR2(4000),
    BFDY_SLL_AMT           VARCHAR2(4000),
    THDT_SLL_AMT           VARCHAR2(4000),
    D2_AUTO_RDPT_AMT       VARCHAR2(4000),
    BFDY_TLEX_AMT          VARCHAR2(4000),
    THDT_TLEX_AMT          VARCHAR2(4000),
    TOT_LOAN_AMT           VARCHAR2(4000),
    SCTS_EVLU_AMT          VARCHAR2(4000),
    TOT_EVLU_AMT           VARCHAR2(4000),
    NASS_AMT               VARCHAR2(4000),
    FNCG_GLD_AUTO_RDPT_YN  VARCHAR2(4000),
    PCHS_AMT_SMTL_AMT      VARCHAR2(4000),
    EVLU_AMT_SMTL_AMT      VARCHAR2(4000),
    EVLU_PFLS_SMTL_AMT     VARCHAR2(4000),
    TOT_STLN_SLNG_CHGS     VARCHAR2(4000),
    BFDY_TOT_ASST_EVLU_AMT VARCHAR2(4000),
    ASST_ICDC_AMT          VARCHAR2(4000),
    ASST_ICDC_ERNG_RT      VARCHAR2(4000),
    RLZT_PFLS              VARCHAR2(4000),
    RLZT_ERNG_RT           VARCHAR2(4000),
    REAL_EVLU_PFLS         VARCHAR2(4000),
    REAL_EVLU_PFLS_ERNG_RT VARCHAR2(4000),
    CREATED_AT             DATE           not null
)
/

create index IX_INQUIRE_BALANCE_RLZ_PL_API_NAME
    on INQUIRE_BALANCE_RLZ_PL (API_NAME)
/

create table INQUIRE_CREDIT_PSAMOUNT
(
    ID                     NUMBER         not null
        primary key,
    API_NAME               VARCHAR2(4000) not null,
    ORD_PSBL_CASH          VARCHAR2(4000),
    ORD_PSBL_SBST          VARCHAR2(4000),
    RUSE_PSBL_AMT          VARCHAR2(4000),
    FUND_RPCH_CHGS         VARCHAR2(4000),
    PSBL_QTY_CALC_UNPR     VARCHAR2(4000),
    NRCVB_BUY_AMT          VARCHAR2(4000),
    NRCVB_BUY_QTY          VARCHAR2(4000),
    MAX_BUY_AMT            VARCHAR2(4000),
    MAX_BUY_QTY            VARCHAR2(4000),
    CMA_EVLU_AMT           VARCHAR2(4000),
    OVRS_RE_USE_AMT_WCRC   VARCHAR2(4000),
    ORD_PSBL_FRCR_AMT_WCRC VARCHAR2(4000),
    CREATED_AT             DATE           not null
)
/

create index IX_INQUIRE_CREDIT_PSAMOUNT_API_NAME
    on INQUIRE_CREDIT_PSAMOUNT (API_NAME)
/

create table INQUIRE_DAILY_INDEXCHARTPRICE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    BSTP_NMIX_PRDY_VRSS VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    BSTP_NMIX_PRDY_CTRT VARCHAR2(4000),
    PRDY_NMIX           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    ACML_TR_PBMN        VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    BSTP_NMIX_PRPR      VARCHAR2(4000),
    BSTP_CLS_CODE       VARCHAR2(4000),
    PRDY_VOL            VARCHAR2(4000),
    BSTP_NMIX_OPRC      VARCHAR2(4000),
    BSTP_NMIX_HGPR      VARCHAR2(4000),
    BSTP_NMIX_LWPR      VARCHAR2(4000),
    FUTS_PRDY_OPRC      VARCHAR2(4000),
    FUTS_PRDY_HGPR      VARCHAR2(4000),
    FUTS_PRDY_LWPR      VARCHAR2(4000),
    STCK_BSOP_DATE      VARCHAR2(4000),
    MOD_YN              VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_INQUIRE_DAILY_INDEXCHARTPRICE_API_NAME
    on INQUIRE_DAILY_INDEXCHARTPRICE (API_NAME)
/

create table INQUIRE_DAILY_OVERTIMEPRICE
(
    ID                            NUMBER         not null
        primary key,
    API_NAME                      VARCHAR2(4000) not null,
    OVTM_UNTP_PRPR                VARCHAR2(4000),
    OVTM_UNTP_PRDY_VRSS           VARCHAR2(4000),
    OVTM_UNTP_PRDY_VRSS_SIGN      VARCHAR2(4000),
    OVTM_UNTP_PRDY_CTRT           VARCHAR2(4000),
    OVTM_UNTP_VOL                 VARCHAR2(4000),
    OVTM_UNTP_TR_PBMN             VARCHAR2(4000),
    OVTM_UNTP_MXPR                VARCHAR2(4000),
    OVTM_UNTP_LLAM                VARCHAR2(4000),
    OVTM_UNTP_OPRC                VARCHAR2(4000),
    OVTM_UNTP_HGPR                VARCHAR2(4000),
    OVTM_UNTP_LWPR                VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNPR           VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_VRSS      VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_CTRT      VARCHAR2(4000),
    OVTM_UNTP_ANTC_VOL            VARCHAR2(4000),
    STCK_BSOP_DATE                VARCHAR2(4000),
    STCK_CLPR                     VARCHAR2(4000),
    PRDY_VRSS                     VARCHAR2(4000),
    PRDY_VRSS_SIGN                VARCHAR2(4000),
    PRDY_CTRT                     VARCHAR2(4000),
    ACML_VOL                      VARCHAR2(4000),
    CREATED_AT                    DATE           not null
)
/

create index IX_INQUIRE_DAILY_OVERTIMEPRICE_API_NAME
    on INQUIRE_DAILY_OVERTIMEPRICE (API_NAME)
/

create table INQUIRE_DAILY_TRADE_VOLUME
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    SHNU_CNQN_SMTN VARCHAR2(4000),
    SELN_CNQN_SMTN VARCHAR2(4000),
    STCK_BSOP_DATE VARCHAR2(4000),
    TOTAL_SELN_QTY VARCHAR2(4000),
    TOTAL_SHNU_QTY VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_INQUIRE_DAILY_TRADE_VOLUME_API_NAME
    on INQUIRE_DAILY_TRADE_VOLUME (API_NAME)
/

create table INQUIRE_ELW_PRICE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    ELW_SHRN_ISCD       VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    ELW_PRPR            VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    PRDY_VRSS_VOL_RATE  VARCHAR2(4000),
    UNAS_SHRN_ISCD      VARCHAR2(4000),
    UNAS_ISNM           VARCHAR2(4000),
    UNAS_PRPR           VARCHAR2(4000),
    UNAS_PRDY_VRSS      VARCHAR2(4000),
    UNAS_PRDY_VRSS_SIGN VARCHAR2(4000),
    UNAS_PRDY_CTRT      VARCHAR2(4000),
    BIDP                VARCHAR2(4000),
    ASKP                VARCHAR2(4000),
    ACML_TR_PBMN        VARCHAR2(4000),
    VOL_TNRT            VARCHAR2(4000),
    ELW_OPRC            VARCHAR2(4000),
    ELW_HGPR            VARCHAR2(4000),
    ELW_LWPR            VARCHAR2(4000),
    STCK_PRDY_CLPR      VARCHAR2(4000),
    HTS_THPR            VARCHAR2(4000),
    DPRT                VARCHAR2(4000),
    ATM_CLS_NAME        VARCHAR2(4000),
    HTS_INTS_VLTL       VARCHAR2(4000),
    ACPR                VARCHAR2(4000),
    PVT_SCND_DMRS_PRC   VARCHAR2(4000),
    PVT_FRST_DMRS_PRC   VARCHAR2(4000),
    PVT_PONT_VAL        VARCHAR2(4000),
    PVT_FRST_DMSP_PRC   VARCHAR2(4000),
    PVT_SCND_DMSP_PRC   VARCHAR2(4000),
    DMSP_VAL            VARCHAR2(4000),
    DMRS_VAL            VARCHAR2(4000),
    ELW_SDPR            VARCHAR2(4000),
    APPRCH_RATE         VARCHAR2(4000),
    TICK_CONV_PRC       VARCHAR2(4000),
    INVT_EPMD_CNTT      VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_INQUIRE_ELW_PRICE_API_NAME
    on INQUIRE_ELW_PRICE (API_NAME)
/

create table INQUIRE_INDEX_CATEGORY_PRICE
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    BSTP_NMIX_PRPR           VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN           VARCHAR2(4000),
    BSTP_NMIX_PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    ACML_TR_PBMN             VARCHAR2(4000),
    BSTP_NMIX_OPRC           VARCHAR2(4000),
    BSTP_NMIX_HGPR           VARCHAR2(4000),
    BSTP_NMIX_LWPR           VARCHAR2(4000),
    PRDY_VOL                 VARCHAR2(4000),
    ASCN_ISSU_CNT            VARCHAR2(4000),
    DOWN_ISSU_CNT            VARCHAR2(4000),
    STNR_ISSU_CNT            VARCHAR2(4000),
    UPLM_ISSU_CNT            VARCHAR2(4000),
    LSLM_ISSU_CNT            VARCHAR2(4000),
    PRDY_TR_PBMN             VARCHAR2(4000),
    DRYY_BSTP_NMIX_HGPR_DATE VARCHAR2(4000),
    DRYY_BSTP_NMIX_HGPR      VARCHAR2(4000),
    DRYY_BSTP_NMIX_LWPR      VARCHAR2(4000),
    DRYY_BSTP_NMIX_LWPR_DATE VARCHAR2(4000),
    BSTP_CLS_CODE            VARCHAR2(4000),
    HTS_KOR_ISNM             VARCHAR2(4000),
    ACML_VOL_RLIM            VARCHAR2(4000),
    ACML_TR_PBMN_RLIM        VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_INQUIRE_INDEX_CATEGORY_PRICE_API_NAME
    on INQUIRE_INDEX_CATEGORY_PRICE (API_NAME)
/

create table INQUIRE_INDEX_DAILY_PRICE
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    BSTP_NMIX_PRPR           VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN           VARCHAR2(4000),
    BSTP_NMIX_PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    ACML_TR_PBMN             VARCHAR2(4000),
    BSTP_NMIX_OPRC           VARCHAR2(4000),
    BSTP_NMIX_HGPR           VARCHAR2(4000),
    BSTP_NMIX_LWPR           VARCHAR2(4000),
    PRDY_VOL                 VARCHAR2(4000),
    ASCN_ISSU_CNT            VARCHAR2(4000),
    DOWN_ISSU_CNT            VARCHAR2(4000),
    STNR_ISSU_CNT            VARCHAR2(4000),
    UPLM_ISSU_CNT            VARCHAR2(4000),
    LSLM_ISSU_CNT            VARCHAR2(4000),
    PRDY_TR_PBMN             VARCHAR2(4000),
    DRYY_BSTP_NMIX_HGPR_DATE VARCHAR2(4000),
    DRYY_BSTP_NMIX_HGPR      VARCHAR2(4000),
    DRYY_BSTP_NMIX_LWPR      VARCHAR2(4000),
    DRYY_BSTP_NMIX_LWPR_DATE VARCHAR2(4000),
    STCK_BSOP_DATE           VARCHAR2(4000),
    ACML_VOL_RLIM            VARCHAR2(4000),
    INVT_NEW_PSDG            VARCHAR2(4000),
    D20_DSRT                 VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_INQUIRE_INDEX_DAILY_PRICE_API_NAME
    on INQUIRE_INDEX_DAILY_PRICE (API_NAME)
/

create table INQUIRE_INDEX_PRICE
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    BSTP_NMIX_PRPR           VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN           VARCHAR2(4000),
    BSTP_NMIX_PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    PRDY_VOL                 VARCHAR2(4000),
    ACML_TR_PBMN             VARCHAR2(4000),
    PRDY_TR_PBMN             VARCHAR2(4000),
    BSTP_NMIX_OPRC           VARCHAR2(4000),
    PRDY_NMIX_VRSS_NMIX_OPRC VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN      VARCHAR2(4000),
    BSTP_NMIX_OPRC_PRDY_CTRT VARCHAR2(4000),
    BSTP_NMIX_HGPR           VARCHAR2(4000),
    PRDY_NMIX_VRSS_NMIX_HGPR VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN      VARCHAR2(4000),
    BSTP_NMIX_HGPR_PRDY_CTRT VARCHAR2(4000),
    BSTP_NMIX_LWPR           VARCHAR2(4000),
    PRDY_CLPR_VRSS_LWPR      VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN      VARCHAR2(4000),
    PRDY_CLPR_VRSS_LWPR_RATE VARCHAR2(4000),
    ASCN_ISSU_CNT            VARCHAR2(4000),
    UPLM_ISSU_CNT            VARCHAR2(4000),
    STNR_ISSU_CNT            VARCHAR2(4000),
    DOWN_ISSU_CNT            VARCHAR2(4000),
    LSLM_ISSU_CNT            VARCHAR2(4000),
    DRYY_BSTP_NMIX_HGPR      VARCHAR2(4000),
    DRYY_HGPR_VRSS_PRPR_RATE VARCHAR2(4000),
    DRYY_BSTP_NMIX_HGPR_DATE VARCHAR2(4000),
    DRYY_BSTP_NMIX_LWPR      VARCHAR2(4000),
    DRYY_LWPR_VRSS_PRPR_RATE VARCHAR2(4000),
    DRYY_BSTP_NMIX_LWPR_DATE VARCHAR2(4000),
    TOTAL_ASKP_RSQN          VARCHAR2(4000),
    TOTAL_BIDP_RSQN          VARCHAR2(4000),
    SELN_RSQN_RATE           VARCHAR2(4000),
    SHNU_RSQN_RATE           VARCHAR2(4000),
    NTBY_RSQN                VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_INQUIRE_INDEX_PRICE_API_NAME
    on INQUIRE_INDEX_PRICE (API_NAME)
/

create table INQUIRE_INDEX_TICKPRICE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    STCK_CNTG_HOUR      VARCHAR2(4000),
    BSTP_NMIX_PRPR      VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    BSTP_NMIX_PRDY_CTRT VARCHAR2(4000),
    ACML_TR_PBMN        VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    CNTG_VOL            VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_INQUIRE_INDEX_TICKPRICE_API_NAME
    on INQUIRE_INDEX_TICKPRICE (API_NAME)
/

create table INQUIRE_INDEX_TIMEPRICE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    BSOP_HOUR           VARCHAR2(4000),
    BSTP_NMIX_PRPR      VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    BSTP_NMIX_PRDY_CTRT VARCHAR2(4000),
    ACML_TR_PBMN        VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    CNTG_VOL            VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_INQUIRE_INDEX_TIMEPRICE_API_NAME
    on INQUIRE_INDEX_TIMEPRICE (API_NAME)
/

create table INQUIRE_INVESTOR
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    STCK_BSOP_DATE    VARCHAR2(4000),
    STCK_CLPR         VARCHAR2(4000),
    PRDY_VRSS         VARCHAR2(4000),
    PRDY_VRSS_SIGN    VARCHAR2(4000),
    PRSN_NTBY_QTY     VARCHAR2(4000),
    FRGN_NTBY_QTY     VARCHAR2(4000),
    ORGN_NTBY_QTY     VARCHAR2(4000),
    PRSN_NTBY_TR_PBMN VARCHAR2(4000),
    FRGN_NTBY_TR_PBMN VARCHAR2(4000),
    ORGN_NTBY_TR_PBMN VARCHAR2(4000),
    PRSN_SHNU_VOL     VARCHAR2(4000),
    FRGN_SHNU_VOL     VARCHAR2(4000),
    ORGN_SHNU_VOL     VARCHAR2(4000),
    PRSN_SHNU_TR_PBMN VARCHAR2(4000),
    FRGN_SHNU_TR_PBMN VARCHAR2(4000),
    ORGN_SHNU_TR_PBMN VARCHAR2(4000),
    PRSN_SELN_VOL     VARCHAR2(4000),
    FRGN_SELN_VOL     VARCHAR2(4000),
    ORGN_SELN_VOL     VARCHAR2(4000),
    PRSN_SELN_TR_PBMN VARCHAR2(4000),
    FRGN_SELN_TR_PBMN VARCHAR2(4000),
    ORGN_SELN_TR_PBMN VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_INQUIRE_INVESTOR_API_NAME
    on INQUIRE_INVESTOR (API_NAME)
/

create table INQUIRE_INVESTOR_DAILY_BY_MARKET
(
    ID                    NUMBER         not null
        primary key,
    API_NAME              VARCHAR2(4000) not null,
    STCK_BSOP_DATE        VARCHAR2(4000),
    BSTP_NMIX_PRPR        VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS   VARCHAR2(4000),
    PRDY_VRSS_SIGN        VARCHAR2(4000),
    BSTP_NMIX_PRDY_CTRT   VARCHAR2(4000),
    BSTP_NMIX_OPRC        VARCHAR2(4000),
    BSTP_NMIX_HGPR        VARCHAR2(4000),
    BSTP_NMIX_LWPR        VARCHAR2(4000),
    STCK_PRDY_CLPR        VARCHAR2(4000),
    FRGN_NTBY_QTY         VARCHAR2(4000),
    FRGN_REG_NTBY_QTY     VARCHAR2(4000),
    FRGN_NREG_NTBY_QTY    VARCHAR2(4000),
    PRSN_NTBY_QTY         VARCHAR2(4000),
    ORGN_NTBY_QTY         VARCHAR2(4000),
    SCRT_NTBY_QTY         VARCHAR2(4000),
    IVTR_NTBY_QTY         VARCHAR2(4000),
    PE_FUND_NTBY_VOL      VARCHAR2(4000),
    BANK_NTBY_QTY         VARCHAR2(4000),
    INSU_NTBY_QTY         VARCHAR2(4000),
    MRBN_NTBY_QTY         VARCHAR2(4000),
    FUND_NTBY_QTY         VARCHAR2(4000),
    ETC_NTBY_QTY          VARCHAR2(4000),
    ETC_ORGT_NTBY_VOL     VARCHAR2(4000),
    ETC_CORP_NTBY_VOL     VARCHAR2(4000),
    FRGN_NTBY_TR_PBMN     VARCHAR2(4000),
    FRGN_REG_NTBY_PBMN    VARCHAR2(4000),
    FRGN_NREG_NTBY_PBMN   VARCHAR2(4000),
    PRSN_NTBY_TR_PBMN     VARCHAR2(4000),
    ORGN_NTBY_TR_PBMN     VARCHAR2(4000),
    SCRT_NTBY_TR_PBMN     VARCHAR2(4000),
    IVTR_NTBY_TR_PBMN     VARCHAR2(4000),
    PE_FUND_NTBY_TR_PBMN  VARCHAR2(4000),
    BANK_NTBY_TR_PBMN     VARCHAR2(4000),
    INSU_NTBY_TR_PBMN     VARCHAR2(4000),
    MRBN_NTBY_TR_PBMN     VARCHAR2(4000),
    FUND_NTBY_TR_PBMN     VARCHAR2(4000),
    ETC_NTBY_TR_PBMN      VARCHAR2(4000),
    ETC_ORGT_NTBY_TR_PBMN VARCHAR2(4000),
    ETC_CORP_NTBY_TR_PBMN VARCHAR2(4000),
    CREATED_AT            DATE           not null
)
/

create index IX_INQUIRE_INVESTOR_DAILY_BY_MARKET_API_NAME
    on INQUIRE_INVESTOR_DAILY_BY_MARKET (API_NAME)
/

create table INQUIRE_INVESTOR_TIME_BY_MARKET
(
    ID                    NUMBER         not null
        primary key,
    API_NAME              VARCHAR2(4000) not null,
    FRGN_SELN_VOL         VARCHAR2(4000),
    FRGN_SHNU_VOL         VARCHAR2(4000),
    FRGN_NTBY_QTY         VARCHAR2(4000),
    FRGN_SELN_TR_PBMN     VARCHAR2(4000),
    FRGN_SHNU_TR_PBMN     VARCHAR2(4000),
    FRGN_NTBY_TR_PBMN     VARCHAR2(4000),
    PRSN_SELN_VOL         VARCHAR2(4000),
    PRSN_SHNU_VOL         VARCHAR2(4000),
    PRSN_NTBY_QTY         VARCHAR2(4000),
    PRSN_SELN_TR_PBMN     VARCHAR2(4000),
    PRSN_SHNU_TR_PBMN     VARCHAR2(4000),
    PRSN_NTBY_TR_PBMN     VARCHAR2(4000),
    ORGN_SELN_VOL         VARCHAR2(4000),
    ORGN_SHNU_VOL         VARCHAR2(4000),
    ORGN_NTBY_QTY         VARCHAR2(4000),
    ORGN_SELN_TR_PBMN     VARCHAR2(4000),
    ORGN_SHNU_TR_PBMN     VARCHAR2(4000),
    ORGN_NTBY_TR_PBMN     VARCHAR2(4000),
    SCRT_SELN_VOL         VARCHAR2(4000),
    SCRT_SHNU_VOL         VARCHAR2(4000),
    SCRT_NTBY_QTY         VARCHAR2(4000),
    SCRT_SELN_TR_PBMN     VARCHAR2(4000),
    SCRT_SHNU_TR_PBMN     VARCHAR2(4000),
    SCRT_NTBY_TR_PBMN     VARCHAR2(4000),
    IVTR_SELN_VOL         VARCHAR2(4000),
    IVTR_SHNU_VOL         VARCHAR2(4000),
    IVTR_NTBY_QTY         VARCHAR2(4000),
    IVTR_SELN_TR_PBMN     VARCHAR2(4000),
    IVTR_SHNU_TR_PBMN     VARCHAR2(4000),
    IVTR_NTBY_TR_PBMN     VARCHAR2(4000),
    PE_FUND_SELN_TR_PBMN  VARCHAR2(4000),
    PE_FUND_SELN_VOL      VARCHAR2(4000),
    PE_FUND_NTBY_VOL      VARCHAR2(4000),
    PE_FUND_SHNU_TR_PBMN  VARCHAR2(4000),
    PE_FUND_SHNU_VOL      VARCHAR2(4000),
    PE_FUND_NTBY_TR_PBMN  VARCHAR2(4000),
    BANK_SELN_VOL         VARCHAR2(4000),
    BANK_SHNU_VOL         VARCHAR2(4000),
    BANK_NTBY_QTY         VARCHAR2(4000),
    BANK_SELN_TR_PBMN     VARCHAR2(4000),
    BANK_SHNU_TR_PBMN     VARCHAR2(4000),
    BANK_NTBY_TR_PBMN     VARCHAR2(4000),
    INSU_SELN_VOL         VARCHAR2(4000),
    INSU_SHNU_VOL         VARCHAR2(4000),
    INSU_NTBY_QTY         VARCHAR2(4000),
    INSU_SELN_TR_PBMN     VARCHAR2(4000),
    INSU_SHNU_TR_PBMN     VARCHAR2(4000),
    INSU_NTBY_TR_PBMN     VARCHAR2(4000),
    MRBN_SELN_VOL         VARCHAR2(4000),
    MRBN_SHNU_VOL         VARCHAR2(4000),
    MRBN_NTBY_QTY         VARCHAR2(4000),
    MRBN_SELN_TR_PBMN     VARCHAR2(4000),
    MRBN_SHNU_TR_PBMN     VARCHAR2(4000),
    MRBN_NTBY_TR_PBMN     VARCHAR2(4000),
    FUND_SELN_VOL         VARCHAR2(4000),
    FUND_SHNU_VOL         VARCHAR2(4000),
    FUND_NTBY_QTY         VARCHAR2(4000),
    FUND_SELN_TR_PBMN     VARCHAR2(4000),
    FUND_SHNU_TR_PBMN     VARCHAR2(4000),
    FUND_NTBY_TR_PBMN     VARCHAR2(4000),
    ETC_ORGT_SELN_VOL     VARCHAR2(4000),
    ETC_ORGT_SHNU_VOL     VARCHAR2(4000),
    ETC_ORGT_NTBY_VOL     VARCHAR2(4000),
    ETC_ORGT_SELN_TR_PBMN VARCHAR2(4000),
    ETC_ORGT_SHNU_TR_PBMN VARCHAR2(4000),
    ETC_ORGT_NTBY_TR_PBMN VARCHAR2(4000),
    ETC_CORP_SELN_VOL     VARCHAR2(4000),
    ETC_CORP_SHNU_VOL     VARCHAR2(4000),
    ETC_CORP_NTBY_VOL     VARCHAR2(4000),
    ETC_CORP_SELN_TR_PBMN VARCHAR2(4000),
    ETC_CORP_SHNU_TR_PBMN VARCHAR2(4000),
    ETC_CORP_NTBY_TR_PBMN VARCHAR2(4000),
    CREATED_AT            DATE           not null
)
/

create index IX_INQUIRE_INVESTOR_TIME_BY_MARKET_API_NAME
    on INQUIRE_INVESTOR_TIME_BY_MARKET (API_NAME)
/

create table INQUIRE_MEMBER
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    SELN_MBCR_NO1            VARCHAR2(4000),
    SELN_MBCR_NO2            VARCHAR2(4000),
    SELN_MBCR_NO3            VARCHAR2(4000),
    SELN_MBCR_NO4            VARCHAR2(4000),
    SELN_MBCR_NO5            VARCHAR2(4000),
    SELN_MBCR_NAME1          VARCHAR2(4000),
    SELN_MBCR_NAME2          VARCHAR2(4000),
    SELN_MBCR_NAME3          VARCHAR2(4000),
    SELN_MBCR_NAME4          VARCHAR2(4000),
    SELN_MBCR_NAME5          VARCHAR2(4000),
    TOTAL_SELN_QTY1          VARCHAR2(4000),
    TOTAL_SELN_QTY2          VARCHAR2(4000),
    TOTAL_SELN_QTY3          VARCHAR2(4000),
    TOTAL_SELN_QTY4          VARCHAR2(4000),
    TOTAL_SELN_QTY5          VARCHAR2(4000),
    SELN_MBCR_RLIM1          VARCHAR2(4000),
    SELN_MBCR_RLIM2          VARCHAR2(4000),
    SELN_MBCR_RLIM3          VARCHAR2(4000),
    SELN_MBCR_RLIM4          VARCHAR2(4000),
    SELN_MBCR_RLIM5          VARCHAR2(4000),
    SELN_QTY_ICDC1           VARCHAR2(4000),
    SELN_QTY_ICDC2           VARCHAR2(4000),
    SELN_QTY_ICDC3           VARCHAR2(4000),
    SELN_QTY_ICDC4           VARCHAR2(4000),
    SELN_QTY_ICDC5           VARCHAR2(4000),
    SHNU_MBCR_NO1            VARCHAR2(4000),
    SHNU_MBCR_NO2            VARCHAR2(4000),
    SHNU_MBCR_NO3            VARCHAR2(4000),
    SHNU_MBCR_NO4            VARCHAR2(4000),
    SHNU_MBCR_NO5            VARCHAR2(4000),
    SHNU_MBCR_NAME1          VARCHAR2(4000),
    SHNU_MBCR_NAME2          VARCHAR2(4000),
    SHNU_MBCR_NAME3          VARCHAR2(4000),
    SHNU_MBCR_NAME4          VARCHAR2(4000),
    SHNU_MBCR_NAME5          VARCHAR2(4000),
    TOTAL_SHNU_QTY1          VARCHAR2(4000),
    TOTAL_SHNU_QTY2          VARCHAR2(4000),
    TOTAL_SHNU_QTY3          VARCHAR2(4000),
    TOTAL_SHNU_QTY4          VARCHAR2(4000),
    TOTAL_SHNU_QTY5          VARCHAR2(4000),
    SHNU_MBCR_RLIM1          VARCHAR2(4000),
    SHNU_MBCR_RLIM2          VARCHAR2(4000),
    SHNU_MBCR_RLIM3          VARCHAR2(4000),
    SHNU_MBCR_RLIM4          VARCHAR2(4000),
    SHNU_MBCR_RLIM5          VARCHAR2(4000),
    SHNU_QTY_ICDC1           VARCHAR2(4000),
    SHNU_QTY_ICDC2           VARCHAR2(4000),
    SHNU_QTY_ICDC3           VARCHAR2(4000),
    SHNU_QTY_ICDC4           VARCHAR2(4000),
    SHNU_QTY_ICDC5           VARCHAR2(4000),
    GLOB_TOTAL_SELN_QTY      VARCHAR2(4000),
    GLOB_SELN_RLIM           VARCHAR2(4000),
    GLOB_NTBY_QTY            VARCHAR2(4000),
    GLOB_TOTAL_SHNU_QTY      VARCHAR2(4000),
    GLOB_SHNU_RLIM           VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_1      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_2      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_3      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_4      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_5      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_1      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_2      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_3      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_4      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_5      VARCHAR2(4000),
    GLOB_TOTAL_SELN_QTY_ICDC VARCHAR2(4000),
    GLOB_TOTAL_SHNU_QTY_ICDC VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_INQUIRE_MEMBER_API_NAME
    on INQUIRE_MEMBER (API_NAME)
/

create table INQUIRE_MEMBER_DAILY
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STCK_BSOP_DATE VARCHAR2(4000),
    TOTAL_SELN_QTY VARCHAR2(4000),
    TOTAL_SHNU_QTY VARCHAR2(4000),
    NTBY_QTY       VARCHAR2(4000),
    STCK_PRPR      VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_INQUIRE_MEMBER_DAILY_API_NAME
    on INQUIRE_MEMBER_DAILY (API_NAME)
/

create table INQUIRE_OVERTIME_ASKING_PRICE
(
    ID                             NUMBER         not null
        primary key,
    API_NAME                       VARCHAR2(4000) not null,
    OVTM_UNTP_LAST_HOUR            VARCHAR2(4000),
    OVTM_UNTP_ASKP1                VARCHAR2(4000),
    OVTM_UNTP_ASKP2                VARCHAR2(4000),
    OVTM_UNTP_ASKP3                VARCHAR2(4000),
    OVTM_UNTP_ASKP4                VARCHAR2(4000),
    OVTM_UNTP_ASKP5                VARCHAR2(4000),
    OVTM_UNTP_ASKP6                VARCHAR2(4000),
    OVTM_UNTP_ASKP7                VARCHAR2(4000),
    OVTM_UNTP_ASKP8                VARCHAR2(4000),
    OVTM_UNTP_ASKP9                VARCHAR2(4000),
    OVTM_UNTP_ASKP10               VARCHAR2(4000),
    OVTM_UNTP_BIDP1                VARCHAR2(4000),
    OVTM_UNTP_BIDP2                VARCHAR2(4000),
    OVTM_UNTP_BIDP3                VARCHAR2(4000),
    OVTM_UNTP_BIDP4                VARCHAR2(4000),
    OVTM_UNTP_BIDP5                VARCHAR2(4000),
    OVTM_UNTP_BIDP6                VARCHAR2(4000),
    OVTM_UNTP_BIDP7                VARCHAR2(4000),
    OVTM_UNTP_BIDP8                VARCHAR2(4000),
    OVTM_UNTP_BIDP9                VARCHAR2(4000),
    OVTM_UNTP_BIDP10               VARCHAR2(4000),
    OVTM_UNTP_ASKP_ICDC1           VARCHAR2(4000),
    OVTM_UNTP_ASKP_ICDC2           VARCHAR2(4000),
    OVTM_UNTP_ASKP_ICDC3           VARCHAR2(4000),
    OVTM_UNTP_ASKP_ICDC4           VARCHAR2(4000),
    OVTM_UNTP_ASKP_ICDC5           VARCHAR2(4000),
    OVTM_UNTP_ASKP_ICDC6           VARCHAR2(4000),
    OVTM_UNTP_ASKP_ICDC7           VARCHAR2(4000),
    OVTM_UNTP_ASKP_ICDC8           VARCHAR2(4000),
    OVTM_UNTP_ASKP_ICDC9           VARCHAR2(4000),
    OVTM_UNTP_ASKP_ICDC10          VARCHAR2(4000),
    OVTM_UNTP_BIDP_ICDC1           VARCHAR2(4000),
    OVTM_UNTP_BIDP_ICDC2           VARCHAR2(4000),
    OVTM_UNTP_BIDP_ICDC3           VARCHAR2(4000),
    OVTM_UNTP_BIDP_ICDC4           VARCHAR2(4000),
    OVTM_UNTP_BIDP_ICDC5           VARCHAR2(4000),
    OVTM_UNTP_BIDP_ICDC6           VARCHAR2(4000),
    OVTM_UNTP_BIDP_ICDC7           VARCHAR2(4000),
    OVTM_UNTP_BIDP_ICDC8           VARCHAR2(4000),
    OVTM_UNTP_BIDP_ICDC9           VARCHAR2(4000),
    OVTM_UNTP_BIDP_ICDC10          VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN1           VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN2           VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN3           VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN4           VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN5           VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN6           VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN7           VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN8           VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN9           VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN10          VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN1           VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN            VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN3           VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN4           VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN5           VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN6           VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN7           VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN8           VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN9           VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN10          VARCHAR2(4000),
    OVTM_UNTP_TOTAL_ASKP_RSQN      VARCHAR2(4000),
    OVTM_UNTP_TOTAL_BIDP_RSQN      VARCHAR2(4000),
    OVTM_UNTP_TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    OVTM_UNTP_TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    OVTM_UNTP_NTBY_BIDP_RSQN       VARCHAR2(4000),
    TOTAL_ASKP_RSQN                VARCHAR2(4000),
    TOTAL_BIDP_RSQN                VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC           VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC           VARCHAR2(4000),
    OVTM_TOTAL_ASKP_RSQN           VARCHAR2(4000),
    OVTM_TOTAL_BIDP_RSQN           VARCHAR2(4000),
    OVTM_TOTAL_ASKP_ICDC           VARCHAR2(4000),
    OVTM_TOTAL_BIDP_ICDC           VARCHAR2(4000),
    CREATED_AT                     DATE           not null
)
/

create index IX_INQUIRE_OVERTIME_ASKING_PRICE_API_NAME
    on INQUIRE_OVERTIME_ASKING_PRICE (API_NAME)
/

create table INQUIRE_OVERTIME_PRICE
(
    ID                            NUMBER         not null
        primary key,
    API_NAME                      VARCHAR2(4000) not null,
    BSTP_KOR_ISNM                 VARCHAR2(4000),
    MANG_ISSU_CLS_NAME            VARCHAR2(4000),
    OVTM_UNTP_PRPR                VARCHAR2(4000),
    OVTM_UNTP_PRDY_VRSS           VARCHAR2(4000),
    OVTM_UNTP_PRDY_VRSS_SIGN      VARCHAR2(4000),
    OVTM_UNTP_PRDY_CTRT           VARCHAR2(4000),
    OVTM_UNTP_VOL                 VARCHAR2(4000),
    OVTM_UNTP_TR_PBMN             VARCHAR2(4000),
    OVTM_UNTP_MXPR                VARCHAR2(4000),
    OVTM_UNTP_LLAM                VARCHAR2(4000),
    OVTM_UNTP_OPRC                VARCHAR2(4000),
    OVTM_UNTP_HGPR                VARCHAR2(4000),
    OVTM_UNTP_LWPR                VARCHAR2(4000),
    MARG_RATE                     VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNPR           VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_VRSS      VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_CTRT      VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNQN           VARCHAR2(4000),
    CRDT_ABLE_YN                  VARCHAR2(4000),
    NEW_LSTN_CLS_NAME             VARCHAR2(4000),
    SLTR_YN                       VARCHAR2(4000),
    MANG_ISSU_YN                  VARCHAR2(4000),
    MRKT_WARN_CLS_CODE            VARCHAR2(4000),
    TRHT_YN                       VARCHAR2(4000),
    VLNT_DEAL_CLS_NAME            VARCHAR2(4000),
    OVTM_UNTP_SDPR                VARCHAR2(4000),
    MRKT_WARN_CLS_NAME            VARCHAR2(4000),
    REVL_ISSU_REAS_NAME           VARCHAR2(4000),
    INSN_PBNT_YN                  VARCHAR2(4000),
    FLNG_CLS_NAME                 VARCHAR2(4000),
    RPRS_MRKT_KOR_NAME            VARCHAR2(4000),
    OVTM_VI_CLS_CODE              VARCHAR2(4000),
    BIDP                          VARCHAR2(4000),
    ASKP                          VARCHAR2(4000),
    CREATED_AT                    DATE           not null
)
/

create index IX_INQUIRE_OVERTIME_PRICE_API_NAME
    on INQUIRE_OVERTIME_PRICE (API_NAME)
/

create table INQUIRE_PERIOD_PROFIT
(
    ID                     NUMBER         not null
        primary key,
    API_NAME               VARCHAR2(4000) not null,
    TRAD_DAY               VARCHAR2(4000),
    OVRS_PDNO              VARCHAR2(4000),
    SLCL_QTY               VARCHAR2(4000),
    PCHS_AVG_PRIC          VARCHAR2(4000),
    FRCR_PCHS_AMT1         VARCHAR2(4000),
    AVG_SLL_UNPR           VARCHAR2(4000),
    FRCR_SLL_AMT_SMTL1     VARCHAR2(4000),
    STCK_SLL_TLEX          VARCHAR2(4000),
    OVRS_RLZT_PFLS_AMT     VARCHAR2(4000),
    PFTRT                  VARCHAR2(4000),
    EXRT                   VARCHAR2(4000),
    OVRS_EXCG_CD           VARCHAR2(4000),
    FRST_BLTN_EXRT         VARCHAR2(4000),
    STCK_SLL_AMT_SMTL      VARCHAR2(4000),
    STCK_BUY_AMT_SMTL      VARCHAR2(4000),
    SMTL_FEE1              VARCHAR2(4000),
    EXCC_DFRM_AMT          VARCHAR2(4000),
    OVRS_RLZT_PFLS_TOT_AMT VARCHAR2(4000),
    TOT_PFTRT              VARCHAR2(4000),
    BASS_DT                VARCHAR2(4000),
    CREATED_AT             DATE           not null
)
/

create index IX_INQUIRE_PERIOD_PROFIT_API_NAME
    on INQUIRE_PERIOD_PROFIT (API_NAME)
/

create table INQUIRE_PERIOD_TRADE_PROFIT
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    TRAD_DT           VARCHAR2(4000),
    PDNO              VARCHAR2(4000),
    PRDT_NAME         VARCHAR2(4000),
    TRAD_DVSN_NAME    VARCHAR2(4000),
    LOAN_DT           VARCHAR2(4000),
    HLDG_QTY          VARCHAR2(4000),
    PCHS_UNPR         VARCHAR2(4000),
    BUY_QTY           VARCHAR2(4000),
    BUY_AMT           VARCHAR2(4000),
    SLL_PRIC          VARCHAR2(4000),
    SLL_QTY           VARCHAR2(4000),
    SLL_AMT           VARCHAR2(4000),
    RLZT_PFLS         VARCHAR2(4000),
    PFLS_RT           VARCHAR2(4000),
    FEE               VARCHAR2(4000),
    TL_TAX            VARCHAR2(4000),
    LOAN_INT          VARCHAR2(4000),
    SLL_QTY_SMTL      VARCHAR2(4000),
    SLL_TR_AMT_SMTL   VARCHAR2(4000),
    SLL_FEE_SMTL      VARCHAR2(4000),
    SLL_TLTX_SMTL     VARCHAR2(4000),
    SLL_EXCC_AMT_SMTL VARCHAR2(4000),
    BUYQTY_SMTL       VARCHAR2(4000),
    BUY_TR_AMT_SMTL   VARCHAR2(4000),
    BUY_FEE_SMTL      VARCHAR2(4000),
    BUY_TAX_SMTL      VARCHAR2(4000),
    BUY_EXCC_AMT_SMTL VARCHAR2(4000),
    TOT_QTY           VARCHAR2(4000),
    TOT_TR_AMT        VARCHAR2(4000),
    TOT_FEE           VARCHAR2(4000),
    TOT_TLTX          VARCHAR2(4000),
    TOT_EXCC_AMT      VARCHAR2(4000),
    TOT_RLZT_PFLS     VARCHAR2(4000),
    TOT_PFTRT         VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_INQUIRE_PERIOD_TRADE_PROFIT_API_NAME
    on INQUIRE_PERIOD_TRADE_PROFIT (API_NAME)
/

create table INQUIRE_PRICE_2
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    RPRS_MRKT_KOR_NAME       VARCHAR2(4000),
    NEW_HGPR_LWPR_CLS_CODE   VARCHAR2(4000),
    MXPR_LLAM_CLS_CODE       VARCHAR2(4000),
    CRDT_ABLE_YN             VARCHAR2(4000),
    STCK_MXPR                VARCHAR2(4000),
    ELW_PBLC_YN              VARCHAR2(4000),
    PRDY_CLPR_VRSS_OPRC_RATE VARCHAR2(4000),
    CRDT_RATE                VARCHAR2(4000),
    MARG_RATE                VARCHAR2(4000),
    LWPR_VRSS_PRPR           VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN      VARCHAR2(4000),
    PRDY_CLPR_VRSS_LWPR_RATE VARCHAR2(4000),
    STCK_LWPR                VARCHAR2(4000),
    HGPR_VRSS_PRPR           VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN      VARCHAR2(4000),
    PRDY_CLPR_VRSS_HGPR_RATE VARCHAR2(4000),
    STCK_HGPR                VARCHAR2(4000),
    OPRC_VRSS_PRPR           VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN      VARCHAR2(4000),
    MANG_ISSU_YN             VARCHAR2(4000),
    DIVI_APP_CLS_CODE        VARCHAR2(4000),
    SHORT_OVER_YN            VARCHAR2(4000),
    MRKT_WARN_CLS_CODE       VARCHAR2(4000),
    INVT_CAFUL_YN            VARCHAR2(4000),
    STANGE_RUNUP_YN          VARCHAR2(4000),
    SSTS_HOT_YN              VARCHAR2(4000),
    LOW_CURRENT_YN           VARCHAR2(4000),
    VI_CLS_CODE              VARCHAR2(4000),
    SHORT_OVER_CLS_CODE      VARCHAR2(4000),
    STCK_LLAM                VARCHAR2(4000),
    NEW_LSTN_CLS_NAME        VARCHAR2(4000),
    VLNT_DEAL_CLS_NAME       VARCHAR2(4000),
    FLNG_CLS_NAME            VARCHAR2(4000),
    REVL_ISSU_REAS_NAME      VARCHAR2(4000),
    MRKT_WARN_CLS_NAME       VARCHAR2(4000),
    STCK_SDPR                VARCHAR2(4000),
    BSTP_CLS_CODE            VARCHAR2(4000),
    STCK_PRDY_CLPR           VARCHAR2(4000),
    INSN_PBNT_YN             VARCHAR2(4000),
    FCAM_MOD_CLS_NAME        VARCHAR2(4000),
    STCK_PRPR                VARCHAR2(4000),
    PRDY_VRSS                VARCHAR2(4000),
    PRDY_VRSS_SIGN           VARCHAR2(4000),
    PRDY_CTRT                VARCHAR2(4000),
    ACML_TR_PBMN             VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    PRDY_VRSS_VOL_RATE       VARCHAR2(4000),
    BSTP_KOR_ISNM            VARCHAR2(4000),
    SLTR_YN                  VARCHAR2(4000),
    TRHT_YN                  VARCHAR2(4000),
    OPRC_RANG_CONT_YN        VARCHAR2(4000),
    VLNT_FIN_CLS_CODE        VARCHAR2(4000),
    STCK_OPRC                VARCHAR2(4000),
    PRDY_VOL                 VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_INQUIRE_PRICE_2_API_NAME
    on INQUIRE_PRICE_2 (API_NAME)
/

create table INQUIRE_PSBL_SELL
(
    ID            NUMBER         not null
        primary key,
    API_NAME      VARCHAR2(4000) not null,
    PDNO          VARCHAR2(4000),
    BUY_QTY       VARCHAR2(4000),
    SLL_QTY       VARCHAR2(4000),
    CBLC_QTY      VARCHAR2(4000),
    NSVG_QTY      VARCHAR2(4000),
    ORD_PSBL_QTY  VARCHAR2(4000),
    PCHS_AVG_PRIC VARCHAR2(4000),
    PCHS_AMT      VARCHAR2(4000),
    NOW_PRIC      VARCHAR2(4000),
    EVLU_AMT      VARCHAR2(4000),
    EVLU_PFLS_AMT VARCHAR2(4000),
    EVLU_PFLS_RT  VARCHAR2(4000),
    CREATED_AT    DATE           not null
)
/

create index IX_INQUIRE_PSBL_SELL_API_NAME
    on INQUIRE_PSBL_SELL (API_NAME)
/

create table INQUIRE_TIME_DAILYCHARTPRICE
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    STCK_PRDY_CLPR VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    ACML_TR_PBMN   VARCHAR2(4000),
    HTS_KOR_ISNM   VARCHAR2(4000),
    STCK_PRPR      VARCHAR2(4000),
    STCK_BSOP_DATE VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    STCK_OPRC      VARCHAR2(4000),
    STCK_HGPR      VARCHAR2(4000),
    STCK_LWPR      VARCHAR2(4000),
    CNTG_VOL       VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_INQUIRE_TIME_DAILYCHARTPRICE_API_NAME
    on INQUIRE_TIME_DAILYCHARTPRICE (API_NAME)
/

create table INQUIRE_TIME_INDEXCHARTPRICE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    OVRS_NMIX_PRDY_VRSS VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    OVRS_NMIX_PRDY_CLPR VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    OVRS_NMIX_PRPR      VARCHAR2(4000),
    STCK_SHRN_ISCD      VARCHAR2(4000),
    OVRS_PROD_OPRC      VARCHAR2(4000),
    OVRS_PROD_HGPR      VARCHAR2(4000),
    OVRS_PROD_LWPR      VARCHAR2(4000),
    STCK_BSOP_DATE      VARCHAR2(4000),
    STCK_CNTG_HOUR      VARCHAR2(4000),
    OPTN_PRPR           VARCHAR2(4000),
    OPTN_OPRC           VARCHAR2(4000),
    OPTN_HGPR           VARCHAR2(4000),
    OPTN_LWPR           VARCHAR2(4000),
    CNTG_VOL            VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_INQUIRE_TIME_INDEXCHARTPRICE_API_NAME
    on INQUIRE_TIME_INDEXCHARTPRICE (API_NAME)
/

create table INQUIRE_TIME_ITEMCHARTPRICE
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    RSYM       VARCHAR2(4000),
    ZDIV       VARCHAR2(4000),
    STIM       VARCHAR2(4000),
    ETIM       VARCHAR2(4000),
    SKTM       VARCHAR2(4000),
    EKTM       VARCHAR2(4000),
    NEXT       VARCHAR2(4000),
    MORE       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    TYMD       VARCHAR2(4000),
    XYMD       VARCHAR2(4000),
    XHMS       VARCHAR2(4000),
    KYMD       VARCHAR2(4000),
    KHMS       VARCHAR2(4000),
    OPEN       VARCHAR2(4000),
    HIGH       VARCHAR2(4000),
    LOW        VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    EVOL       VARCHAR2(4000),
    EAMT       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_INQUIRE_TIME_ITEMCHARTPRICE_API_NAME
    on INQUIRE_TIME_ITEMCHARTPRICE (API_NAME)
/

create table INQUIRE_TIME_ITEMCONCLUSION
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    STCK_PRPR          VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    PRDY_VOL           VARCHAR2(4000),
    RPRS_MRKT_KOR_NAME VARCHAR2(4000),
    STCK_CNTG_HOUR     VARCHAR2(4000),
    STCK_PBPR          VARCHAR2(4000),
    ASKP               VARCHAR2(4000),
    BIDP               VARCHAR2(4000),
    TDAY_RLTV          VARCHAR2(4000),
    CNQN               VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_INQUIRE_TIME_ITEMCONCLUSION_API_NAME
    on INQUIRE_TIME_ITEMCONCLUSION (API_NAME)
/

create table INQUIRE_TIME_OVERTIMECONCLUSION
(
    ID                            NUMBER         not null
        primary key,
    API_NAME                      VARCHAR2(4000) not null,
    OVTM_UNTP_PRPR                VARCHAR2(4000),
    OVTM_UNTP_PRDY_VRSS           VARCHAR2(4000),
    OVTM_UNTP_PRDY_VRSS_SIGN      VARCHAR2(4000),
    OVTM_UNTP_PRDY_CTRT           VARCHAR2(4000),
    OVTM_UNTP_VOL                 VARCHAR2(4000),
    OVTM_UNTP_TR_PBMN             VARCHAR2(4000),
    OVTM_UNTP_MXPR                VARCHAR2(4000),
    OVTM_UNTP_LLAM                VARCHAR2(4000),
    OVTM_UNTP_OPRC                VARCHAR2(4000),
    OVTM_UNTP_HGPR                VARCHAR2(4000),
    OVTM_UNTP_LWPR                VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNPR           VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_VRSS      VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_CTRT      VARCHAR2(4000),
    OVTM_UNTP_ANTC_VOL            VARCHAR2(4000),
    UPLM_SIGN                     VARCHAR2(4000),
    LSLM_SIGN                     VARCHAR2(4000),
    STCK_CNTG_HOUR                VARCHAR2(4000),
    STCK_PRPR                     VARCHAR2(4000),
    PRDY_VRSS                     VARCHAR2(4000),
    PRDY_VRSS_SIGN                VARCHAR2(4000),
    PRDY_CTRT                     VARCHAR2(4000),
    ASKP                          VARCHAR2(4000),
    BIDP                          VARCHAR2(4000),
    ACML_VOL                      VARCHAR2(4000),
    CNTG_VOL                      VARCHAR2(4000),
    CREATED_AT                    DATE           not null
)
/

create index IX_INQUIRE_TIME_OVERTIMECONCLUSION_API_NAME
    on INQUIRE_TIME_OVERTIMECONCLUSION (API_NAME)
/

create table INQUIRE_VI_STATUS
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    "Output1"       VARCHAR2(4000),
    HTS_KOR_ISNM    VARCHAR2(4000),
    MKSC_SHRN_ISCD  VARCHAR2(4000),
    VI_CLS_CODE     VARCHAR2(4000),
    BSOP_DATE       VARCHAR2(4000),
    CNTG_VI_HOUR    VARCHAR2(4000),
    VI_CNCL_HOUR    VARCHAR2(4000),
    VI_KIND_CODE    VARCHAR2(4000),
    VI_PRC          VARCHAR2(4000),
    VI_STND_PRC     VARCHAR2(4000),
    VI_DPRT         VARCHAR2(4000),
    VI_DMC_STND_PRC VARCHAR2(4000),
    VI_DMC_DPRT     VARCHAR2(4000),
    VI_COUNT        VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_INQUIRE_VI_STATUS_API_NAME
    on INQUIRE_VI_STATUS (API_NAME)
/

create table INTGR_MARGIN
(
    ID                             NUMBER         not null
        primary key,
    API_NAME                       VARCHAR2(4000) not null,
    ACMGA_RT                       VARCHAR2(4000),
    ACMGA_PCT100_APTM_RSON         VARCHAR2(4000),
    STCK_CASH_OBJT_AMT             VARCHAR2(4000),
    STCK_SBST_OBJT_AMT             VARCHAR2(4000),
    STCK_EVLU_OBJT_AMT             VARCHAR2(4000),
    STCK_RUSE_PSBL_OBJT_AMT        VARCHAR2(4000),
    STCK_FUND_RPCH_CHGS_OBJT_AMT   VARCHAR2(4000),
    STCK_FNCG_RDPT_OBJT_ATM        VARCHAR2(4000),
    BOND_RUSE_PSBL_OBJT_AMT        VARCHAR2(4000),
    STCK_CASH_USE_AMT              VARCHAR2(4000),
    STCK_SBST_USE_AMT              VARCHAR2(4000),
    STCK_EVLU_USE_AMT              VARCHAR2(4000),
    STCK_RUSE_PSBL_AMT_USE_AMT     VARCHAR2(4000),
    STCK_FUND_RPCH_CHGS_USE_AMT    VARCHAR2(4000),
    STCK_FNCG_RDPT_AMT_USE_AMT     VARCHAR2(4000),
    BOND_RUSE_PSBL_AMT_USE_AMT     VARCHAR2(4000),
    STCK_CASH_ORD_PSBL_AMT         VARCHAR2(4000),
    STCK_SBST_ORD_PSBL_AMT         VARCHAR2(4000),
    STCK_EVLU_ORD_PSBL_AMT         VARCHAR2(4000),
    STCK_RUSE_PSBL_ORD_PSBL_AMT    VARCHAR2(4000),
    STCK_FUND_RPCH_ORD_PSBL_AMT    VARCHAR2(4000),
    BOND_RUSE_PSBL_ORD_PSBL_AMT    VARCHAR2(4000),
    RCVB_AMT                       VARCHAR2(4000),
    STCK_LOAN_GRTA_RUSE_PSBL_AMT   VARCHAR2(4000),
    STCK_CASH20_MAX_ORD_PSBL_AMT   VARCHAR2(4000),
    STCK_CASH30_MAX_ORD_PSBL_AMT   VARCHAR2(4000),
    STCK_CASH40_MAX_ORD_PSBL_AMT   VARCHAR2(4000),
    STCK_CASH50_MAX_ORD_PSBL_AMT   VARCHAR2(4000),
    STCK_CASH60_MAX_ORD_PSBL_AMT   VARCHAR2(4000),
    STCK_CASH100_MAX_ORD_PSBL_AMT  VARCHAR2(4000),
    STCK_RSIP100_MAX_ORD_PSBL_AMT  VARCHAR2(4000),
    BOND_MAX_ORD_PSBL_AMT          VARCHAR2(4000),
    STCK_FNCG45_MAX_ORD_PSBL_AMT   VARCHAR2(4000),
    STCK_FNCG50_MAX_ORD_PSBL_AMT   VARCHAR2(4000),
    STCK_FNCG60_MAX_ORD_PSBL_AMT   VARCHAR2(4000),
    STCK_FNCG70_MAX_ORD_PSBL_AMT   VARCHAR2(4000),
    STCK_STLN_MAX_ORD_PSBL_AMT     VARCHAR2(4000),
    LMT_AMT                        VARCHAR2(4000),
    OVRS_STCK_ITGR_MGNA_DVSN_NAME  VARCHAR2(4000),
    USD_OBJT_AMT                   VARCHAR2(4000),
    USD_USE_AMT                    VARCHAR2(4000),
    USD_ORD_PSBL_AMT               VARCHAR2(4000),
    HKD_OBJT_AMT                   VARCHAR2(4000),
    HKD_USE_AMT                    VARCHAR2(4000),
    HKD_ORD_PSBL_AMT               VARCHAR2(4000),
    JPY_OBJT_AMT                   VARCHAR2(4000),
    JPY_USE_AMT                    VARCHAR2(4000),
    JPY_ORD_PSBL_AMT               VARCHAR2(4000),
    CNY_OBJT_AMT                   VARCHAR2(4000),
    CNY_USE_AMT                    VARCHAR2(4000),
    CNY_ORD_PSBL_AMT               VARCHAR2(4000),
    USD_RUSE_OBJT_AMT              VARCHAR2(4000),
    USD_RUSE_AMT                   VARCHAR2(4000),
    USD_RUSE_ORD_PSBL_AMT          VARCHAR2(4000),
    HKD_RUSE_OBJT_AMT              VARCHAR2(4000),
    HKD_RUSE_AMT                   VARCHAR2(4000),
    HKD_RUSE_ORD_PSBL_AMT          VARCHAR2(4000),
    JPY_RUSE_OBJT_AMT              VARCHAR2(4000),
    JPY_RUSE_AMT                   VARCHAR2(4000),
    JPY_RUSE_ORD_PSBL_AMT          VARCHAR2(4000),
    CNY_RUSE_OBJT_AMT              VARCHAR2(4000),
    CNY_RUSE_AMT                   VARCHAR2(4000),
    CNY_RUSE_ORD_PSBL_AMT          VARCHAR2(4000),
    USD_GNRL_ORD_PSBL_AMT          VARCHAR2(4000),
    USD_ITGR_ORD_PSBL_AMT          VARCHAR2(4000),
    HKD_GNRL_ORD_PSBL_AMT          VARCHAR2(4000),
    HKD_ITGR_ORD_PSBL_AMT          VARCHAR2(4000),
    JPY_GNRL_ORD_PSBL_AMT          VARCHAR2(4000),
    JPY_ITGR_ORD_PSBL_AMT          VARCHAR2(4000),
    CNY_GNRL_ORD_PSBL_AMT          VARCHAR2(4000),
    CNY_ITGR_ORD_PSBL_AMT          VARCHAR2(4000),
    STCK_ITGR_CASH20_ORD_PSBL_AMT  VARCHAR2(4000),
    STCK_ITGR_CASH30_ORD_PSBL_AMT  VARCHAR2(4000),
    STCK_ITGR_CASH40_ORD_PSBL_AMT  VARCHAR2(4000),
    STCK_ITGR_CASH50_ORD_PSBL_AMT  VARCHAR2(4000),
    STCK_ITGR_CASH60_ORD_PSBL_AMT  VARCHAR2(4000),
    STCK_ITGR_CASH100_ORD_PSBL_AMT VARCHAR2(4000),
    STCK_ITGR_100_ORD_PSBL_AMT     VARCHAR2(4000),
    STCK_ITGR_FNCG45_ORD_PSBL_AMT  VARCHAR2(4000),
    STCK_ITGR_FNCG50_ORD_PSBL_AMT  VARCHAR2(4000),
    STCK_ITGR_FNCG60_ORD_PSBL_AMT  VARCHAR2(4000),
    STCK_ITGR_FNCG70_ORD_PSBL_AMT  VARCHAR2(4000),
    STCK_ITGR_STLN_ORD_PSBL_AMT    VARCHAR2(4000),
    BOND_ITGR_ORD_PSBL_AMT         VARCHAR2(4000),
    STCK_CASH_OVRS_USE_AMT         VARCHAR2(4000),
    STCK_SBST_OVRS_USE_AMT         VARCHAR2(4000),
    STCK_EVLU_OVRS_USE_AMT         VARCHAR2(4000),
    STCK_RE_USE_AMT_OVRS_USE_AMT   VARCHAR2(4000),
    STCK_FUND_RPCH_OVRS_USE_AMT    VARCHAR2(4000),
    STCK_FNCG_RDPT_OVRS_USE_AMT    VARCHAR2(4000),
    BOND_RE_USE_OVRS_USE_AMT       VARCHAR2(4000),
    USD_OTH_MKET_USE_AMT           VARCHAR2(4000),
    JPY_OTH_MKET_USE_AMT           VARCHAR2(4000),
    CNY_OTH_MKET_USE_AMT           VARCHAR2(4000),
    HKD_OTH_MKET_USE_AMT           VARCHAR2(4000),
    USD_RE_USE_OTH_MKET_USE_AMT    VARCHAR2(4000),
    JPY_RE_USE_OTH_MKET_USE_AMT    VARCHAR2(4000),
    CNY_RE_USE_OTH_MKET_USE_AMT    VARCHAR2(4000),
    HKD_RE_USE_OTH_MKET_USE_AMT    VARCHAR2(4000),
    HGKG_CNY_RE_USE_AMT            VARCHAR2(4000),
    USD_FRST_BLTN_EXRT             VARCHAR2(4000),
    HKD_FRST_BLTN_EXRT             VARCHAR2(4000),
    JPY_FRST_BLTN_EXRT             VARCHAR2(4000),
    CNY_FRST_BLTN_EXRT             VARCHAR2(4000),
    CREATED_AT                     DATE           not null
)
/

create index IX_INTGR_MARGIN_API_NAME
    on INTGR_MARGIN (API_NAME)
/

create table INTSTOCK_GROUPLIST
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    "date"         VARCHAR2(4000),
    TRNM_HOUR      VARCHAR2(4000),
    DATA_RANK      VARCHAR2(4000),
    INTER_GRP_CODE VARCHAR2(4000),
    INTER_GRP_NAME VARCHAR2(4000),
    ASK_CNT        VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_INTSTOCK_GROUPLIST_API_NAME
    on INTSTOCK_GROUPLIST (API_NAME)
/

create table INTSTOCK_MULTPRICE
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    KOSPI_KOSDAQ_CLS_NAME    VARCHAR2(4000),
    MRKT_TRTM_CLS_NAME       VARCHAR2(4000),
    HOUR_CLS_CODE            VARCHAR2(4000),
    INTER_SHRN_ISCD          VARCHAR2(4000),
    INTER_KOR_ISNM           VARCHAR2(4000),
    INTER2_PRPR              VARCHAR2(4000),
    INTER2_PRDY_VRSS         VARCHAR2(4000),
    PRDY_VRSS_SIGN           VARCHAR2(4000),
    PRDY_CTRT                VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    INTER2_OPRC              VARCHAR2(4000),
    INTER2_HGPR              VARCHAR2(4000),
    INTER2_LWPR              VARCHAR2(4000),
    INTER2_LLAM              VARCHAR2(4000),
    INTER2_MXPR              VARCHAR2(4000),
    INTER2_ASKP              VARCHAR2(4000),
    INTER2_BIDP              VARCHAR2(4000),
    SELN_RSQN                VARCHAR2(4000),
    SHNU_RSQN                VARCHAR2(4000),
    TOTAL_ASKP_RSQN          VARCHAR2(4000),
    TOTAL_BIDP_RSQN          VARCHAR2(4000),
    ACML_TR_PBMN             VARCHAR2(4000),
    INTER2_PRDY_CLPR         VARCHAR2(4000),
    OPRC_VRSS_HGPR_RATE      VARCHAR2(4000),
    INTR_ANTC_CNTG_VRSS      VARCHAR2(4000),
    INTR_ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    INTR_ANTC_CNTG_PRDY_CTRT VARCHAR2(4000),
    INTR_ANTC_VOL            VARCHAR2(4000),
    INTER2_SDPR              VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_INTSTOCK_MULTPRICE_API_NAME
    on INTSTOCK_MULTPRICE (API_NAME)
/

create table INTSTOCK_STOCKLIST_BY_GROUP
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    FID_MRKT_CLS_CODE VARCHAR2(4000),
    DATA_RANK         VARCHAR2(4000),
    EXCH_CODE         VARCHAR2(4000),
    JONG_CODE         VARCHAR2(4000),
    COLOR_CODE        VARCHAR2(4000),
    MEMO              VARCHAR2(4000),
    HTS_KOR_ISNM      VARCHAR2(4000),
    FXDT_NTBY_QTY     VARCHAR2(4000),
    CNTG_UNPR         VARCHAR2(4000),
    CNTG_CLS_CODE     VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_INTSTOCK_STOCKLIST_BY_GROUP_API_NAME
    on INTSTOCK_STOCKLIST_BY_GROUP (API_NAME)
/

create table INVESTOR_PROGRAM_TRADE_TODAY
(
    ID            NUMBER         not null
        primary key,
    API_NAME      VARCHAR2(4000) not null,
    INVR_CLS_CODE VARCHAR2(4000),
    ALL_SELN_QTY  VARCHAR2(4000),
    ALL_SELN_AMT  VARCHAR2(4000),
    INVR_CLS_NAME VARCHAR2(4000),
    ALL_SHNU_QTY  VARCHAR2(4000),
    ALL_SHNU_AMT  VARCHAR2(4000),
    ALL_NTBY_AMT  VARCHAR2(4000),
    ARBT_SELN_QTY VARCHAR2(4000),
    ALL_NTBY_QTY  VARCHAR2(4000),
    ARBT_SHNU_QTY VARCHAR2(4000),
    ARBT_NTBY_QTY VARCHAR2(4000),
    ARBT_SELN_AMT VARCHAR2(4000),
    ARBT_SHNU_AMT VARCHAR2(4000),
    ARBT_NTBY_AMT VARCHAR2(4000),
    NABT_SELN_QTY VARCHAR2(4000),
    NABT_SHNU_QTY VARCHAR2(4000),
    NABT_NTBY_QTY VARCHAR2(4000),
    NABT_SELN_AMT VARCHAR2(4000),
    NABT_SHNU_AMT VARCHAR2(4000),
    NABT_NTBY_AMT VARCHAR2(4000),
    CREATED_AT    DATE           not null
)
/

create index IX_INVESTOR_PROGRAM_TRADE_TODAY_API_NAME
    on INVESTOR_PROGRAM_TRADE_TODAY (API_NAME)
/

create table INVESTOR_TRADE_BY_STOCK_DAILY
(
    ID                    NUMBER         not null
        primary key,
    API_NAME              VARCHAR2(4000) not null,
    STCK_PRPR             VARCHAR2(4000),
    PRDY_VRSS             VARCHAR2(4000),
    PRDY_VRSS_SIGN        VARCHAR2(4000),
    PRDY_CTRT             VARCHAR2(4000),
    ACML_VOL              VARCHAR2(4000),
    PRDY_VOL              VARCHAR2(4000),
    RPRS_MRKT_KOR_NAME    VARCHAR2(4000),
    STCK_BSOP_DATE        VARCHAR2(4000),
    STCK_CLPR             VARCHAR2(4000),
    ACML_TR_PBMN          VARCHAR2(4000),
    STCK_OPRC             VARCHAR2(4000),
    STCK_HGPR             VARCHAR2(4000),
    STCK_LWPR             VARCHAR2(4000),
    FRGN_NTBY_QTY         VARCHAR2(4000),
    FRGN_REG_NTBY_QTY     VARCHAR2(4000),
    FRGN_NREG_NTBY_QTY    VARCHAR2(4000),
    PRSN_NTBY_QTY         VARCHAR2(4000),
    ORGN_NTBY_QTY         VARCHAR2(4000),
    SCRT_NTBY_QTY         VARCHAR2(4000),
    IVTR_NTBY_QTY         VARCHAR2(4000),
    PE_FUND_NTBY_VOL      VARCHAR2(4000),
    BANK_NTBY_QTY         VARCHAR2(4000),
    INSU_NTBY_QTY         VARCHAR2(4000),
    MRBN_NTBY_QTY         VARCHAR2(4000),
    FUND_NTBY_QTY         VARCHAR2(4000),
    ETC_NTBY_QTY          VARCHAR2(4000),
    ETC_CORP_NTBY_VOL     VARCHAR2(4000),
    ETC_ORGT_NTBY_VOL     VARCHAR2(4000),
    FRGN_REG_NTBY_PBMN    VARCHAR2(4000),
    FRGN_NTBY_TR_PBMN     VARCHAR2(4000),
    FRGN_NREG_NTBY_PBMN   VARCHAR2(4000),
    PRSN_NTBY_TR_PBMN     VARCHAR2(4000),
    ORGN_NTBY_TR_PBMN     VARCHAR2(4000),
    SCRT_NTBY_TR_PBMN     VARCHAR2(4000),
    PE_FUND_NTBY_TR_PBMN  VARCHAR2(4000),
    IVTR_NTBY_TR_PBMN     VARCHAR2(4000),
    BANK_NTBY_TR_PBMN     VARCHAR2(4000),
    INSU_NTBY_TR_PBMN     VARCHAR2(4000),
    MRBN_NTBY_TR_PBMN     VARCHAR2(4000),
    FUND_NTBY_TR_PBMN     VARCHAR2(4000),
    ETC_NTBY_TR_PBMN      VARCHAR2(4000),
    ETC_CORP_NTBY_TR_PBMN VARCHAR2(4000),
    ETC_ORGT_NTBY_TR_PBMN VARCHAR2(4000),
    FRGN_SELN_VOL         VARCHAR2(4000),
    FRGN_SHNU_VOL         VARCHAR2(4000),
    FRGN_SELN_TR_PBMN     VARCHAR2(4000),
    FRGN_SHNU_TR_PBMN     VARCHAR2(4000),
    FRGN_REG_ASKP_QTY     VARCHAR2(4000),
    FRGN_REG_BIDP_QTY     VARCHAR2(4000),
    FRGN_REG_ASKP_PBMN    VARCHAR2(4000),
    FRGN_REG_BIDP_PBMN    VARCHAR2(4000),
    FRGN_NREG_ASKP_QTY    VARCHAR2(4000),
    FRGN_NREG_BIDP_QTY    VARCHAR2(4000),
    FRGN_NREG_ASKP_PBMN   VARCHAR2(4000),
    FRGN_NREG_BIDP_PBMN   VARCHAR2(4000),
    PRSN_SELN_VOL         VARCHAR2(4000),
    PRSN_SHNU_VOL         VARCHAR2(4000),
    PRSN_SELN_TR_PBMN     VARCHAR2(4000),
    PRSN_SHNU_TR_PBMN     VARCHAR2(4000),
    ORGN_SELN_VOL         VARCHAR2(4000),
    ORGN_SHNU_VOL         VARCHAR2(4000),
    ORGN_SELN_TR_PBMN     VARCHAR2(4000),
    ORGN_SHNU_TR_PBMN     VARCHAR2(4000),
    SCRT_SELN_VOL         VARCHAR2(4000),
    SCRT_SHNU_VOL         VARCHAR2(4000),
    SCRT_SELN_TR_PBMN     VARCHAR2(4000),
    SCRT_SHNU_TR_PBMN     VARCHAR2(4000),
    IVTR_SELN_VOL         VARCHAR2(4000),
    IVTR_SHNU_VOL         VARCHAR2(4000),
    IVTR_SELN_TR_PBMN     VARCHAR2(4000),
    IVTR_SHNU_TR_PBMN     VARCHAR2(4000),
    PE_FUND_SELN_TR_PBMN  VARCHAR2(4000),
    PE_FUND_SELN_VOL      VARCHAR2(4000),
    PE_FUND_SHNU_TR_PBMN  VARCHAR2(4000),
    PE_FUND_SHNU_VOL      VARCHAR2(4000),
    BANK_SELN_VOL         VARCHAR2(4000),
    BANK_SHNU_VOL         VARCHAR2(4000),
    BANK_SELN_TR_PBMN     VARCHAR2(4000),
    BANK_SHNU_TR_PBMN     VARCHAR2(4000),
    INSU_SELN_VOL         VARCHAR2(4000),
    INSU_SHNU_VOL         VARCHAR2(4000),
    INSU_SELN_TR_PBMN     VARCHAR2(4000),
    INSU_SHNU_TR_PBMN     VARCHAR2(4000),
    MRBN_SELN_VOL         VARCHAR2(4000),
    MRBN_SHNU_VOL         VARCHAR2(4000),
    MRBN_SELN_TR_PBMN     VARCHAR2(4000),
    MRBN_SHNU_TR_PBMN     VARCHAR2(4000),
    FUND_SELN_VOL         VARCHAR2(4000),
    FUND_SHNU_VOL         VARCHAR2(4000),
    FUND_SELN_TR_PBMN     VARCHAR2(4000),
    FUND_SHNU_TR_PBMN     VARCHAR2(4000),
    ETC_SELN_VOL          VARCHAR2(4000),
    ETC_SHNU_VOL          VARCHAR2(4000),
    ETC_SELN_TR_PBMN      VARCHAR2(4000),
    ETC_SHNU_TR_PBMN      VARCHAR2(4000),
    ETC_ORGT_SELN_VOL     VARCHAR2(4000),
    ETC_ORGT_SHNU_VOL     VARCHAR2(4000),
    ETC_ORGT_SELN_TR_PBMN VARCHAR2(4000),
    ETC_ORGT_SHNU_TR_PBMN VARCHAR2(4000),
    ETC_CORP_SELN_VOL     VARCHAR2(4000),
    ETC_CORP_SHNU_VOL     VARCHAR2(4000),
    ETC_CORP_SELN_TR_PBMN VARCHAR2(4000),
    ETC_CORP_SHNU_TR_PBMN VARCHAR2(4000),
    BOLD_YN               VARCHAR2(4000),
    CREATED_AT            DATE           not null
)
/

create index IX_INVESTOR_TRADE_BY_STOCK_DAILY_API_NAME
    on INVESTOR_TRADE_BY_STOCK_DAILY (API_NAME)
/

create table INVESTOR_TREND_ESTIMATE
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    BSOP_HOUR_GB       VARCHAR2(4000),
    FRGN_FAKE_NTBY_QTY VARCHAR2(4000),
    ORGN_FAKE_NTBY_QTY VARCHAR2(4000),
    SUM_FAKE_NTBY_QTY  VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_INVESTOR_TREND_ESTIMATE_API_NAME
    on INVESTOR_TREND_ESTIMATE (API_NAME)
/

create table INVEST_OPBYSEC
(
    ID                      NUMBER         not null
        primary key,
    API_NAME                VARCHAR2(4000) not null,
    STCK_BSOP_DATE          VARCHAR2(4000),
    STCK_SHRN_ISCD          VARCHAR2(4000),
    HTS_KOR_ISNM            VARCHAR2(4000),
    INVT_OPNN               VARCHAR2(4000),
    INVT_OPNN_CLS_CODE      VARCHAR2(4000),
    RGBF_INVT_OPNN          VARCHAR2(4000),
    RGBF_INVT_OPNN_CLS_CODE VARCHAR2(4000),
    STCK_PRPR               VARCHAR2(4000),
    PRDY_VRSS               VARCHAR2(4000),
    PRDY_VRSS_SIGN          VARCHAR2(4000),
    PRDY_CTRT               VARCHAR2(4000),
    HTS_GOAL_PRC            VARCHAR2(4000),
    STCK_PRDY_CLPR          VARCHAR2(4000),
    STFT_ESDG               VARCHAR2(4000),
    DPRT                    VARCHAR2(4000),
    CREATED_AT              DATE           not null
)
/

create index IX_INVEST_OPBYSEC_API_NAME
    on INVEST_OPBYSEC (API_NAME)
/

create table INVEST_OPINION
(
    ID                      NUMBER         not null
        primary key,
    API_NAME                VARCHAR2(4000) not null,
    STCK_BSOP_DATE          VARCHAR2(4000),
    INVT_OPNN               VARCHAR2(4000),
    INVT_OPNN_CLS_CODE      VARCHAR2(4000),
    RGBF_INVT_OPNN          VARCHAR2(4000),
    RGBF_INVT_OPNN_CLS_CODE VARCHAR2(4000),
    HTS_GOAL_PRC            VARCHAR2(4000),
    STCK_PRDY_CLPR          VARCHAR2(4000),
    STCK_NDAY_ESDG          VARCHAR2(4000),
    NDAY_DPRT               VARCHAR2(4000),
    STFT_ESDG               VARCHAR2(4000),
    DPRT                    VARCHAR2(4000),
    CREATED_AT              DATE           not null
)
/

create index IX_INVEST_OPINION_API_NAME
    on INVEST_OPINION (API_NAME)
/

create table KSDINFO_BONUS_ISSUE
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    RECORD_DATE       VARCHAR2(4000),
    SHT_CD            VARCHAR2(4000),
    FIX_RATE          VARCHAR2(4000),
    ODD_REC_PRICE     VARCHAR2(4000),
    RIGHT_DT          VARCHAR2(4000),
    ODD_PAY_DT        VARCHAR2(4000),
    LIST_DATE         VARCHAR2(4000),
    TOT_ISSUE_STK_QTY VARCHAR2(4000),
    ISSUE_STK_QTY     VARCHAR2(4000),
    STK_KIND          VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_KSDINFO_BONUS_ISSUE_API_NAME
    on KSDINFO_BONUS_ISSUE (API_NAME)
/

create table KSDINFO_CAP_DCRS
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    RECORD_DATE     VARCHAR2(4000),
    SHT_CD          VARCHAR2(4000),
    STK_KIND        VARCHAR2(4000),
    REDUCE_CAP_TYPE VARCHAR2(4000),
    REDUCE_CAP_RATE VARCHAR2(4000),
    COMP_WAY        VARCHAR2(4000),
    TD_STOP_DT      VARCHAR2(4000),
    LIST_DT         VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_KSDINFO_CAP_DCRS_API_NAME
    on KSDINFO_CAP_DCRS (API_NAME)
/

create table KSDINFO_DIVIDEND
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    RECORD_DATE      VARCHAR2(4000),
    SHT_CD           VARCHAR2(4000),
    DIVI_KIND        VARCHAR2(4000),
    FACE_VAL         VARCHAR2(4000),
    PER_STO_DIVI_AMT VARCHAR2(4000),
    DIVI_RATE        VARCHAR2(4000),
    STK_DIVI_RATE    VARCHAR2(4000),
    DIVI_PAY_DT      VARCHAR2(4000),
    STK_DIV_PAY_DT   VARCHAR2(4000),
    ODD_PAY_DT       VARCHAR2(4000),
    STK_KIND         VARCHAR2(4000),
    HIGH_DIVI_GB     VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_KSDINFO_DIVIDEND_API_NAME
    on KSDINFO_DIVIDEND (API_NAME)
/

create table KSDINFO_FORFEIT
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    RECORD_DATE    VARCHAR2(4000),
    SHT_CD         VARCHAR2(4000),
    SUBSCR_DT      VARCHAR2(4000),
    SUBSCR_PRICE   VARCHAR2(4000),
    SUBSCR_STK_QTY VARCHAR2(4000),
    REFUND_DT      VARCHAR2(4000),
    LIST_DT        VARCHAR2(4000),
    LEAD_MGR       VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_KSDINFO_FORFEIT_API_NAME
    on KSDINFO_FORFEIT (API_NAME)
/

create table KSDINFO_LIST_INFO
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    LIST_DT           VARCHAR2(4000),
    SHT_CD            VARCHAR2(4000),
    STK_KIND          VARCHAR2(4000),
    ISSUE_TYPE        VARCHAR2(4000),
    ISSUE_STK_QTY     VARCHAR2(4000),
    TOT_ISSUE_STK_QTY VARCHAR2(4000),
    ISSUE_PRICE       VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_KSDINFO_LIST_INFO_API_NAME
    on KSDINFO_LIST_INFO (API_NAME)
/

create table KSDINFO_MAND_DEPOSIT
(
    ID                     NUMBER         not null
        primary key,
    API_NAME               VARCHAR2(4000) not null,
    SHT_CD                 VARCHAR2(4000),
    STK_QTY                VARCHAR2(4000),
    DEPO_DATE              VARCHAR2(4000),
    DEPO_REASON            VARCHAR2(4000),
    TOT_ISSUE_QTY_PER_RATE VARCHAR2(4000),
    CREATED_AT             DATE           not null
)
/

create index IX_KSDINFO_MAND_DEPOSIT_API_NAME
    on KSDINFO_MAND_DEPOSIT (API_NAME)
/

create table KSDINFO_MERGER_SPLIT
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    RECORD_DATE       VARCHAR2(4000),
    SHT_CD            VARCHAR2(4000),
    OPP_CUST_CD       VARCHAR2(4000),
    OPP_CUST_NM       VARCHAR2(4000),
    CUST_CD           VARCHAR2(4000),
    CUST_NM           VARCHAR2(4000),
    MERGE_TYPE        VARCHAR2(4000),
    MERGE_RATE        VARCHAR2(4000),
    TD_STOP_DT        VARCHAR2(4000),
    LIST_DT           VARCHAR2(4000),
    ODD_AMT_PAY_DT    VARCHAR2(4000),
    TOT_ISSUE_STK_QTY VARCHAR2(4000),
    ISSUE_STK_QTY     VARCHAR2(4000),
    SEQ               VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_KSDINFO_MERGER_SPLIT_API_NAME
    on KSDINFO_MERGER_SPLIT (API_NAME)
/

create table KSDINFO_PAIDIN_CAPIN
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    RECORD_DATE       VARCHAR2(4000),
    SHT_CD            VARCHAR2(4000),
    TOT_ISSUE_STK_QTY VARCHAR2(4000),
    ISSUE_STK_QTY     VARCHAR2(4000),
    FIX_RATE          VARCHAR2(4000),
    DISC_RATE         VARCHAR2(4000),
    FIX_PRICE         VARCHAR2(4000),
    RIGHT_DT          VARCHAR2(4000),
    SUB_TERM_FT       VARCHAR2(4000),
    SUB_TERM          VARCHAR2(4000),
    LIST_DATE         VARCHAR2(4000),
    STK_KIND          VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_KSDINFO_PAIDIN_CAPIN_API_NAME
    on KSDINFO_PAIDIN_CAPIN (API_NAME)
/

create table KSDINFO_PUB_OFFER
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    RECORD_DATE    VARCHAR2(4000),
    SHT_CD         VARCHAR2(4000),
    FIX_SUBSCR_PRI VARCHAR2(4000),
    FACE_VALUE     VARCHAR2(4000),
    SUBSCR_DT      VARCHAR2(4000),
    PAY_DT         VARCHAR2(4000),
    REFUND_DT      VARCHAR2(4000),
    LIST_DT        VARCHAR2(4000),
    LEAD_MGR       VARCHAR2(4000),
    PUB_BF_CAP     VARCHAR2(4000),
    PUB_AF_CAP     VARCHAR2(4000),
    ASSIGN_STK_QTY VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_KSDINFO_PUB_OFFER_API_NAME
    on KSDINFO_PUB_OFFER (API_NAME)
/

create table KSDINFO_PURREQ
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    RECORD_DATE       VARCHAR2(4000),
    SHT_CD            VARCHAR2(4000),
    STK_KIND          VARCHAR2(4000),
    OPP_OPI_RCPT_TERM VARCHAR2(4000),
    BUY_REQ_RCPT_TERM VARCHAR2(4000),
    BUY_REQ_PRICE     VARCHAR2(4000),
    BUY_AMT_PAY_DT    VARCHAR2(4000),
    MEET_DT           VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_KSDINFO_PURREQ_API_NAME
    on KSDINFO_PURREQ (API_NAME)
/

create table KSDINFO_REV_SPLIT
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    RECORD_DATE       VARCHAR2(4000),
    SHT_CD            VARCHAR2(4000),
    INTER_BF_FACE_AMT VARCHAR2(4000),
    INTER_AF_FACE_AMT VARCHAR2(4000),
    TD_STOP_DT        VARCHAR2(4000),
    LIST_DT           VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_KSDINFO_REV_SPLIT_API_NAME
    on KSDINFO_REV_SPLIT (API_NAME)
/

create table KSDINFO_SHAREHLD_MEET
(
    ID            NUMBER         not null
        primary key,
    API_NAME      VARCHAR2(4000) not null,
    RECORD_DATE   VARCHAR2(4000),
    SHT_CD        VARCHAR2(4000),
    GEN_MEET_DT   VARCHAR2(4000),
    GEN_MEET_TYPE VARCHAR2(4000),
    AGENDA        VARCHAR2(4000),
    VOTE_TOT_QTY  VARCHAR2(4000),
    CREATED_AT    DATE           not null
)
/

create index IX_KSDINFO_SHAREHLD_MEET_API_NAME
    on KSDINFO_SHAREHLD_MEET (API_NAME)
/

create table LENDABLE_BY_COMPANY
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    PDNO             VARCHAR2(4000),
    PAPR             VARCHAR2(4000),
    BFDY_CLPR        VARCHAR2(4000),
    SBST_PRVS        VARCHAR2(4000),
    LMT_QTY1         VARCHAR2(4000),
    USE_QTY1         VARCHAR2(4000),
    TRAD_PSBL_QTY2   VARCHAR2(4000),
    RGHT_TYPE_CD     VARCHAR2(4000),
    BASS_DT          VARCHAR2(4000),
    PSBL_YN          VARCHAR2(4000),
    TOT_STUP_LMT_QTY VARCHAR2(4000),
    BRCH_LMT_QTY     VARCHAR2(4000),
    RQST_PSBL_QTY    VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_LENDABLE_BY_COMPANY_API_NAME
    on LENDABLE_BY_COMPANY (API_NAME)
/

create table MARKET_CAP
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    CREC       VARCHAR2(4000),
    TREC       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    SHAR       VARCHAR2(4000),
    TOMV       VARCHAR2(4000),
    GRAV       VARCHAR2(4000),
    RANK       VARCHAR2(4000),
    ENAME      VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    MCAP       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_MARKET_CAP_API_NAME
    on MARKET_CAP (API_NAME)
/

create table MARKET_STATUS_KRX
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD     VARCHAR2(4000),
    TRHT_YN            VARCHAR2(4000),
    TR_SUSP_REAS_CNTT  VARCHAR2(4000),
    MKOP_CLS_CODE      VARCHAR2(4000),
    ANTC_MKOP_CLS_CODE VARCHAR2(4000),
    MRKT_TRTM_CLS_CODE VARCHAR2(4000),
    DIVI_APP_CLS_CODE  VARCHAR2(4000),
    ISCD_STAT_CLS_CODE VARCHAR2(4000),
    VI_CLS_CODE        VARCHAR2(4000),
    OVTM_VI_CLS_CODE   VARCHAR2(4000),
    EXCH_CLS_CODE      VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_MARKET_STATUS_KRX_API_NAME
    on MARKET_STATUS_KRX (API_NAME)
/

create table MARKET_STATUS_NXT
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD     VARCHAR2(4000),
    TRHT_YN            VARCHAR2(4000),
    TR_SUSP_REAS_CNTT  VARCHAR2(4000),
    MKOP_CLS_CODE      VARCHAR2(4000),
    ANTC_MKOP_CLS_CODE VARCHAR2(4000),
    MRKT_TRTM_CLS_CODE VARCHAR2(4000),
    DIVI_APP_CLS_CODE  VARCHAR2(4000),
    ISCD_STAT_CLS_CODE VARCHAR2(4000),
    VI_CLS_CODE        VARCHAR2(4000),
    OVTM_VI_CLS_CODE   VARCHAR2(4000),
    EXCH_CLS_CODE      VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_MARKET_STATUS_NXT_API_NAME
    on MARKET_STATUS_NXT (API_NAME)
/

create table MARKET_STATUS_TOTAL
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    TRHT_YN            VARCHAR2(4000),
    TR_SUSP_REAS_CNTT  VARCHAR2(4000),
    MKOP_CLS_CODE      VARCHAR2(4000),
    ANTC_MKOP_CLS_CODE VARCHAR2(4000),
    MRKT_TRTM_CLS_CODE VARCHAR2(4000),
    DIVI_APP_CLS_CODE  VARCHAR2(4000),
    ISCD_STAT_CLS_CODE VARCHAR2(4000),
    VI_CLS_CODE        VARCHAR2(4000),
    OVTM_VI_CLS_CODE   VARCHAR2(4000),
    EXCH_CLS_CODE      VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_MARKET_STATUS_TOTAL_API_NAME
    on MARKET_STATUS_TOTAL (API_NAME)
/

create table MARKET_TIME
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    FM_PDGR_CD         VARCHAR2(4000),
    FM_PDGR_NAME       VARCHAR2(4000),
    FM_EXCG_CD         VARCHAR2(4000),
    FM_EXCG_NAME       VARCHAR2(4000),
    FUOP_DVSN_NAME     VARCHAR2(4000),
    FM_CLAS_CD         VARCHAR2(4000),
    FM_CLAS_NAME       VARCHAR2(4000),
    AM_MKMN_STRT_TMD   VARCHAR2(4000),
    AM_MKMN_END_TMD    VARCHAR2(4000),
    PM_MKMN_STRT_TMD   VARCHAR2(4000),
    PM_MKMN_END_TMD    VARCHAR2(4000),
    MKMN_NXDY_STRT_TMD VARCHAR2(4000),
    MKMN_NXDY_END_TMD  VARCHAR2(4000),
    BASE_MKET_STRT_TMD VARCHAR2(4000),
    BASE_MKET_END_TMD  VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_MARKET_TIME_API_NAME
    on MARKET_TIME (API_NAME)
/

create table MARKET_VALUE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    DATA_RANK            VARCHAR2(4000),
    HTS_KOR_ISNM         VARCHAR2(4000),
    MKSC_SHRN_ISCD       VARCHAR2(4000),
    STCK_PRPR            VARCHAR2(4000),
    PRDY_VRSS            VARCHAR2(4000),
    PRDY_VRSS_SIGN       VARCHAR2(4000),
    PRDY_CTRT            VARCHAR2(4000),
    ACML_VOL             VARCHAR2(4000),
    PER                  VARCHAR2(4000),
    PBR                  VARCHAR2(4000),
    PCR                  VARCHAR2(4000),
    PSR                  VARCHAR2(4000),
    EPS                  VARCHAR2(4000),
    EVA                  VARCHAR2(4000),
    EBITDA               VARCHAR2(4000),
    PV_DIV_EBITDA        VARCHAR2(4000),
    EBITDA_DIV_FNNC_EXPN VARCHAR2(4000),
    STAC_MONTH           VARCHAR2(4000),
    STAC_MONTH_CLS_CODE  VARCHAR2(4000),
    IQRY_CSNU            VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_MARKET_VALUE_API_NAME
    on MARKET_VALUE (API_NAME)
/

create table MEMBER_KRX
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD           VARCHAR2(4000),
    SELN2_MBCR_NAME1         VARCHAR2(4000),
    SELN2_MBCR_NAME2         VARCHAR2(4000),
    SELN2_MBCR_NAME3         VARCHAR2(4000),
    SELN2_MBCR_NAME4         VARCHAR2(4000),
    SELN2_MBCR_NAME5         VARCHAR2(4000),
    BYOV_MBCR_NAME1          VARCHAR2(4000),
    BYOV_MBCR_NAME2          VARCHAR2(4000),
    BYOV_MBCR_NAME3          VARCHAR2(4000),
    BYOV_MBCR_NAME4          VARCHAR2(4000),
    BYOV_MBCR_NAME5          VARCHAR2(4000),
    TOTAL_SELN_QTY1          VARCHAR2(4000),
    TOTAL_SELN_QTY2          VARCHAR2(4000),
    TOTAL_SELN_QTY3          VARCHAR2(4000),
    TOTAL_SELN_QTY4          VARCHAR2(4000),
    TOTAL_SELN_QTY5          VARCHAR2(4000),
    TOTAL_SHNU_QTY1          VARCHAR2(4000),
    TOTAL_SHNU_QTY2          VARCHAR2(4000),
    TOTAL_SHNU_QTY3          VARCHAR2(4000),
    TOTAL_SHNU_QTY4          VARCHAR2(4000),
    TOTAL_SHNU_QTY5          VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_1      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_2      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_3      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_4      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_5      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_1      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_2      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_3      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_4      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_5      VARCHAR2(4000),
    SELN_MBCR_NO1            VARCHAR2(4000),
    SELN_MBCR_NO2            VARCHAR2(4000),
    SELN_MBCR_NO3            VARCHAR2(4000),
    SELN_MBCR_NO4            VARCHAR2(4000),
    SELN_MBCR_NO5            VARCHAR2(4000),
    SHNU_MBCR_NO1            VARCHAR2(4000),
    SHNU_MBCR_NO2            VARCHAR2(4000),
    SHNU_MBCR_NO3            VARCHAR2(4000),
    SHNU_MBCR_NO4            VARCHAR2(4000),
    SHNU_MBCR_NO5            VARCHAR2(4000),
    SELN_MBCR_RLIM1          VARCHAR2(4000),
    SELN_MBCR_RLIM2          VARCHAR2(4000),
    SELN_MBCR_RLIM3          VARCHAR2(4000),
    SELN_MBCR_RLIM4          VARCHAR2(4000),
    SELN_MBCR_RLIM5          VARCHAR2(4000),
    SHNU_MBCR_RLIM1          VARCHAR2(4000),
    SHNU_MBCR_RLIM2          VARCHAR2(4000),
    SHNU_MBCR_RLIM3          VARCHAR2(4000),
    SHNU_MBCR_RLIM4          VARCHAR2(4000),
    SHNU_MBCR_RLIM5          VARCHAR2(4000),
    SELN_QTY_ICDC1           VARCHAR2(4000),
    SELN_QTY_ICDC2           VARCHAR2(4000),
    SELN_QTY_ICDC3           VARCHAR2(4000),
    SELN_QTY_ICDC4           VARCHAR2(4000),
    SELN_QTY_ICDC5           VARCHAR2(4000),
    SHNU_QTY_ICDC1           VARCHAR2(4000),
    SHNU_QTY_ICDC2           VARCHAR2(4000),
    SHNU_QTY_ICDC3           VARCHAR2(4000),
    SHNU_QTY_ICDC4           VARCHAR2(4000),
    SHNU_QTY_ICDC5           VARCHAR2(4000),
    GLOB_TOTAL_SELN_QTY      VARCHAR2(4000),
    GLOB_TOTAL_SHNU_QTY      VARCHAR2(4000),
    GLOB_TOTAL_SELN_QTY_ICDC VARCHAR2(4000),
    GLOB_TOTAL_SHNU_QTY_ICDC VARCHAR2(4000),
    GLOB_NTBY_QTY            VARCHAR2(4000),
    GLOB_SELN_RLIM           VARCHAR2(4000),
    GLOB_SHNU_RLIM           VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME1     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME2     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME3     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME4     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME5     VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME1      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME2      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME3      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME4      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME5      VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_MEMBER_KRX_API_NAME
    on MEMBER_KRX (API_NAME)
/

create table MEMBER_NXT
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD           VARCHAR2(4000),
    SELN2_MBCR_NAME1         VARCHAR2(4000),
    SELN2_MBCR_NAME2         VARCHAR2(4000),
    SELN2_MBCR_NAME3         VARCHAR2(4000),
    SELN2_MBCR_NAME4         VARCHAR2(4000),
    SELN2_MBCR_NAME5         VARCHAR2(4000),
    BYOV_MBCR_NAME1          VARCHAR2(4000),
    BYOV_MBCR_NAME2          VARCHAR2(4000),
    BYOV_MBCR_NAME3          VARCHAR2(4000),
    BYOV_MBCR_NAME4          VARCHAR2(4000),
    BYOV_MBCR_NAME5          VARCHAR2(4000),
    TOTAL_SELN_QTY1          VARCHAR2(4000),
    TOTAL_SELN_QTY2          VARCHAR2(4000),
    TOTAL_SELN_QTY3          VARCHAR2(4000),
    TOTAL_SELN_QTY4          VARCHAR2(4000),
    TOTAL_SELN_QTY5          VARCHAR2(4000),
    TOTAL_SHNU_QTY1          VARCHAR2(4000),
    TOTAL_SHNU_QTY2          VARCHAR2(4000),
    TOTAL_SHNU_QTY3          VARCHAR2(4000),
    TOTAL_SHNU_QTY4          VARCHAR2(4000),
    TOTAL_SHNU_QTY5          VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_1      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_2      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_3      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_4      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_5      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_1      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_2      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_3      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_4      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_5      VARCHAR2(4000),
    SELN_MBCR_NO1            VARCHAR2(4000),
    SELN_MBCR_NO2            VARCHAR2(4000),
    SELN_MBCR_NO3            VARCHAR2(4000),
    SELN_MBCR_NO4            VARCHAR2(4000),
    SELN_MBCR_NO5            VARCHAR2(4000),
    SHNU_MBCR_NO1            VARCHAR2(4000),
    SHNU_MBCR_NO2            VARCHAR2(4000),
    SHNU_MBCR_NO3            VARCHAR2(4000),
    SHNU_MBCR_NO4            VARCHAR2(4000),
    SHNU_MBCR_NO5            VARCHAR2(4000),
    SELN_MBCR_RLIM1          VARCHAR2(4000),
    SELN_MBCR_RLIM2          VARCHAR2(4000),
    SELN_MBCR_RLIM3          VARCHAR2(4000),
    SELN_MBCR_RLIM4          VARCHAR2(4000),
    SELN_MBCR_RLIM5          VARCHAR2(4000),
    SHNU_MBCR_RLIM1          VARCHAR2(4000),
    SHNU_MBCR_RLIM2          VARCHAR2(4000),
    SHNU_MBCR_RLIM3          VARCHAR2(4000),
    SHNU_MBCR_RLIM4          VARCHAR2(4000),
    SHNU_MBCR_RLIM5          VARCHAR2(4000),
    SELN_QTY_ICDC1           VARCHAR2(4000),
    SELN_QTY_ICDC2           VARCHAR2(4000),
    SELN_QTY_ICDC3           VARCHAR2(4000),
    SELN_QTY_ICDC4           VARCHAR2(4000),
    SELN_QTY_ICDC5           VARCHAR2(4000),
    SHNU_QTY_ICDC1           VARCHAR2(4000),
    SHNU_QTY_ICDC2           VARCHAR2(4000),
    SHNU_QTY_ICDC3           VARCHAR2(4000),
    SHNU_QTY_ICDC4           VARCHAR2(4000),
    SHNU_QTY_ICDC5           VARCHAR2(4000),
    GLOB_TOTAL_SELN_QTY      VARCHAR2(4000),
    GLOB_TOTAL_SHNU_QTY      VARCHAR2(4000),
    GLOB_TOTAL_SELN_QTY_ICDC VARCHAR2(4000),
    GLOB_TOTAL_SHNU_QTY_ICDC VARCHAR2(4000),
    GLOB_NTBY_QTY            VARCHAR2(4000),
    GLOB_SELN_RLIM           VARCHAR2(4000),
    GLOB_SHNU_RLIM           VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME1     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME2     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME3     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME4     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME5     VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME1      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME2      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME3      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME4      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME5      VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_MEMBER_NXT_API_NAME
    on MEMBER_NXT (API_NAME)
/

create table MEMBER_TOTAL
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD           VARCHAR2(4000),
    SELN2_MBCR_NAME1         VARCHAR2(4000),
    SELN2_MBCR_NAME2         VARCHAR2(4000),
    SELN2_MBCR_NAME3         VARCHAR2(4000),
    SELN2_MBCR_NAME4         VARCHAR2(4000),
    SELN2_MBCR_NAME5         VARCHAR2(4000),
    BYOV_MBCR_NAME1          VARCHAR2(4000),
    BYOV_MBCR_NAME2          VARCHAR2(4000),
    BYOV_MBCR_NAME3          VARCHAR2(4000),
    BYOV_MBCR_NAME4          VARCHAR2(4000),
    BYOV_MBCR_NAME5          VARCHAR2(4000),
    TOTAL_SELN_QTY1          VARCHAR2(4000),
    TOTAL_SELN_QTY2          VARCHAR2(4000),
    TOTAL_SELN_QTY3          VARCHAR2(4000),
    TOTAL_SELN_QTY4          VARCHAR2(4000),
    TOTAL_SELN_QTY5          VARCHAR2(4000),
    TOTAL_SHNU_QTY1          VARCHAR2(4000),
    TOTAL_SHNU_QTY2          VARCHAR2(4000),
    TOTAL_SHNU_QTY3          VARCHAR2(4000),
    TOTAL_SHNU_QTY4          VARCHAR2(4000),
    TOTAL_SHNU_QTY5          VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_1      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_2      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_3      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_4      VARCHAR2(4000),
    SELN_MBCR_GLOB_YN_5      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_1      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_2      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_3      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_4      VARCHAR2(4000),
    SHNU_MBCR_GLOB_YN_5      VARCHAR2(4000),
    SELN_MBCR_NO1            VARCHAR2(4000),
    SELN_MBCR_NO2            VARCHAR2(4000),
    SELN_MBCR_NO3            VARCHAR2(4000),
    SELN_MBCR_NO4            VARCHAR2(4000),
    SELN_MBCR_NO5            VARCHAR2(4000),
    SHNU_MBCR_NO1            VARCHAR2(4000),
    SHNU_MBCR_NO2            VARCHAR2(4000),
    SHNU_MBCR_NO3            VARCHAR2(4000),
    SHNU_MBCR_NO4            VARCHAR2(4000),
    SHNU_MBCR_NO5            VARCHAR2(4000),
    SELN_MBCR_RLIM1          VARCHAR2(4000),
    SELN_MBCR_RLIM2          VARCHAR2(4000),
    SELN_MBCR_RLIM3          VARCHAR2(4000),
    SELN_MBCR_RLIM4          VARCHAR2(4000),
    SELN_MBCR_RLIM5          VARCHAR2(4000),
    SHNU_MBCR_RLIM1          VARCHAR2(4000),
    SHNU_MBCR_RLIM2          VARCHAR2(4000),
    SHNU_MBCR_RLIM3          VARCHAR2(4000),
    SHNU_MBCR_RLIM4          VARCHAR2(4000),
    SHNU_MBCR_RLIM5          VARCHAR2(4000),
    SELN_QTY_ICDC1           VARCHAR2(4000),
    SELN_QTY_ICDC2           VARCHAR2(4000),
    SELN_QTY_ICDC3           VARCHAR2(4000),
    SELN_QTY_ICDC4           VARCHAR2(4000),
    SELN_QTY_ICDC5           VARCHAR2(4000),
    SHNU_QTY_ICDC1           VARCHAR2(4000),
    SHNU_QTY_ICDC2           VARCHAR2(4000),
    SHNU_QTY_ICDC3           VARCHAR2(4000),
    SHNU_QTY_ICDC4           VARCHAR2(4000),
    SHNU_QTY_ICDC5           VARCHAR2(4000),
    GLOB_TOTAL_SELN_QTY      VARCHAR2(4000),
    GLOB_TOTAL_SHNU_QTY      VARCHAR2(4000),
    GLOB_TOTAL_SELN_QTY_ICDC VARCHAR2(4000),
    GLOB_TOTAL_SHNU_QTY_ICDC VARCHAR2(4000),
    GLOB_NTBY_QTY            VARCHAR2(4000),
    GLOB_SELN_RLIM           VARCHAR2(4000),
    GLOB_SHNU_RLIM           VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME1     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME2     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME3     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME4     VARCHAR2(4000),
    SELN2_MBCR_ENG_NAME5     VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME1      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME2      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME3      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME4      VARCHAR2(4000),
    BYOV_MBCR_ENG_NAME5      VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_MEMBER_TOTAL_API_NAME
    on MEMBER_TOTAL (API_NAME)
/

create table MKTFUNDS
(
    ID                      NUMBER         not null
        primary key,
    API_NAME                VARCHAR2(4000) not null,
    BSOP_DATE               VARCHAR2(4000),
    BSTP_NMIX_PRPR          VARCHAR2(4000),
    BSTP_NMIX_PRDY_VRSS     VARCHAR2(4000),
    PRDY_VRSS_SIGN          VARCHAR2(4000),
    PRDY_CTRT               VARCHAR2(4000),
    HTS_AVLS                VARCHAR2(4000),
    CUST_DPMN_AMT           VARCHAR2(4000),
    CUST_DPMN_AMT_PRDY_VRSS VARCHAR2(4000),
    AMT_TNRT                VARCHAR2(4000),
    UNCL_AMT                VARCHAR2(4000),
    CRDT_LOAN_RMND          VARCHAR2(4000),
    FUTS_TFAM_AMT           VARCHAR2(4000),
    STTP_AMT                VARCHAR2(4000),
    MXTP_AMT                VARCHAR2(4000),
    BNTP_AMT                VARCHAR2(4000),
    MMF_AMT                 VARCHAR2(4000),
    SECU_LEND_AMT           VARCHAR2(4000),
    CREATED_AT              DATE           not null
)
/

create index IX_MKTFUNDS_API_NAME
    on MKTFUNDS (API_NAME)
/

create table NEAR_NEW_HIGHLOW
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    HTS_KOR_ISNM   VARCHAR2(4000),
    MKSC_SHRN_ISCD VARCHAR2(4000),
    STCK_PRPR      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ASKP           VARCHAR2(4000),
    ASKP_RSQN1     VARCHAR2(4000),
    BIDP           VARCHAR2(4000),
    BIDP_RSQN1     VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    NEW_HGPR       VARCHAR2(4000),
    HPRC_NEAR_RATE VARCHAR2(4000),
    NEW_LWPR       VARCHAR2(4000),
    LWPR_NEAR_RATE VARCHAR2(4000),
    STCK_SDPR      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_NEAR_NEW_HIGHLOW_API_NAME
    on NEAR_NEW_HIGHLOW (API_NAME)
/

create table NEWS_TITLE
(
    ID          NUMBER         not null
        primary key,
    API_NAME    VARCHAR2(4000) not null,
    INFO_GB     VARCHAR2(4000),
    NEWS_KEY    VARCHAR2(4000),
    DATA_DT     VARCHAR2(4000),
    DATA_TM     VARCHAR2(4000),
    CLASS_CD    VARCHAR2(4000),
    CLASS_NAME  VARCHAR2(4000),
    SOURCE      VARCHAR2(4000),
    NATION_CD   VARCHAR2(4000),
    EXCHANGE_CD VARCHAR2(4000),
    SYMB        VARCHAR2(4000),
    SYMB_NAME   VARCHAR2(4000),
    TITLE       VARCHAR2(4000),
    CREATED_AT  DATE           not null
)
/

create index IX_NEWS_TITLE_API_NAME
    on NEWS_TITLE (API_NAME)
/

create table ORDER_CASH
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    KRX_FWDG_ORD_ORGNO VARCHAR2(4000),
    ODNO               VARCHAR2(4000),
    ORD_TMD            VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_ORDER_CASH_API_NAME
    on ORDER_CASH (API_NAME)
/

create table ORDER_CREDIT
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    KRX_FWDG_ORD_ORGNO VARCHAR2(4000),
    ODNO               VARCHAR2(4000),
    ORD_TMD            VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_ORDER_CREDIT_API_NAME
    on ORDER_CREDIT (API_NAME)
/

create table ORDER_RESV
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    ODNO             VARCHAR2(4000),
    RSVN_ORD_RCIT_DT VARCHAR2(4000),
    OVRS_RSVN_ODNO   VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_ORDER_RESV_API_NAME
    on ORDER_RESV (API_NAME)
/

create table ORDER_RESV_CCNL
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    OVRS_RSVN_ODNO VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_ORDER_RESV_CCNL_API_NAME
    on ORDER_RESV_CCNL (API_NAME)
/

create table ORDER_RESV_RVSECNCL
(
    ID           NUMBER         not null
        primary key,
    API_NAME     VARCHAR2(4000) not null,
    NRML_PRCS_YN VARCHAR2(4000),
    CREATED_AT   DATE           not null
)
/

create index IX_ORDER_RESV_RVSECNCL_API_NAME
    on ORDER_RESV_RVSECNCL (API_NAME)
/

create table OVERTIME_ASKING_PRICE_KRX
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD       VARCHAR2(4000),
    BSOP_HOUR            VARCHAR2(4000),
    HOUR_CLS_CODE        VARCHAR2(4000),
    ASKP1                VARCHAR2(4000),
    ASKP2                VARCHAR2(4000),
    ASKP3                VARCHAR2(4000),
    ASKP4                VARCHAR2(4000),
    ASKP5                VARCHAR2(4000),
    ASKP6                VARCHAR2(4000),
    ASKP7                VARCHAR2(4000),
    ASKP8                VARCHAR2(4000),
    ASKP9                VARCHAR2(4000),
    BIDP1                VARCHAR2(4000),
    BIDP2                VARCHAR2(4000),
    BIDP3                VARCHAR2(4000),
    BIDP4                VARCHAR2(4000),
    BIDP5                VARCHAR2(4000),
    BIDP6                VARCHAR2(4000),
    BIDP7                VARCHAR2(4000),
    BIDP8                VARCHAR2(4000),
    BIDP9                VARCHAR2(4000),
    ASKP_RSQN1           VARCHAR2(4000),
    ASKP_RSQN2           VARCHAR2(4000),
    ASKP_RSQN3           VARCHAR2(4000),
    ASKP_RSQN4           VARCHAR2(4000),
    ASKP_RSQN5           VARCHAR2(4000),
    ASKP_RSQN6           VARCHAR2(4000),
    ASKP_RSQN7           VARCHAR2(4000),
    ASKP_RSQN8           VARCHAR2(4000),
    ASKP_RSQN9           VARCHAR2(4000),
    BIDP_RSQN1           VARCHAR2(4000),
    BIDP_RSQN2           VARCHAR2(4000),
    BIDP_RSQN3           VARCHAR2(4000),
    BIDP_RSQN4           VARCHAR2(4000),
    BIDP_RSQN5           VARCHAR2(4000),
    BIDP_RSQN6           VARCHAR2(4000),
    BIDP_RSQN7           VARCHAR2(4000),
    BIDP_RSQN8           VARCHAR2(4000),
    BIDP_RSQN9           VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    OVTM_TOTAL_ASKP_RSQN VARCHAR2(4000),
    OVTM_TOTAL_BIDP_RSQN VARCHAR2(4000),
    ANTC_CNPR            VARCHAR2(4000),
    ANTC_CNQN            VARCHAR2(4000),
    ANTC_VOL             VARCHAR2(4000),
    ANTC_CNTG_VRSS       VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN  VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT  VARCHAR2(4000),
    ACML_VOL             VARCHAR2(4000),
    TOTAL_ASKP_RSQN_ICDC VARCHAR2(4000),
    TOTAL_BIDP_RSQN_ICDC VARCHAR2(4000),
    OVTM_TOTAL_ASKP_ICDC VARCHAR2(4000),
    OVTM_TOTAL_BIDP_ICDC VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_OVERTIME_ASKING_PRICE_KRX_API_NAME
    on OVERTIME_ASKING_PRICE_KRX (API_NAME)
/

create table OVERTIME_CCNL_KRX
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD               VARCHAR2(4000),
    STCK_CNTG_HOUR               VARCHAR2(4000),
    STCK_PRPR                    VARCHAR2(4000),
    PRDY_VRSS_SIGN               VARCHAR2(4000),
    PRDY_VRSS                    VARCHAR2(4000),
    PRDY_CTRT                    VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC           VARCHAR2(4000),
    STCK_OPRC                    VARCHAR2(4000),
    STCK_HGPR                    VARCHAR2(4000),
    STCK_LWPR                    VARCHAR2(4000),
    ASKP1                        VARCHAR2(4000),
    BIDP1                        VARCHAR2(4000),
    CNTG_VOL                     VARCHAR2(4000),
    ACML_VOL                     VARCHAR2(4000),
    ACML_TR_PBMN                 VARCHAR2(4000),
    SELN_CNTG_CSNU               VARCHAR2(4000),
    SHNU_CNTG_CSNU               VARCHAR2(4000),
    NTBY_CNTG_CSNU               VARCHAR2(4000),
    CTTR                         VARCHAR2(4000),
    SELN_CNTG_SMTN               VARCHAR2(4000),
    SHNU_CNTG_SMTN               VARCHAR2(4000),
    CNTG_CLS_CODE                VARCHAR2(4000),
    SHNU_RATE                    VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE  VARCHAR2(4000),
    OPRC_HOUR                    VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN          VARCHAR2(4000),
    OPRC_VRSS_PRPR               VARCHAR2(4000),
    HGPR_HOUR                    VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    HGPR_VRSS_PRPR               VARCHAR2(4000),
    LWPR_HOUR                    VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    LWPR_VRSS_PRPR               VARCHAR2(4000),
    BSOP_DATE                    VARCHAR2(4000),
    NEW_MKOP_CLS_CODE            VARCHAR2(4000),
    TRHT_YN                      VARCHAR2(4000),
    ASKP_RSQN1                   VARCHAR2(4000),
    BIDP_RSQN1                   VARCHAR2(4000),
    TOTAL_ASKP_RSQN              VARCHAR2(4000),
    TOTAL_BIDP_RSQN              VARCHAR2(4000),
    VOL_TNRT                     VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL      VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL_RATE VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_OVERTIME_CCNL_KRX_API_NAME
    on OVERTIME_CCNL_KRX (API_NAME)
/

create table OVERTIME_EXP_CCNL_KRX
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD               VARCHAR2(4000),
    STCK_CNTG_HOUR               VARCHAR2(4000),
    STCK_PRPR                    VARCHAR2(4000),
    PRDY_VRSS_SIGN               VARCHAR2(4000),
    PRDY_VRSS                    VARCHAR2(4000),
    PRDY_CTRT                    VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC           VARCHAR2(4000),
    STCK_OPRC                    VARCHAR2(4000),
    STCK_HGPR                    VARCHAR2(4000),
    STCK_LWPR                    VARCHAR2(4000),
    ASKP1                        VARCHAR2(4000),
    BIDP1                        VARCHAR2(4000),
    CNTG_VOL                     VARCHAR2(4000),
    ACML_VOL                     VARCHAR2(4000),
    ACML_TR_PBMN                 VARCHAR2(4000),
    SELN_CNTG_CSNU               VARCHAR2(4000),
    SHNU_CNTG_CSNU               VARCHAR2(4000),
    NTBY_CNTG_CSNU               VARCHAR2(4000),
    CTTR                         VARCHAR2(4000),
    SELN_CNTG_SMTN               VARCHAR2(4000),
    SHNU_CNTG_SMTN               VARCHAR2(4000),
    CNTG_CLS_CODE                VARCHAR2(4000),
    SHNU_RATE                    VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE  VARCHAR2(4000),
    OPRC_HOUR                    VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN          VARCHAR2(4000),
    OPRC_VRSS_PRPR               VARCHAR2(4000),
    HGPR_HOUR                    VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    HGPR_VRSS_PRPR               VARCHAR2(4000),
    LWPR_HOUR                    VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    LWPR_VRSS_PRPR               VARCHAR2(4000),
    BSOP_DATE                    VARCHAR2(4000),
    NEW_MKOP_CLS_CODE            VARCHAR2(4000),
    TRHT_YN                      VARCHAR2(4000),
    ASKP_RSQN1                   VARCHAR2(4000),
    BIDP_RSQN1                   VARCHAR2(4000),
    TOTAL_ASKP_RSQN              VARCHAR2(4000),
    TOTAL_BIDP_RSQN              VARCHAR2(4000),
    VOL_TNRT                     VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL      VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL_RATE VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_OVERTIME_EXP_CCNL_KRX_API_NAME
    on OVERTIME_EXP_CCNL_KRX (API_NAME)
/

create table OVERTIME_EXP_TRANS_FLUCT
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    DATA_RANK                    VARCHAR2(4000),
    ISCD_STAT_CLS_CODE           VARCHAR2(4000),
    STCK_SHRN_ISCD               VARCHAR2(4000),
    HTS_KOR_ISNM                 VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNPR          VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_VRSS     VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_VRSSSIGN VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNTG_CTRT     VARCHAR2(4000),
    OVTM_UNTP_ASKP_RSQN1         VARCHAR2(4000),
    OVTM_UNTP_BIDP_RSQN1         VARCHAR2(4000),
    OVTM_UNTP_ANTC_CNQN          VARCHAR2(4000),
    ITMT_VOL                     VARCHAR2(4000),
    STCK_PRPR                    VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_OVERTIME_EXP_TRANS_FLUCT_API_NAME
    on OVERTIME_EXP_TRANS_FLUCT (API_NAME)
/

create table OVERTIME_FLUCTUATION
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    OVTM_UNTP_UPLM_ISSU_CNT  VARCHAR2(4000),
    OVTM_UNTP_ASCN_ISSU_CNT  VARCHAR2(4000),
    OVTM_UNTP_STNR_ISSU_CNT  VARCHAR2(4000),
    OVTM_UNTP_LSLM_ISSU_CNT  VARCHAR2(4000),
    OVTM_UNTP_DOWN_ISSU_CNT  VARCHAR2(4000),
    OVTM_UNTP_ACML_VOL       VARCHAR2(4000),
    OVTM_UNTP_ACML_TR_PBMN   VARCHAR2(4000),
    OVTM_UNTP_EXCH_VOL       VARCHAR2(4000),
    OVTM_UNTP_EXCH_TR_PBMN   VARCHAR2(4000),
    OVTM_UNTP_KOSDAQ_VOL     VARCHAR2(4000),
    OVTM_UNTP_KOSDAQ_TR_PBMN VARCHAR2(4000),
    MKSC_SHRN_ISCD           VARCHAR2(4000),
    HTS_KOR_ISNM             VARCHAR2(4000),
    OVTM_UNTP_PRPR           VARCHAR2(4000),
    OVTM_UNTP_PRDY_VRSS      VARCHAR2(4000),
    OVTM_UNTP_PRDY_VRSS_SIGN VARCHAR2(4000),
    OVTM_UNTP_PRDY_CTRT      VARCHAR2(4000),
    OVTM_UNTP_ASKP1          VARCHAR2(4000),
    OVTM_UNTP_SELN_RSQN      VARCHAR2(4000),
    OVTM_UNTP_BIDP1          VARCHAR2(4000),
    OVTM_UNTP_SHNU_RSQN      VARCHAR2(4000),
    OVTM_UNTP_VOL            VARCHAR2(4000),
    OVTM_VRSS_ACML_VOL_RLIM  VARCHAR2(4000),
    STCK_PRPR                VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    BIDP                     VARCHAR2(4000),
    ASKP                     VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_OVERTIME_FLUCTUATION_API_NAME
    on OVERTIME_FLUCTUATION (API_NAME)
/

create table OVERTIME_VOLUME
(
    ID                       NUMBER         not null
        primary key,
    API_NAME                 VARCHAR2(4000) not null,
    OVTM_UNTP_EXCH_VOL       VARCHAR2(4000),
    OVTM_UNTP_EXCH_TR_PBMN   VARCHAR2(4000),
    OVTM_UNTP_KOSDAQ_VOL     VARCHAR2(4000),
    OVTM_UNTP_KOSDAQ_TR_PBMN VARCHAR2(4000),
    STCK_SHRN_ISCD           VARCHAR2(4000),
    HTS_KOR_ISNM             VARCHAR2(4000),
    OVTM_UNTP_PRPR           VARCHAR2(4000),
    OVTM_UNTP_PRDY_VRSS      VARCHAR2(4000),
    OVTM_UNTP_PRDY_VRSS_SIGN VARCHAR2(4000),
    OVTM_UNTP_PRDY_CTRT      VARCHAR2(4000),
    OVTM_UNTP_SELN_RSQN      VARCHAR2(4000),
    OVTM_UNTP_SHNU_RSQN      VARCHAR2(4000),
    OVTM_UNTP_VOL            VARCHAR2(4000),
    OVTM_VRSS_ACML_VOL_RLIM  VARCHAR2(4000),
    STCK_PRPR                VARCHAR2(4000),
    ACML_VOL                 VARCHAR2(4000),
    BIDP                     VARCHAR2(4000),
    ASKP                     VARCHAR2(4000),
    CREATED_AT               DATE           not null
)
/

create index IX_OVERTIME_VOLUME_API_NAME
    on OVERTIME_VOLUME (API_NAME)
/

create table PBAR_TRATIO
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    RPRS_MRKT_KOR_NAME VARCHAR2(4000),
    STCK_SHRN_ISCD     VARCHAR2(4000),
    HTS_KOR_ISNM       VARCHAR2(4000),
    STCK_PRPR          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    PRDY_VOL           VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC VARCHAR2(4000),
    LSTN_STCN          VARCHAR2(4000),
    DATA_RANK          VARCHAR2(4000),
    CNTG_VOL           VARCHAR2(4000),
    ACML_VOL_RLIM      VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_PBAR_TRATIO_API_NAME
    on PBAR_TRATIO (API_NAME)
/

create table PENSION_INQUIRE_BALANCE
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    CBLC_DVSN_NAME     VARCHAR2(4000),
    PRDT_NAME          VARCHAR2(4000),
    PDNO               VARCHAR2(4000),
    ITEM_DVSN_NAME     VARCHAR2(4000),
    THDT_BUYQTY        VARCHAR2(4000),
    THDT_SLL_QTY       VARCHAR2(4000),
    HLDG_QTY           VARCHAR2(4000),
    ORD_PSBL_QTY       VARCHAR2(4000),
    PCHS_AVG_PRIC      VARCHAR2(4000),
    PCHS_AMT           VARCHAR2(4000),
    PRPR               VARCHAR2(4000),
    EVLU_AMT           VARCHAR2(4000),
    EVLU_PFLS_AMT      VARCHAR2(4000),
    EVLU_ERNG_RT       VARCHAR2(4000),
    DNCA_TOT_AMT       VARCHAR2(4000),
    NXDY_EXCC_AMT      VARCHAR2(4000),
    PRVS_RCDL_EXCC_AMT VARCHAR2(4000),
    THDT_BUY_AMT       VARCHAR2(4000),
    THDT_SLL_AMT       VARCHAR2(4000),
    THDT_TLEX_AMT      VARCHAR2(4000),
    SCTS_EVLU_AMT      VARCHAR2(4000),
    TOT_EVLU_AMT       VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_PENSION_INQUIRE_BALANCE_API_NAME
    on PENSION_INQUIRE_BALANCE (API_NAME)
/

create table PENSION_INQUIRE_DAILY_CCLD
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    ORD_GNO_BRNO        VARCHAR2(4000),
    SLL_BUY_DVSN_CD     VARCHAR2(4000),
    TRAD_DVSN_NAME      VARCHAR2(4000),
    ODNO                VARCHAR2(4000),
    PDNO                VARCHAR2(4000),
    PRDT_NAME           VARCHAR2(4000),
    ORD_UNPR            VARCHAR2(4000),
    ORD_QTY             VARCHAR2(4000),
    TOT_CCLD_QTY        VARCHAR2(4000),
    NCCS_QTY            VARCHAR2(4000),
    ORD_DVSN_CD         VARCHAR2(4000),
    ORD_DVSN_NAME       VARCHAR2(4000),
    ORGN_ODNO           VARCHAR2(4000),
    ORD_TMD             VARCHAR2(4000),
    OBJT_CUST_DVSN_NAME VARCHAR2(4000),
    PCHS_AVG_PRIC       VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_PENSION_INQUIRE_DAILY_CCLD_API_NAME
    on PENSION_INQUIRE_DAILY_CCLD (API_NAME)
/

create table PENSION_INQUIRE_DEPOSIT
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    DNCA_TOTA        VARCHAR2(4000),
    NXDY_EXCC_AMT    VARCHAR2(4000),
    NXDY_STTL_AMT    VARCHAR2(4000),
    NX2_DAY_STTL_AMT VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_PENSION_INQUIRE_DEPOSIT_API_NAME
    on PENSION_INQUIRE_DEPOSIT (API_NAME)
/

create table PENSION_INQUIRE_PRESENT_BALANCE
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    CBLC_DVSN          VARCHAR2(4000),
    CBLC_DVSN_NAME     VARCHAR2(4000),
    PDNO               VARCHAR2(4000),
    PRDT_NAME          VARCHAR2(4000),
    HLDG_QTY           VARCHAR2(4000),
    SLPSB_QTY          VARCHAR2(4000),
    PCHS_AVG_PRIC      VARCHAR2(4000),
    EVLU_PFLS_AMT      VARCHAR2(4000),
    EVLU_PFLS_RT       VARCHAR2(4000),
    PRPR               VARCHAR2(4000),
    EVLU_AMT           VARCHAR2(4000),
    PCHS_AMT           VARCHAR2(4000),
    CBLC_WEIT          VARCHAR2(4000),
    PCHS_AMT_SMTL_AMT  VARCHAR2(4000),
    EVLU_AMT_SMTL_AMT  VARCHAR2(4000),
    EVLU_PFLS_SMTL_AMT VARCHAR2(4000),
    TRAD_PFLS_SMTL     VARCHAR2(4000),
    THDT_TOT_PFLS_AMT  VARCHAR2(4000),
    PFTRT              VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_PENSION_INQUIRE_PRESENT_BALANCE_API_NAME
    on PENSION_INQUIRE_PRESENT_BALANCE (API_NAME)
/

create table PENSION_INQUIRE_PSBL_ORDER
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    ORD_PSBL_CASH      VARCHAR2(4000),
    RUSE_PSBL_AMT      VARCHAR2(4000),
    PSBL_QTY_CALC_UNPR VARCHAR2(4000),
    MAX_BUY_AMT        VARCHAR2(4000),
    MAX_BUY_QTY        VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_PENSION_INQUIRE_PSBL_ORDER_API_NAME
    on PENSION_INQUIRE_PSBL_ORDER (API_NAME)
/

create table PERIOD_RIGHTS
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    BASS_DT             VARCHAR2(4000),
    RGHT_TYPE_CD        VARCHAR2(4000),
    PDNO                VARCHAR2(4000),
    PRDT_NAME           VARCHAR2(4000),
    PRDT_TYPE_CD        VARCHAR2(4000),
    STD_PDNO            VARCHAR2(4000),
    ACPL_BASS_DT        VARCHAR2(4000),
    SBSC_STRT_DT        VARCHAR2(4000),
    SBSC_END_DT         VARCHAR2(4000),
    CASH_ALCT_RT        VARCHAR2(4000),
    STCK_ALCT_RT        VARCHAR2(4000),
    CRCY_CD             VARCHAR2(4000),
    CRCY_CD2            VARCHAR2(4000),
    CRCY_CD3            VARCHAR2(4000),
    CRCY_CD4            VARCHAR2(4000),
    ALCT_FRCR_UNPR      VARCHAR2(4000),
    STKP_DVDN_FRCR_AMT2 VARCHAR2(4000),
    STKP_DVDN_FRCR_AMT3 VARCHAR2(4000),
    STKP_DVDN_FRCR_AMT4 VARCHAR2(4000),
    DFNT_YN             VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_PERIOD_RIGHTS_API_NAME
    on PERIOD_RIGHTS (API_NAME)
/

create table PREFER_DISPARATE_RATIO
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD      VARCHAR2(4000),
    DATA_RANK           VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    STCK_PRPR           VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    PRST_ISCD           VARCHAR2(4000),
    PRST_KOR_ISNM       VARCHAR2(4000),
    PRST_PRPR           VARCHAR2(4000),
    PRST_PRDY_VRSS      VARCHAR2(4000),
    PRST_PRDY_VRSS_SIGN VARCHAR2(4000),
    PRST_ACML_VOL       VARCHAR2(4000),
    DIFF_PRPR           VARCHAR2(4000),
    DPRT                VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    PRST_PRDY_CTRT      VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_PREFER_DISPARATE_RATIO_API_NAME
    on PREFER_DISPARATE_RATIO (API_NAME)
/

create table PROFIT_ASSET_INDEX
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    DATA_RANK           VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    MKSC_SHRN_ISCD      VARCHAR2(4000),
    STCK_PRPR           VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    SALE_TOTL_PRFI      VARCHAR2(4000),
    BSOP_PRTI           VARCHAR2(4000),
    OP_PRFI             VARCHAR2(4000),
    THTR_NTIN           VARCHAR2(4000),
    TOTAL_ASET          VARCHAR2(4000),
    TOTAL_LBLT          VARCHAR2(4000),
    TOTAL_CPTL          VARCHAR2(4000),
    STAC_MONTH          VARCHAR2(4000),
    STAC_MONTH_CLS_CODE VARCHAR2(4000),
    IQRY_CSNU           VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_PROFIT_ASSET_INDEX_API_NAME
    on PROFIT_ASSET_INDEX (API_NAME)
/

create table PROGRAM_TRADE_BY_STOCK
(
    ID                     NUMBER         not null
        primary key,
    API_NAME               VARCHAR2(4000) not null,
    BSOP_HOUR              VARCHAR2(4000),
    STCK_PRPR              VARCHAR2(4000),
    PRDY_VRSS              VARCHAR2(4000),
    PRDY_VRSS_SIGN         VARCHAR2(4000),
    PRDY_CTRT              VARCHAR2(4000),
    ACML_VOL               VARCHAR2(4000),
    WHOL_SMTN_SELN_VOL     VARCHAR2(4000),
    WHOL_SMTN_SHNU_VOL     VARCHAR2(4000),
    WHOL_SMTN_NTBY_QTY     VARCHAR2(4000),
    WHOL_SMTN_SELN_TR_PBMN VARCHAR2(4000),
    WHOL_SMTN_SHNU_TR_PBMN VARCHAR2(4000),
    WHOL_SMTN_NTBY_TR_PBMN VARCHAR2(4000),
    WHOL_NTBY_VOL_ICDC     VARCHAR2(4000),
    WHOL_NTBY_TR_PBMN_ICDC VARCHAR2(4000),
    CREATED_AT             DATE           not null
)
/

create index IX_PROGRAM_TRADE_BY_STOCK_API_NAME
    on PROGRAM_TRADE_BY_STOCK (API_NAME)
/

create table PROGRAM_TRADE_BY_STOCK_DAILY
(
    ID                      NUMBER         not null
        primary key,
    API_NAME                VARCHAR2(4000) not null,
    STCK_BSOP_DATE          VARCHAR2(4000),
    STCK_CLPR               VARCHAR2(4000),
    PRDY_VRSS               VARCHAR2(4000),
    PRDY_VRSS_SIGN          VARCHAR2(4000),
    PRDY_CTRT               VARCHAR2(4000),
    ACML_VOL                VARCHAR2(4000),
    ACML_TR_PBMN            VARCHAR2(4000),
    WHOL_SMTN_SELN_VOL      VARCHAR2(4000),
    WHOL_SMTN_SHNU_VOL      VARCHAR2(4000),
    WHOL_SMTN_NTBY_QTY      VARCHAR2(4000),
    WHOL_SMTN_SELN_TR_PBMN  VARCHAR2(4000),
    WHOL_SMTN_SHNU_TR_PBMN  VARCHAR2(4000),
    WHOL_SMTN_NTBY_TR_PBMN  VARCHAR2(4000),
    WHOL_NTBY_VOL_ICDC      VARCHAR2(4000),
    WHOL_NTBY_TR_PBMN_ICDC2 VARCHAR2(4000),
    CREATED_AT              DATE           not null
)
/

create index IX_PROGRAM_TRADE_BY_STOCK_DAILY_API_NAME
    on PROGRAM_TRADE_BY_STOCK_DAILY (API_NAME)
/

create table PROGRAM_TRADE_KRX
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    SELN_CNQN      VARCHAR2(4000),
    SELN_TR_PBMN   VARCHAR2(4000),
    SHNU_CNQN      VARCHAR2(4000),
    SHNU_TR_PBMN   VARCHAR2(4000),
    NTBY_CNQN      VARCHAR2(4000),
    NTBY_TR_PBMN   VARCHAR2(4000),
    SELN_RSQN      VARCHAR2(4000),
    SHNU_RSQN      VARCHAR2(4000),
    WHOL_NTBY_QTY  VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_PROGRAM_TRADE_KRX_API_NAME
    on PROGRAM_TRADE_KRX (API_NAME)
/

create table PROGRAM_TRADE_NXT
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    SELN_CNQN      VARCHAR2(4000),
    SELN_TR_PBMN   VARCHAR2(4000),
    SHNU_CNQN      VARCHAR2(4000),
    SHNU_TR_PBMN   VARCHAR2(4000),
    NTBY_CNQN      VARCHAR2(4000),
    NTBY_TR_PBMN   VARCHAR2(4000),
    SELN_RSQN      VARCHAR2(4000),
    SHNU_RSQN      VARCHAR2(4000),
    WHOL_NTBY_QTY  VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_PROGRAM_TRADE_NXT_API_NAME
    on PROGRAM_TRADE_NXT (API_NAME)
/

create table PROGRAM_TRADE_TOTAL
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    SELN_CNQN      VARCHAR2(4000),
    SELN_TR_PBMN   VARCHAR2(4000),
    SHNU_CNQN      VARCHAR2(4000),
    SHNU_TR_PBMN   VARCHAR2(4000),
    NTBY_CNQN      VARCHAR2(4000),
    NTBY_TR_PBMN   VARCHAR2(4000),
    SELN_RSQN      VARCHAR2(4000),
    SHNU_RSQN      VARCHAR2(4000),
    WHOL_NTBY_QTY  VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_PROGRAM_TRADE_TOTAL_API_NAME
    on PROGRAM_TRADE_TOTAL (API_NAME)
/

create table PSEARCH_RESULT
(
    ID          NUMBER         not null
        primary key,
    API_NAME    VARCHAR2(4000) not null,
    CODE        VARCHAR2(4000),
    NAME        VARCHAR2(4000),
    DAEBI       VARCHAR2(4000),
    PRICE       VARCHAR2(4000),
    CHGRATE     VARCHAR2(4000),
    ACML_VOL    VARCHAR2(4000),
    TRADE_AMT   VARCHAR2(4000),
    CHANGE      VARCHAR2(4000),
    CTTR        VARCHAR2(4000),
    OPEN        VARCHAR2(4000),
    HIGH        VARCHAR2(4000),
    LOW         VARCHAR2(4000),
    HIGH52      VARCHAR2(4000),
    LOW52       VARCHAR2(4000),
    EXPPRICE    VARCHAR2(4000),
    EXPCHANGE   VARCHAR2(4000),
    EXPCHGGRATE VARCHAR2(4000),
    EXPCVOL     VARCHAR2(4000),
    CHGRATE2    VARCHAR2(4000),
    EXPDAEBI    VARCHAR2(4000),
    RECPRICE    VARCHAR2(4000),
    UPLMTPRICE  VARCHAR2(4000),
    DNLMTPRICE  VARCHAR2(4000),
    STOTPRICE   VARCHAR2(4000),
    CREATED_AT  DATE           not null
)
/

create index IX_PSEARCH_RESULT_API_NAME
    on PSEARCH_RESULT (API_NAME)
/

create table PSEARCH_TITLE
(
    ID           NUMBER         not null
        primary key,
    API_NAME     VARCHAR2(4000) not null,
    USER_ID      VARCHAR2(4000),
    SEQ          VARCHAR2(4000),
    GRP_NM       VARCHAR2(4000),
    CONDITION_NM VARCHAR2(4000),
    CREATED_AT   DATE           not null
)
/

create index IX_PSEARCH_TITLE_API_NAME
    on PSEARCH_TITLE (API_NAME)
/

create table QUOTE_BALANCE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD       VARCHAR2(4000),
    DATA_RANK            VARCHAR2(4000),
    HTS_KOR_ISNM         VARCHAR2(4000),
    STCK_PRPR            VARCHAR2(4000),
    PRDY_VRSS            VARCHAR2(4000),
    PRDY_VRSS_SIGN       VARCHAR2(4000),
    PRDY_CTRT            VARCHAR2(4000),
    ACML_VOL             VARCHAR2(4000),
    TOTAL_ASKP_RSQN      VARCHAR2(4000),
    TOTAL_BIDP_RSQN      VARCHAR2(4000),
    TOTAL_NTSL_BIDP_RSQN VARCHAR2(4000),
    SHNU_RSQN_RATE       VARCHAR2(4000),
    SELN_RSQN_RATE       VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_QUOTE_BALANCE_API_NAME
    on QUOTE_BALANCE (API_NAME)
/

create table SEARCH_INFO
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    STD_PDNO                    VARCHAR2(4000),
    PRDT_ENG_NAME               VARCHAR2(4000),
    NATN_CD                     VARCHAR2(4000),
    NATN_NAME                   VARCHAR2(4000),
    TR_MKET_CD                  VARCHAR2(4000),
    TR_MKET_NAME                VARCHAR2(4000),
    OVRS_EXCG_CD                VARCHAR2(4000),
    OVRS_EXCG_NAME              VARCHAR2(4000),
    TR_CRCY_CD                  VARCHAR2(4000),
    OVRS_PAPR                   VARCHAR2(4000),
    CRCY_NAME                   VARCHAR2(4000),
    OVRS_STCK_DVSN_CD           VARCHAR2(4000),
    PRDT_CLSF_CD                VARCHAR2(4000),
    PRDT_CLSF_NAME              VARCHAR2(4000),
    SLL_UNIT_QTY                VARCHAR2(4000),
    BUY_UNIT_QTY                VARCHAR2(4000),
    TR_UNIT_AMT                 VARCHAR2(4000),
    LSTG_STCK_NUM               VARCHAR2(4000),
    LSTG_DT                     VARCHAR2(4000),
    OVRS_STCK_TR_STOP_DVSN_CD   VARCHAR2(4000),
    LSTG_ABOL_ITEM_YN           VARCHAR2(4000),
    OVRS_STCK_PRDT_GRP_NO       VARCHAR2(4000),
    LSTG_YN                     VARCHAR2(4000),
    TAX_LEVY_YN                 VARCHAR2(4000),
    OVRS_STCK_ERLM_ROSN_CD      VARCHAR2(4000),
    OVRS_STCK_HIST_RGHT_DVSN_CD VARCHAR2(4000),
    CHNG_BF_PDNO                VARCHAR2(4000),
    PRDT_TYPE_CD_2              VARCHAR2(4000),
    OVRS_ITEM_NAME              VARCHAR2(4000),
    SEDOL_NO                    VARCHAR2(4000),
    BLBG_TCKR_TEXT              VARCHAR2(4000),
    OVRS_STCK_ETF_RISK_DRTP_CD  VARCHAR2(4000),
    ETP_CHAS_ERNG_RT_DBNB       VARCHAR2(4000),
    ISTT_USGE_ISIN_CD           VARCHAR2(4000),
    MINT_SVC_YN                 VARCHAR2(4000),
    MINT_SVC_YN_CHNG_DT         VARCHAR2(4000),
    PRDT_NAME                   VARCHAR2(4000),
    LEI_CD                      VARCHAR2(4000),
    OVRS_STCK_STOP_RSON_CD      VARCHAR2(4000),
    LSTG_ABOL_DT                VARCHAR2(4000),
    MINI_STK_TR_STAT_DVSN_CD    VARCHAR2(4000),
    MINT_FRST_SVC_ERLM_DT       VARCHAR2(4000),
    MINT_DCPT_TRAD_PSBL_YN      VARCHAR2(4000),
    MINT_FNUM_TRAD_PSBL_YN      VARCHAR2(4000),
    MINT_CBLC_CVSN_IPSB_YN      VARCHAR2(4000),
    PTP_ITEM_YN                 VARCHAR2(4000),
    PTP_ITEM_TRFX_EXMT_YN       VARCHAR2(4000),
    PTP_ITEM_TRFX_EXMT_STRT_DT  VARCHAR2(4000),
    PTP_ITEM_TRFX_EXMT_END_DT   VARCHAR2(4000),
    DTM_TR_PSBL_YN              VARCHAR2(4000),
    SDRF_STOP_ECLS_YN           VARCHAR2(4000),
    SDRF_STOP_ECLS_ERLM_DT      VARCHAR2(4000),
    MEMO_TEXT1                  VARCHAR2(4000),
    OVRS_NOW_PRIC1              VARCHAR2(4000),
    LAST_RCVG_DTIME             VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_SEARCH_INFO_API_NAME
    on SEARCH_INFO (API_NAME)
/

create table SEARCH_STOCK_INFO
(
    ID                        NUMBER         not null
        primary key,
    API_NAME                  VARCHAR2(4000) not null,
    PDNO                      VARCHAR2(4000),
    PRDT_TYPE_CD              VARCHAR2(4000),
    PRDT_NAME                 VARCHAR2(4000),
    PRDT_NAME120              VARCHAR2(4000),
    PRDT_ABRV_NAME            VARCHAR2(4000),
    PRDT_ENG_NAME             VARCHAR2(4000),
    PRDT_ENG_NAME120          VARCHAR2(4000),
    PRDT_ENG_ABRV_NAME        VARCHAR2(4000),
    MKET_ID_CD                VARCHAR2(4000),
    SCTY_GRP_ID_CD            VARCHAR2(4000),
    EXCG_DVSN_CD              VARCHAR2(4000),
    SETL_MMDD                 VARCHAR2(4000),
    LSTG_STQT                 VARCHAR2(4000),
    LSTG_CPTL_AMT             VARCHAR2(4000),
    CPTA                      VARCHAR2(4000),
    PAPR                      VARCHAR2(4000),
    ISSU_PRIC                 VARCHAR2(4000),
    KOSPI200_ITEM_YN          VARCHAR2(4000),
    SCTS_MKET_LSTG_DT         VARCHAR2(4000),
    SCTS_MKET_LSTG_ABOL_DT    VARCHAR2(4000),
    KOSDAQ_MKET_LSTG_DT       VARCHAR2(4000),
    KOSDAQ_MKET_LSTG_ABOL_DT  VARCHAR2(4000),
    FRBD_MKET_LSTG_DT         VARCHAR2(4000),
    FRBD_MKET_LSTG_ABOL_DT    VARCHAR2(4000),
    REITS_KIND_CD             VARCHAR2(4000),
    ETF_DVSN_CD               VARCHAR2(4000),
    OILF_FUND_YN              VARCHAR2(4000),
    IDX_BZTP_LCLS_CD          VARCHAR2(4000),
    IDX_BZTP_MCLS_CD          VARCHAR2(4000),
    IDX_BZTP_SCLS_CD          VARCHAR2(4000),
    IDX_BZTP_LCLS_CD_NAME     VARCHAR2(4000),
    IDX_BZTP_MCLS_CD_NAME     VARCHAR2(4000),
    IDX_BZTP_SCLS_CD_NAME     VARCHAR2(4000),
    STCK_KIND_CD              VARCHAR2(4000),
    MFND_OPNG_DT              VARCHAR2(4000),
    MFND_END_DT               VARCHAR2(4000),
    DPSI_ERLM_CNCL_DT         VARCHAR2(4000),
    ETF_CU_QTY                VARCHAR2(4000),
    STD_PDNO                  VARCHAR2(4000),
    DPSI_APTM_ERLM_YN         VARCHAR2(4000),
    ETF_TXTN_TYPE_CD          VARCHAR2(4000),
    ETF_TYPE_CD               VARCHAR2(4000),
    LSTG_ABOL_DT              VARCHAR2(4000),
    NWST_ODST_DVSN_CD         VARCHAR2(4000),
    SBST_PRIC                 VARCHAR2(4000),
    THCO_SBST_PRIC            VARCHAR2(4000),
    THCO_SBST_PRIC_CHNG_DT    VARCHAR2(4000),
    TR_STOP_YN                VARCHAR2(4000),
    ADMN_ITEM_YN              VARCHAR2(4000),
    THDT_CLPR                 VARCHAR2(4000),
    BFDY_CLPR                 VARCHAR2(4000),
    CLPR_CHNG_DT              VARCHAR2(4000),
    STD_IDST_CLSF_CD          VARCHAR2(4000),
    STD_IDST_CLSF_CD_NAME     VARCHAR2(4000),
    OCR_NO                    VARCHAR2(4000),
    CRFD_ITEM_YN              VARCHAR2(4000),
    ELEC_SCTY_YN              VARCHAR2(4000),
    ISSU_ISTT_CD              VARCHAR2(4000),
    ETF_CHAS_ERNG_RT_DBNB     VARCHAR2(4000),
    ETF_ETN_IVST_HEED_ITEM_YN VARCHAR2(4000),
    STLN_INT_RT_DVSN_CD       VARCHAR2(4000),
    FRNR_PSNL_LMT_RT          VARCHAR2(4000),
    LSTG_RQSR_ISSU_ISTT_CD    VARCHAR2(4000),
    LSTG_RQSR_ITEM_CD         VARCHAR2(4000),
    TRST_ISTT_ISSU_ISTT_CD    VARCHAR2(4000),
    CPTT_TRAD_TR_PSBL_YN      VARCHAR2(4000),
    NXT_TR_STOP_YN            VARCHAR2(4000),
    CREATED_AT                DATE           not null
)
/

create index IX_SEARCH_STOCK_INFO_API_NAME
    on SEARCH_STOCK_INFO (API_NAME)
/

create table SHORT_SALE
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD    VARCHAR2(4000),
    HTS_KOR_ISNM      VARCHAR2(4000),
    STCK_PRPR         VARCHAR2(4000),
    PRDY_VRSS         VARCHAR2(4000),
    PRDY_VRSS_SIGN    VARCHAR2(4000),
    PRDY_CTRT         VARCHAR2(4000),
    ACML_VOL          VARCHAR2(4000),
    ACML_TR_PBMN      VARCHAR2(4000),
    SSTS_CNTG_QTY     VARCHAR2(4000),
    SSTS_VOL_RLIM     VARCHAR2(4000),
    SSTS_TR_PBMN      VARCHAR2(4000),
    SSTS_TR_PBMN_RLIM VARCHAR2(4000),
    STND_DATE1        VARCHAR2(4000),
    STND_DATE2        VARCHAR2(4000),
    AVRG_PRC          VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_SHORT_SALE_API_NAME
    on SHORT_SALE (API_NAME)
/

create table TOP_INTEREST_STOCK
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD      VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    STCK_PRPR           VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    ACML_TR_PBMN        VARCHAR2(4000),
    ASKP                VARCHAR2(4000),
    BIDP                VARCHAR2(4000),
    DATA_RANK           VARCHAR2(4000),
    INTER_ISSU_REG_CSNU VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_TOP_INTEREST_STOCK_API_NAME
    on TOP_INTEREST_STOCK (API_NAME)
/

create table TRADED_BY_COMPANY
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    DATA_RANK      VARCHAR2(4000),
    MKSC_SHRN_ISCD VARCHAR2(4000),
    HTS_KOR_ISNM   VARCHAR2(4000),
    STCK_PRPR      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    ACML_TR_PBMN   VARCHAR2(4000),
    SELN_CNQN_SMTN VARCHAR2(4000),
    SHNU_CNQN_SMTN VARCHAR2(4000),
    NTBY_CNQN      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_TRADED_BY_COMPANY_API_NAME
    on TRADED_BY_COMPANY (API_NAME)
/

create table TRADPRT_BYAMT
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    PRPR_NAME          VARCHAR2(4000),
    SMTN_AVRG_PRPR     VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    WHOL_NTBY_QTY_RATE VARCHAR2(4000),
    NTBY_CNTG_CSNU     VARCHAR2(4000),
    SELN_CNQN_SMTN     VARCHAR2(4000),
    WHOL_SELN_VOL_RATE VARCHAR2(4000),
    SELN_CNTG_CSNU     VARCHAR2(4000),
    SHNU_CNQN_SMTN     VARCHAR2(4000),
    WHOL_SHUN_VOL_RATE VARCHAR2(4000),
    SHNU_CNTG_CSNU     VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_TRADPRT_BYAMT_API_NAME
    on TRADPRT_BYAMT (API_NAME)
/

create table VOLUME_POWER
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    KNAM       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    TPOW       VARCHAR2(4000),
    POWX       VARCHAR2(4000),
    ENAM       VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    BIVL       VARCHAR2(4000),
    ASVL       VARCHAR2(4000),
    STRN       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_VOLUME_POWER_API_NAME
    on VOLUME_POWER (API_NAME)
/

create table VOLUME_RANK
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    ELW_KOR_ISNM        VARCHAR2(4000),
    ELW_SHRN_ISCD       VARCHAR2(4000),
    ELW_PRPR            VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    LSTN_STCN           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    N_PRDY_VOL          VARCHAR2(4000),
    N_PRDY_VOL_VRSS     VARCHAR2(4000),
    VOL_INRT            VARCHAR2(4000),
    VOL_TNRT            VARCHAR2(4000),
    NDAY_VOL_TNRT       VARCHAR2(4000),
    ACML_TR_PBMN        VARCHAR2(4000),
    N_PRDY_TR_PBMN      VARCHAR2(4000),
    N_PRDY_TR_PBMN_VRSS VARCHAR2(4000),
    TOTAL_ASKP_RSQN     VARCHAR2(4000),
    TOTAL_BIDP_RSQN     VARCHAR2(4000),
    NTSL_RSQN           VARCHAR2(4000),
    NTBY_RSQN           VARCHAR2(4000),
    SELN_RSQN_RATE      VARCHAR2(4000),
    SHNU_RSQN_RATE      VARCHAR2(4000),
    STCK_CNVR_RATE      VARCHAR2(4000),
    HTS_RMNN_DYNU       VARCHAR2(4000),
    INVL_VAL            VARCHAR2(4000),
    TMVL_VAL            VARCHAR2(4000),
    ACPR                VARCHAR2(4000),
    UNAS_ISNM           VARCHAR2(4000),
    STCK_LAST_TR_DATE   VARCHAR2(4000),
    UNAS_SHRN_ISCD      VARCHAR2(4000),
    PRDY_VOL            VARCHAR2(4000),
    LP_HLDN_RATE        VARCHAR2(4000),
    PRIT                VARCHAR2(4000),
    PRLS_QRYR_STPR_PRC  VARCHAR2(4000),
    DELTA_VAL           VARCHAR2(4000),
    THETA               VARCHAR2(4000),
    PRLS_QRYR_RATE      VARCHAR2(4000),
    STCK_LSTN_DATE      VARCHAR2(4000),
    HTS_INTS_VLTL       VARCHAR2(4000),
    LVRG_VAL            VARCHAR2(4000),
    LP_NTBY_QTY         VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_VOLUME_RANK_API_NAME
    on VOLUME_RANK (API_NAME)
/

create table COMPARE_STOCKS
(
    ID            NUMBER         not null
        primary key,
    API_NAME      VARCHAR2(4000) not null,
    ELW_SHRN_ISCD VARCHAR2(4000),
    ELW_KOR_ISNM  VARCHAR2(4000),
    CREATED_AT    DATE           not null
)
/

create index IX_COMPARE_STOCKS_API_NAME
    on COMPARE_STOCKS (API_NAME)
/

create table COND_SEARCH
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    BOND_SHRN_ISCD      VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    RGHT_TYPE_NAME      VARCHAR2(4000),
    ELW_PRPR            VARCHAR2(4000),
    PRDY_VRSS           VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    ACPR                VARCHAR2(4000),
    STCK_CNVR_RATE      VARCHAR2(4000),
    STCK_LSTN_DATE      VARCHAR2(4000),
    STCK_LAST_TR_DATE   VARCHAR2(4000),
    HTS_RMNN_DYNU       VARCHAR2(4000),
    UNAS_ISNM           VARCHAR2(4000),
    UNAS_PRPR           VARCHAR2(4000),
    UNAS_PRDY_VRSS      VARCHAR2(4000),
    UNAS_PRDY_VRSS_SIGN VARCHAR2(4000),
    UNAS_PRDY_CTRT      VARCHAR2(4000),
    UNAS_ACML_VOL       VARCHAR2(4000),
    MONEYNESS           VARCHAR2(4000),
    ATM_CLS_NAME        VARCHAR2(4000),
    PRIT                VARCHAR2(4000),
    DELTA_VAL           VARCHAR2(4000),
    HTS_INTS_VLTL       VARCHAR2(4000),
    TMVL_VAL            VARCHAR2(4000),
    GEAR                VARCHAR2(4000),
    LVRG_VAL            VARCHAR2(4000),
    PRLS_QRYR_RATE      VARCHAR2(4000),
    CFP                 VARCHAR2(4000),
    LSTN_STCN           VARCHAR2(4000),
    PBLC_CO_NAME        VARCHAR2(4000),
    LP_MBCR_NAME        VARCHAR2(4000),
    LP_HLDN_RATE        VARCHAR2(4000),
    ELW_RGHT_FORM       VARCHAR2(4000),
    ELW_KO_BARRIER      VARCHAR2(4000),
    APPRCH_RATE         VARCHAR2(4000),
    UNAS_SHRN_ISCD      VARCHAR2(4000),
    MTRT_DATE           VARCHAR2(4000),
    PRMM_VAL            VARCHAR2(4000),
    STCK_LP_FIN_DATE    VARCHAR2(4000),
    TICK_CONV_PRC       VARCHAR2(4000),
    PRLS_QRYR_STPR_PRC  VARCHAR2(4000),
    LP_HVOL             VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_COND_SEARCH_API_NAME
    on COND_SEARCH (API_NAME)
/

create table ELW_ASKING_PRICE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD      VARCHAR2(4000),
    BSOP_HOUR           VARCHAR2(4000),
    HOUR_CLS_CODE       VARCHAR2(4000),
    ASKP1               VARCHAR2(4000),
    ASKP2               VARCHAR2(4000),
    ASKP3               VARCHAR2(4000),
    ASKP4               VARCHAR2(4000),
    ASKP5               VARCHAR2(4000),
    ASKP6               VARCHAR2(4000),
    ASKP7               VARCHAR2(4000),
    ASKP8               VARCHAR2(4000),
    ASKP9               VARCHAR2(4000),
    ASKP10              VARCHAR2(4000),
    BIDP1               VARCHAR2(4000),
    BIDP2               VARCHAR2(4000),
    BIDP3               VARCHAR2(4000),
    BIDP4               VARCHAR2(4000),
    BIDP5               VARCHAR2(4000),
    BIDP6               VARCHAR2(4000),
    BIDP7               VARCHAR2(4000),
    BIDP8               VARCHAR2(4000),
    BIDP9               VARCHAR2(4000),
    BIDP10              VARCHAR2(4000),
    ASKP_RSQN1          VARCHAR2(4000),
    ASKP_RSQN2          VARCHAR2(4000),
    ASKP_RSQN3          VARCHAR2(4000),
    ASKP_RSQN4          VARCHAR2(4000),
    ASKP_RSQN5          VARCHAR2(4000),
    ASKP_RSQN6          VARCHAR2(4000),
    ASKP_RSQN7          VARCHAR2(4000),
    ASKP_RSQN8          VARCHAR2(4000),
    ASKP_RSQN9          VARCHAR2(4000),
    ASKP_RSQN10         VARCHAR2(4000),
    BIDP_RSQN1          VARCHAR2(4000),
    BIDP_RSQN2          VARCHAR2(4000),
    BIDP_RSQN3          VARCHAR2(4000),
    BIDP_RSQN4          VARCHAR2(4000),
    BIDP_RSQN5          VARCHAR2(4000),
    BIDP_RSQN6          VARCHAR2(4000),
    BIDP_RSQN7          VARCHAR2(4000),
    BIDP_RSQN8          VARCHAR2(4000),
    BIDP_RSQN9          VARCHAR2(4000),
    BIDP_RSQN10         VARCHAR2(4000),
    TOTAL_ASKP_RSQN     VARCHAR2(4000),
    TOTAL_BIDP_RSQN     VARCHAR2(4000),
    ANTC_CNPR           VARCHAR2(4000),
    ANTC_CNQN           VARCHAR2(4000),
    ANTC_CNTG_VRSS_SIGN VARCHAR2(4000),
    ANTC_CNTG_VRSS      VARCHAR2(4000),
    ANTC_CNTG_PRDY_CTRT VARCHAR2(4000),
    LP_ASKP_RSQN1       VARCHAR2(4000),
    LP_ASKP_RSQN2       VARCHAR2(4000),
    LP_ASKP_RSQN3       VARCHAR2(4000),
    LP_BIDP_RSQN4       VARCHAR2(4000),
    LP_ASKP_RSQN4       VARCHAR2(4000),
    LP_BIDP_RSQN5       VARCHAR2(4000),
    LP_ASKP_RSQN5       VARCHAR2(4000),
    LP_BIDP_RSQN6       VARCHAR2(4000),
    LP_ASKP_RSQN6       VARCHAR2(4000),
    LP_BIDP_RSQN7       VARCHAR2(4000),
    LP_ASKP_RSQN7       VARCHAR2(4000),
    LP_ASKP_RSQN8       VARCHAR2(4000),
    LP_BIDP_RSQN8       VARCHAR2(4000),
    LP_ASKP_RSQN9       VARCHAR2(4000),
    LP_BIDP_RSQN9       VARCHAR2(4000),
    LP_ASKP_RSQN10      VARCHAR2(4000),
    LP_BIDP_RSQN10      VARCHAR2(4000),
    LP_BIDP_RSQN1       VARCHAR2(4000),
    LP_TOTAL_ASKP_RSQN  VARCHAR2(4000),
    LP_BIDP_RSQN2       VARCHAR2(4000),
    LP_TOTAL_BIDP_RSQN  VARCHAR2(4000),
    LP_BIDP_RSQN3       VARCHAR2(4000),
    ANTC_VOL            VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_ELW_ASKING_PRICE_API_NAME
    on ELW_ASKING_PRICE (API_NAME)
/

create table ELW_CCNL
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD               VARCHAR2(4000),
    STCK_CNTG_HOUR               VARCHAR2(4000),
    STCK_PRPR                    VARCHAR2(4000),
    PRDY_VRSS_SIGN               VARCHAR2(4000),
    PRDY_VRSS                    VARCHAR2(4000),
    PRDY_CTRT                    VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC           VARCHAR2(4000),
    STCK_OPRC                    VARCHAR2(4000),
    STCK_HGPR                    VARCHAR2(4000),
    STCK_LWPR                    VARCHAR2(4000),
    ASKP1                        VARCHAR2(4000),
    BIDP1                        VARCHAR2(4000),
    CNTG_VOL                     VARCHAR2(4000),
    ACML_VOL                     VARCHAR2(4000),
    ACML_TR_PBMN                 VARCHAR2(4000),
    SELN_CNTG_CSNU               VARCHAR2(4000),
    SHNU_CNTG_CSNU               VARCHAR2(4000),
    NTBY_CNTG_CSNU               VARCHAR2(4000),
    CTTR                         VARCHAR2(4000),
    SELN_CNTG_SMTN               VARCHAR2(4000),
    SHNU_CNTG_SMTN               VARCHAR2(4000),
    CNTG_CLS_CODE                VARCHAR2(4000),
    SHNU_RATE                    VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE  VARCHAR2(4000),
    OPRC_HOUR                    VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN          VARCHAR2(4000),
    OPRC_VRSS_PRPR               VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    HGPR_VRSS_PRPR               VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN          VARCHAR2(4000),
    LWPR_VRSS_PRPR               VARCHAR2(4000),
    BSOP_DATE                    VARCHAR2(4000),
    NEW_MKOP_CLS_CODE            VARCHAR2(4000),
    TRHT_YN                      VARCHAR2(4000),
    ASKP_RSQN1                   VARCHAR2(4000),
    BIDP_RSQN1                   VARCHAR2(4000),
    TOTAL_ASKP_RSQN              VARCHAR2(4000),
    TOTAL_BIDP_RSQN              VARCHAR2(4000),
    VOL_RATE                     VARCHAR2(4000),
    PRDY_VRSS_VOL_RATE           VARCHAR2(4000),
    ASKP_RSQN_ICDC               VARCHAR2(4000),
    BIDP_RSQN_ICDC               VARCHAR2(4000),
    HOUR_CLS_CODE                VARCHAR2(4000),
    MRKT_TRTM_CLS_CODE           VARCHAR2(4000),
    VI_CLS_CODE                  VARCHAR2(4000),
    TIMR_VAL                     VARCHAR2(4000),
    PARITY                       VARCHAR2(4000),
    PRM_VAL                      VARCHAR2(4000),
    GEAR                         VARCHAR2(4000),
    BEP_RATE                     VARCHAR2(4000),
    ITMV_VAL                     VARCHAR2(4000),
    PRM_RATE                     VARCHAR2(4000),
    SPPT_PNT                     VARCHAR2(4000),
    LVRG_VAL                     VARCHAR2(4000),
    DELTA                        VARCHAR2(4000),
    GAMMA                        VARCHAR2(4000),
    VEGA                         VARCHAR2(4000),
    THETA                        VARCHAR2(4000),
    RHO                          VARCHAR2(4000),
    HTS_ANTC_VOL                 VARCHAR2(4000),
    HTS_THEO_PRC                 VARCHAR2(4000),
    VOL_TNRT                     VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL      VARCHAR2(4000),
    PRDY_SMNS_HOUR_ACML_VOL_RATE VARCHAR2(4000),
    APPRCH_RATE                  VARCHAR2(4000),
    LP_HVOL                      VARCHAR2(4000),
    LP_HLDN_RATE                 VARCHAR2(4000),
    LP_NTBY_QTY                  VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_ELW_CCNL_API_NAME
    on ELW_CCNL (API_NAME)
/

create table ELW_EXP_CCNL
(
    ID                          NUMBER         not null
        primary key,
    API_NAME                    VARCHAR2(4000) not null,
    MKSC_SHRN_ISCD              VARCHAR2(4000),
    STCK_CNTG_HOUR              VARCHAR2(4000),
    STCK_PRPR                   VARCHAR2(4000),
    PRDY_VRSS_SIGN              VARCHAR2(4000),
    PRDY_VRSS                   VARCHAR2(4000),
    PRDY_CTRT                   VARCHAR2(4000),
    WGHN_AVRG_STCK_PRC          VARCHAR2(4000),
    STCK_OPRC                   VARCHAR2(4000),
    STCK_HGPR                   VARCHAR2(4000),
    STCK_LWPR                   VARCHAR2(4000),
    ASKP1                       VARCHAR2(4000),
    BIDP1                       VARCHAR2(4000),
    CNTG_VOL                    VARCHAR2(4000),
    ACML_VOL                    VARCHAR2(4000),
    ACML_TR_PBMN                VARCHAR2(4000),
    SELN_CNTG_CSNU              VARCHAR2(4000),
    SHNU_CNTG_CSNU              VARCHAR2(4000),
    NTBY_CNTG_CSNU              VARCHAR2(4000),
    CTTR                        VARCHAR2(4000),
    SELN_CNTG_SMTN              VARCHAR2(4000),
    SHNU_CNTG_SMTN              VARCHAR2(4000),
    CNTG_CLS_CODE               VARCHAR2(4000),
    SHNU_RATE                   VARCHAR2(4000),
    PRDY_VOL_VRSS_ACML_VOL_RATE VARCHAR2(4000),
    OPRC_HOUR                   VARCHAR2(4000),
    OPRC_VRSS_PRPR_SIGN         VARCHAR2(4000),
    OPRC_VRSS_PRPR              VARCHAR2(4000),
    HGPR_HOUR                   VARCHAR2(4000),
    HGPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    HGPR_VRSS_PRPR              VARCHAR2(4000),
    LWPR_HOUR                   VARCHAR2(4000),
    LWPR_VRSS_PRPR_SIGN         VARCHAR2(4000),
    LWPR_VRSS_PRPR              VARCHAR2(4000),
    BSOP_DATE                   VARCHAR2(4000),
    NEW_MKOP_CLS_CODE           VARCHAR2(4000),
    TRHT_YN                     VARCHAR2(4000),
    ASKP_RSQN1                  VARCHAR2(4000),
    BIDP_RSQN1                  VARCHAR2(4000),
    TOTAL_ASKP_RSQN             VARCHAR2(4000),
    TOTAL_BIDP_RSQN             VARCHAR2(4000),
    TMVL_VAL                    VARCHAR2(4000),
    PRIT                        VARCHAR2(4000),
    PRMM_VAL                    VARCHAR2(4000),
    GEAR                        VARCHAR2(4000),
    PRLS_QRYR_RATE              VARCHAR2(4000),
    INVL_VAL                    VARCHAR2(4000),
    PRMM_RATE                   VARCHAR2(4000),
    CFP                         VARCHAR2(4000),
    LVRG_VAL                    VARCHAR2(4000),
    DELTA                       VARCHAR2(4000),
    GAMA                        VARCHAR2(4000),
    VEGA                        VARCHAR2(4000),
    THETA                       VARCHAR2(4000),
    RHO                         VARCHAR2(4000),
    HTS_INTS_VLTL               VARCHAR2(4000),
    HTS_THPR                    VARCHAR2(4000),
    VOL_TNRT                    VARCHAR2(4000),
    LP_HVOL                     VARCHAR2(4000),
    LP_HLDN_RATE                VARCHAR2(4000),
    CREATED_AT                  DATE           not null
)
/

create index IX_ELW_EXP_CCNL_API_NAME
    on ELW_EXP_CCNL (API_NAME)
/

create table EXPIRATION_STOCKS
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    ELW_SHRN_ISCD     VARCHAR2(4000),
    ELW_KOR_ISNM      VARCHAR2(4000),
    UNAS_ISNM         VARCHAR2(4000),
    UNAS_PRPR         VARCHAR2(4000),
    ACPR              VARCHAR2(4000),
    STCK_CNVR_RATE    VARCHAR2(4000),
    ELW_PRPR          VARCHAR2(4000),
    STCK_LSTN_DATE    VARCHAR2(4000),
    STCK_LAST_TR_DATE VARCHAR2(4000),
    TOTAL_RDMP_AMT    VARCHAR2(4000),
    RDMP_AMT          VARCHAR2(4000),
    LSTN_STCN         VARCHAR2(4000),
    LP_HVOL           VARCHAR2(4000),
    CCLS_PAYM_PRC     VARCHAR2(4000),
    MTRT_VLTN_AMT     VARCHAR2(4000),
    EVNT_PRD_FIN_DATE VARCHAR2(4000),
    STLM_DATE         VARCHAR2(4000),
    PBLC_PRC          VARCHAR2(4000),
    UNAS_SHRN_ISCD    VARCHAR2(4000),
    STND_ISCD         VARCHAR2(4000),
    RDMP_ASK_AMT      VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_EXPIRATION_STOCKS_API_NAME
    on EXPIRATION_STOCKS (API_NAME)
/

create table INDICATOR
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    ELW_SHRN_ISCD  VARCHAR2(4000),
    ELW_KOR_ISNM   VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    STCK_CNVR_RATE VARCHAR2(4000),
    LVRG_VAL       VARCHAR2(4000),
    ACPR           VARCHAR2(4000),
    TMVL_VAL       VARCHAR2(4000),
    INVL_VAL       VARCHAR2(4000),
    ELW_KO_BARRIER VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_INDICATOR_API_NAME
    on INDICATOR (API_NAME)
/

create table INDICATOR_TREND_CCNL
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STCK_CNTG_HOUR VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    LVRG_VAL       VARCHAR2(4000),
    GEAR           VARCHAR2(4000),
    TMVL_VAL       VARCHAR2(4000),
    INVL_VAL       VARCHAR2(4000),
    PRIT           VARCHAR2(4000),
    APPRCH_RATE    VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_INDICATOR_TREND_CCNL_API_NAME
    on INDICATOR_TREND_CCNL (API_NAME)
/

create table INDICATOR_TREND_DAILY
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STCK_BSOP_DATE VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    LVRG_VAL       VARCHAR2(4000),
    GEAR           VARCHAR2(4000),
    TMVL_VAL       VARCHAR2(4000),
    INVL_VAL       VARCHAR2(4000),
    PRIT           VARCHAR2(4000),
    ELW_OPRC       VARCHAR2(4000),
    ELW_HGPR       VARCHAR2(4000),
    ELW_LWPR       VARCHAR2(4000),
    APPRCH_RATE    VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_INDICATOR_TREND_DAILY_API_NAME
    on INDICATOR_TREND_DAILY (API_NAME)
/

create table INDICATOR_TREND_MINUTE
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STCK_BSOP_DATE VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    ELW_OPRC       VARCHAR2(4000),
    ELW_HGPR       VARCHAR2(4000),
    ELW_LWPR       VARCHAR2(4000),
    LVRG_VAL       VARCHAR2(4000),
    GEAR           VARCHAR2(4000),
    PRMM_VAL       VARCHAR2(4000),
    INVL_VAL       VARCHAR2(4000),
    PRIT           VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    CNTG_VOL       VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_INDICATOR_TREND_MINUTE_API_NAME
    on INDICATOR_TREND_MINUTE (API_NAME)
/

create table LP_TRADE_TREND
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    CNTG_HOUR      VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    ACML_TR_PBMN   VARCHAR2(4000),
    LP_BUY_QTY     VARCHAR2(4000),
    LP_SELL_QTY    VARCHAR2(4000),
    LP_NTBY_QTY    VARCHAR2(4000),
    LP_BUY_AMT     VARCHAR2(4000),
    LP_SELL_AMT    VARCHAR2(4000),
    LP_NTBY_AMT    VARCHAR2(4000),
    INST_DEAL_QTY  VARCHAR2(4000),
    FRGN_DEAL_QTY  VARCHAR2(4000),
    PRSN_DEAL_QTY  VARCHAR2(4000),
    APPRCH_RATE    VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_LP_TRADE_TREND_API_NAME
    on LP_TRADE_TREND (API_NAME)
/

create table NEWLY_LISTED
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    ELW_SHRN_ISCD     VARCHAR2(4000),
    UNAS_ISNM         VARCHAR2(4000),
    LSTN_STCN         VARCHAR2(4000),
    ACPR              VARCHAR2(4000),
    STCK_LAST_TR_DATE VARCHAR2(4000),
    ELW_KO_BARRIER    VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_NEWLY_LISTED_API_NAME
    on NEWLY_LISTED (API_NAME)
/

create table QUICK_CHANGE
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    ELW_SHRN_ISCD   VARCHAR2(4000),
    ELW_KOR_ISNM    VARCHAR2(4000),
    ELW_PRPR        VARCHAR2(4000),
    PRDY_VRSS_SIGN  VARCHAR2(4000),
    PRDY_VRSS       VARCHAR2(4000),
    PRDY_CTRT       VARCHAR2(4000),
    ASKP            VARCHAR2(4000),
    BIDP            VARCHAR2(4000),
    TOTAL_ASKP_RSQN VARCHAR2(4000),
    TOTAL_BIDP_RSQN VARCHAR2(4000),
    ACML_VOL        VARCHAR2(4000),
    STND_VAL        VARCHAR2(4000),
    STND_VAL_VRSS   VARCHAR2(4000),
    STND_VAL_CTRT   VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_QUICK_CHANGE_API_NAME
    on QUICK_CHANGE (API_NAME)
/

create table SENSITIVITY
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    ELW_SHRN_ISCD  VARCHAR2(4000),
    ELW_KOR_ISNM   VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    HTS_THPR       VARCHAR2(4000),
    DELTA_VAL      VARCHAR2(4000),
    GAMA           VARCHAR2(4000),
    THETA          VARCHAR2(4000),
    VEGA           VARCHAR2(4000),
    RHO            VARCHAR2(4000),
    HTS_INTS_VLTL  VARCHAR2(4000),
    D90_HIST_VLTL  VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_SENSITIVITY_API_NAME
    on SENSITIVITY (API_NAME)
/

create table SENSITIVITY_TREND_CCNL
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STCK_CNTG_HOUR VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    HTS_THPR       VARCHAR2(4000),
    DELTA_VAL      VARCHAR2(4000),
    GAMA           VARCHAR2(4000),
    THETA          VARCHAR2(4000),
    VEGA           VARCHAR2(4000),
    RHO            VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_SENSITIVITY_TREND_CCNL_API_NAME
    on SENSITIVITY_TREND_CCNL (API_NAME)
/

create table SENSITIVITY_TREND_DAILY
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STCK_BSOP_DATE VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    HTS_THPR       VARCHAR2(4000),
    DELTA_VAL      VARCHAR2(4000),
    GAMA           VARCHAR2(4000),
    THETA          VARCHAR2(4000),
    VEGA           VARCHAR2(4000),
    RHO            VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_SENSITIVITY_TREND_DAILY_API_NAME
    on SENSITIVITY_TREND_DAILY (API_NAME)
/

create table UDRL_ASSET_LIST
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    UNAS_SHRN_ISCD      VARCHAR2(4000),
    UNAS_ISNM           VARCHAR2(4000),
    UNAS_PRPR           VARCHAR2(4000),
    UNAS_PRDY_VRSS      VARCHAR2(4000),
    UNAS_PRDY_VRSS_SIGN VARCHAR2(4000),
    UNAS_PRDY_CTRT      VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_UDRL_ASSET_LIST_API_NAME
    on UDRL_ASSET_LIST (API_NAME)
/

create table UDRL_ASSET_PRICE
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    ELW_SHRN_ISCD      VARCHAR2(4000),
    HTS_KOR_ISNM       VARCHAR2(4000),
    ELW_PRPR           VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    ACPR               VARCHAR2(4000),
    PRLS_QRYR_STPR_PRC VARCHAR2(4000),
    HTS_RMNN_DYNU      VARCHAR2(4000),
    HTS_INTS_VLTL      VARCHAR2(4000),
    STCK_CNVR_RATE     VARCHAR2(4000),
    LP_HVOL            VARCHAR2(4000),
    LP_RLIM            VARCHAR2(4000),
    LVRG_VAL           VARCHAR2(4000),
    GEAR               VARCHAR2(4000),
    DELTA_VAL          VARCHAR2(4000),
    GAMA               VARCHAR2(4000),
    VEGA               VARCHAR2(4000),
    THETA              VARCHAR2(4000),
    PRLS_QRYR_RATE     VARCHAR2(4000),
    CFP                VARCHAR2(4000),
    PRIT               VARCHAR2(4000),
    INVL_VAL           VARCHAR2(4000),
    TMVL_VAL           VARCHAR2(4000),
    HTS_THPR           VARCHAR2(4000),
    STCK_LSTN_DATE     VARCHAR2(4000),
    STCK_LAST_TR_DATE  VARCHAR2(4000),
    LP_NTBY_QTY        VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_UDRL_ASSET_PRICE_API_NAME
    on UDRL_ASSET_PRICE (API_NAME)
/

create table UPDOWN_RATE
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    CREC       VARCHAR2(4000),
    TREC       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    N_BASE     VARCHAR2(4000),
    N_DIFF     VARCHAR2(4000),
    N_RATE     VARCHAR2(4000),
    RANK       VARCHAR2(4000),
    ENAME      VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_UPDOWN_RATE_API_NAME
    on UPDOWN_RATE (API_NAME)
/

create table VOLATILITY_TREND_CCNL
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STCK_CNTG_HOUR VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    BIDP           VARCHAR2(4000),
    ASKP           VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    HTS_INTS_VLTL  VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_VOLATILITY_TREND_CCNL_API_NAME
    on VOLATILITY_TREND_CCNL (API_NAME)
/

create table VOLATILITY_TREND_DAILY
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STCK_BSOP_DATE VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    PRDY_VRSS      VARCHAR2(4000),
    PRDY_VRSS_SIGN VARCHAR2(4000),
    PRDY_CTRT      VARCHAR2(4000),
    ELW_OPRC       VARCHAR2(4000),
    ELW_HGPR       VARCHAR2(4000),
    ELW_LWPR       VARCHAR2(4000),
    ACML_VOL       VARCHAR2(4000),
    D10_HIST_VLTL  VARCHAR2(4000),
    D20_HIST_VLTL  VARCHAR2(4000),
    D30_HIST_VLTL  VARCHAR2(4000),
    D60_HIST_VLTL  VARCHAR2(4000),
    D90_HIST_VLTL  VARCHAR2(4000),
    HTS_INTS_VLTL  VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_VOLATILITY_TREND_DAILY_API_NAME
    on VOLATILITY_TREND_DAILY (API_NAME)
/

create table VOLATILITY_TREND_MINUTE
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    STCK_BSOP_DATE VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    STCK_PRPR      VARCHAR2(4000),
    ELW_OPRC       VARCHAR2(4000),
    ELW_HGPR       VARCHAR2(4000),
    ELW_LWPR       VARCHAR2(4000),
    HTS_INTS_VLTL  VARCHAR2(4000),
    HIST_VLTL      VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_VOLATILITY_TREND_MINUTE_API_NAME
    on VOLATILITY_TREND_MINUTE (API_NAME)
/

create table VOLATILITY_TREND_TICK
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null,
    BSOP_DATE      VARCHAR2(4000),
    STCK_CNTG_HOUR VARCHAR2(4000),
    ELW_PRPR       VARCHAR2(4000),
    HTS_INTS_VLTL  VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_VOLATILITY_TREND_TICK_API_NAME
    on VOLATILITY_TREND_TICK (API_NAME)
/

create table ETF_NAV_TREND
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    RT_CD              VARCHAR2(4000),
    MSG_CD             VARCHAR2(4000),
    MKSC_SHRN_ISCD     VARCHAR2(4000),
    NAV                VARCHAR2(4000),
    NAV_PRDY_VRSS_SIGN VARCHAR2(4000),
    NAV_PRDY_VRSS      VARCHAR2(4000),
    NAV_PRDY_CTRT      VARCHAR2(4000),
    OPRC_NAV           VARCHAR2(4000),
    HPRC_NAV           VARCHAR2(4000),
    LPRC_NAV           VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_ETF_NAV_TREND_API_NAME
    on ETF_NAV_TREND (API_NAME)
/

create table INQUIRE_COMPONENT_STOCK_PRICE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    STCK_PRPR            VARCHAR2(4000),
    PRDY_VRSS            VARCHAR2(4000),
    PRDY_VRSS_SIGN       VARCHAR2(4000),
    PRDY_CTRT            VARCHAR2(4000),
    ETF_CNFG_ISSU_AVLS   VARCHAR2(4000),
    NAV                  VARCHAR2(4000),
    NAV_PRDY_VRSS_SIGN   VARCHAR2(4000),
    NAV_PRDY_VRSS        VARCHAR2(4000),
    NAV_PRDY_CTRT        VARCHAR2(4000),
    ETF_NTAS_TTAM        VARCHAR2(4000),
    PRDY_CLPR_NAV        VARCHAR2(4000),
    OPRC_NAV             VARCHAR2(4000),
    HPRC_NAV             VARCHAR2(4000),
    LPRC_NAV             VARCHAR2(4000),
    ETF_CU_UNIT_SCRT_CNT VARCHAR2(4000),
    ETF_CNFG_ISSU_CNT    VARCHAR2(4000),
    STCK_SHRN_ISCD       VARCHAR2(4000),
    HTS_KOR_ISNM         VARCHAR2(4000),
    ACML_VOL             VARCHAR2(4000),
    ACML_TR_PBMN         VARCHAR2(4000),
    TDAY_RSFL_RATE       VARCHAR2(4000),
    PRDY_VRSS_VOL        VARCHAR2(4000),
    TR_PBMN_TNRT         VARCHAR2(4000),
    HTS_AVLS             VARCHAR2(4000),
    ETF_VLTN_AMT         VARCHAR2(4000),
    ETF_CNFG_ISSU_RLIM   VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_INQUIRE_COMPONENT_STOCK_PRICE_API_NAME
    on INQUIRE_COMPONENT_STOCK_PRICE (API_NAME)
/

create table NAV_COMPARISON_DAILY_TREND
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    STCK_BSOP_DATE     VARCHAR2(4000),
    STCK_CLPR          VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    CNTG_VOL           VARCHAR2(4000),
    DPRT               VARCHAR2(4000),
    NAV_VRSS_PRPR      VARCHAR2(4000),
    NAV                VARCHAR2(4000),
    NAV_PRDY_VRSS_SIGN VARCHAR2(4000),
    NAV_PRDY_VRSS      VARCHAR2(4000),
    NAV_PRDY_CTRT      VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_NAV_COMPARISON_DAILY_TREND_API_NAME
    on NAV_COMPARISON_DAILY_TREND (API_NAME)
/

create table NAV_COMPARISON_TIME_TREND
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    BSOP_HOUR          VARCHAR2(4000),
    NAV                VARCHAR2(4000),
    NAV_PRDY_VRSS_SIGN VARCHAR2(4000),
    NAV_PRDY_VRSS      VARCHAR2(4000),
    NAV_PRDY_CTRT      VARCHAR2(4000),
    NAV_VRSS_PRPR      VARCHAR2(4000),
    DPRT               VARCHAR2(4000),
    STCK_PRPR          VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    CNTG_VOL           VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_NAV_COMPARISON_TIME_TREND_API_NAME
    on NAV_COMPARISON_TIME_TREND (API_NAME)
/

create table NAV_COMPARISON_TREND
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    STCK_PRPR          VARCHAR2(4000),
    PRDY_VRSS          VARCHAR2(4000),
    PRDY_VRSS_SIGN     VARCHAR2(4000),
    PRDY_CTRT          VARCHAR2(4000),
    ACML_VOL           VARCHAR2(4000),
    ACML_TR_PBMN       VARCHAR2(4000),
    STCK_PRDY_CLPR     VARCHAR2(4000),
    STCK_OPRC          VARCHAR2(4000),
    STCK_HGPR          VARCHAR2(4000),
    STCK_LWPR          VARCHAR2(4000),
    STCK_MXPR          VARCHAR2(4000),
    STCK_LLAM          VARCHAR2(4000),
    NAV                VARCHAR2(4000),
    NAV_PRDY_VRSS_SIGN VARCHAR2(4000),
    NAV_PRDY_VRSS      VARCHAR2(4000),
    NAV_PRDY_CTRT      VARCHAR2(4000),
    PRDY_CLPR_NAV      VARCHAR2(4000),
    OPRC_NAV           VARCHAR2(4000),
    HPRC_NAV           VARCHAR2(4000),
    LPRC_NAV           VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_NAV_COMPARISON_TREND_API_NAME
    on NAV_COMPARISON_TREND (API_NAME)
/

create table ASKING_PRICE
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    SYMB       VARCHAR2(4000),
    ZDIV       VARCHAR2(4000),
    XYMD       VARCHAR2(4000),
    XHMS       VARCHAR2(4000),
    KYMD       VARCHAR2(4000),
    KHMS       VARCHAR2(4000),
    BVOL       VARCHAR2(4000),
    AVOL       VARCHAR2(4000),
    BDVL       VARCHAR2(4000),
    ADVL       VARCHAR2(4000),
    PBID1      VARCHAR2(4000),
    PASK1      VARCHAR2(4000),
    VBID1      VARCHAR2(4000),
    VASK1      VARCHAR2(4000),
    DBID1      VARCHAR2(4000),
    DASK1      VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_ASKING_PRICE_API_NAME
    on ASKING_PRICE (API_NAME)
/

create table CCNL
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    SERIES_CD        VARCHAR2(4000),
    BSNS_DATE        VARCHAR2(4000),
    MRKT_OPEN_DATE   VARCHAR2(4000),
    MRKT_OPEN_TIME   VARCHAR2(4000),
    MRKT_CLOSE_DATE  VARCHAR2(4000),
    MRKT_CLOSE_TIME  VARCHAR2(4000),
    PREV_PRICE       VARCHAR2(4000),
    RECV_DATE        VARCHAR2(4000),
    RECV_TIME        VARCHAR2(4000),
    ACTIVE_FLAG      VARCHAR2(4000),
    LAST_PRICE       VARCHAR2(4000),
    LAST_QNTT        VARCHAR2(4000),
    PREV_DIFF_PRICE  VARCHAR2(4000),
    PREV_DIFF_RATE   VARCHAR2(4000),
    OPEN_PRICE       VARCHAR2(4000),
    HIGH_PRICE       VARCHAR2(4000),
    LOW_PRICE        VARCHAR2(4000),
    VOL              VARCHAR2(4000),
    PREV_SIGN        VARCHAR2(4000),
    QUOTSIGN         VARCHAR2(4000),
    RECV_TIME2       VARCHAR2(4000),
    PSTTL_PRICE      VARCHAR2(4000),
    PSTTL_SIGN       VARCHAR2(4000),
    PSTTL_DIFF_PRICE VARCHAR2(4000),
    PSTTL_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_CCNL_API_NAME
    on CCNL (API_NAME)
/

create table DAILY_CCNL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    TRET_CNT        VARCHAR2(4000),
    LAST_N_CNT      VARCHAR2(4000),
    INDEX_KEY       VARCHAR2(4000),
    DATA_DATE       VARCHAR2(4000),
    DATA_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_DAILY_CCNL_API_NAME
    on DAILY_CCNL (API_NAME)
/

create table INQUIRE_CCLD
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    CANO                VARCHAR2(4000),
    ACNT_PRDT_CD        VARCHAR2(4000),
    ORD_DT              VARCHAR2(4000),
    ODNO                VARCHAR2(4000),
    ORGN_ORD_DT         VARCHAR2(4000),
    ORGN_ODNO           VARCHAR2(4000),
    OVRS_FUTR_FX_PDNO   VARCHAR2(4000),
    RCIT_DVSN_CD        VARCHAR2(4000),
    SLL_BUY_DVSN_CD     VARCHAR2(4000),
    TRAD_STGY_DVSN_CD   VARCHAR2(4000),
    BASS_PRIC_TYPE_CD   VARCHAR2(4000),
    ORD_STAT_CD         VARCHAR2(4000),
    FM_ORD_QTY          VARCHAR2(4000),
    FM_ORD_PRIC         VARCHAR2(4000),
    FM_STOP_ORD_PRIC    VARCHAR2(4000),
    RSVN_DVSN           VARCHAR2(4000),
    FM_CCLD_QTY         VARCHAR2(4000),
    FM_CCLD_PRIC        VARCHAR2(4000),
    FM_ORD_RMN_QTY      VARCHAR2(4000),
    ORD_GRP_NAME        VARCHAR2(4000),
    ERLM_DTL_DTIME      VARCHAR2(4000),
    CCLD_DTL_DTIME      VARCHAR2(4000),
    ORD_STFNO           VARCHAR2(4000),
    RMKS1               VARCHAR2(4000),
    NEW_LQD_DVSN_CD     VARCHAR2(4000),
    FM_LQD_LMT_ORD_PRIC VARCHAR2(4000),
    FM_LQD_STOP_PRIC    VARCHAR2(4000),
    CCLD_CNDT_CD        VARCHAR2(4000),
    NOTI_VALD_DT        VARCHAR2(4000),
    ACNT_TYPE_CD        VARCHAR2(4000),
    FUOP_DVSN           VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_INQUIRE_CCLD_API_NAME
    on INQUIRE_CCLD (API_NAME)
/

create table INQUIRE_DAILY_ORDER
(
    ID                NUMBER         not null
        primary key,
    API_NAME          VARCHAR2(4000) not null,
    CANO              VARCHAR2(4000),
    ACNT_PRDT_CD      VARCHAR2(4000),
    DT                VARCHAR2(4000),
    ORD_DT            VARCHAR2(4000),
    ODNO              VARCHAR2(4000),
    ORGN_ORD_DT       VARCHAR2(4000),
    ORGN_ODNO         VARCHAR2(4000),
    OVRS_FUTR_FX_PDNO VARCHAR2(4000),
    RVSE_CNCL_DVSN_CD VARCHAR2(4000),
    SLL_BUY_DVSN_CD   VARCHAR2(4000),
    CPLX_ORD_DVSN_CD  VARCHAR2(4000),
    PRIC_DVSN_CD      VARCHAR2(4000),
    RCIT_DVSN_CD      VARCHAR2(4000),
    FM_ORD_QTY        VARCHAR2(4000),
    FM_ORD_PRIC       VARCHAR2(4000),
    FM_STOP_ORD_PRIC  VARCHAR2(4000),
    ECIS_RSVN_ORD_YN  VARCHAR2(4000),
    FM_CCLD_QTY       VARCHAR2(4000),
    FM_CCLD_PRIC      VARCHAR2(4000),
    FM_ORD_RMN_QTY    VARCHAR2(4000),
    ORD_GRP_NAME      VARCHAR2(4000),
    RCIT_DTL_DTIME    VARCHAR2(4000),
    CCLD_DTL_DTIME    VARCHAR2(4000),
    ORDR_EMP_NO       VARCHAR2(4000),
    RJCT_RSON_NAME    VARCHAR2(4000),
    CCLD_CNDT_CD      VARCHAR2(4000),
    TRAD_END_DT       VARCHAR2(4000),
    CREATED_AT        DATE           not null
)
/

create index IX_INQUIRE_DAILY_ORDER_API_NAME
    on INQUIRE_DAILY_ORDER (API_NAME)
/

create table INQUIRE_PERIOD_CCLD
(
    ID                         NUMBER         not null
        primary key,
    API_NAME                   VARCHAR2(4000) not null,
    CANO                       VARCHAR2(4000),
    ACNT_PRDT_CD               VARCHAR2(4000),
    CRCY_CD                    VARCHAR2(4000),
    FM_BUY_QTY                 VARCHAR2(4000),
    FM_SLL_QTY                 VARCHAR2(4000),
    FM_LQD_PFLS_AMT            VARCHAR2(4000),
    FM_FEE                     VARCHAR2(4000),
    FM_NET_PFLS_AMT            VARCHAR2(4000),
    FM_USTL_BUY_QTY            VARCHAR2(4000),
    FM_USTL_SLL_QTY            VARCHAR2(4000),
    FM_USTL_EVLU_PFLS_AMT      VARCHAR2(4000),
    FM_USTL_EVLU_PFLS_AMT2     VARCHAR2(4000),
    FM_USTL_EVLU_PFLS_ICDC_AMT VARCHAR2(4000),
    FM_USTL_AGRM_AMT           VARCHAR2(4000),
    FM_OPT_LQD_AMT             VARCHAR2(4000),
    OVRS_FUTR_FX_PDNO          VARCHAR2(4000),
    FM_CCLD_AVG_PRIC           VARCHAR2(4000),
    CREATED_AT                 DATE           not null
)
/

create index IX_INQUIRE_PERIOD_CCLD_API_NAME
    on INQUIRE_PERIOD_CCLD (API_NAME)
/

create table INQUIRE_PERIOD_TRANS
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    TRAD_DT             VARCHAR2(4000),
    STTL_DT             VARCHAR2(4000),
    SLL_BUY_DVSN_CD     VARCHAR2(4000),
    SLL_BUY_DVSN_NAME   VARCHAR2(4000),
    PDNO                VARCHAR2(4000),
    OVRS_ITEM_NAME      VARCHAR2(4000),
    CCLD_QTY            VARCHAR2(4000),
    AMT_UNIT_CCLD_QTY   VARCHAR2(4000),
    FT_CCLD_UNPR2       VARCHAR2(4000),
    OVRS_STCK_CCLD_UNPR VARCHAR2(4000),
    TR_FRCR_AMT2        VARCHAR2(4000),
    TR_AMT              VARCHAR2(4000),
    FRCR_EXCC_AMT_1     VARCHAR2(4000),
    WCRC_EXCC_AMT       VARCHAR2(4000),
    DMST_FRCR_FEE1      VARCHAR2(4000),
    FRCR_FEE1           VARCHAR2(4000),
    DMST_WCRC_FEE       VARCHAR2(4000),
    OVRS_WCRC_FEE       VARCHAR2(4000),
    CRCY_CD             VARCHAR2(4000),
    STD_PDNO            VARCHAR2(4000),
    ERLM_EXRT           VARCHAR2(4000),
    LOAN_DVSN_CD        VARCHAR2(4000),
    LOAN_DVSN_NAME      VARCHAR2(4000),
    FRCR_BUY_AMT_SMTL   VARCHAR2(4000),
    FRCR_SLL_AMT_SMTL   VARCHAR2(4000),
    DMST_FEE_SMTL       VARCHAR2(4000),
    OVRS_FEE_SMTL       VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_INQUIRE_PERIOD_TRANS_API_NAME
    on INQUIRE_PERIOD_TRANS (API_NAME)
/

create table INQUIRE_PSAMOUNT
(
    ID                    NUMBER         not null
        primary key,
    API_NAME              VARCHAR2(4000) not null,
    TR_CRCY_CD            VARCHAR2(4000),
    ORD_PSBL_FRCR_AMT     VARCHAR2(4000),
    SLL_RUSE_PSBL_AMT     VARCHAR2(4000),
    OVRS_ORD_PSBL_AMT     VARCHAR2(4000),
    MAX_ORD_PSBL_QTY      VARCHAR2(4000),
    ECHM_AF_ORD_PSBL_AMT  VARCHAR2(4000),
    ECHM_AF_ORD_PSBL_QTY  VARCHAR2(4000),
    ORD_PSBL_QTY          VARCHAR2(4000),
    EXRT                  VARCHAR2(4000),
    FRCR_ORD_PSBL_AMT1    VARCHAR2(4000),
    OVRS_MAX_ORD_PSBL_QTY VARCHAR2(4000),
    CREATED_AT            DATE           not null
)
/

create index IX_INQUIRE_PSAMOUNT_API_NAME
    on INQUIRE_PSAMOUNT (API_NAME)
/

create table INQUIRE_TIME_FUTURECHARTPRICE
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    RET_CNT         VARCHAR2(4000),
    LAST_N_CNT      VARCHAR2(4000),
    INDEX_KEY       VARCHAR2(4000),
    DATA_DATE       VARCHAR2(4000),
    DATA_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_INQUIRE_TIME_FUTURECHARTPRICE_API_NAME
    on INQUIRE_TIME_FUTURECHARTPRICE (API_NAME)
/

create table INQUIRE_TIME_OPTCHARTPRICE
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    RET_CNT         VARCHAR2(4000),
    LAST_N_CNT      VARCHAR2(4000),
    INDEX_KEY       VARCHAR2(4000),
    DATA_DATE       VARCHAR2(4000),
    DATA_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_INQUIRE_TIME_OPTCHARTPRICE_API_NAME
    on INQUIRE_TIME_OPTCHARTPRICE (API_NAME)
/

create table INQUIRE_UNPD
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    CANO                 VARCHAR2(4000),
    ACNT_PRDT_CD         VARCHAR2(4000),
    OVRS_FUTR_FX_PDNO    VARCHAR2(4000),
    PRDT_TYPE_CD         VARCHAR2(4000),
    CRCY_CD              VARCHAR2(4000),
    SLL_BUY_DVSN_CD      VARCHAR2(4000),
    FM_USTL_QTY          VARCHAR2(4000),
    FM_CCLD_AVG_PRIC     VARCHAR2(4000),
    FM_NOW_PRIC          VARCHAR2(4000),
    FM_EVLU_PFLS_AMT     VARCHAR2(4000),
    FM_OPT_EVLU_AMT      VARCHAR2(4000),
    FM_OTP_EVLU_PFLS_AMT VARCHAR2(4000),
    FUOP_DVSN            VARCHAR2(4000),
    ECIS_RSVN_ORD_YN     VARCHAR2(4000),
    FM_LQD_PSBL_QTY      VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_INQUIRE_UNPD_API_NAME
    on INQUIRE_UNPD (API_NAME)
/

create table INVESTOR_UNPD_TREND
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    ROW_CNT          VARCHAR2(4000),
    PROD_ISCD        VARCHAR2(4000),
    CFTC_ISCD        VARCHAR2(4000),
    BSOP_DATE        VARCHAR2(4000),
    BIDP_SPEC        VARCHAR2(4000),
    ASKP_SPEC        VARCHAR2(4000),
    SPREAD_SPEC      VARCHAR2(4000),
    BIDP_HEDGE       VARCHAR2(4000),
    ASKP_HEDGE       VARCHAR2(4000),
    HTS_OTST_SMTN    VARCHAR2(4000),
    BIDP_MISSING     VARCHAR2(4000),
    ASKP_MISSING     VARCHAR2(4000),
    BIDP_SPEC_CUST   VARCHAR2(4000),
    ASKP_SPEC_CUST   VARCHAR2(4000),
    SPREAD_SPEC_CUST VARCHAR2(4000),
    BIDP_HEDGE_CUST  VARCHAR2(4000),
    ASKP_HEDGE_CUST  VARCHAR2(4000),
    CUST_SMTN        VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_INVESTOR_UNPD_TREND_API_NAME
    on INVESTOR_UNPD_TREND (API_NAME)
/

create table MARGIN_DETAIL
(
    ID                             NUMBER         not null
        primary key,
    API_NAME                       VARCHAR2(4000) not null,
    CANO                           VARCHAR2(4000),
    ACNT_PRDT_CD                   VARCHAR2(4000),
    CRCY_CD                        VARCHAR2(4000),
    RESP_DT                        VARCHAR2(4000),
    ACNT_NET_RISK_MGNA_APLY_YN     VARCHAR2(4000),
    FM_ORD_PSBL_AMT                VARCHAR2(4000),
    FM_ADD_MGN_AMT                 VARCHAR2(4000),
    FM_BRKG_MGN_AMT                VARCHAR2(4000),
    FM_EXCC_BRKG_MGN_AMT           VARCHAR2(4000),
    FM_USTL_MGN_AMT                VARCHAR2(4000),
    FM_MNTN_MGN_AMT                VARCHAR2(4000),
    FM_ORD_MGN_AMT                 VARCHAR2(4000),
    FM_FUTR_ORD_MGN_AMT            VARCHAR2(4000),
    FM_OPT_BUY_ORD_AMT             VARCHAR2(4000),
    FM_OPT_SLL_ORD_MGN_AMT         VARCHAR2(4000),
    FM_OPT_BUY_ORD_MGN_AMT         VARCHAR2(4000),
    FM_ECIS_RSVN_MGN_AMT           VARCHAR2(4000),
    FM_SPAN_BRKG_MGN_AMT           VARCHAR2(4000),
    FM_SPAN_PRIC_ALTR_MGN_AMT      VARCHAR2(4000),
    FM_SPAN_TERM_SPRD_MGN_AMT      VARCHAR2(4000),
    FM_SPAN_BUY_OPT_MIN_MGN_AMT    VARCHAR2(4000),
    FM_SPAN_OPT_MIN_MGN_AMT        VARCHAR2(4000),
    FM_SPAN_TOT_RISK_MGN_AMT       VARCHAR2(4000),
    FM_SPAN_MNTN_MGN_AMT           VARCHAR2(4000),
    FM_SPAN_MNTN_PRIC_ALTR_MGN_AMT VARCHAR2(4000),
    FM_SPAN_MNTN_TERM_SPRD_MGN_AMT VARCHAR2(4000),
    FM_SPAN_MNTN_OPT_PRIC_MGN_AMT  VARCHAR2(4000),
    FM_SPAN_MNTN_OPT_MIN_MGN_AMT   VARCHAR2(4000),
    FM_SPAN_MNTN_TOT_RISK_MGN_AMT  VARCHAR2(4000),
    FM_EURX_BRKG_MGN_AMT           VARCHAR2(4000),
    FM_EURX_PRIC_ALTR_MGN_AMT      VARCHAR2(4000),
    FM_EURX_TERM_SPRD_MGN_AMT      VARCHAR2(4000),
    FM_EURX_OPT_PRIC_MGN_AMT       VARCHAR2(4000),
    FM_EURX_BUY_OPT_MIN_MGN_AMT    VARCHAR2(4000),
    FM_EURX_TOT_RISK_MGN_AMT       VARCHAR2(4000),
    FM_EURX_MNTN_MGN_AMT           VARCHAR2(4000),
    FM_EURX_MNTN_PRIC_ALTR_MGN_AMT VARCHAR2(4000),
    FM_EURX_MNTN_TERM_SPRD_MGN_AMT VARCHAR2(4000),
    FM_EURX_MNTN_OPT_PRIC_MGN_AMT  VARCHAR2(4000),
    FM_EURX_MNTN_TOT_RISK_MGN_AMT  VARCHAR2(4000),
    FM_GNRL_BRKG_MGN_AMT           VARCHAR2(4000),
    FM_FUTR_USTL_MGN_AMT           VARCHAR2(4000),
    FM_SLL_OPT_USTL_MGN_AMT        VARCHAR2(4000),
    FM_BUY_OPT_USTL_MGN_AMT        VARCHAR2(4000),
    FM_SPRD_USTL_MGN_AMT           VARCHAR2(4000),
    FM_AVG_DSCT_MGN_AMT            VARCHAR2(4000),
    FM_GNRL_MNTN_MGN_AMT           VARCHAR2(4000),
    FM_FUTR_MNTN_MGN_AMT           VARCHAR2(4000),
    FM_OPT_MNTN_MGN_AMT            VARCHAR2(4000),
    CREATED_AT                     DATE           not null
)
/

create index IX_MARGIN_DETAIL_API_NAME
    on MARGIN_DETAIL (API_NAME)
/

create table MONTHLY_CCNL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    TRET_CNT        VARCHAR2(4000),
    LAST_N_CNT      VARCHAR2(4000),
    INDEX_KEY       VARCHAR2(4000),
    DATA_DATE       VARCHAR2(4000),
    DATA_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_MONTHLY_CCNL_API_NAME
    on MONTHLY_CCNL (API_NAME)
/

create table OPT_ASKING_PRICE
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOWP_RICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    STTL_PRICE      VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    QUOT_DATE       VARCHAR2(4000),
    QUOT_TIME       VARCHAR2(4000),
    BID_QNTT        VARCHAR2(4000),
    BID_NUM         VARCHAR2(4000),
    BID_PRICE       VARCHAR2(4000),
    ASK_QNTT        VARCHAR2(4000),
    ASK_NUM         VARCHAR2(4000),
    ASK_PRICE       VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_OPT_ASKING_PRICE_API_NAME
    on OPT_ASKING_PRICE (API_NAME)
/

create table OPT_DAILY_CCNL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    RET_CNT         VARCHAR2(4000),
    LAST_N_CNT      VARCHAR2(4000),
    INDEX_KEY       VARCHAR2(4000),
    DATA_DATE       VARCHAR2(4000),
    DATA_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_OPT_DAILY_CCNL_API_NAME
    on OPT_DAILY_CCNL (API_NAME)
/

create table OPT_DETAIL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    EXCH_CD         VARCHAR2(4000),
    CLAS_CD         VARCHAR2(4000),
    CRC_CD          VARCHAR2(4000),
    STTL_PRICE      VARCHAR2(4000),
    STTL_DATE       VARCHAR2(4000),
    TRST_MGN        VARCHAR2(4000),
    DISP_DIGIT      VARCHAR2(4000),
    TICK_SZ         VARCHAR2(4000),
    TICK_VAL        VARCHAR2(4000),
    MRKT_OPEN_DATE  VARCHAR2(4000),
    MRKT_OPEN_TIME  VARCHAR2(4000),
    MRKT_CLOSE_DATE VARCHAR2(4000),
    MRKT_CLOSE_TIME VARCHAR2(4000),
    TRD_FR_DATE     VARCHAR2(4000),
    EXPR_DATE       VARCHAR2(4000),
    TRD_TO_DATE     VARCHAR2(4000),
    REMN_CNT        VARCHAR2(4000),
    STAT_TP         VARCHAR2(4000),
    CTRT_SIZE       VARCHAR2(4000),
    STL_TP          VARCHAR2(4000),
    FRST_NOTI_DATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_OPT_DETAIL_API_NAME
    on OPT_DETAIL (API_NAME)
/

create table OPT_MONTHLY_CCNL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    RET_CNT         VARCHAR2(4000),
    LAST_N_CNT      VARCHAR2(4000),
    INDEX_KEY       VARCHAR2(4000),
    DATA_DATE       VARCHAR2(4000),
    DATA_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_OPT_MONTHLY_CCNL_API_NAME
    on OPT_MONTHLY_CCNL (API_NAME)
/

create table OPT_PRICE
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    PROC_DATE       VARCHAR2(4000),
    PROC_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    BID_QNTT        VARCHAR2(4000),
    BID_PRICE       VARCHAR2(4000),
    ASK_QNTT        VARCHAR2(4000),
    ASK_PRICE       VARCHAR2(4000),
    TRST_MGN        VARCHAR2(4000),
    EXCH_CD         VARCHAR2(4000),
    CRC_CD          VARCHAR2(4000),
    TRD_FR_DATE     VARCHAR2(4000),
    EXPR_DATE       VARCHAR2(4000),
    TRD_TO_DATE     VARCHAR2(4000),
    REMN_CNT        VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    TOT_ASK_QNTT    VARCHAR2(4000),
    TOT_BID_QNTT    VARCHAR2(4000),
    TICK_SIZE       VARCHAR2(4000),
    OPEN_DATE       VARCHAR2(4000),
    OPEN_TIME       VARCHAR2(4000),
    CLOSE_DATE      VARCHAR2(4000),
    CLOSE_TIME      VARCHAR2(4000),
    SBSNSDATE       VARCHAR2(4000),
    STTL_PRICE      VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_OPT_PRICE_API_NAME
    on OPT_PRICE (API_NAME)
/

create table OPT_TICK_CCNL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    RET_CNT         VARCHAR2(4000),
    LAST_N_CNT      VARCHAR2(4000),
    INDEX_KEY       VARCHAR2(4000),
    DATA_DATE       VARCHAR2(4000),
    DATA_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_OPT_TICK_CCNL_API_NAME
    on OPT_TICK_CCNL (API_NAME)
/

create table OPT_WEEKLY_CCNL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    RET_CNT         VARCHAR2(4000),
    LAST_N_CNT      VARCHAR2(4000),
    INDEX_KEY       VARCHAR2(4000),
    DATA_DATE       VARCHAR2(4000),
    DATA_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_OPT_WEEKLY_CCNL_API_NAME
    on OPT_WEEKLY_CCNL (API_NAME)
/

create table ORDER_NOTICE
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    ACCT_NO              VARCHAR2(4000),
    ORD_DT               VARCHAR2(4000),
    ODNO                 VARCHAR2(4000),
    ORGN_ORD_DT          VARCHAR2(4000),
    ORGN_ODNO            VARCHAR2(4000),
    SERIES               VARCHAR2(4000),
    RVSE_CNCL_DVSN_CD    VARCHAR2(4000),
    SLL_BUY_DVSN_CD      VARCHAR2(4000),
    CPLX_ORD_DVSN_CD     VARCHAR2(4000),
    PRCE_TP              VARCHAR2(4000),
    FM_EXCG_RCIT_DVSN_CD VARCHAR2(4000),
    ORD_QTY              VARCHAR2(4000),
    FM_LMT_PRIC          VARCHAR2(4000),
    FM_STOP_ORD_PRIC     VARCHAR2(4000),
    TOT_CCLD_QTY         VARCHAR2(4000),
    TOT_CCLD_UV          VARCHAR2(4000),
    ORD_REMQ             VARCHAR2(4000),
    FM_ORD_GRP_DT        VARCHAR2(4000),
    ORD_GRP_STNO         VARCHAR2(4000),
    ORD_DTL_DTIME        VARCHAR2(4000),
    OPRT_DTL_DTIME       VARCHAR2(4000),
    WORK_EMPL            VARCHAR2(4000),
    CRCY_CD              VARCHAR2(4000),
    LQD_YN               VARCHAR2(4000),
    LQD_LMT_PRIC         VARCHAR2(4000),
    LQD_STOP_PRIC        VARCHAR2(4000),
    TRD_COND             VARCHAR2(4000),
    TERM_ORD_VALD_DTIME  VARCHAR2(4000),
    SPEC_TP              VARCHAR2(4000),
    ECIS_RSVN_ORD_YN     VARCHAR2(4000),
    FUOP_ITEM_DVSN_CD    VARCHAR2(4000),
    AUTO_ORD_DVSN_CD     VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_ORDER_NOTICE_API_NAME
    on ORDER_NOTICE (API_NAME)
/

create table SEARCH_CONTRACT_DETAIL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    EXCH_CD         VARCHAR2(4000),
    CLAS_CD         VARCHAR2(4000),
    CRC_CD          VARCHAR2(4000),
    STTL_PRICE      VARCHAR2(4000),
    STTL_DATE       VARCHAR2(4000),
    TRST_MGN        VARCHAR2(4000),
    DISP_DIGIT      VARCHAR2(4000),
    TICK_SZ         VARCHAR2(4000),
    TICK_VAL        VARCHAR2(4000),
    MRKT_OPEN_DATE  VARCHAR2(4000),
    MRKT_OPEN_TIME  VARCHAR2(4000),
    MRKT_CLOSE_DATE VARCHAR2(4000),
    MRKT_CLOSE_TIME VARCHAR2(4000),
    TRD_FR_DATE     VARCHAR2(4000),
    EXPR_DATE       VARCHAR2(4000),
    TRD_TO_DATE     VARCHAR2(4000),
    REMN_CNT        VARCHAR2(4000),
    STAT_TP         VARCHAR2(4000),
    CTRT_SIZE       VARCHAR2(4000),
    STL_TP          VARCHAR2(4000),
    FRST_NOTI_DATE  VARCHAR2(4000),
    SUB_EXCH_NM     VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_SEARCH_CONTRACT_DETAIL_API_NAME
    on SEARCH_CONTRACT_DETAIL (API_NAME)
/

create table SEARCH_OPT_DETAIL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    EXCH_CD         VARCHAR2(4000),
    CLAS_CD         VARCHAR2(4000),
    CRC_CD          VARCHAR2(4000),
    STTL_PRICE      VARCHAR2(4000),
    STTL_DATE       VARCHAR2(4000),
    TRST_MGN        VARCHAR2(4000),
    DISP_DIGIT      VARCHAR2(4000),
    TICK_SZ         VARCHAR2(4000),
    TICK_VAL        VARCHAR2(4000),
    MRKT_OPEN_DATE  VARCHAR2(4000),
    MRKT_OPEN_TIME  VARCHAR2(4000),
    MRKT_CLOSE_DATE VARCHAR2(4000),
    MRKT_CLOSE_TIME VARCHAR2(4000),
    TRD_FR_DATE     VARCHAR2(4000),
    EXPR_DATE       VARCHAR2(4000),
    TRD_TO_DATE     VARCHAR2(4000),
    REMN_CNT        VARCHAR2(4000),
    STAT_TP         VARCHAR2(4000),
    CTRT_SIZE       VARCHAR2(4000),
    STL_TP          VARCHAR2(4000),
    FRST_NOTI_DATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_SEARCH_OPT_DETAIL_API_NAME
    on SEARCH_OPT_DETAIL (API_NAME)
/

create table STOCK_DETAIL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    EXCH_CD         VARCHAR2(4000),
    TICK_SZ         VARCHAR2(4000),
    DISP_DIGIT      VARCHAR2(4000),
    TRST_MGN        VARCHAR2(4000),
    STTL_DATE       VARCHAR2(4000),
    PREV_PRICE      VARCHAR2(4000),
    CRC_CD          VARCHAR2(4000),
    CLAS_CD         VARCHAR2(4000),
    TICK_VAL        VARCHAR2(4000),
    MRKT_OPEN_DATE  VARCHAR2(4000),
    MRKT_OPEN_TIME  VARCHAR2(4000),
    MRKT_CLOSE_DATE VARCHAR2(4000),
    MRKT_CLOSE_TIME VARCHAR2(4000),
    TRD_FR_DATE     VARCHAR2(4000),
    EXPR_DATE       VARCHAR2(4000),
    TRD_TO_DATE     VARCHAR2(4000),
    REMN_CNT        VARCHAR2(4000),
    STAT_TP         VARCHAR2(4000),
    CTRT_SIZE       VARCHAR2(4000),
    STL_TP          VARCHAR2(4000),
    FRST_NOTI_DATE  VARCHAR2(4000),
    SPRD_SRS_CD1    VARCHAR2(4000),
    SPRD_SRS_CD2    VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_STOCK_DETAIL_API_NAME
    on STOCK_DETAIL (API_NAME)
/

create table TICK_CCNL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    TRET_CNT        VARCHAR2(4000),
    LAST_N_CNT      VARCHAR2(4000),
    INDEX_KEY       VARCHAR2(4000),
    DATA_DATE       VARCHAR2(4000),
    DATA_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_TICK_CCNL_API_NAME
    on TICK_CCNL (API_NAME)
/

create table WEEKLY_CCNL
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null,
    RET_CNT         VARCHAR2(4000),
    LAST_N_CNT      VARCHAR2(4000),
    INDEX_KEY       VARCHAR2(4000),
    DATA_DATE       VARCHAR2(4000),
    DATA_TIME       VARCHAR2(4000),
    OPEN_PRICE      VARCHAR2(4000),
    HIGH_PRICE      VARCHAR2(4000),
    LOW_PRICE       VARCHAR2(4000),
    LAST_PRICE      VARCHAR2(4000),
    LAST_QNTT       VARCHAR2(4000),
    VOL             VARCHAR2(4000),
    PREV_DIFF_FLAG  VARCHAR2(4000),
    PREV_DIFF_PRICE VARCHAR2(4000),
    PREV_DIFF_RATE  VARCHAR2(4000),
    CREATED_AT      DATE           not null
)
/

create index IX_WEEKLY_CCNL_API_NAME
    on WEEKLY_CCNL (API_NAME)
/

create table ALGO_ORDNO
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    ODNO               VARCHAR2(4000),
    TRAD_DVSN_NAME     VARCHAR2(4000),
    PDNO               VARCHAR2(4000),
    ITEM_NAME          VARCHAR2(4000),
    FT_ORD_QTY         VARCHAR2(4000),
    FT_ORD_UNPR3       VARCHAR2(4000),
    SPLT_BUY_ATTR_NAME VARCHAR2(4000),
    FT_CCLD_QTY        VARCHAR2(4000),
    ORD_GNO_BRNO       VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_ALGO_ORDNO_API_NAME
    on ALGO_ORDNO (API_NAME)
/

create table BRKNEWS_TITLE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    CNTT_USIQ_SRNO      VARCHAR2(4000),
    NEWS_OFER_ENTP_CODE VARCHAR2(4000),
    DATA_DT             VARCHAR2(4000),
    DATA_TM             VARCHAR2(4000),
    HTS_PBNT_TITL_CNTT  VARCHAR2(4000),
    NEWS_LRDV_CODE      VARCHAR2(4000),
    DORG                VARCHAR2(4000),
    ISCD1               VARCHAR2(4000),
    ISCD2               VARCHAR2(4000),
    ISCD3               VARCHAR2(4000),
    ISCD4               VARCHAR2(4000),
    ISCD5               VARCHAR2(4000),
    ISCD6               VARCHAR2(4000),
    ISCD7               VARCHAR2(4000),
    ISCD8               VARCHAR2(4000),
    ISCD9               VARCHAR2(4000),
    ISCD10              VARCHAR2(4000),
    KOR_ISNM1           VARCHAR2(4000),
    KOR_ISNM2           VARCHAR2(4000),
    KOR_ISNM3           VARCHAR2(4000),
    KOR_ISNM4           VARCHAR2(4000),
    KOR_ISNM5           VARCHAR2(4000),
    KOR_ISNM6           VARCHAR2(4000),
    KOR_ISNM7           VARCHAR2(4000),
    KOR_ISNM8           VARCHAR2(4000),
    KOR_ISNM9           VARCHAR2(4000),
    KOR_ISNM10          VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_BRKNEWS_TITLE_API_NAME
    on BRKNEWS_TITLE (API_NAME)
/

create table COLABLE_BY_COMPANY
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    PDNO               VARCHAR2(4000),
    OVRS_ITEM_NAME     VARCHAR2(4000),
    LOAN_RT            VARCHAR2(4000),
    MGGE_MNTN_RT       VARCHAR2(4000),
    MGGE_ENSU_RT       VARCHAR2(4000),
    LOAN_EXEC_PSBL_YN  VARCHAR2(4000),
    STFF_NAME          VARCHAR2(4000),
    ERLM_DT            VARCHAR2(4000),
    TR_MKET_NAME       VARCHAR2(4000),
    CRCY_CD            VARCHAR2(4000),
    NATN_KOR_NAME      VARCHAR2(4000),
    OVRS_EXCG_CD       VARCHAR2(4000),
    LOAN_PSBL_ITEM_NUM VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_COLABLE_BY_COMPANY_API_NAME
    on COLABLE_BY_COMPANY (API_NAME)
/

create table COUNTRIES_HOLIDAY
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    PRDT_TYPE_CD     VARCHAR2(4000),
    TR_NATN_CD       VARCHAR2(4000),
    NATN_ENG_ABRV_CD VARCHAR2(4000),
    TR_MKET_CD       VARCHAR2(4000),
    TR_MKET_NAME     VARCHAR2(4000),
    ACPL_STTL_DT     VARCHAR2(4000),
    DMST_STTL_DT     VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_COUNTRIES_HOLIDAY_API_NAME
    on COUNTRIES_HOLIDAY (API_NAME)
/

create table DAILYPRICE
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    RSYM       VARCHAR2(4000),
    ZDIV       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    XYMD       VARCHAR2(4000),
    CLOS       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    OPEN       VARCHAR2(4000),
    HIGH       VARCHAR2(4000),
    LOW        VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    VBID       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    VASK       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_DAILYPRICE_API_NAME
    on DAILYPRICE (API_NAME)
/

create table DAYTIME_ORDER
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    KRX_FWDG_ORD_ORGNO VARCHAR2(4000),
    ODNO               VARCHAR2(4000),
    ORD_TMD            VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_DAYTIME_ORDER_API_NAME
    on DAYTIME_ORDER (API_NAME)
/

create table DAYTIME_ORDER_RVSECNCL
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    "Output1"          VARCHAR2(4000),
    KRX_FWDG_ORD_ORGNO VARCHAR2(4000),
    ODNO               VARCHAR2(4000),
    ORD_TMD            VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_DAYTIME_ORDER_RVSECNCL_API_NAME
    on DAYTIME_ORDER_RVSECNCL (API_NAME)
/

create table DELAYED_ASKING_PRICE_ASIA
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    SYMB       VARCHAR2(4000),
    ZDIV       VARCHAR2(4000),
    XYMD       VARCHAR2(4000),
    XHMS       VARCHAR2(4000),
    KYMD       VARCHAR2(4000),
    KHMS       VARCHAR2(4000),
    BVOL       VARCHAR2(4000),
    AVOL       VARCHAR2(4000),
    BDVL       VARCHAR2(4000),
    ADVL       VARCHAR2(4000),
    PBID1      VARCHAR2(4000),
    PASK1      VARCHAR2(4000),
    VBID1      VARCHAR2(4000),
    VASK1      VARCHAR2(4000),
    DBID1      VARCHAR2(4000),
    DASK1      VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_DELAYED_ASKING_PRICE_ASIA_API_NAME
    on DELAYED_ASKING_PRICE_ASIA (API_NAME)
/

create table DELAYED_CCNL
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    SYMB       VARCHAR2(4000),
    ZDIV       VARCHAR2(4000),
    TYMD       VARCHAR2(4000),
    XYMD       VARCHAR2(4000),
    XHMS       VARCHAR2(4000),
    KYMD       VARCHAR2(4000),
    KHMS       VARCHAR2(4000),
    OPEN       VARCHAR2(4000),
    HIGH       VARCHAR2(4000),
    LOW        VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    VBID       VARCHAR2(4000),
    VASK       VARCHAR2(4000),
    EVOL       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    BIVL       VARCHAR2(4000),
    ASVL       VARCHAR2(4000),
    STRN       VARCHAR2(4000),
    MTYP       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_DELAYED_CCNL_API_NAME
    on DELAYED_CCNL (API_NAME)
/

create table FOREIGN_MARGIN
(
    ID                     NUMBER         not null
        primary key,
    API_NAME               VARCHAR2(4000) not null,
    NATN_NAME              VARCHAR2(4000),
    FRCR_DNCL_AMT1         VARCHAR2(4000),
    USTL_BUY_AMT           VARCHAR2(4000),
    USTL_SLL_AMT           VARCHAR2(4000),
    FRCR_RCVB_AMT          VARCHAR2(4000),
    FRCR_MGN_AMT           VARCHAR2(4000),
    FRCR_GNRL_ORD_PSBL_AMT VARCHAR2(4000),
    FRCR_ORD_PSBL_AMT1     VARCHAR2(4000),
    ITGR_ORD_PSBL_AMT      VARCHAR2(4000),
    BASS_EXRT              VARCHAR2(4000),
    CREATED_AT             DATE           not null
)
/

create index IX_FOREIGN_MARGIN_API_NAME
    on FOREIGN_MARGIN (API_NAME)
/

create table INDUSTRY_PRICE
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    NREC       VARCHAR2(4000),
    ICOD       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_INDUSTRY_PRICE_API_NAME
    on INDUSTRY_PRICE (API_NAME)
/

create table INDUSTRY_THEME
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    CREC       VARCHAR2(4000),
    TREC       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    VASK       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    VBID       VARCHAR2(4000),
    SEQN       VARCHAR2(4000),
    ENAME      VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_INDUSTRY_THEME_API_NAME
    on INDUSTRY_THEME (API_NAME)
/

create table INQUIRE_ALGO_CCNL
(
    ID                 NUMBER         not null
        primary key,
    API_NAME           VARCHAR2(4000) not null,
    CCLD_SEQ           VARCHAR2(4000),
    CCLD_BTWN          VARCHAR2(4000),
    PDNO               VARCHAR2(4000),
    ITEM_NAME          VARCHAR2(4000),
    FT_CCLD_QTY        VARCHAR2(4000),
    FT_CCLD_UNPR3      VARCHAR2(4000),
    FT_CCLD_AMT3       VARCHAR2(4000),
    ODNO               VARCHAR2(4000),
    TRAD_DVSN_NAME     VARCHAR2(4000),
    FT_ORD_QTY         VARCHAR2(4000),
    FT_ORD_UNPR3       VARCHAR2(4000),
    ORD_TMD            VARCHAR2(4000),
    SPLT_BUY_ATTR_NAME VARCHAR2(4000),
    TR_CRCY            VARCHAR2(4000),
    CCLD_CNT           VARCHAR2(4000),
    CREATED_AT         DATE           not null
)
/

create index IX_INQUIRE_ALGO_CCNL_API_NAME
    on INQUIRE_ALGO_CCNL (API_NAME)
/

create table INQUIRE_DAILY_CHARTPRICE
(
    ID                  NUMBER         not null
        primary key,
    API_NAME            VARCHAR2(4000) not null,
    OVRS_NMIX_PRDY_VRSS VARCHAR2(4000),
    PRDY_VRSS_SIGN      VARCHAR2(4000),
    PRDY_CTRT           VARCHAR2(4000),
    OVRS_NMIX_PRDY_CLPR VARCHAR2(4000),
    ACML_VOL            VARCHAR2(4000),
    HTS_KOR_ISNM        VARCHAR2(4000),
    OVRS_NMIX_PRPR      VARCHAR2(4000),
    STCK_SHRN_ISCD      VARCHAR2(4000),
    PRDY_VOL            VARCHAR2(4000),
    OVRS_PROD_OPRC      VARCHAR2(4000),
    OVRS_PROD_HGPR      VARCHAR2(4000),
    OVRS_PROD_LWPR      VARCHAR2(4000),
    STCK_BSOP_DATE      VARCHAR2(4000),
    OVRS_NMIX_OPRC      VARCHAR2(4000),
    OVRS_NMIX_HGPR      VARCHAR2(4000),
    OVRS_NMIX_LWPR      VARCHAR2(4000),
    MOD_YN              VARCHAR2(4000),
    CREATED_AT          DATE           not null
)
/

create index IX_INQUIRE_DAILY_CHARTPRICE_API_NAME
    on INQUIRE_DAILY_CHARTPRICE (API_NAME)
/

create table INQUIRE_NCCS
(
    ID                   NUMBER         not null
        primary key,
    API_NAME             VARCHAR2(4000) not null,
    ORD_DT               VARCHAR2(4000),
    ORD_GNO_BRNO         VARCHAR2(4000),
    ODNO                 VARCHAR2(4000),
    ORGN_ODNO            VARCHAR2(4000),
    PDNO                 VARCHAR2(4000),
    SLL_BUY_DVSN_CD      VARCHAR2(4000),
    RVSE_CNCL_DVSN_CD    VARCHAR2(4000),
    RJCT_RSON            VARCHAR2(4000),
    ORD_TMD              VARCHAR2(4000),
    TR_CRCY_CD           VARCHAR2(4000),
    NATN_CD              VARCHAR2(4000),
    FT_ORD_QTY           VARCHAR2(4000),
    FT_CCLD_QTY          VARCHAR2(4000),
    NCCS_QTY             VARCHAR2(4000),
    FT_ORD_UNPR3         VARCHAR2(4000),
    FT_CCLD_UNPR3        VARCHAR2(4000),
    FT_CCLD_AMT3         VARCHAR2(4000),
    OVRS_EXCG_CD         VARCHAR2(4000),
    LOAN_TYPE_CD         VARCHAR2(4000),
    LOAN_DT              VARCHAR2(4000),
    USA_AMK_EXTS_RQST_YN VARCHAR2(4000),
    CREATED_AT           DATE           not null
)
/

create index IX_INQUIRE_NCCS_API_NAME
    on INQUIRE_NCCS (API_NAME)
/

create table INQUIRE_PAYMT_STDR_BALANCE
(
    ID                           NUMBER         not null
        primary key,
    API_NAME                     VARCHAR2(4000) not null,
    PDNO                         VARCHAR2(4000),
    PRDT_NAME                    VARCHAR2(4000),
    CBLC_QTY13                   VARCHAR2(4000),
    ORD_PSBL_QTY1                VARCHAR2(4000),
    AVG_UNPR3                    VARCHAR2(4000),
    OVRS_NOW_PRIC1               VARCHAR2(4000),
    FRCR_PCHS_AMT                VARCHAR2(4000),
    FRCR_EVLU_AMT2               VARCHAR2(4000),
    EVLU_PFLS_AMT2               VARCHAR2(4000),
    BASS_EXRT                    VARCHAR2(4000),
    OPRT_DTL_DTIME               VARCHAR2(4000),
    BUY_CRCY_CD                  VARCHAR2(4000),
    THDT_SLL_CCLD_QTY1           VARCHAR2(4000),
    THDT_BUY_CCLD_QTY1           VARCHAR2(4000),
    EVLU_PFLS_RT1                VARCHAR2(4000),
    TR_MKET_NAME                 VARCHAR2(4000),
    NATN_KOR_NAME                VARCHAR2(4000),
    STD_PDNO                     VARCHAR2(4000),
    MGGE_QTY                     VARCHAR2(4000),
    LOAN_RMND                    VARCHAR2(4000),
    PRDT_TYPE_CD                 VARCHAR2(4000),
    OVRS_EXCG_CD                 VARCHAR2(4000),
    SCTS_DVSN_NAME               VARCHAR2(4000),
    LDNG_CBLC_QTY                VARCHAR2(4000),
    CRCY_CD                      VARCHAR2(4000),
    CRCY_CD_NAME                 VARCHAR2(4000),
    FRCR_DNCL_AMT_2              VARCHAR2(4000),
    FRST_BLTN_EXRT               VARCHAR2(4000),
    PCHS_AMT_SMTL_AMT            VARCHAR2(4000),
    TOT_EVLU_PFLS_AMT            VARCHAR2(4000),
    EVLU_ERNG_RT1                VARCHAR2(4000),
    TOT_DNCL_AMT                 VARCHAR2(4000),
    WCRC_EVLU_AMT_SMTL           VARCHAR2(4000),
    TOT_ASST_AMT2                VARCHAR2(4000),
    FRCR_CBLC_WCRC_EVLU_AMT_SMTL VARCHAR2(4000),
    TOT_LOAN_AMT                 VARCHAR2(4000),
    TOT_LDNG_EVLU_AMT            VARCHAR2(4000),
    CREATED_AT                   DATE           not null
)
/

create index IX_INQUIRE_PAYMT_STDR_BALANCE_API_NAME
    on INQUIRE_PAYMT_STDR_BALANCE (API_NAME)
/

create table INQUIRE_PRESENT_BALANCE
(
    ID                      NUMBER         not null
        primary key,
    API_NAME                VARCHAR2(4000) not null,
    CBLC_QTY13              VARCHAR2(4000),
    THDT_BUY_CCLD_QTY1      VARCHAR2(4000),
    THDT_SLL_CCLD_QTY1      VARCHAR2(4000),
    CCLD_QTY_SMTL1          VARCHAR2(4000),
    ORD_PSBL_QTY1           VARCHAR2(4000),
    FRCR_PCHS_AMT           VARCHAR2(4000),
    FRCR_EVLU_AMT2          VARCHAR2(4000),
    EVLU_PFLS_AMT2          VARCHAR2(4000),
    EVLU_PFLS_RT1           VARCHAR2(4000),
    PDNO                    VARCHAR2(4000),
    BASS_EXRT               VARCHAR2(4000),
    BUY_CRCY_CD             VARCHAR2(4000),
    OVRS_NOW_PRIC1          VARCHAR2(4000),
    AVG_UNPR3               VARCHAR2(4000),
    TR_MKET_NAME            VARCHAR2(4000),
    NATN_KOR_NAME           VARCHAR2(4000),
    PCHS_RMND_WCRC_AMT      VARCHAR2(4000),
    THDT_BUY_CCLD_FRCR_AMT  VARCHAR2(4000),
    THDT_SLL_CCLD_FRCR_AMT  VARCHAR2(4000),
    UNIT_AMT                VARCHAR2(4000),
    STD_PDNO                VARCHAR2(4000),
    PRDT_TYPE_CD            VARCHAR2(4000),
    LOAN_RMND               VARCHAR2(4000),
    LOAN_DT                 VARCHAR2(4000),
    LOAN_EXPD_DT            VARCHAR2(4000),
    OVRS_EXCG_CD            VARCHAR2(4000),
    ITEM_LNKG_EXCG_CD       VARCHAR2(4000),
    CRCY_CD                 VARCHAR2(4000),
    FRCR_BUY_AMT_SMTL       VARCHAR2(4000),
    FRCR_SLL_AMT_SMTL       VARCHAR2(4000),
    FRCR_DNCL_AMT_2         VARCHAR2(4000),
    FRST_BLTN_EXRT          VARCHAR2(4000),
    FRCR_BUY_MGN_AMT        VARCHAR2(4000),
    FRCR_ETC_MGNA           VARCHAR2(4000),
    FRCR_DRWG_PSBL_AMT_1    VARCHAR2(4000),
    ACPL_CSTD_CRCY_YN       VARCHAR2(4000),
    NXDY_FRCR_DRWG_PSBL_AMT VARCHAR2(4000),
    OUTPUT3                 VARCHAR2(4000),
    PCHS_AMT_SMTL           VARCHAR2(4000),
    EVLU_AMT_SMTL           VARCHAR2(4000),
    EVLU_PFLS_AMT_SMTL      VARCHAR2(4000),
    DNCL_AMT                VARCHAR2(4000),
    CMA_EVLU_AMT            VARCHAR2(4000),
    TOT_DNCL_AMT            VARCHAR2(4000),
    ETC_MGNA                VARCHAR2(4000),
    WDRW_PSBL_TOT_AMT       VARCHAR2(4000),
    FRCR_EVLU_TOTA          VARCHAR2(4000),
    EVLU_ERNG_RT1           VARCHAR2(4000),
    PCHS_AMT_SMTL_AMT       VARCHAR2(4000),
    EVLU_AMT_SMTL_AMT       VARCHAR2(4000),
    TOT_EVLU_PFLS_AMT       VARCHAR2(4000),
    TOT_ASST_AMT            VARCHAR2(4000),
    BUY_MGN_AMT             VARCHAR2(4000),
    MGNA_TOTA               VARCHAR2(4000),
    FRCR_USE_PSBL_AMT       VARCHAR2(4000),
    USTL_SLL_AMT_SMTL       VARCHAR2(4000),
    USTL_BUY_AMT_SMTL       VARCHAR2(4000),
    TOT_FRCR_CBLC_SMTL      VARCHAR2(4000),
    TOT_LOAN_AMT            VARCHAR2(4000),
    CREATED_AT              DATE           not null
)
/

create index IX_INQUIRE_PRESENT_BALANCE_API_NAME
    on INQUIRE_PRESENT_BALANCE (API_NAME)
/

create table INQUIRE_SEARCH
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    CREC       VARCHAR2(4000),
    TREC       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SHAR       VARCHAR2(4000),
    VALX       VARCHAR2(4000),
    PLOW       VARCHAR2(4000),
    PHIGH      VARCHAR2(4000),
    POPEN      VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    AVOL       VARCHAR2(4000),
    EPS        VARCHAR2(4000),
    PER        VARCHAR2(4000),
    RANK       VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_INQUIRE_SEARCH_API_NAME
    on INQUIRE_SEARCH (API_NAME)
/

create table NEW_HIGHLOW
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    N_BASE     VARCHAR2(4000),
    N_DIFF     VARCHAR2(4000),
    N_RATE     VARCHAR2(4000),
    ENAME      VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    NHGH       VARCHAR2(4000),
    NLOW       VARCHAR2(4000),
    RANK       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_NEW_HIGHLOW_API_NAME
    on NEW_HIGHLOW (API_NAME)
/

create table ORDER_RESV_LIST
(
    ID                         NUMBER         not null
        primary key,
    API_NAME                   VARCHAR2(4000) not null,
    CNCL_YN                    VARCHAR2(4000),
    RSVN_ORD_RCIT_DT           VARCHAR2(4000),
    OVRS_RSVN_ODNO             VARCHAR2(4000),
    ORD_DT                     VARCHAR2(4000),
    ORD_GNO_BRNO               VARCHAR2(4000),
    ODNO                       VARCHAR2(4000),
    SLL_BUY_DVSN_CD            VARCHAR2(4000),
    SLL_BUY_DVSN_CD_NAME       VARCHAR2(4000),
    OVRS_RSVN_ORD_STAT_CD      VARCHAR2(4000),
    OVRS_RSVN_ORD_STAT_CD_NAME VARCHAR2(4000),
    PDNO                       VARCHAR2(4000),
    PRDT_TYPE_CD               VARCHAR2(4000),
    PRDT_NAME                  VARCHAR2(4000),
    ORD_RCIT_TMD               VARCHAR2(4000),
    ORD_FWDG_TMD               VARCHAR2(4000),
    TR_DVSN_NAME               VARCHAR2(4000),
    OVRS_EXCG_CD               VARCHAR2(4000),
    TR_MKET_NAME               VARCHAR2(4000),
    ORD_STFNO                  VARCHAR2(4000),
    FT_ORD_QTY                 VARCHAR2(4000),
    FT_ORD_UNPR3               VARCHAR2(4000),
    FT_CCLD_QTY                VARCHAR2(4000),
    NPRC_RSON_TEXT             VARCHAR2(4000),
    SPLT_BUY_ATTR_NAME         VARCHAR2(4000),
    CREATED_AT                 DATE           not null
)
/

create index IX_ORDER_RESV_LIST_API_NAME
    on ORDER_RESV_LIST (API_NAME)
/

create table PRICE
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    RSYM       VARCHAR2(4000),
    ZDIV       VARCHAR2(4000),
    BASE       VARCHAR2(4000),
    PVOL       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    ORDY       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_PRICE_API_NAME
    on PRICE (API_NAME)
/

create table PRICE_DETAIL
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    RSYM       VARCHAR2(4000),
    PVOL       VARCHAR2(4000),
    OPEN       VARCHAR2(4000),
    HIGH       VARCHAR2(4000),
    LOW        VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    BASE       VARCHAR2(4000),
    TOMV       VARCHAR2(4000),
    PAMT       VARCHAR2(4000),
    UPLP       VARCHAR2(4000),
    DNLP       VARCHAR2(4000),
    H52P       VARCHAR2(4000),
    H52D       VARCHAR2(4000),
    L52P       VARCHAR2(4000),
    L52D       VARCHAR2(4000),
    PERX       VARCHAR2(4000),
    PBRX       VARCHAR2(4000),
    EPSX       VARCHAR2(4000),
    BPSX       VARCHAR2(4000),
    SHAR       VARCHAR2(4000),
    MCAP       VARCHAR2(4000),
    CURR       VARCHAR2(4000),
    ZDIV       VARCHAR2(4000),
    VNIT       VARCHAR2(4000),
    T_XPRC     VARCHAR2(4000),
    T_XDIF     VARCHAR2(4000),
    T_XRAT     VARCHAR2(4000),
    P_XPRC     VARCHAR2(4000),
    P_XDIF     VARCHAR2(4000),
    P_XRAT     VARCHAR2(4000),
    T_RATE     VARCHAR2(4000),
    P_RATE     VARCHAR2(4000),
    T_XSGN     VARCHAR2(4000),
    P_XSNG     VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    E_HOGAU    VARCHAR2(4000),
    E_ICOD     VARCHAR2(4000),
    E_PARP     VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    ETYP_NM    VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_PRICE_DETAIL_API_NAME
    on PRICE_DETAIL (API_NAME)
/

create table PRICE_FLUCT
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    KNAM       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    N_BASE     VARCHAR2(4000),
    N_DIFF     VARCHAR2(4000),
    N_RATE     VARCHAR2(4000),
    ENAM       VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    N_LAST     VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_PRICE_FLUCT_API_NAME
    on PRICE_FLUCT (API_NAME)
/

create table QUOT_INQUIRE_CCNL
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    VPOW       VARCHAR2(4000),
    EVOL       VARCHAR2(4000),
    KHMS       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    MTYP       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_QUOT_INQUIRE_CCNL_API_NAME
    on QUOT_INQUIRE_CCNL (API_NAME)
/

create table RIGHTS_BY_ICE
(
    ID               NUMBER         not null
        primary key,
    API_NAME         VARCHAR2(4000) not null,
    ANNO_DT          VARCHAR2(4000),
    CA_TITLE         VARCHAR2(4000),
    DIV_LOCK_DT      VARCHAR2(4000),
    PAY_DT           VARCHAR2(4000),
    RECORD_DT        VARCHAR2(4000),
    VALIDITY_DT      VARCHAR2(4000),
    LOCAL_END_DT     VARCHAR2(4000),
    LOCK_DT          VARCHAR2(4000),
    DELIST_DT        VARCHAR2(4000),
    REDEMPT_DT       VARCHAR2(4000),
    EARLY_REDEMPT_DT VARCHAR2(4000),
    EFFECTIVE_DT     VARCHAR2(4000),
    CREATED_AT       DATE           not null
)
/

create index IX_RIGHTS_BY_ICE_API_NAME
    on RIGHTS_BY_ICE (API_NAME)
/

create table TRADE_GROWTH
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    CREC       VARCHAR2(4000),
    TREC       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    N_TVOL     VARCHAR2(4000),
    N_RATE     VARCHAR2(4000),
    RANK       VARCHAR2(4000),
    ENAME      VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    N_DIFF     VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_TRADE_GROWTH_API_NAME
    on TRADE_GROWTH (API_NAME)
/

create table TRADE_PBMN
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    CREC       VARCHAR2(4000),
    TREC       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    A_TAMT     VARCHAR2(4000),
    RANK       VARCHAR2(4000),
    ENAME      VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_TRADE_PBMN_API_NAME
    on TRADE_PBMN (API_NAME)
/

create table TRADE_TURNOVER
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    CREC       VARCHAR2(4000),
    TREC       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    N_TVOL     VARCHAR2(4000),
    SHAR       VARCHAR2(4000),
    TOVER      VARCHAR2(4000),
    RANK       VARCHAR2(4000),
    ENAME      VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    TRAT       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_TRADE_TURNOVER_API_NAME
    on TRADE_TURNOVER (API_NAME)
/

create table TRADE_VOL
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    CREC       VARCHAR2(4000),
    TREC       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    A_TVOL     VARCHAR2(4000),
    RANK       VARCHAR2(4000),
    ENAME      VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_TRADE_VOL_API_NAME
    on TRADE_VOL (API_NAME)
/

create table VOLUME_SURGE
(
    ID         NUMBER         not null
        primary key,
    API_NAME   VARCHAR2(4000) not null,
    ZDIV       VARCHAR2(4000),
    STAT       VARCHAR2(4000),
    NREC       VARCHAR2(4000),
    RSYM       VARCHAR2(4000),
    EXCD       VARCHAR2(4000),
    SYMB       VARCHAR2(4000),
    KNAM       VARCHAR2(4000),
    NAME       VARCHAR2(4000),
    LAST       VARCHAR2(4000),
    SIGN       VARCHAR2(4000),
    DIFF       VARCHAR2(4000),
    RATE       VARCHAR2(4000),
    TVOL       VARCHAR2(4000),
    PASK       VARCHAR2(4000),
    PBID       VARCHAR2(4000),
    N_TVOL     VARCHAR2(4000),
    N_DIFF     VARCHAR2(4000),
    N_RATE     VARCHAR2(4000),
    ENAM       VARCHAR2(4000),
    E_ORDYN    VARCHAR2(4000),
    TAMT       VARCHAR2(4000),
    TRAT       VARCHAR2(4000),
    CREATED_AT DATE           not null
)
/

create index IX_VOLUME_SURGE_API_NAME
    on VOLUME_SURGE (API_NAME)
/

create table DOM_FUTURE_MST
(
    ID                    NUMBER not null
        primary key,
    PRODUCT_TYPE          VARCHAR2(4000),
    SHORT_CODE            VARCHAR2(4000),
    STANDARD_CODE         VARCHAR2(4000),
    KOR_NAME              VARCHAR2(4000),
    ATM_DIVISION          VARCHAR2(4000),
    STRIKE_PRICE          VARCHAR2(4000),
    MONTH_CODE            VARCHAR2(4000),
    UNDERLYING_SHORT_CODE VARCHAR2(4000),
    UNDERLYING_NAME       VARCHAR2(4000),
    CREATED_AT            DATE   not null,
    UPDATED_AT            DATE   not null
)
/

create index IX_DOM_FUTURE_MST_STANDARD_CODE
    on DOM_FUTURE_MST (STANDARD_CODE)
/

create index IX_DOM_FUTURE_MST_SHORT_CODE
    on DOM_FUTURE_MST (SHORT_CODE)
/

create table OVER_FUTURE_MST
(
    ID                    NUMBER not null
        primary key,
    SYMBOL_CODE           VARCHAR2(4000),
    AUTO_ORDER_YN         VARCHAR2(4000),
    TWAP_ORDER_YN         VARCHAR2(4000),
    ECON_ORDER_YN         VARCHAR2(4000),
    FILLER                VARCHAR2(4000),
    KOR_NAME              VARCHAR2(4000),
    EXCHANGE_CODE         VARCHAR2(4000),
    ITEM_CODE             VARCHAR2(4000),
    ITEM_TYPE             VARCHAR2(4000),
    DISPLAY_DECIMAL       VARCHAR2(4000),
    CALC_DECIMAL          VARCHAR2(4000),
    TICK_SIZE             VARCHAR2(4000),
    TICK_VALUE            VARCHAR2(4000),
    CONTRACT_SIZE         VARCHAR2(4000),
    PRICE_NOTATION        VARCHAR2(4000),
    CONVERSION_MULTIPLIER VARCHAR2(4000),
    MOST_ACTIVE_YN        VARCHAR2(4000),
    NEAREST_MONTH_YN      VARCHAR2(4000),
    SPREAD_YN             VARCHAR2(4000),
    SPREAD_LEG1_YN        VARCHAR2(4000),
    SUB_EXCHANGE_CODE     VARCHAR2(4000),
    CREATED_AT            DATE   not null,
    UPDATED_AT            DATE   not null
)
/

create index IX_OVER_FUTURE_MST_EXCHANGE_CODE
    on OVER_FUTURE_MST (EXCHANGE_CODE)
/

create index IX_OVER_FUTURE_MST_SYMBOL_CODE
    on OVER_FUTURE_MST (SYMBOL_CODE)
/

create table DOM_STOCK_FUTURE_MST
(
    ID                    NUMBER not null
        primary key,
    PRODUCT_TYPE          VARCHAR2(4000),
    SHORT_CODE            VARCHAR2(4000),
    STANDARD_CODE         VARCHAR2(4000),
    KOR_NAME              VARCHAR2(4000),
    ATM_DIVISION          VARCHAR2(4000),
    STRIKE_PRICE          VARCHAR2(4000),
    MONTH_CODE            VARCHAR2(4000),
    UNDERLYING_SHORT_CODE VARCHAR2(4000),
    UNDERLYING_NAME       VARCHAR2(4000),
    CREATED_AT            DATE   not null,
    UPDATED_AT            DATE   not null
)
/

create index IX_DOM_STOCK_FUTURE_MST_STANDARD_CODE
    on DOM_STOCK_FUTURE_MST (STANDARD_CODE)
/

create index IX_DOM_STOCK_FUTURE_MST_SHORT_CODE
    on DOM_STOCK_FUTURE_MST (SHORT_CODE)
/

create table OVER_STOCK_MST
(
    ID                    NUMBER not null
        primary key,
    NATIONAL_CODE         VARCHAR2(4000),
    EXCHANGE_ID           VARCHAR2(4000),
    EXCHANGE_CODE         VARCHAR2(4000),
    EXCHANGE_NAME         VARCHAR2(4000),
    SYMBOL                VARCHAR2(4000),
    REALTIME_SYMBOL       VARCHAR2(4000),
    KOREA_NAME            VARCHAR2(4000),
    ENGLISH_NAME          VARCHAR2(4000),
    SECURITY_TYPE         VARCHAR2(4000),
    CURRENCY              VARCHAR2(4000),
    FLOAT_POSITION        VARCHAR2(4000),
    DATA_TYPE             VARCHAR2(4000),
    BASE_PRICE            VARCHAR2(4000),
    BID_ORDER_SIZE        VARCHAR2(4000),
    ASK_ORDER_SIZE        VARCHAR2(4000),
    MARKET_START_TIME     VARCHAR2(4000),
    MARKET_END_TIME       VARCHAR2(4000),
    DR_YN                 VARCHAR2(4000),
    DR_COUNTRY_CODE       VARCHAR2(4000),
    INDUSTRY_CODE         VARCHAR2(4000),
    INDEX_CONSTITUENT_YN  VARCHAR2(4000),
    TICK_SIZE_TYPE        VARCHAR2(4000),
    DIVISION_CODE         VARCHAR2(4000),
    TICK_SIZE_TYPE_DETAIL VARCHAR2(4000),
    CREATED_AT            DATE   not null,
    UPDATED_AT            DATE   not null
)
/

create index IX_OVER_STOCK_MST_SYMBOL
    on OVER_STOCK_MST (SYMBOL)
/

create index IX_OVER_STOCK_MST_EXCHANGE_CODE
    on OVER_STOCK_MST (EXCHANGE_CODE)
/

create table DOM_BOND_MST
(
    ID                NUMBER not null
        primary key,
    BOND_TYPE         VARCHAR2(4000),
    BOND_CLS_CODE     VARCHAR2(4000),
    STANDARD_CODE     VARCHAR2(4000),
    KOR_NAME          VARCHAR2(4000),
    BOND_INT_CLS_CODE VARCHAR2(4000),
    LISTED_DATE       VARCHAR2(4000),
    PUBLIC_DATE       VARCHAR2(4000),
    REDEMPTION_DATE   VARCHAR2(4000),
    CREATED_AT        DATE   not null,
    UPDATED_AT        DATE   not null
)
/

create index IX_DOM_BOND_MST_STANDARD_CODE
    on DOM_BOND_MST (STANDARD_CODE)
/

create table DOM_CME_FUTURE_MST
(
    ID                    NUMBER not null
        primary key,
    PRODUCT_TYPE          VARCHAR2(4000),
    SHORT_CODE            VARCHAR2(4000),
    STANDARD_CODE         VARCHAR2(4000),
    KOR_NAME              VARCHAR2(4000),
    STRIKE_PRICE          VARCHAR2(4000),
    UNDERLYING_SHORT_CODE VARCHAR2(4000),
    UNDERLYING_NAME       VARCHAR2(4000),
    CREATED_AT            DATE   not null,
    UPDATED_AT            DATE   not null
)
/

create index IX_DOM_CME_FUTURE_MST_STANDARD_CODE
    on DOM_CME_FUTURE_MST (STANDARD_CODE)
/

create index IX_DOM_CME_FUTURE_MST_SHORT_CODE
    on DOM_CME_FUTURE_MST (SHORT_CODE)
/

create table DOM_COM_FUTURE_MST
(
    ID                    NUMBER not null
        primary key,
    PRODUCT_CLASS         VARCHAR2(4000),
    PRODUCT_TYPE          VARCHAR2(4000),
    SHORT_CODE            VARCHAR2(4000),
    STANDARD_CODE         VARCHAR2(4000),
    KOR_NAME              VARCHAR2(4000),
    MONTH_CODE            VARCHAR2(4000),
    UNDERLYING_SHORT_CODE VARCHAR2(4000),
    UNDERLYING_NAME       VARCHAR2(4000),
    CREATED_AT            DATE   not null,
    UPDATED_AT            DATE   not null
)
/

create index IX_DOM_COM_FUTURE_MST_STANDARD_CODE
    on DOM_COM_FUTURE_MST (STANDARD_CODE)
/

create index IX_DOM_COM_FUTURE_MST_SHORT_CODE
    on DOM_COM_FUTURE_MST (SHORT_CODE)
/

create table DOM_ELW_MST
(
    ID                  NUMBER not null
        primary key,
    SHORT_CODE          VARCHAR2(4000),
    STANDARD_CODE       VARCHAR2(4000),
    KOR_NAME            VARCHAR2(4000),
    ELW_RIGHT_TYPE      VARCHAR2(4000),
    ELW_EARLY_END_PRICE VARCHAR2(4000),
    BASKET_YN           VARCHAR2(4000),
    UNDERLYING_CODE1    VARCHAR2(4000),
    UNDERLYING_CODE2    VARCHAR2(4000),
    UNDERLYING_CODE3    VARCHAR2(4000),
    UNDERLYING_CODE4    VARCHAR2(4000),
    UNDERLYING_CODE5    VARCHAR2(4000),
    ISSUER_NAME         VARCHAR2(4000),
    ISSUER_CODE         VARCHAR2(4000),
    STRIKE_PRICE        VARCHAR2(4000),
    LAST_TRADE_DATE     VARCHAR2(4000),
    REMAIN_DAYS         VARCHAR2(4000),
    RIGHT_TYPE_CODE     VARCHAR2(4000),
    PAYMENT_DATE        VARCHAR2(4000),
    PREV_MARKET_CAP     VARCHAR2(4000),
    LISTED_SHARES       VARCHAR2(4000),
    CREATED_AT          DATE   not null,
    UPDATED_AT          DATE   not null
)
/

create index IX_DOM_ELW_MST_SHORT_CODE
    on DOM_ELW_MST (SHORT_CODE)
/

create index IX_DOM_ELW_MST_STANDARD_CODE
    on DOM_ELW_MST (STANDARD_CODE)
/

create table DOM_EUREX_OPTION_MST
(
    ID                    NUMBER not null
        primary key,
    PRODUCT_TYPE          VARCHAR2(4000),
    SHORT_CODE            VARCHAR2(4000),
    STANDARD_CODE         VARCHAR2(4000),
    KOR_NAME              VARCHAR2(4000),
    ATM_DIVISION          VARCHAR2(4000),
    STRIKE_PRICE          VARCHAR2(4000),
    UNDERLYING_SHORT_CODE VARCHAR2(4000),
    UNDERLYING_NAME       VARCHAR2(4000),
    CREATED_AT            DATE   not null,
    UPDATED_AT            DATE   not null
)
/

create index IX_DOM_EUREX_OPTION_MST_STANDARD_CODE
    on DOM_EUREX_OPTION_MST (STANDARD_CODE)
/

create index IX_DOM_EUREX_OPTION_MST_SHORT_CODE
    on DOM_EUREX_OPTION_MST (SHORT_CODE)
/

create table DOM_KONEX_MST
(
    ID            NUMBER not null
        primary key,
    SHORT_CODE    VARCHAR2(4000),
    STANDARD_CODE VARCHAR2(4000),
    KOR_NAME      VARCHAR2(4000),
    GROUP_CODE    VARCHAR2(4000),
    BASE_PRICE    VARCHAR2(4000),
    LISTED_DATE   VARCHAR2(4000),
    LISTED_SHARES VARCHAR2(4000),
    CAPITAL       VARCHAR2(4000),
    FACE_VALUE    VARCHAR2(4000),
    CREATED_AT    DATE   not null,
    UPDATED_AT    DATE   not null
)
/

create index IX_DOM_KONEX_MST_SHORT_CODE
    on DOM_KONEX_MST (SHORT_CODE)
/

create index IX_DOM_KONEX_MST_STANDARD_CODE
    on DOM_KONEX_MST (STANDARD_CODE)
/

create table DOM_KOSDAQ_MST
(
    ID               NUMBER not null
        primary key,
    SHORT_CODE       VARCHAR2(4000),
    STANDARD_CODE    VARCHAR2(4000),
    KOR_NAME         VARCHAR2(4000),
    GROUP_CODE       VARCHAR2(4000),
    MARKET_CAP_SCALE VARCHAR2(4000),
    INDUSTRY_CODE_L  VARCHAR2(4000),
    INDUSTRY_CODE_M  VARCHAR2(4000),
    INDUSTRY_CODE_S  VARCHAR2(4000),
    BASE_PRICE       VARCHAR2(4000),
    LISTED_DATE      VARCHAR2(4000),
    LISTED_SHARES    VARCHAR2(4000),
    CAPITAL          VARCHAR2(4000),
    FACE_VALUE       VARCHAR2(4000),
    CREATED_AT       DATE   not null,
    UPDATED_AT       DATE   not null
)
/

create index IX_DOM_KOSDAQ_MST_SHORT_CODE
    on DOM_KOSDAQ_MST (SHORT_CODE)
/

create index IX_DOM_KOSDAQ_MST_STANDARD_CODE
    on DOM_KOSDAQ_MST (STANDARD_CODE)
/

create table DOM_KOSPI_MST
(
    ID               NUMBER not null
        primary key,
    SHORT_CODE       VARCHAR2(4000),
    STANDARD_CODE    VARCHAR2(4000),
    KOR_NAME         VARCHAR2(4000),
    GROUP_CODE       VARCHAR2(4000),
    MARKET_CAP_SCALE VARCHAR2(4000),
    INDUSTRY_CODE_L  VARCHAR2(4000),
    INDUSTRY_CODE_M  VARCHAR2(4000),
    INDUSTRY_CODE_S  VARCHAR2(4000),
    BASE_PRICE       VARCHAR2(4000),
    LISTED_DATE      VARCHAR2(4000),
    LISTED_SHARES    VARCHAR2(4000),
    CAPITAL          VARCHAR2(4000),
    FACE_VALUE       VARCHAR2(4000),
    CREATED_AT       DATE   not null,
    UPDATED_AT       DATE   not null
)
/

create index IX_DOM_KOSPI_MST_STANDARD_CODE
    on DOM_KOSPI_MST (STANDARD_CODE)
/

create index IX_DOM_KOSPI_MST_SHORT_CODE
    on DOM_KOSPI_MST (SHORT_CODE)
/

create table MEMBER_CODE_MST
(
    ID          NUMBER not null
        primary key,
    MEMBER_CODE VARCHAR2(4000),
    MEMBER_NAME VARCHAR2(4000),
    REGION_CODE VARCHAR2(4000),
    CREATED_AT  DATE   not null,
    UPDATED_AT  DATE   not null
)
/

create index IX_MEMBER_CODE_MST_MEMBER_CODE
    on MEMBER_CODE_MST (MEMBER_CODE)
/

create table OVER_INDEX_MST
(
    ID            NUMBER not null
        primary key,
    DIVISION_CODE VARCHAR2(4000),
    SYMBOL        VARCHAR2(4000),
    ENG_NAME      VARCHAR2(4000),
    KOR_NAME      VARCHAR2(4000),
    INDUSTRY_CODE VARCHAR2(4000),
    DOW30_YN      VARCHAR2(4000),
    NASDAQ100_YN  VARCHAR2(4000),
    SP500_YN      VARCHAR2(4000),
    EXCHANGE_CODE VARCHAR2(4000),
    NATION_CODE   VARCHAR2(4000),
    CREATED_AT    DATE   not null,
    UPDATED_AT    DATE   not null
)
/

create index IX_OVER_INDEX_MST_SYMBOL
    on OVER_INDEX_MST (SYMBOL)
/

create table SECTOR_MST
(
    ID          NUMBER not null
        primary key,
    SECTOR_CODE VARCHAR2(4000),
    SECTOR_NAME VARCHAR2(4000),
    CREATED_AT  DATE   not null,
    UPDATED_AT  DATE   not null
)
/

create index IX_SECTOR_MST_SECTOR_CODE
    on SECTOR_MST (SECTOR_CODE)
/

create table THEME_MST
(
    ID         NUMBER not null
        primary key,
    THEME_CODE VARCHAR2(4000),
    THEME_NAME VARCHAR2(4000),
    STOCK_CODE VARCHAR2(4000),
    CREATED_AT DATE   not null,
    UPDATED_AT DATE   not null
)
/

create index IX_THEME_MST_THEME_CODE
    on THEME_MST (THEME_CODE)
/

create table META_TABLE_MST
(
    TABLE_NAME  VARCHAR2(4000) not null
        primary key,
    DESCRIPTION VARCHAR2(4000),
    CREATED_AT  DATE           not null,
    UPDATED_AT  DATE           not null
)
/

create table META_COLUMN_MST
(
    ID          NUMBER         not null
        primary key,
    TABLE_NAME  VARCHAR2(4000) not null,
    COLUMN_NAME VARCHAR2(4000) not null,
    DESCRIPTION VARCHAR2(4000),
    CREATED_AT  DATE           not null,
    UPDATED_AT  DATE           not null
)
/

create index IX_META_COLUMN_MST_COLUMN_NAME
    on META_COLUMN_MST (COLUMN_NAME)
/

create index IX_META_COLUMN_MST_TABLE_NAME
    on META_COLUMN_MST (TABLE_NAME)
/

create table API_PARAM
(
    ID             NUMBER         not null
        primary key,
    API_NAME       VARCHAR2(4000) not null
        references API_MST,
    PARAM_NAME     VARCHAR2(4000) not null,
    PARAM_TYPE     VARCHAR2(4000) not null,
    IS_REQUIRED    NUMBER         not null,
    DEFAULT_VALUE  VARCHAR2(4000),
    MIN_LENGTH     NUMBER,
    MAX_LENGTH     NUMBER,
    ALLOWED_VALUES VARCHAR2(4000),
    DESCRIPTION    VARCHAR2(4000),
    CREATED_AT     DATE           not null
)
/

create index IX_API_PARAM_PARAM_NAME
    on API_PARAM (PARAM_NAME)
/

create table JOB_MST
(
    ID              NUMBER         not null
        primary key,
    API_NAME        VARCHAR2(4000) not null
        references API_MST,
    PARAMS_JSON     VARCHAR2(4000) not null,
    IS_ACTIVE       NUMBER         not null,
    SAVE_MODE       VARCHAR2(4000) not null,
    EXECUTION_CYCLE VARCHAR2(4000) not null,
    DESCRIPTION     VARCHAR2(4000),
    CREATED_AT      DATE           not null,
    UPDATED_AT      DATE           not null
)
/

create unique index IX_JOB_MST_API_NAME
    on JOB_MST (API_NAME)
/


