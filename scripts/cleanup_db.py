"""
cleanup_db.py
models_gofcon.py 에 정의되지 않은 테이블을 kis_api.db 에서 모두 삭제합니다.
"""
import sqlite3, sys

DB_PATH = r'd:\Python\deriv\data\kis_api.db'

# models_gofcon.py 에 정의된 테이블 (유지 대상)
MODEL_TABLES = {
    'api_mst', 'api_param', 'api_schedule_mst', 'api_job_mst',
    'browser_mst', 'browser_schedule_mst', 'browser_job_mst', 'browser_rst',
    'krx_isin_mst',
    'kis_stock_price', 'kis_daily_price', 'kis_display_board_top',
    'kis_dom_future_mst', 'kis_over_future_mst', 'kis_dom_stock_future_mst',
    'kis_over_stock_mst', 'kis_dom_bond_mst', 'kis_dom_cme_future_mst',
    'kis_dom_com_future_mst', 'kis_dom_elw_mst', 'kis_dom_eurex_option_mst',
    'kis_dom_konex_mst', 'kis_dom_kosdaq_mst', 'kis_dom_kospi_mst',
    'kis_member_code_mst', 'kis_over_index_mst', 'kis_sector_mst',
    'kis_theme_mst', 'kis_meta_table_mst', 'kis_meta_column_mst',
}

conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys = OFF")
cur = conn.cursor()

# 현재 테이블 목록 조회
cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
all_tables = [r[0] for r in cur.fetchall()]

# sqlite_sequence 는 SQLite 내부 시스템 테이블 → 삭제 불가, 제외
SYSTEM_TABLES = {'sqlite_sequence', 'sqlite_stat1', 'sqlite_stat2', 'sqlite_stat3', 'sqlite_stat4'}
to_drop   = [t for t in all_tables if t not in MODEL_TABLES and t not in SYSTEM_TABLES]
to_keep   = [t for t in all_tables if t in MODEL_TABLES]

print(f"전체 테이블: {len(all_tables)}개")
print(f"유지 대상  : {len(to_keep)}개")
print(f"삭제 대상  : {len(to_drop)}개")
print()
print("=== 삭제 대상 목록 ===")
for t in sorted(to_drop):
    cur.execute(f'SELECT COUNT(*) FROM "{t}"')
    n = cur.fetchone()[0]
    print(f"  DROP {t:<50s} ({n}건)")

# 드라이런 모드: --dry-run 인자 없으면 실제 삭제 수행
dry_run = "--dry-run" in sys.argv

if dry_run:
    print(f"\n[DRY-RUN] 실제 삭제는 수행하지 않습니다.")
else:
    print(f"\n실제 삭제 시작...")
    dropped = 0
    for t in to_drop:
        cur.execute(f'DROP TABLE IF EXISTS "{t}"')
        dropped += 1
    conn.commit()
    print(f"✅ {dropped}개 테이블 삭제 완료")
    
    # 최종 확인
    cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
    remain = cur.fetchone()[0]
    print(f"남은 테이블: {remain}개")

conn.execute("PRAGMA foreign_keys = ON")
conn.close()
