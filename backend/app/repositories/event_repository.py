from sqlalchemy.orm import Session

from app.models.event import Event


class EventRepository:

    @staticmethod
    def list(db: Session):
        return db.query(Event).all()

    @staticmethod
    def get(db: Session, event_id: str):
        return db.query(Event).filter(Event.id == event_id).first()

    @staticmethod
    def create(db: Session, event: Event):
        db.add(event)
        db.commit()
        db.refresh(event)
        return event

    @staticmethod
    def delete(db: Session, event: Event):
        db.delete(event)
        db.commit()
