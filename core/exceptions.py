class NotificationEngineException(Exception):
    """Base exception for notification engine."""
    pass


class EventNotFoundException(NotificationEngineException):
    """Raised when an event is not found."""
    pass


class NotificationNotFoundException(NotificationEngineException):
    """Raised when a notification is not found."""
    pass


class UserNotFoundException(NotificationEngineException):
    """Raised when a user is not found."""
    pass


class RateLimitExceededException(NotificationEngineException):
    """Raised when rate limit is exceeded."""
    pass


class DeliveryException(NotificationEngineException):
    """Raised when delivery fails."""
    pass


class ChannelNotSupportedException(NotificationEngineException):
    """Raised when channel is not supported."""
    pass