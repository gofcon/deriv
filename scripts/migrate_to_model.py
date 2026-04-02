"""
migrate_to_model.py
models_gofcon.py 기준으로 kis_api.db 스키마를 일치시킵니다.

변경 대상:
  1. api_mst   : PK api_name → api_id, 컬럼 재구성 (데이터 백업 후 재생성)
  2. api_param : PK id(auto) → composite(api_id, param_name), 컬럼 재구성

나머지 테이블은 이미 일치하므로 건드리지 않습니다.
"""

import sqlite3
import json
import sys
import os
from datetime import datetime

DB_PATH = r'd:\Python\deriv\data\kis_api.db'

def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def migrate():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = OFF")  # FK 비활성화 (재구성 중)
    cur = conn.cursor()

    try:
        # ════════════════════════════════════════════════
        # 1. api_mst 재구성
        #    현재: PK=api_name, columns: api_url, tr_id, tr_cont, request_type,
        #                                description, output_table_name, created_at, updated_at
        #    목표: PK=api_id, columns: api_name, api_type, api_url, header_json,
        #                              request_type, description, output_table_name, updated_at
        # ════════════════════════════════════════════════
        print("▶ [1/2] api_mst 마이그레이션 시작")

        # 기존 데이터 백업
        cur.execute("SELECT api_name, api_url, tr_id, tr_cont, request_type, description, output_table_name FROM api_mst")
        old_api_rows = cur.fetchall()
        print(f"  기존 데이터 {len(old_api_rows)}건 백업")

        # 백업 테이블 생성
        cur.execute("DROP TABLE IF EXISTS api_mst_bak")
        cur.execute("""
            CREATE TABLE api_mst_bak AS SELECT * FROM api_mst
        """)
        print("  api_mst_bak 생성 완료")

        # 기존 테이블 삭제
        cur.execute("DROP TABLE api_mst")

        # 새 테이블 생성 (models_gofcon.py ApiMst 기준)
        cur.execute("""
            CREATE TABLE api_mst (
                api_id          VARCHAR    NOT NULL PRIMARY KEY,
                api_name        VARCHAR(100) NOT NULL,
                api_type        VARCHAR(100) NOT NULL,
                api_url         VARCHAR(100) NOT NULL,
                header_json     JSON       NOT NULL,
                request_type    VARCHAR(20)  NOT NULL,
                description     VARCHAR(100),
                output_table_name VARCHAR(100),
                updated_at      DATETIME   DEFAULT (datetime('now'))
            )
        """)
        print("  새 api_mst 테이블 생성 완료")

        # 기존 데이터 -> 새 테이블로 이전
        # 매핑: api_id = api_name(PK), api_name = api_name, api_type = 'legacy',
        #        api_url = api_url, header_json = {"tr_id": tr_id, "tr_cont": tr_cont}
        migrated = 0
        for row in old_api_rows:
            old_api_name, old_api_url, old_tr_id, old_tr_cont, old_req_type, old_desc, old_output = row
            new_api_id   = old_api_name          # 기존 api_name을 api_id로 사용
            new_api_name = old_api_name
            new_api_type = "legacy"              # 기존 데이터는 legacy로 표시
            new_header   = json.dumps({"tr_id": old_tr_id, "tr_cont": old_tr_cont}, ensure_ascii=False)
            cur.execute("""
                INSERT INTO api_mst
                    (api_id, api_name, api_type, api_url, header_json,
                     request_type, description, output_table_name, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                new_api_id, new_api_name, new_api_type, old_api_url,
                new_header, old_req_type, old_desc, old_output, now_str(),
            ))
            migrated += 1
        print(f"  데이터 이전 완료: {migrated}건")

        # ════════════════════════════════════════════════
        # 2. api_param 재구성
        #    현재: PK=id(auto), FK=api_name, columns: param_type 포함
        #    목표: PK=(api_id, param_name) composite, FK=api_id → api_mst.api_id
        #          columns: is_required, default_value, min_length, max_length,
        #                   allowed_values, description, updated_at
        # ════════════════════════════════════════════════
        print("\n▶ [2/2] api_param 마이그레이션 시작")

        # 기존 데이터 백업
        cur.execute("""
            SELECT api_name, param_name, is_required, default_value,
                   min_length, max_length, allowed_values, description
            FROM api_param
        """)
        old_param_rows = cur.fetchall()
        print(f"  기존 데이터 {len(old_param_rows)}건 백업")

        # 백업 테이블
        cur.execute("DROP TABLE IF EXISTS api_param_bak")
        cur.execute("CREATE TABLE api_param_bak AS SELECT * FROM api_param")
        print("  api_param_bak 생성 완료")

        # 기존 테이블 삭제
        cur.execute("DROP TABLE api_param")

        # 새 테이블 생성 (models_gofcon.py ApiParam 기준)
        cur.execute("""
            CREATE TABLE api_param (
                api_id          VARCHAR    NOT NULL REFERENCES api_mst(api_id),
                param_name      VARCHAR(100) NOT NULL,
                is_required     INTEGER    NOT NULL DEFAULT 0,
                default_value   VARCHAR(20),
                min_length      INTEGER,
                max_length      INTEGER,
                allowed_values  VARCHAR(50),
                description     VARCHAR(100),
                updated_at      DATETIME   DEFAULT (datetime('now')),
                PRIMARY KEY (api_id, param_name)
            )
        """)
        print("  새 api_param 테이블 생성 완료")

        # 기존 데이터 이전
        # api_name = api_id (1:1 매핑)
        migrated = 0
        skipped  = 0
        for row in old_param_rows:
            old_api_name, pname, is_req, dflt, minl, maxl, allowed, desc = row
            # api_id가 새 api_mst에 존재하는지 확인
            cur.execute("SELECT api_id FROM api_mst WHERE api_id = ?", (old_api_name,))
            if not cur.fetchone():
                print(f"    ⚠ api_id='{old_api_name}' 가 api_mst에 없음 → 건너뜀")
                skipped += 1
                continue
            cur.execute("""
                INSERT OR IGNORE INTO api_param
                    (api_id, param_name, is_required, default_value,
                     min_length, max_length, allowed_values, description, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                old_api_name, pname,
                1 if is_req else 0,
                dflt, minl, maxl, allowed, desc, now_str(),
            ))
            migrated += 1
        print(f"  데이터 이전 완료: {migrated}건 (건너뜀: {skipped}건)")

        # ════════════════════════════════════════════════
        # 커밋 & FK 복원
        # ════════════════════════════════════════════════
        conn.commit()
        conn.execute("PRAGMA foreign_keys = ON")

        # 최종 검증
        print("\n✅ 마이그레이션 완료 - 최종 스키마 확인")
        print("\n[api_mst]")
        cur.execute('PRAGMA table_info("api_mst")')
        for r in cur.fetchall():
            print(f"  {r[1]:25s} {r[2]:20s} pk={r[5]}")
        cur.execute("SELECT COUNT(*) FROM api_mst")
        print(f"  → {cur.fetchone()[0]}건")

        print("\n[api_param]")
        cur.execute('PRAGMA table_info("api_param")')
        for r in cur.fetchall():
            print(f"  {r[1]:25s} {r[2]:20s} pk={r[5]}")
        cur.execute("SELECT COUNT(*) FROM api_param")
        print(f"  → {cur.fetchone()[0]}건")

        print("\n백업 테이블: api_mst_bak, api_param_bak (필요 없으면 수동으로 삭제하세요)")

    except Exception as e:
        conn.rollback()
        print(f"\n❌ 오류 발생: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
