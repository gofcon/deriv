from sqlmodel import SQLModel, create_engine, Session, select
from app.models import MetaTableMst, MetaColumnMst
from app.config import DB_PATH

engine = create_engine(f"sqlite:///{DB_PATH}")

def check_metadata():
    with Session(engine) as session:
        # Check Tables
        tables = session.exec(select(MetaTableMst)).all()
        print(f"\n[MetaTableMst] Count: {len(tables)}")
        for t in tables:
            print(f" - {t.table_name}: {t.description}")
            
        # Check Columns (Sample)
        columns = session.exec(select(MetaColumnMst).limit(10)).all()
        print(f"\n[MetaColumnMst] Sample (Total: {session.query(MetaColumnMst).count()}):")
        for c in columns:
            print(f" - {c.table_name}.{c.column_name}: {c.description}")

if __name__ == "__main__":
    check_metadata()
