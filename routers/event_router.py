from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from schemas.event import EventCreate, EventResponse
from services.event_service import create_event

router = APIRouter(prefix="/events", tags=["events"])


@router.post("", response_model=EventResponse, status_code=201)
def post_event(event_data: EventCreate, db: Session = Depends(get_db)):
    """Create a new event."""
    return create_event(db, event_data)
