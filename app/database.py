from app.app_settings import get_settings
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL


settings = get_settings()

username = settings.ORACLE_DB_USER
password = settings.ORACLE_DB_PASSWORD
dsn = settings.ORACLE_DB_DSN

connection_url =URL.create("oracle+oracledb",
                           username=username,
                           password=password,
                           query={"dsn": dsn})

engine = create_engine(connection_url,pool_pre_ping=True)
metadata = MetaData()

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()