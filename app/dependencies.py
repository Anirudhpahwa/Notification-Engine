from sqlalchemy.orm import Session
from core.database import SessionLocal


def get_db() -> Session:
    """Database dependency for FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()