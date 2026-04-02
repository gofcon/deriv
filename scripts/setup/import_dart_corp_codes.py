import os
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
import logging

# 프로젝트 루트 경로 추가 (app 패키지 인식을 위해)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from app.database import DatabaseManager
from app.models_dart import DartCorpCode
from sqlmodel import Session, select, func

# 로그 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def import_corp_codes(xml_path: str):
    if not os.path.exists(xml_path):
        logging.error(f"XML 파일을 찾을 수 없습니다: {xml_path}")
        return

    db = DatabaseManager()
    
    # 테이블 생성 (없을 경우)
    from app.models_dart import SQLModel
    SQLModel.metadata.create_all(db.engine)
    
    count = 0
    batch_size = 5000
    batch_data = []

    logging.info(f"XML 파싱 시작: {xml_path}")
    
    # KST Now
    kst_now = datetime.now(timezone(timedelta(hours=9))).replace(tzinfo=None)

    # 대용량 XML 처리를 위한 스트리밍 파싱
    context = ET.iterparse(xml_path, events=('end',))
    
    with Session(db.engine) as session:
        for event, elem in context:
            if elem.tag == 'list':
                # 데이터 추출
                corp_code = elem.findtext('corp_code')
                corp_name = elem.findtext('corp_name')
                corp_eng_name = elem.findtext('corp_eng_name', '').strip()
                stock_code = elem.findtext('stock_code', '').strip()
                modify_date = elem.findtext('modify_date')

                # 상장 코드가 스페이스 하나로 오는 경우 처리
                if not stock_code or stock_code == 'None':
                    stock_code = None
                
                # 객체 생성
                record = DartCorpCode(
                    api_id="dart_corp_code",
                    corp_code=corp_code,
                    corp_name=corp_name,
                    corp_eng_name=corp_eng_name if corp_eng_name else None,
                    stock_code=stock_code,
                    modify_date=modify_date,
                    updated_at=kst_now
                )
                
                batch_data.append(record)
                count += 1
                
                # 배치 단위 적재 (성능 최적화)
                if len(batch_data) >= batch_size:
                    for item in batch_data:
                        session.merge(item)  # INSERT OR UPDATE (Upsert)
                    session.commit()
                    logging.info(f"... {count}개 처리 완료")
                    batch_data = []
                
                # 메모리 해제
                elem.clear()

        # 남은 데이터 처리
        if batch_data:
            for item in batch_data:
                session.merge(item)
            session.commit()
            logging.info(f"최종 {count}개 처리 완료")

if __name__ == "__main__":
    # 기본 경로 설정
    xml_file = os.path.join(project_root, "data", "CORPCODE.xml")
    import_corp_codes(xml_file)
