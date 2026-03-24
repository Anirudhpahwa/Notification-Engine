from abc import ABC, abstractmethod
from models.notification import Notification


class BaseChannel(ABC):
    """Base class for notification channels."""

    @abstractmethod
    def send(self, notification: Notification) -> bool:
        """Send notification through this channel."""
        pass
