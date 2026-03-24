import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
rate_limit = int(os.getenv("RATE_LIMIT_PER_USER", "10"))
rate_window = int(os.getenv("RATE_LIMIT_WINDOW_SECONDS", "60"))


def get_redis_client():
    """Get Redis client."""
    try:
        return redis.from_url(redis_url, decode_responses=True)
    except Exception:
        return None


def allow_request(user_id: str) -> bool:
    """Check if user is allowed to send notification."""
    client = get_redis_client()
    if not client:
        return True

    key = f"rate_limit:{user_id}"
    
    try:
        current = client.get(key)
        if current is None:
            client.setex(key, rate_window, 1)
            return True
        
        if int(current) >= rate_limit:
            return False
        
        client.incr(key)
        return True
    except Exception:
        return True


def get_remaining_quota(user_id: str) -> int:
    """Get remaining notifications user can send."""
    client = get_redis_client()
    if not client:
        return rate_limit
    
    key = f"rate_limit:{user_id}"
    
    try:
        current = client.get(key)
        if current is None:
            return rate_limit
        return max(0, rate_limit - int(current))
    except Exception:
        return rate_limit
