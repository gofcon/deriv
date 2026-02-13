"""
Generate SQLModel output table classes from COLUMN_MAPPING
"""

import json
from pathlib import Path


def to_pascal_case(snake_str):
    """Convert snake_case to PascalCase"""
    return ''.join(word.capitalize() for word in snake_str.split('_'))


def generate_output_model(program_name, column_mapping):
    """Generate SQLModel class code for an output table"""
    class_name = to_pascal_case(program_name)
    table_name = program_name
    
    # Generate class header
    code = f'''
class {class_name}(SQLModel, table=True):
    """Output table for {program_name}"""
    __tablename__ = "{table_name}"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    program_name: str = Field(index=True)
    
'''
    
    # Generate column definitions
    for col_name, description in column_mapping.items():
        code += f"    {col_name}: Optional[str] = None  # {description}\n"
    
    # Add timestamp
    code += '''    
    created_at: datetime = Field(default_factory=datetime.utcnow)
'''
    
    return code


def main():
    """Generate all output models"""
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    input_file = PROJECT_ROOT / "data" / "column_mappings.json"
    
    # Load column mappings
    with open(input_file, 'r', encoding='utf-8') as f:
        mappings = json.load(f)
    
    print("Generating output model classes...\n")
    print("=" * 80)
    
    all_code = []
    
    for program_name, column_mapping in mappings.items():
        code = generate_output_model(program_name, column_mapping)
        all_code.append(code)
        print(f"✓ Generated {to_pascal_case(program_name)} ({len(column_mapping)} columns)")
    
    # Write to file
    output_file = "generated_output_models.py"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Auto-generated output table models\n")
        f.write("# Generated from column_mappings.json\n\n")
        f.write("from datetime import datetime\n")
        f.write("from typing import Optional\n")
        f.write("from sqlmodel import Field, SQLModel\n\n")
        
        for code in all_code:
            f.write(code)
            f.write("\n")
    
    print(f"\n저장 완료: {output_file}")
    print("\n다음 단계: generated_output_models.py 내용을 models.py에 복사하세요.")


if __name__ == "__main__":
    main()
