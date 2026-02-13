"""
csv_importer.py - CSV와 DB 간 변환
"""

import logging
import argparse
import pandas as pd
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import DatabaseManager

from logs.log_setup import setup_logging

setup_logging()

# Default DB path relative to script location
DEFAULT_DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "kis_api.db")

def import_from_csv(csv_file: str, db_path: str = DEFAULT_DB_PATH) -> None:
    """CSV → DB 임포트"""
    
    db = DatabaseManager(db_path)
    
    print("="*80)
    print(f"CSV 임포트: {csv_file}")
    print("="*80)
    
    df = pd.read_csv(csv_file)
    
    api_count = 0
    param_count = 0
    
    for program_name, group in df.groupby('program_name'):
        first_row = group.iloc[0]
        
        # API 정의
        api_def = db.add_api_definition(
            program_name=program_name,
            api_url=first_row['api_url'],
            tr_id=first_row['tr_id'],
            tr_cont=first_row.get('tr_cont', '') if pd.notna(first_row.get('tr_cont')) else '',
            description=first_row.get('api_description') if pd.notna(first_row.get('api_description')) else None
        )
        
        if api_def:
            api_count += 1
            print(f"\n[{api_count}] {program_name}")
            
            # 파라미터 정의
            for _, row in group.iterrows():
                param_name = row['param_name']
                param_value = row.get('param_value', '')
                param_required = row.get('param_required', 'N')
                allowed_values = row.get('allowed_values')
                min_length = row.get('min_length')
                max_length = row.get('max_length')
                
                # NaN 처리
                if pd.isna(param_value):
                    param_value = ''
                if pd.isna(allowed_values):
                    allowed_values = None
                if pd.isna(min_length):
                    min_length = None
                else:
                    min_length = int(min_length)
                if pd.isna(max_length):
                    max_length = None
                else:
                    max_length = int(max_length)
                
                is_required = str(param_required).upper() == 'Y'
                
                param_def = db.add_parameter_definition(
                    program_name=program_name,
                    param_name=param_name,
                    is_required=is_required,
                    default_value=param_value if param_value else None,
                    allowed_values=allowed_values,
                    min_length=min_length,
                    max_length=max_length,
                    description=row.get('param_description')
                )
                
                if param_def:
                    param_count += 1
                    print(f"  - {param_name}")
    
    print(f"\n{'='*80}")
    print(f"✓ 임포트 완료: API {api_count}개, 파라미터 {param_count}개")
    print(f"{'='*80}")


def export_to_csv(db_path: str = DEFAULT_DB_PATH, output_file: str = "export.csv") -> None:
    """DB → CSV 익스포트"""
    
    db = DatabaseManager(db_path)
    
    print("="*80)
    print(f"CSV 익스포트: {output_file}")
    print("="*80)
    
    rows = []
    
    for api in db.list_api_definitions():
        params = db.get_parameter_definitions(api.program_name)
        
        for param in params:
            rows.append({
                'program_name': api.program_name,
                'api_url': api.api_url,
                'tr_id': api.tr_id,
                'tr_cont': api.tr_cont,
                'api_description': api.description,
                'param_name': param.param_name,
                'param_value': param.default_value or '',
                'param_required': 'Y' if param.is_required else 'N',
                'allowed_values': param.allowed_values or '',
                'min_length': param.min_length if param.min_length else '',
                'max_length': param.max_length if param.max_length else '',
                'param_description': param.description or ''
            })
    
    if rows:
        df = pd.DataFrame(rows)
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"✓ 익스포트 완료: {len(rows)}개 행")
    else:
        print("! 데이터 없음")
    
    print("="*80)


def main():
    parser = argparse.ArgumentParser(description='CSV ↔ DB 변환')
    
    parser.add_argument('--action', choices=['import', 'export'])
    parser.add_argument('--file', required=True)
    parser.add_argument('--db', default=DEFAULT_DB_PATH)
    
    args = parser.parse_args()
    
    if args.action == 'import':
        import_from_csv(args.file, args.db)
    else:
        export_to_csv(args.db, args.file)


if __name__ == "__main__":
    main()
