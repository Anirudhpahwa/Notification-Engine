from core.celery_app import celery_app
from core.database import SessionLocal
from models.event import Event
from models.notification import Notification
from services.notification_service import create_notifications_from_event
from services.delivery_service import send_notification
from app.utils.rate_limiter import allow_request


@celery_app.task(
    name="process_event",
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 3, "countdown": 60},
    retry_backoff=True
)
def process_event(event_id: str):
    """Process event, create notifications, and deliver them."""
    db = SessionLocal()
    try:
        event = db.query(Event).filter(Event.id == event_id).first()
        if not event:
            return {"status": "error", "message": "Event not found"}
        
        notifications = create_notifications_from_event(db, event)
        
        for notification in notifications:
            if not allow_request(notification.user_id):
                notification.status = "rate_limited"
                db.commit()
                continue
            
            try:
                send_notification(db, notification)
            except Exception as e:
                notification.status = "failed"
                db.commit()
                raise
        
        return {"status": "success", "event_id": event_id, "notifications": len(notifications)}
    finally:
        db.close()


def schedule_notification(notification_id: str, scheduled_time):
    """Schedule a notification to be sent at a specific time."""
    return process_event.apply_async(
        args=[notification_id],
        eta=scheduled_time
    )
