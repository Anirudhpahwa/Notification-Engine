from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from models.base import BaseModel


class NotificationLog(BaseModel):
    """NotificationLog model for logging delivery attempts."""
    __tablename__ = "notification_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    notification_id = Column(UUID(as_uuid=True), ForeignKey("notifications.id"), nullable=False, index=True)
    status = Column(String(20), nullable=False)
    message = Column(Text, nullable=True)
    level = Column(String(20), nullable=False, default="info")
    attempt_number = Column(Integer, nullable=False, default=1)

    notification = relationship("Notification", back_populates="logs")