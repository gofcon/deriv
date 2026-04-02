"""
Seibro Open API (http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp)
형식의 api_mst, api_param, api_schedule_mst 테이블을 채웁니다.

URL 형식: callOpenAPI.jsp?key=SEIBRO_KEY&apiId=getBondStatInfo&params=ISIN:KR...
"""
import sqlite3
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SEIBRO_OPEN_BASE_URL = "http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp"
SEIBRO_OPEN_API_TYPE = "seibro_open"
ISIN_PLACEHOLDER = "{{ISIN}}"

# Seibro Open API 목록 정의
# 형식: (api_id, apiId(실제호출ID), description, params: [(이름, 기본값, 필수여부, 설명)])
SEIBRO_OPEN_APIS = [
    (
        "seibro_open_getBondStatInfo",
        "getBondStatInfo",
        "채권 기본정보 조회",
        [
            ("ISIN", ISIN_PLACEHOLDER, True, "채권 ISIN 코드"),
        ]
    ),
]

def main(db_path='data/kis_api.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    inserted_api = inserted_param = inserted_sched = 0

    for api_id, api_id_real, description, params in SEIBRO_OPEN_APIS:
        api_name = api_id_real  # apiId 값을 api_name에 저장 (SeibroOpenHttpClient에서 api_id로 사용)
        header_json = json.dumps({}, ensure_ascii=False)

        # ---- api_mst ----
        cursor.execute("SELECT api_id FROM api_mst WHERE api_id = ?", (api_id,))
        if cursor.fetchone():
            logging.info(f"  [SKIP] api_mst 이미 존재: {api_id}")
        else:
            cursor.execute("""
                INSERT INTO api_mst (api_id, api_name, api_type, api_url, header_json, request_type, description, output_table_name)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                api_id, api_name, SEIBRO_OPEN_API_TYPE,
                SEIBRO_OPEN_BASE_URL, header_json,
                "GET", description, "api_rst"
            ))
            logging.info(f"  [OK] api_mst 삽입: {api_id}")
            inserted_api += 1

        # ---- api_param ----
        for p_name, p_default, required, p_desc in params:
            cursor.execute(
                "SELECT param_name FROM api_param WHERE api_id = ? AND param_name = ?",
                (api_id, p_name)
            )
            if cursor.fetchone():
                continue
            cursor.execute("""
                INSERT INTO api_param (api_id, param_name, is_required, default_value, description)
                VALUES (?, ?, ?, ?, ?)
            """, (api_id, p_name, 1 if required else 0, p_default, p_desc))
            inserted_param += 1
            logging.info(f"  [OK] api_param 삽입: {api_id}.{p_name}")

        # ---- api_schedule_mst ----
        schedule_id = f"{api_id}_daily"
        cursor.execute("SELECT schedule_id FROM api_schedule_mst WHERE schedule_id = ?", (schedule_id,))
        if cursor.fetchone():
            logging.info(f"  [SKIP] api_schedule_mst 이미 존재: {schedule_id}")
        else:
            macro_params = {p_name: p_default for p_name, p_default, _, _ in params}
            cursor.execute("""
                INSERT INTO api_schedule_mst (schedule_id, api_id, macro_params_json, is_active, save_mode, execution_cycle, description)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                schedule_id, api_id,
                json.dumps(macro_params, ensure_ascii=False),
                1, "overwrite", "daily",
                f"{description} daily schedule"
            ))
            logging.info(f"  [OK] api_schedule_mst 삽입: {schedule_id}")
            inserted_sched += 1

    conn.commit()
    conn.close()
    logging.info("=" * 50)
    logging.info(f"완료! api_mst: {inserted_api}건, api_param: {inserted_param}건, api_schedule_mst: {inserted_sched}건 삽입")

if __name__ == "__main__":
    main()
