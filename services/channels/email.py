from models.notification import Notification
from services.channels.base import BaseChannel


class EmailChannel(BaseChannel):
    """Email notification channel (mock implementation)."""

    def send(self, notification: Notification) -> bool:
        """Send email notification (mock)."""
        print(f"[EMAIL] Sending to user {notification.user_id}: {notification.message}")
        return True
