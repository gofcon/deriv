import sqlite3
import json
import os
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_kacd_jobs(db_path='data/kis_api.db'):
    if not os.path.exists(db_path):
        logging.error(f"데이터베이스 파일을 찾을 수 없습니다: {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # 1. KACD 코드 및 명칭 조회 (테이블명 대문자 주의: SEIBRO_BOND_KACD_LIST)
        cursor.execute("SELECT kacd_cd, bond_kor_nm FROM SEIBRO_BOND_KACD_LIST")
        kacd_list = cursor.fetchall()
        logging.info(f"조회된 KACD 코드 수: {len(kacd_list)}")

        if not kacd_list:
            logging.warning("조회된 KACD 코드가 없습니다.")
            return

        # 2. 기준 API 정보 조회 (seibro_bond_isin_by_KACD)
        cursor.execute("SELECT save_mode, execution_cycle FROM api_mst WHERE api_id = 'seibro_bond_isin_by_KACD'")
        api_meta = cursor.fetchone()
        
        default_save_mode = api_meta[0] if api_meta else 'overwrite'
        default_cycle = api_meta[1] if api_meta else 'daily'

        # 3. Job 생성 루프
        new_jobs_count = 0
        skipped_count = 0
        
        for kacd_cd, bond_kor_nm in kacd_list:
            if not kacd_cd:
                continue
                
            job_id = f"seibro_bond_isin_by_KACD_{kacd_cd}"
            api_id = "seibro_bond_isin_by_KACD"
            
            # 파라미터 JSON 구성
            params = {
                "ACTION": "searchBondDepthContentList",
                "PAGE_NUM": "1",
                "PAGE_ON_CNT": "100",
                "SECN_DTAIL_KACD": kacd_cd,
                "TASK": "ksd.safe.bip.cmuc.User.process.SearchPTask"
            }
            params_json = json.dumps(params, ensure_ascii=False)
            
            # 중복 체크
            cursor.execute("SELECT count(*) FROM api_job_mst WHERE job_id = ?", (job_id,))
            if cursor.fetchone()[0] > 0:
                skipped_count += 1
                continue
            
            # 데이터 삽입 (api_job_mst 스키마 기준)
            # id는 자동생성이므로 제외
            cursor.execute("""
                INSERT INTO api_job_mst (
                    job_id, api_id, params_json, save_mode, execution_cycle, is_active, description
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (job_id, api_id, params_json, default_save_mode, default_cycle, 1, bond_kor_nm))
            
            new_jobs_count += 1

        conn.commit()
        logging.info(f"작업 완료: 신규 생성 {new_jobs_count}건, 중복 건너뜀 {skipped_count}건")

    except Exception as e:
        logging.error(f"데이터 생성 중 오류 발생: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    generate_kacd_jobs()
