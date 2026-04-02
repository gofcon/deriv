"""
Postman Collection (bond.postman_collection4.json)을 파싱하여
api_mst, api_param, api_schedule_mst 테이블에 데이터를 채우는 스크립트.
"""
import json
import sqlite3
import re
import sys
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SEIBRO_URL = "https://seibro.or.kr/websquare/engine/proworks/callServletService.jsp"
SEIBRO_REFERER = "https://seibro.or.kr/websquare/control.jsp?w2xPath=/IPORTAL/user/bond/BIP_CNTS03005V.xml&menuNo=88"

# Postman body XML을 파싱하여 action, task, params를 추출
def parse_xml_body(raw_body: str):
    """reqParam의 action, task와 내부 파라미터 목록을 추출합니다."""
    action = re.search(r'action="([^"]+)"', raw_body)
    task   = re.search(r'task="([^"]+)"', raw_body)
    # 모든 XML 태그 내 파라미터 추출: <PARAM_NAME value="..."/>
    params = re.findall(r'<([A-Z_]+)\s+value="([^"]*)"', raw_body)
    return (
        action.group(1) if action else None,
        task.group(1) if task else None,
        params  # [(param_name, default_value), ...]
    )

# API 이름 → api_id 변환 (소문자, snake_case 사용)
def to_api_id(name: str) -> str:
    return f"seibro_bond_{name}"

def main():
    collection_path = "data/bond.postman_collection4.json"
    db_path = "data/kis_api.db"

    with open(collection_path, "r", encoding="utf-8") as f:
        collection = json.load(f)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    items = collection.get("item", [])
    inserted_api = 0
    inserted_param = 0
    inserted_sched = 0

    for item in items:
        name = item.get("name", "")
        request = item.get("request", {})
        url_raw = request.get("url", {}).get("raw", SEIBRO_URL)
        method = request.get("method", "POST")
        body_raw = request.get("body", {}).get("raw", "")
        headers_list = request.get("header", [])

        # header → dict (활성화된 것만)
        header_dict = {}
        for h in headers_list:
            if not h.get("disabled", False):
                header_dict[h["key"]] = h["value"]

        # XML Body 파싱
        action, task, params = parse_xml_body(body_raw)

        api_id = to_api_id(name)
        api_name = f"Seibro Bond {name}"
        api_type = "seibro"
        description = f"Seibro API: {action or name}"
        output_table = "api_rst"

        # ---- api_mst 삽입 ----
        cursor.execute("SELECT api_id FROM api_mst WHERE api_id = ?", (api_id,))
        if cursor.fetchone():
            logging.info(f"  [SKIP] api_mst 이미 존재: {api_id}")
        else:
            cursor.execute("""
                INSERT INTO api_mst (api_id, api_name, api_type, api_url, header_json, request_type, description, output_table_name)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                api_id, api_name, api_type, SEIBRO_URL,
                json.dumps(header_dict, ensure_ascii=False),
                method, description, output_table
            ))
            logging.info(f"  [OK] api_mst 삽입: {api_id}")
            inserted_api += 1

        # ---- api_param 삽입 ----
        # 공통 파라미터 (action, task) 추가
        common_params = [
            ("ACTION", action or "", True),
            ("TASK", task or "", True),
        ]
        # XML body 내부 파라미터 추가
        body_params = [(p_name, p_val, False) for p_name, p_val in params]

        all_params = common_params + body_params

        for p_name, p_default, required in all_params:
            cursor.execute(
                "SELECT param_name FROM api_param WHERE api_id = ? AND param_name = ?",
                (api_id, p_name)
            )
            if cursor.fetchone():
                continue
            cursor.execute("""
                INSERT INTO api_param (api_id, param_name, is_required, default_value, description)
                VALUES (?, ?, ?, ?, ?)
            """, (api_id, p_name, 1 if required else 0, p_default, f"{p_name} parameter"))
            inserted_param += 1

        # ---- api_schedule_mst 삽입 ----
        schedule_id = f"{api_id}_daily"
        cursor.execute("SELECT schedule_id FROM api_schedule_mst WHERE schedule_id = ?", (schedule_id,))
        if cursor.fetchone():
            logging.info(f"  [SKIP] api_schedule_mst 이미 존재: {schedule_id}")
        else:
            # macro_params_json: 파라미터 기본값들로 구성
            # ISIN은 요청마다 달라지는 변수이므로 플레이스홀더로 처리
            macro_params = {"ACTION": action or "", "TASK": task or ""}
            for p_name, p_val in params:
                if p_name == "ISIN":
                    macro_params[p_name] = "{{ISIN}}"
                else:
                    macro_params[p_name] = p_val

            cursor.execute("""
                INSERT INTO api_schedule_mst (schedule_id, api_id, macro_params_json, is_active, save_mode, execution_cycle, description)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                schedule_id, api_id,
                json.dumps(macro_params, ensure_ascii=False),
                1, "overwrite", "daily",
                f"{api_name} daily schedule"
            ))
            logging.info(f"  [OK] api_schedule_mst 삽입: {schedule_id}")
            inserted_sched += 1

    conn.commit()
    conn.close()

    logging.info("=" * 50)
    logging.info(f"완료! api_mst: {inserted_api}건, api_param: {inserted_param}건, api_schedule_mst: {inserted_sched}건 삽입")

if __name__ == "__main__":
    main()
