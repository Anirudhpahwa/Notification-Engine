from core.celery_app import celery_app
from core.database import SessionLocal
from models.event import Event
from services.notification_service import create_notifications_from_event


@celery_app.task(name="process_event")
def process_event(event_id: str):
    """Process event and create notifications."""
    db = SessionLocal()
    try:
        event = db.query(Event).filter(Event.id == event_id).first()
        if not event:
            return {"status": "error", "message": "Event not found"}
        
        create_notifications_from_event(db, event)
        return {"status": "success", "event_id": event_id}
    finally:
        db.close()
