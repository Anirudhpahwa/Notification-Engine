from pydantic import BaseModel, ConfigDict
from typing import Optional, Any, Dict
from datetime import datetime


class EventCreate(BaseModel):
    """Schema for creating an event."""
    event_type: str
    payload: Optional[Dict[str, Any]] = None


class EventResponse(BaseModel):
    """Schema for event response."""
    model_config = ConfigDict(from_attributes=True)

    id: str
    event_type: str
    payload: Optional[Dict[str, Any]] = None
    status: str
    created_at: datetime