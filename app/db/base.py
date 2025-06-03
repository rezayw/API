# app/db/base.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import config

Base = declarative_base()  # ← INI yang error kamu

engine = create_engine(
    config.DATABASE_URL,
    connect_args={"check_same_thread": False}  # Hanya untuk SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
