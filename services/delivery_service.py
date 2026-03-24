from sqlalchemy.orm import Session
from models.notification import Notification
from services.channels.email import EmailChannel
from services.channels.in_app import InAppChannel
from services.channels.sms import SMSChannel


def send_notification(db: Session, notification: Notification) -> bool:
    """Send notification through appropriate channel."""
    channel_map = {
        "email": EmailChannel(),
        "in_app": InAppChannel(),
        "sms": SMSChannel(),
    }

    channel = channel_map.get(notification.channel)
    if not channel:
        notification.status = "failed"
        db.commit()
        return False

    try:
        success = channel.send(notification)
        if success:
            notification.status = "sent"
            db.commit()
            return True
        else:
            notification.status = "failed"
            db.commit()
            return False
    except Exception as e:
        notification.status = "failed"
        db.commit()
        return False
