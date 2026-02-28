"""
generate_models.py - Parse Oracle DDL to generate SQLModel classes.
"""

import os
import re

def parse_ddl_and_generate_models(sql_file_path, output_file_path):
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match CREATE TABLE statements, allowing optional schema prefix
    table_pattern = re.compile(
        r'CREATE TABLE (?:\"[^\"]+\"\.)?\"([^\"]+)\"\s*\(\s*(.*?)\s*\)\s*DEFAULT COLLATION', 
        re.DOTALL | re.IGNORECASE
    )
    
    tables = {}
    
    for table_match in table_pattern.finditer(content):
        table_name = table_match.group(1).lower()
        columns_text = table_match.group(2)
        
        class_name = ''.join(word.capitalize() for word in table_name.split('_'))
        
        # Parse lines
        lines = []
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
        fk_constraints = []
        parsed_columns = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check for PRIMARY KEY constraint
            pk_match = re.search(r'PRIMARY KEY\s*\((.*?)\)', line, re.IGNORECASE)
            if pk_match:
                pk_cols = [c.strip().replace('"', '').lower() for c in pk_match.group(1).split(',')]
                pk_columns.extend(pk_cols)
                continue
                
            # Check for FOREIGN KEY constraint
            fk_match = re.search(r'FOREIGN KEY\s*\(\"(.*?)\"\)\s*REFERENCES\s*(?:\"[^\"]+\"\.)?\"([^\"]+)\"\s*\(\"(.*?)\"\)', line, re.IGNORECASE)
            if fk_match:
                col_name = fk_match.group(1).lower()
                ref_table = fk_match.group(2).lower()
                ref_col = fk_match.group(3).lower()
                fk_constraints.append({
                    "col_name": col_name,
                    "ref_table": ref_table,
                    "ref_col": ref_col
                })
                continue
                
            # Parse column definition
            col_match = re.match(r'^"([^"]+)"\s+(.+)', line)
            if col_match:
                col_name = col_match.group(1)
                col_def = col_match.group(2).upper()
                
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
                elif "JSON" in col_def:
                    py_type = "dict"
                
                is_nullable = "NOT NULL" not in col_def
                parsed_columns.append({
                    "name": col_name.lower(),
                    "type": py_type,
                    "nullable": is_nullable
                })
                
        tables[table_name] = {
            "class_name": class_name,
            "columns": parsed_columns,
            "pk_columns": pk_columns,
            "fk_constraints": fk_constraints,
            "relationships": [] # will store relationships to generate
        }
        
    # Build bi-directional relationships
    for table_name, table_data in tables.items():
        for fk in table_data["fk_constraints"]:
            parent_table = fk["ref_table"]
            if parent_table in tables:
                parent_data = tables[parent_table]
                parent_class = parent_data["class_name"]
                child_class = table_data["class_name"]
                
                # Naming for properties
                parent_prop = parent_table
                child_prop_plural = table_name + "s"
                
                # Add to child
                table_data["relationships"].append({
                    "prop_name": parent_prop,
                    "type_hint": f'Optional["{parent_class}"]',
                    "back_populates": child_prop_plural
                })
                
                # Add to parent
                parent_data["relationships"].append({
                    "prop_name": child_prop_plural,
                    "type_hint": f'list["{child_class}"]',
                    "back_populates": parent_prop
                })

    # Generate models_code
    models_code = '"""\nAuto-generated SQLModel classes from Oracle DDL.\n"""\n\n'
    models_code += 'from typing import Optional, List, Dict, Any\n'
    models_code += 'from datetime import datetime\n'
    models_code += 'from sqlmodel import Field, SQLModel, Relationship\n'
    models_code += 'from sqlalchemy import Column, JSON, DateTime, func\n\n'
    models_code += 'import app.oracle_mapping  # noqa: F401\n\n'
    
    for table_name, table_data in tables.items():
        class_name = table_data["class_name"]
        models_code += f'class {class_name}(SQLModel, table=True):\n'
        models_code += f'    __tablename__ = "{table_name}"\n\n'
        
        for col in table_data["columns"]:
            col_name = col['name']
            py_type = col['type']
            
            field_args = []
            
            # FK
            fk_ref = None
            for fk in table_data["fk_constraints"]:
                if fk["col_name"] == col_name:
                    fk_ref = f"{fk['ref_table']}.{fk['ref_col']}"
                    break
            
            if fk_ref:
                field_args.append(f'foreign_key="{fk_ref}"')
                
            # PK
            if col_name in table_data["pk_columns"]:
                field_args.append("primary_key=True")
                
            if col_name == "updated_at" and py_type == "datetime":
                type_hint = f"Optional[{py_type}]"
                field_args.append("default=None")
                field_args.append("sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now())")
            elif col_name == "description":
                type_hint = f"Optional[{py_type}]"
                field_args.append("default=None")
                field_args.append("max_length=100")
            elif field_args:
                type_hint = py_type
            else:
                if col['nullable'] and py_type != "dict":
                    type_hint = f"Optional[{py_type}]"
                    field_args.append("default=None")
                else:
                    type_hint = py_type
                    
            if py_type == "dict":
                field_args.append("sa_column=Column(JSON)")
                    
            field_str = f"Field({', '.join(field_args)})" if field_args else ""
            if field_str:
                models_code += f'    {col_name}: {type_hint} = {field_str}\n'
            else:
                models_code += f'    {col_name}: {type_hint}\n'
                
        # Relationships
        if table_data["relationships"]:
            models_code += '\n'
            for rel in table_data["relationships"]:
                models_code += f'    {rel["prop_name"]}: {rel["type_hint"]} = Relationship(back_populates="{rel["back_populates"]}")\n'
                
        models_code += '\n\n'

    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(models_code)
    
    print(f"Generated ORM models at {output_file_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sql_file_path = os.path.join(base_dir, "data", "script_gof.sql")
    output_file_path = os.path.join(base_dir, "app", "models_gof.py")
    parse_ddl_and_generate_models(sql_file_path, output_file_path)
