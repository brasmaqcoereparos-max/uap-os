from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.event import EventCreate
from app.modules.events.service import EventService

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)


@router.get("/")
def list_events(db: Session = Depends(get_db)):
    return EventService.list(db)


@router.get("/{event_id}")
def get_event(event_id: str, db: Session = Depends(get_db)):
    event = EventService.get(db, event_id)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return event


@router.post("/")
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db),
):
    return EventService.create(
        db=db,
        name=event.name,
        category=event.category,
        description=event.description,
    )


@router.delete("/{event_id}")
def delete_event(
    event_id: str,
    db: Session = Depends(get_db),
):
    deleted = EventService.delete(db, event_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Event not found")

    return {"message": "Event deleted successfully"}
