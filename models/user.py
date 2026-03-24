from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import uuid
from models.base import BaseModel


class User(BaseModel):
    """User model."""
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(50), nullable=True)

    notifications = relationship("Notification", back_populates="user")