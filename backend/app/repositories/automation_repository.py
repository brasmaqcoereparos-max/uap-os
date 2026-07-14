from sqlalchemy.orm import Session

from app.models.automation import Automation


class AutomationRepository:

    @staticmethod
    def list(db: Session):
        return db.query(Automation).all()

    @staticmethod
    def get(db: Session, automation_id: str):
        return db.query(Automation).filter(
            Automation.id == automation_id
        ).first()

    @staticmethod
    def create(db: Session, automation: Automation):
        db.add(automation)
        db.commit()
        db.refresh(automation)
        return automation

    @staticmethod
    def delete(db: Session, automation: Automation):
        db.delete(automation)
        db.commit()
