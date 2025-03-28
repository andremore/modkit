from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.engine import Engine
from typing import Generator

Base = declarative_base()
engine: Engine = None
SessionLocal: sessionmaker = None

def init_db(external_engine: Engine):
    global engine, SessionLocal
    engine = external_engine
    SessionLocal = sessionmaker(bind=engine)

def get_db() -> Generator[Session, None, None]:
    if SessionLocal is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
