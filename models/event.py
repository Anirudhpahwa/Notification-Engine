from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import relationship
import uuid
from models.base import BaseModel


class Event(BaseModel):
    """Event model."""
    __tablename__ = "events"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    event_type = Column(String(100), nullable=False, index=True)
    payload = Column(JSON, nullable=True)
    status = Column(String(20), default="pending", nullable=False)

    notifications = relationship("Notification", back_populates="event")