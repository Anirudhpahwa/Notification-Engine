from models.notification import Notification
from services.channels.base import BaseChannel


class SMSChannel(BaseChannel):
    """SMS notification channel (placeholder)."""

    def send(self, notification: Notification) -> bool:
        """Send SMS notification (placeholder)."""
        print(f"[SMS] Sending to user {notification.user_id}: {notification.message}")
        return True
