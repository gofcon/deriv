"""
generate_models.py - Parse Oracle DDL to generate SQLModel classes.
"""

import os
import re

def parse_ddl_and_generate_models(sql_file_path, output_file_path):
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match CREATE TABLE statements
    table_pattern = re.compile(
        r'CREATE TABLE "[^"]+"."([^"]+)"\s*\(\s*(.*?)\s*\)\s*DEFAULT COLLATION', 
        re.DOTALL | re.IGNORECASE
    )
    
    # Process each table
    models_code = '"""\nAuto-generated SQLModel classes from Oracle DDL.\n"""\n\n'
    models_code += 'from typing import Optional\n'
    models_code += 'from datetime import datetime\n'
    models_code += 'from sqlmodel import Field, SQLModel\n\n'
    
    for table_match in table_pattern.finditer(content):
        table_name = table_match.group(1)
        columns_text = table_match.group(2)
        
        # Convert table name to CamelCase class name
        class_name = ''.join(word.capitalize() for word in table_name.lower().split('_'))
        
        models_code += f'class {class_name}(SQLModel, table=True):\n'
        models_code += f'    __tablename__ = "{table_name.lower()}"\n\n'
        
        # Parse columns and constraints
        lines = []
        # split by comma, but be careful with functions/precisions like NUMBER(20,2) or TIMESTAMP(6)
        # However, Oracle DDL from DBMS_METADATA usually puts PRIMARY KEY on a separate line at the end
        # Or inline. Let's do a simple split by comma considering parenthesis depth.
        current_line = ""
        paren_depth = 0
        for char in columns_text:
            if char == '(':
                paren_depth += 1
            elif char == ')':
                paren_depth -= 1
            
            if char == ',' and paren_depth == 0:
                lines.append(current_line.strip())
                current_line = ""
            else:
                current_line += char
        if current_line.strip():
            lines.append(current_line.strip())
            
        pk_columns = []
        parsed_columns = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check for PRIMARY KEY constraint
            pk_match = re.search(r'PRIMARY KEY\s*\((.*?)\)', line, re.IGNORECASE)
            if pk_match:
                pk_cols = [c.strip().replace('"', '') for c in pk_match.group(1).split(',')]
                pk_columns.extend(pk_cols)
                continue
                
            # Parse column definition
            col_match = re.match(r'^"([^"]+)"\s+(.+)', line)
            if col_match:
                col_name = col_match.group(1)
                col_def = col_match.group(2).upper()
                
                # Determine Python type
                py_type = "str"
                if "NUMBER" in col_def:
                    if "NUMBER(*,0)" in col_def or "NUMBER(38)" in col_def or "INTEGER" in col_def:
                        py_type = "int"
                    elif "," in col_def:
                        py_type = "float"
                    else:
                        py_type = "float" # Safe fallback
                elif "DATE" in col_def or "TIMESTAMP" in col_def:
                    py_type = "datetime"
                elif "CLOB" in col_def:
                    py_type = "str"
                
                is_nullable = "NOT NULL" not in col_def
                parsed_columns.append({
                    "name": col_name,
                    "type": py_type,
                    "nullable": is_nullable
                })
        
        # Generate properties
        for col in parsed_columns:
            col_name_lower = col['name'].lower()
            py_type = col['type']
            
            field_args = []
            
            # Primary Key
            if col['name'] in pk_columns:
                field_args.append("primary_key=True")
            
            # Nullability
            if field_args: # usually PK implies not null in sqlmodel logic
                type_hint = py_type
            else:
                if col['nullable']:
                    type_hint = f"Optional[{py_type}]"
                    field_args.append("default=None")
                else:
                    type_hint = py_type
            
            field_str = f"Field({', '.join(field_args)})" if field_args else ""
            if field_str:
                models_code += f'    {col_name_lower}: {type_hint} = {field_str}\n'
            else:
                models_code += f'    {col_name_lower}: {type_hint}\n'
                
        models_code += '\n\n'

    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(models_code)
    
    print(f"Generated ORM models at {output_file_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sql_file_path = os.path.join(base_dir, "data", "script_gof.sql")
    output_file_path = os.path.join(base_dir, "app", "models_gof.py")
    parse_ddl_and_generate_models(sql_file_path, output_file_path)
