import sqlite3
import json
import os
import subprocess
import sys

# app 모듈 로드를 위한 경로 추가
sys.path.append(os.getcwd())

def test_seibro_isin():
    db_path = 'data/kis_api.db'
    python_exe = os.path.join(os.getcwd(), '.venv', 'Scripts', 'python.exe')
    main_py = os.path.join(os.getcwd(), 'main.py')

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # 1. Seibro 전용 채권 상세 Job 등록
    # 기존 테스트용 Job 모두 정리 (검증 실패 방지)
    cur.execute("DELETE FROM api_job_mst WHERE job_id LIKE 'test_seibro_isin_final%'")
    
    job_id = 'test_seibro_isin_final_v2'
    params = {
        'ACTION': 'issuInfoViewEL1',
        'TASK': 'ksd.safe.bip.cnts.bone.process.BondSecnDetailPTask',
        'ISIN': 'KR6268761881'
    }
    
    # seibro_bond_baseinfo API 사용 (api_type='seibro')
    cur.execute("DELETE FROM api_job_mst WHERE job_id=?", (job_id,))
    cur.execute("""
        INSERT INTO api_job_mst (job_id, api_id, status, is_active, execution_cycle, params_json, save_mode)
        VALUES (?, 'seibro_bond_baseinfo', 'READY', 1, 'once', ?, 'overwrite')
    """, (job_id, json.dumps(params)))
    
    # 2. 필수 헤더 설정
    cur.execute("SELECT header_json FROM api_mst WHERE api_id='seibro_bond_baseinfo'")
    row = cur.fetchone()
    header_json = json.loads(row[0]) if row and row[0] else {}
    header_json['Content-Type'] = 'application/xml'
    cur.execute("UPDATE api_mst SET header_json=? WHERE api_id='seibro_bond_baseinfo'", (json.dumps(header_json),))

    conn.commit()
    conn.close()

    print(f"\n>>> Running Seibro ISIN Test (Job: {job_id})")
    subprocess.run([python_exe, main_py, '--cycle', 'once'])

    # 3. 결과 확인 (api_rst 또는 텍스트 로그 확인)
    # main.py 실행로그에서 "성공: 1건 (DB 저장: 1건)"이 뜨는지 확인하는 것이 최선
    print("\n" + "="*60)
    print("CHECK LOGS FOR SUCCESS: '성공: 1건 (DB 저장: 1건)'")
    print("="*60 + "\n")

if __name__ == '__main__':
    test_seibro_isin()
