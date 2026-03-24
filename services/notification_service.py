from typing import List
from sqlalchemy.orm import Session
from models.notification import Notification
from models.event import Event


def create_notifications_from_event(db: Session, event: Event) -> List[Notification]:
    """Create notifications from an event."""
    if not event.payload:
        return []

    user_id = event.payload.get("user_id")
    message = event.payload.get("message", "New notification")
    channel = event.payload.get("channel", "in_app")

    if not user_id:
        return []

    notification = Notification(
        user_id=user_id,
        event_id=event.id,
        channel=channel,
        message=message,
        status="pending",
        retry_count=0
    )
    db.add(notification)
    db.commit()
    db.refresh(notification)

    return [notification]
