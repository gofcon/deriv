import re

def update_models():
    with open('app/models_gofcon.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to target Fields inside DomFutureMst, OverFutureMst, DomStockFutureMst, OverStockMst, etc.
    # A safe bet is to just replace:
    # Optional[str] = Field(default=None, description="...")
    # with
    # Optional[str] = Field(default=None, max_length=100, description="...")
    # where max_length is not already present.

    # Find Field(default=None, description="...")
    # and we want to inject max_length=100
    
    pattern = re.compile(r'(Field\([^)]*default=None,\s*description="[^"]*"\))')
    
    def replacer(match):
        field_str = match.group(1)
        if 'max_length' not in field_str:
            return field_str.replace('default=None,', 'default=None, max_length=100,')
        return field_str
    
    new_content = pattern.sub(replacer, content)
    
    with open('app/models_gofcon.py', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update_models()
    print("Models updated.")
