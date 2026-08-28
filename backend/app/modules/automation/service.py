from sqlalchemy.orm import Session

from app.models.automatico import (
    Automation,
)

from app.repositories.automation_repository import (
    AutomationRepository,
)


class AutomationService:
    @staticmethod
    def list(db: Session):
        return AutomationRepository.list(
            db
        )

    @staticmethod
    def get(
        db: Session,
        automation_id: str,
    ):
        if not automation_id:
            return None

        return AutomationRepository.get(
            db,
            str(automation_id),
        )

    @staticmethod
    def create(
        db: Session,
        name: str,
        description: str = "",
    ):
        name = str(name).strip()

        if not name:
            raise ValueError(
                "Nome da automação "
                "é obrigatório."
            )

        automation = Automation(
            name=name,
            description=str(
                description or ""
            ),
        )

        return (
            AutomationRepository.create(
                db,
                automation,
            )
        )

    @staticmethod
    def update(
        db: Session,
        automation_id: str,
        name=None,
        description=None,
    ):
        automation = (
            AutomationRepository.get(
                db,
                str(automation_id),
            )
        )

        if automation is None:
            return None

        if name is not None:
            value = str(name).strip()

            if not value:
                raise ValueError(
                    "Nome da automação "
                    "não pode ficar vazio."
                )

            automation.name = value

        if description is not None:
            automation.description = str(
                description
            )

        update_method = getattr(
            AutomationRepository,
            "update",
            None,
        )

        if callable(update_method):
            return update_method(
                db,
                automation,
            )

        db.add(automation)
        db.commit()
        db.refresh(automation)

        return automation

    @staticmethod
    def delete(
        db: Session,
        automation_id: str,
    ):
        automation = (
            AutomationRepository.get(
                db,
                str(automation_id),
            )
        )

        if automation is None:
            return False

        AutomationRepository.delete(
            db,
            automation,
        )

        return True
