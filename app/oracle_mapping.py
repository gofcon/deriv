from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import String, VARCHAR, Boolean, DateTime, JSON, Integer, Float, Numeric

@compiles(String, 'oracle')
@compiles(VARCHAR, 'oracle')
def compile_varchar_oracle(element, compiler, **kw):
    """
    Oracle requires VARCHAR2 length. SQLModel's default str maps to lengthless VARCHAR.
    This override enforces a default length of 20 for Oracle connections.
    """
    if getattr(element, 'length', None) is None:
        return "VARCHAR2(20)"
    else:
        return compiler.visit_VARCHAR(element, **kw)

@compiles(JSON, 'oracle')
def compile_json_oracle(element, compiler, **kw):
    """
    Oracle 21c supports native JSON, but SQLAlchemy's generic JSON type 
    might not know how to render it in this dialect version.
    """
    return "JSON"

@compiles(Boolean, 'oracle')
def compile_boolean_oracle(element, compiler, **kw):
    """
    Oracle 23ai native mapping for Python bool instead of NUMBER(38,0)
    """
    return "BOOLEAN"

@compiles(DateTime, 'oracle')
def compile_datetime_oracle(element, compiler, **kw):
    """
    Map Python datetime to TIMESTAMP(0) WITH TIME ZONE instead of DATE
    """
    return "TIMESTAMP(0) WITH TIME ZONE"

@compiles(Integer, 'oracle')
def compile_integer_oracle(element, compiler, **kw):
    """
    Map Python int to NUMBER(10)
    """
    return "NUMBER(10)"

@compiles(Float, 'oracle')
def compile_float_oracle(element, compiler, **kw):
    """
    Map Python float to NUMBER(10, 4)
    """
    return "NUMBER(10, 4)"

@compiles(Numeric, 'oracle')
def compile_numeric_oracle(element, compiler, **kw):
    """
    Map Python Decimal to NUMBER(18, 4)
    """
    return "NUMBER(18, 4)"
