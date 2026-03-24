from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from core.database import Base


class BaseModel(Base):
    """Base model with timestamp columns."""
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)