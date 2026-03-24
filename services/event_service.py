from sqlalchemy.orm import Session
from datetime import datetime
from models.event import Event
from schemas.event import EventCreate
from services.notification_service import create_notifications_from_event
from services.delivery_service import send_notification
from app.utils.rate_limiter import allow_request


def create_event(db: Session, event_data: EventCreate) -> Event:
    """Create a new event in the database."""
    scheduled_at = None
    if event_data.payload and event_data.payload.get("scheduled_at"):
        scheduled_at = datetime.fromisoformat(event_data.payload["scheduled_at"])

    event = Event(
        event_type=event_data.event_type,
        payload=event_data.payload,
        status="pending"
    )
    db.add(event)
    db.commit()
    db.refresh(event)

    notifications = create_notifications_from_event(db, event)
    
    for notification in notifications:
        notification.scheduled_at = scheduled_at
        db.commit()
        
        if scheduled_at and scheduled_at > datetime.utcnow():
            notification.status = "scheduled"
            db.commit()
            continue
        
        if not allow_request(notification.user_id):
            notification.status = "rate_limited"
            db.commit()
            continue
        
        send_notification(db, notification)

    return event
