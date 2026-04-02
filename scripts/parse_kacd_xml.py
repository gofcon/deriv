import xml.etree.ElementTree as ET
import json
import logging
from sqlmodel import Session, create_engine
import sys
import os

# Add parent directory to path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models import SeibroBondKacdList

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_and_load(xml_file_path: str, db_url: str):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    records = []
    
    # Seibro XML is <vector><data><result><...></result></data></vector>
    for data_node in root.findall('./data/result'):
        record_dict = {}
        # Each column is a node like <CODEVALUE value="..."/>
        for child in data_node:
            tag = child.tag
            value = child.get('value', '')
            record_dict[tag] = value
            
        records.append(record_dict)

    logging.info(f"Parsed {len(records)} records from {xml_file_path}")

    # Load to DB
    engine = create_engine(db_url)
    with Session(engine) as session:
        count = 0
        for rec in records:
            # Map fields
            code = rec.get('CODEVALUE', '')
            nm = rec.get('CODEVALUE_NM', '')
            
            db_rec = SeibroBondKacdList(
                api_id='seibro_bond_KACD_list',
                api_name='KACD_list',
                kacd_cd=code,
                bond_kor_nm=nm,
                record_json=json.dumps(rec, ensure_ascii=False)
            )
            session.add(db_rec)
            count += 1
            
        session.commit()
    
    logging.info(f"Successfully loaded {count} records into seibro_bond_KACD_list table.")

if __name__ == "__main__":
    xml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'kacd_list.xml')
    db_path = 'sqlite:///' + os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'kis_api.db')
    parse_and_load(xml_path, db_path)
