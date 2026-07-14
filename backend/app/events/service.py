from sqlalchemy.orm import Session

from app.models.event import Event
from app.repositories.event_repository import EventRepository


class EventService:

    @staticmethod
    def list(db: Session):
        return EventRepository.list(db)

    @staticmethod
    def get(db: Session, event_id: str):
        return EventRepository.get(db, event_id)

    @staticmethod
    def create(
        db: Session,
        name: str,
        category: str,
        description: str,
    ):
        event = Event(
            name=name,
            category=category,
            description=description,
        )

        return EventRepository.create(db, event)

    @staticmethod
    def delete(
        db: Session,
        event_id: str,
    ):
        event = EventRepository.get(db, event_id)

        if not event:
            return False

        EventRepository.delete(db, event)

        return True
