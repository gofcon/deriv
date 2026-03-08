import sys
import os
sys.path.append(os.getcwd())
import logging

from sqlalchemy import text
from app.database import DatabaseManager
from app.models_gofcon import SQLModel

logging.basicConfig(level=logging.INFO)

db = DatabaseManager()
engine = db.engine

with engine.begin() as conn:
    try:
        conn.execute(text("DROP TABLE api_job_mst CASCADE CONSTRAINTS"))
        logging.info("Dropped api_job_mst")
    except Exception as e:
        print(e)
        
    try:
        conn.execute(text("DROP TABLE browser_job_mst CASCADE CONSTRAINTS"))
        logging.info("Dropped browser_job_mst")
    except Exception as e:
        print(e)

logging.info("Creating all tables in models_gofcon...")
SQLModel.metadata.create_all(engine)
logging.info("Tables created successfully.")
