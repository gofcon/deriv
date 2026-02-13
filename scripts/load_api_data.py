"""
load_api_data.py - GitHub examples_llm 폴더에서 API 정의 로드
"""

import os
import ast
import logging
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Optional, List, Dict
from app.database import DatabaseManager
from app.config import DB_PATH
import json

from logs.log_setup import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_DIR = os.path.join(PROJECT_ROOT, "temp_repo", "examples_llm")
DB_PATH = os.path.join(PROJECT_ROOT, "data", "kis_api.db")
MAPPING_FILE = os.path.join(PROJECT_ROOT, "data", "column_mappings.json")

class APIParser(ast.NodeVisitor):
    def __init__(self, db_path=DB_PATH):
        self.db = DatabaseManager(db_path)
        self.api_url = None
        self.tr_id = None
        self.description = None
        self.params = []
        
    def visit_Assign(self, node):
        # API_URL = "..." 찾기
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "API_URL":
                if isinstance(node.value, ast.Constant):
                    self.api_url = node.value.value
                    
        # tr_id = "..." 찾기 (간소화: 함수 내부/외부 불문 첫 발견값 사용)
        # 실제 코드는 env_dv에 따라 분기하지만, 대부분 동일하거나 비슷함.
        # 여기서는 단순하게 문자열 리터럴 할당을 찾음.
        for target in node.targets:
             if isinstance(target, ast.Name) and target.id == "tr_id":
                 if isinstance(node.value, ast.Constant):
                    if not self.tr_id: # 첫 번째 발견만 사용
                        self.tr_id = node.value.value
        
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if not self.description:
            self.description = ast.get_docstring(node)
            if self.description:
                 self.parse_docstring_params(self.description)
        
        self.generic_visit(node)


    def parse_docstring_params(self, docstring):
        """Docstring에서 Args 섹션 파싱"""
        IGNORE_PARAMS = ["env_dv"]  # 무시할 파라미터 목록
        
        lines = docstring.split('\n')
        in_args = False
        
        for line in lines:
            line = line.strip()
            if line.startswith("Args:"):
                in_args = True
                continue
            
            if in_args:
                if line == "" or line.startswith("Returns:") or line.startswith("Raises:") or line.startswith("Example:"):
                    in_args = False
                    continue
                
                # 파라미터 라인 파싱 (예: param_name (type): [필수] 설명)
                if ":" in line:
                    try:
                        part1, part2 = line.split(":", 1)
                        # part1: param_name (type)
                        # part2: description
                        
                        param_part = part1.split("(")
                        param_name = param_part[0].strip()
                        
                        # 무시할 파라미터 체크
                        if param_name.lower() in IGNORE_PARAMS:
                            continue
                        
                        desc = part2.strip()

                        is_required = "[필수]" in desc
                        
                        self.params.append({
                            "name": param_name,
                            "description": desc,
                            "is_required": is_required
                        })
                    except:
                        pass

def load_data():
    if not os.path.exists(DB_PATH):
        logger.error(f"DB file not found: {DB_PATH}")
        return

    # Load column mappings
    output_tables = set()
    if os.path.exists(MAPPING_FILE):
        try:
            with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
                mappings = json.load(f)
                output_tables = set(mappings.keys())
            logger.info(f"Loaded {len(output_tables)} output table mappings.")
        except Exception as e:
            logger.error(f"Failed to load mapping file: {e}")

    db = DatabaseManager(DB_PATH)
    
    count = 0
    
    
    # Program aliases to match init_database.py and models
    ALIASES = {
        "inquire_price": "stock_price",
        "inquire_daily_price": "daily_price",
        # display_board_top matches, no alias needed
    }

    for root, dirs, files in os.walk(REPO_DIR):
        for file in files:
            if file.endswith(".py") and file != "kis_auth.py" and not file.startswith("chk_"):
                file_path = os.path.join(root, file)
                raw_program_name = os.path.splitext(file)[0]
                program_name = ALIASES.get(raw_program_name, raw_program_name)

                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        source = f.read()
                    
                    tree = ast.parse(source)
                    parser = APIParser()
                    parser.visit(tree)
                    
                    if parser.api_url and parser.tr_id:
                        logger.info(f"Loading {program_name}...")
                        
                        # Output table matching
                        output_table_name = program_name if program_name in output_tables else None

                        # API 정의 저장
                        desc = parser.description.split("\n")[0] if parser.description else program_name
                        db.add_api_definition(
                            program_name=program_name,
                            api_url=parser.api_url,
                            tr_id=parser.tr_id,
                            description=desc,
                            output_table_name=output_table_name
                        )
                        
                        # 파라미터 저장
                        for p in parser.params:
                            db.add_parameter_definition(
                                program_name=program_name,
                                param_name=p["name"],
                                is_required=p["is_required"],
                                description=p["description"]
                            )
                        
                        count += 1
                        
                except Exception as e:
                    logger.warning(f"Failed to parse {file}: {e}")

    logger.info(f"Loaded {count} APIs.")

if __name__ == "__main__":
    load_data()
