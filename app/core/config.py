from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:Shawerma228@127.0.0.1:5432/fitmed"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Database = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
