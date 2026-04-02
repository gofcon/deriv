import sqlite3
import json
import logging
import os
import sys

# 프로젝트 루트를 경로에 추가 (app 모듈 임포트용)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import DatabaseManager
from app.models_seibro import SeibroBondIsinList
from sqlmodel import select

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_and_load_isin_data(job_id: str = "seibro_bond_isin_by_KACD_daily_110110"):
    db = DatabaseManager('data/kis_api.db')
    
    # DB 연결 및 테이블 생성 보장
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(db.engine)
    
    with db.get_session() as session:
        # 먼저 api_rst에서 데이터를 읽어옴 (SQLite 쿼리 직접 사용 또는 모델 사용)
        # ApiRst 모델을 임포트하는 것보다 범용적으로 연결 활용
        pass
        
    # sqlite3 직접 연결을 활용해 읽기 (대량 혹은 원시 JSON 처리에 유용)
    conn = sqlite3.connect('data/kis_api.db')
    cursor = conn.cursor()
    cursor.execute("SELECT result_json FROM api_rst WHERE job_id = ?", (job_id,))
    row = cursor.fetchone()
    
    if not row:
        logging.warning(f"{job_id}에 대한 결과 데이터가 api_rst에 없습니다.")
        conn.close()
        return
        
    try:
        data = json.loads(row[0])
        records = []
        if isinstance(data, dict) and 'data' in data:
            records = data['data']
        elif isinstance(data, list):
            records = data
            
        if not records:
            logging.warning("파싱된 JSON 내부에 레코드가 없습니다.")
            conn.close()
            return
            
        logging.info(f"파싱 완료. 총 {len(records)}개의 종목 정보를 적재합니다.")
        
        # SQLAlchemy Session으로 데이터 검증 및 적재
        with db.get_session() as session:
            # 먼저 기존 데이터 삭제 (해당 job_id 기준 덮어쓰기 로직 원할 시)
            statement = select(SeibroBondIsinList).where(SeibroBondIsinList.job_id == job_id)
            existing = session.exec(statement).all()
            for obj in existing:
                session.delete(obj)
            session.commit()
                
            count = 0
            for item in records:
                isin = item.get('ISIN')
                bond_kor_nm = item.get('KOR_SECN_NM')
                issue_dt = item.get('ISSU_DT')
                
                if not isin:
                    continue
                    
                new_record = SeibroBondIsinList(
                    job_id=job_id,
                    isin=isin,
                    bond_kor_nm=bond_kor_nm,
                    issue_dt=issue_dt
                )
                session.add(new_record)
                count += 1
                
            session.commit()
            logging.info(f"DB 적재 완료: {count}건")
            
    except Exception as e:
        logging.error(f"데이터 추출 및 적재 중 오류 발생: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    extract_and_load_isin_data()
