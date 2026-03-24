from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from models.base import BaseModel


class Notification(BaseModel):
    """Notification model."""
    __tablename__ = "notifications"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), nullable=False, index=True)
    event_id = Column(String(36), ForeignKey("events.id"), nullable=True, index=True)
    channel = Column(String(20), nullable=False)
    message = Column(Text, nullable=False)
    status = Column(String(20), default="pending", nullable=False, index=True)
    scheduled_at = Column(DateTime(timezone=True), nullable=True, index=True)
    retry_count = Column(Integer, default=0, nullable=False)

    event = relationship("Event", back_populates="notifications")
    logs = relationship("NotificationLog", back_populates="notification")