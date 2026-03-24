from sqlalchemy import Column, String, JSON, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from models.base import BaseModel


class Event(BaseModel):
    """Event model."""
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_type = Column(String(100), nullable=False, index=True)
    payload = Column(JSON, nullable=True)
    status = Column(String(20), default="pending", nullable=False)

    notifications = relationship("Notification", back_populates="event")