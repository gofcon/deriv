"""
seed_bond_api.py
bond.postman_collection.json → kis_api.db (api_mst / api_param / api_schedule_mst)

DB 스키마 (models_gofcon.py 기준):
  api_mst          PK: api_id
  api_param        PK: (api_id, param_name) 복합키
  api_schedule_mst PK: schedule_id, FK: api_id → api_mst.api_id
"""

import sys, os, json, sqlite3, logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH   = os.path.join(BASE_DIR, "data", "kis_api.db")
JSON_PATH = os.path.join(BASE_DIR, "data", "bond.postman_collection2.json")

# ──────────────────────────────────────────────────────────
# seibro 채권 API 메타 정의
# 각 Postman request name → action / task / description
# ──────────────────────────────────────────────────────────
BOND_META = {
    "cashflow": {
        "action": "bondPrinXchgList",
        "task":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "채권 원리금 현금흐름 목록 조회",
    },
    "cashflow_cnt": {
        "action": "bondPrinXchgListCnt",
        "task":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "채권 원리금 현금흐름 건수 조회",
    },
    "exerPrice": {
        "action": "bondExerPriceList",
        "task":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "채권 행사가격 목록 조회",
    },
    "exerDetail": {
        "action": "bondExerDetailList",
        "task":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "채권 행사 세부 목록 조회",
    },
    "exerInfo": {
        "action": "bondExerInfoList",
        "task":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "채권 행사 정보 조회",
    },
    "optionSche": {
        "action": "bondOptionScheList",
        "task":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "채권 옵션 스케줄 조회",
    },
    "yield": {
        "action": "bondYieldList",
        "task":   "ksd.safe.bip.cnts.bond.process.BondSecnYieldPTask",
        "desc":   "채권 수익률 목록 조회",
    },
    "yield_cnt": {
        "action": "bondYieldListCnt",
        "task":   "ksd.safe.bip.cnts.bond.process.BondSecnYieldPTask",
        "desc":   "채권 수익률 건수 조회",
    },
    "credit": {
        "action": "bondCreditList",
        "task":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "채권 신용등급 조회",
    },
    "creditList": {
        "action": "bondCreditRatingList",
        "task":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "채권 신용등급 이력 목록 조회",
    },
    "coupon_sche": {
        "action": "bondCouponScheList",
        "task":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "채권 이자(쿠폰) 지급 스케줄 조회",
    },
    # ── v2 신규 추가 ──
    "isin_by_KACD": {
        "ACTION": "bondIsinByKacdList",
        "TASK":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "KACD 코드로 채권 ISIN 조회",
    },
    "KACD_list": {
        "ACTION": "bondKacdList",
        "TASK":   "ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask",
        "desc":   "채권 KACD 코드 목록 조회",
        "no_isin": True,   # KACD 전체 목록 조회 → ISIN 불필요
    },
}

SEIBRO_URL     = "https://seibro.or.kr/websquare/engine/proworks/callServletService.jsp"
SEIBRO_REFERER = "https://seibro.or.kr/websquare/control.jsp?w2xPath=/IPORTAL/user/bond/BIP_CNTS03005V.xml&menuNo=88"


def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ──────────────────────────────────────────────
# api_mst  UPSERT
# PK: api_id
# ──────────────────────────────────────────────
def upsert_api_mst(cur, api_id: str, api_name: str, meta: dict):
    header_json = json.dumps({
        "Referer":      SEIBRO_REFERER,
        "Content-Type": "application/xml; charset=UTF-8",
        "Accept":       "application/xml",
    }, ensure_ascii=False)

    cur.execute("SELECT api_id FROM api_mst WHERE api_id = ?", (api_id,))
    if cur.fetchone():
        cur.execute("""
            UPDATE api_mst SET
                api_name=?, api_type=?, api_url=?, header_json=?,
                request_type=?, description=?, updated_at=?
            WHERE api_id=?
        """, (api_name, "seibro_bond", SEIBRO_URL, header_json,
              "POST", meta["desc"], now_str(), api_id))
        logging.info(f"  [api_mst] UPDATE {api_id}")
    else:
        cur.execute("""
            INSERT INTO api_mst
                (api_id, api_name, api_type, api_url, header_json,
                 request_type, description, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (api_id, api_name, "seibro_bond", SEIBRO_URL, header_json,
              "POST", meta["desc"], now_str()))
        logging.info(f"  [api_mst] INSERT {api_id}")


# ──────────────────────────────────────────────
# api_param  UPSERT
# PK: (api_id, param_name) 복합키
# ──────────────────────────────────────────────
def upsert_api_param(cur, api_id: str, param_name: str,
                     is_required: bool, default_value, description: str,
                     allowed_values=None):
    cur.execute(
        "SELECT api_id FROM api_param WHERE api_id=? AND param_name=?",
        (api_id, param_name)
    )
    ts = now_str()
    if cur.fetchone():
        cur.execute("""
            UPDATE api_param SET
                is_required=?, default_value=?, allowed_values=?,
                description=?, updated_at=?
            WHERE api_id=? AND param_name=?
        """, (1 if is_required else 0, default_value, allowed_values,
              description, ts, api_id, param_name))
    else:
        cur.execute("""
            INSERT INTO api_param
                (api_id, param_name, is_required, default_value,
                 allowed_values, description, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (api_id, param_name,
              1 if is_required else 0,
              default_value, allowed_values, description, ts))
    logging.info(f"    [api_param] {api_id}.{param_name}")


# ──────────────────────────────────────────────
# api_schedule_mst  UPSERT
# PK: schedule_id,  FK: api_id
# ──────────────────────────────────────────────
def upsert_schedule(cur, schedule_id: str, api_id: str,
                    macro_params: dict, description: str):
    macro_json = json.dumps(macro_params, ensure_ascii=False)
    ts = now_str()
    cur.execute(
        "SELECT schedule_id FROM api_schedule_mst WHERE schedule_id=?",
        (schedule_id,)
    )
    if cur.fetchone():
        cur.execute("""
            UPDATE api_schedule_mst SET
                api_id=?, macro_params_json=?, is_active=1,
                save_mode=?, execution_cycle=?, description=?, updated_at=?
            WHERE schedule_id=?
        """, (api_id, macro_json, "overwrite", "daily", description, ts, schedule_id))
        logging.info(f"  [api_schedule_mst] UPDATE {schedule_id}")
    else:
        cur.execute("""
            INSERT INTO api_schedule_mst
                (schedule_id, api_id, macro_params_json, is_active,
                 save_mode, execution_cycle, description, updated_at)
            VALUES (?, ?, ?, 1, ?, ?, ?, ?)
        """, (schedule_id, api_id, macro_json,
              "overwrite", "daily", description, ts))
        logging.info(f"  [api_schedule_mst] INSERT {schedule_id}")


# ──────────────────────────────────────────────
# 메인
# ──────────────────────────────────────────────
def main():
    with open(JSON_PATH, encoding="utf-8") as f:
        collection = json.load(f)

    items = collection.get("item", [])
    logging.info(f"Postman 요청 수: {len(items)}건 → {[i['name'] for i in items]}")

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    cur  = conn.cursor()

    try:
        for item in items:
            name = item["name"]
            if name not in BOND_META:
                logging.warning(f"⚠ '{name}' 메타 정의 없음 → 건너뜀")
                continue

            meta     = BOND_META[name]
            api_id   = f"seibro_bond_{name}"     # PK

            logging.info(f"\n▶ {name}  (api_id={api_id})")

            # 1. api_mst
            upsert_api_mst(cur, api_id, name, meta)

            # 2. api_param
            #    ISIN        : 필수 매크로 (채권 종목코드) - no_isin 플래그가 있는 API는 제외
            #    PAGE_ON_CNT : 페이지당 건수
            #    PAGE_NUM    : 페이지 번호
            #    ACTION      : XML body action (고정값)
            #    TASK        : XML body task   (고정값)
            no_isin = meta.get("no_isin", False)
            params = [
                # (param_name, is_required, default, description, allowed_values)
                ("PAGE_ON_CNT", False, "100",          "페이지당 조회 건수",                       None),
                ("PAGE_NUM",    False, "1",            "조회 페이지 번호 (1부터 시작)",             None),
                ("ACTION",      True,  meta["ACTION"], "XML body reqParam action 값 (고정)",       meta["ACTION"]),
                ("TASK",        True,  meta["TASK"],   "XML body reqParam task 값 (고정)",         meta["TASK"]),
            ]
            if not no_isin:
                params.insert(0, ("ISIN", True, None, "조회 대상 채권 ISIN 코드 (예: KR103502G990)", None))
            for p in params:
                upsert_api_param(cur, api_id, p[0], p[1], p[2], p[3], p[4])

            # 3. api_schedule_mst
            schedule_id  = f"seibro_bond_{name}_daily"
            macro_params = {
                "PAGE_ON_CNT": "100",
                "PAGE_NUM":    "1",
                "ACTION":      meta["ACTION"],
                "TASK":        meta["TASK"],
            }
            if not no_isin:
                macro_params["ISIN"] = "{ISIN}"   # 실행 시 종목코드로 치환
            upsert_schedule(cur, schedule_id, api_id, macro_params, meta["desc"])

        conn.commit()

        # ── 결과 요약 ──
        logging.info("\n" + "="*50)
        logging.info("✅ 데이터 적재 완료")
        cur.execute("SELECT COUNT(*) FROM api_mst WHERE api_type='seibro_bond'")
        logging.info(f"  api_mst          : {cur.fetchone()[0]}건 (seibro_bond)")
        cur.execute("SELECT COUNT(*) FROM api_param WHERE api_id LIKE 'seibro_bond_%'")
        logging.info(f"  api_param        : {cur.fetchone()[0]}건")
        cur.execute("SELECT COUNT(*) FROM api_schedule_mst WHERE schedule_id LIKE 'seibro_bond_%'")
        logging.info(f"  api_schedule_mst : {cur.fetchone()[0]}건")
        logging.info("="*50)

        # ── 상세 데이터 확인 ──
        logging.info("\n[적재된 api_mst 목록]")
        cur.execute("""
            SELECT api_id, api_name, api_type, request_type, description
            FROM api_mst WHERE api_type='seibro_bond' ORDER BY api_id
        """)
        for r in cur.fetchall():
            logging.info(f"  {r[0]:40s} | {r[4]}")

    except Exception as e:
        conn.rollback()
        logging.error(f"❌ 오류: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
