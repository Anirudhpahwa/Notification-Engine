from models.notification import Notification
from services.channels.base import BaseChannel


class InAppChannel(BaseChannel):
    """In-app notification channel."""

    def send(self, notification: Notification) -> bool:
        """Send in-app notification (mark as delivered)."""
        print(f"[IN_APP] Delivered to user {notification.user_id}: {notification.message}")
        return True
