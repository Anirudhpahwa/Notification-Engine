from sqlalchemy.orm import Session
from models.event import Event
from schemas.event import EventCreate
from services.notification_service import create_notifications_from_event


def create_event(db: Session, event_data: EventCreate) -> Event:
    """Create a new event in the database."""
    event = Event(
        event_type=event_data.event_type,
        payload=event_data.payload,
        status="pending"
    )
    db.add(event)
    db.commit()
    db.refresh(event)

    create_notifications_from_event(db, event)

    return event
