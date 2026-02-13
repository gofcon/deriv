"""
Extract COLUMN_MAPPING from temp_repo chk_*.py files
"""

import os
import ast
import json
from pathlib import Path

def extract_column_mapping_from_file(filepath):
    """Extract COLUMN_MAPPING dictionary from a Python file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'COLUMN_MAPPING':
                        if isinstance(node.value, ast.Dict):
                            mapping = {}
                            for key, value in zip(node.value.keys, node.value.values):
                                if isinstance(key, ast.Constant) and isinstance(value, ast.Constant):
                                    mapping[key.value] = value.value
                            return mapping
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
    
    return None


def main():
    """Extract COLUMN_MAPPING for 3 active APIs"""
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    repo_path = PROJECT_ROOT / "temp_repo" / "examples_llm"
    
    # Scan all chk_*.py files in the repo
    print(f"Scanning {repo_path} for chk_*.py files...")
    
    results = {}
    cnt = 0
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.startswith("chk_") and file.endswith(".py"):
                filepath = Path(root) / file
                
                # Derive program name from filename (remove chk_ prefix and .py extension)
                program_name = file[4:-3]
                
                # Check for aliases (optional, but good for consistency with known ones)
                # We can keep original names for new ones
                
                mapping = extract_column_mapping_from_file(filepath)
                if mapping:
                    results[program_name] = mapping
                    print(f"✓ {program_name}: {len(mapping)} columns")
                    cnt += 1
                else:
                    print(f"✗ {program_name}: No COLUMN_MAPPING found in {file}")
    
    # Save to JSON
    output_file = PROJECT_ROOT / "data" / "column_mappings.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n저장 완료: {output_file}")
    
    # Print summary
    print("\n=== Summary ===")
    for program_name, mapping in results.items():
        print(f"{program_name}: {len(mapping)} columns")


if __name__ == "__main__":
    main()
