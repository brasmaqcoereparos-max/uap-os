from sqlalchemy.orm import Session

from app.models.automation import Automation
from app.repositories.automation_repository import AutomationRepository


class AutomationService:

    @staticmethod
    def list(db: Session):
        return AutomationRepository.list(db)

    @staticmethod
    def get(db: Session, automation_id: str):
        return AutomationRepository.get(db, automation_id)

    @staticmethod
    def create(
        db: Session,
        name: str,
        description: str,
    ):
        automation = Automation(
            name=name,
            description=description,
        )

        return AutomationRepository.create(db, automation)

    @staticmethod
    def delete(
        db: Session,
        automation_id: str,
    ):
        automation = AutomationRepository.get(db, automation_id)

        if not automation:
            return False

        AutomationRepository.delete(db, automation)

        return True
