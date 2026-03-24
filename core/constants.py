from enum import Enum


class EventStatus(str, Enum):
    PENDING = "pending"
    PROCESSED = "processed"
    FAILED = "failed"


class NotificationStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"
    SCHEDULED = "scheduled"


class Channel(str, Enum):
    EMAIL = "email"
    IN_APP = "in_app"
    SMS = "sms"


class LogLevel(str, Enum):
    INFO = "info"
    ERROR = "error"
    WARNING = "warning"
    DEBUG = "debug"


class DeliveryStatus(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    RETRY = "retry"