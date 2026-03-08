import re

with open('app/models.py', 'r', encoding='utf-8') as f:
    content = f.read()

# adding import if not present
if 'from sqlalchemy import Column, DateTime, func' not in content:
    content = content.replace('from sqlmodel import Field, SQLModel, Relationship', 
                              'from sqlmodel import Field, SQLModel, Relationship\nfrom sqlalchemy import Column, DateTime, func')

# Replace tablenames
content = re.sub(r'__tablename__\s*=\s*"([^"]+)"', r'__tablename__ = "kis_\1"', content)

# Remove double kis_kis_ just in case some were already prefixed
content = re.sub(r'__tablename__\s*=\s*"kis_kis_', r'__tablename__ = "kis_', content)

# Replace created_at
replacement = "updated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()))"
content = re.sub(r'created_at\s*:\s*datetime\s*=\s*Field\(default_factory=datetime\.utcnow\)', replacement, content)

with open('app/models.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
