from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class NotificationCreate(BaseModel):
    """Schema for creating a notification."""
    user_id: str
    event_id: Optional[str] = None
    channel: str
    message: str
    scheduled_at: Optional[datetime] = None


class NotificationResponse(BaseModel):
    """Schema for notification response."""
    model_config = ConfigDict(from_attributes=True)

    id: str
    user_id: str
    event_id: Optional[str] = None
    channel: str
    message: str
    status: str
    scheduled_at: Optional[datetime] = None
    retry_count: int
    created_at: datetime