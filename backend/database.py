"""
Database session management module.

This module creates a SQLAlchemy engine and sessionmaker based on the
configured DATABASE_URL, and provides a generator function to obtain
a database session that is properly closed after use.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Yield a SQLAlchemy database session.

    This function provides a database session that is yielded to the caller.
    The session is closed automatically when the calling context is exited,
    ensuring proper resource management.

    Yields:
        Session: A SQLAlchemy session instance.
    """
    db_secondbrain = SessionLocal()
    try:
        yield db_secondbrain
    finally:
        db_secondbrain.close()
