from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")


class HealthCheckResponse(BaseModel):
    """Health check response schema."""
    status: str
    service: str


class ErrorResponse(BaseModel):
    """Error response schema."""
    detail: str


class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response schema."""
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int