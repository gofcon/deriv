"""
api_schedule_mst 의 macro_params_json 에서 ISIN 고정값을 {{ISIN}} 변수로 교체합니다.
"""
import sqlite3
import json
import logging
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ISIN_PLACEHOLDER = "{{ISIN}}"

def update_isin_as_variable(db_path='data/kis_api.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT schedule_id, macro_params_json FROM api_schedule_mst")
    rows = cursor.fetchall()

    updated = 0
    for schedule_id, macro_json_str in rows:
        if not macro_json_str:
            continue

        try:
            macro = json.loads(macro_json_str)
        except Exception:
            continue

        # ISIN 키가 있고, 변수 플레이스홀더가 아닌 경우 교체
        if "ISIN" in macro and macro["ISIN"] != ISIN_PLACEHOLDER:
            old_val = macro["ISIN"]
            macro["ISIN"] = ISIN_PLACEHOLDER
            new_json = json.dumps(macro, ensure_ascii=False)
            cursor.execute(
                "UPDATE api_schedule_mst SET macro_params_json = ? WHERE schedule_id = ?",
                (new_json, schedule_id)
            )
            logging.info(f"  [UPDATED] {schedule_id}: ISIN '{old_val}' → '{ISIN_PLACEHOLDER}'")
            updated += 1

    conn.commit()
    conn.close()
    logging.info(f"완료: {updated}건 업데이트")

if __name__ == "__main__":
    update_isin_as_variable()
