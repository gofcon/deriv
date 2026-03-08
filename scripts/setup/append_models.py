"""
Append output models to models.py
"""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
generated_file = Path(__file__).parent / 'generated_output_models.py'
models_file = PROJECT_ROOT / 'app' / 'models.py'

# Read generated output models
with open(generated_file, 'r', encoding='utf-8') as f:
    output_models = f.read()

# Extract only the class definitions (skip imports and header comments)
lines = output_models.split('\n')
start_idx = 0
for i, line in enumerate(lines):
    if line.startswith('class '):
        start_idx = i
        break

class_definitions = '\n'.join(lines[start_idx:])

# Append to models.py
with open(models_file, 'a', encoding='utf-8') as f:
    f.write('\n\n# ===== Output Table Models =====\n')
    f.write('# Auto-generated from COLUMN_MAPPING in temp_repo\n\n')
    f.write(class_definitions)

print("✓ Output models appended to models.py")
