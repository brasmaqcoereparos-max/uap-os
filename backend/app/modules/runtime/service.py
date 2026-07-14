from sqlalchemy.orm import Session

from app.models.runtime import Runtime
from app.repositories.runtime_repository import RuntimeRepository


class RuntimeService:

    @staticmethod
    def list(db: Session):
        return RuntimeRepository.list(db)

    @staticmethod
    def get(db: Session, runtime_id: str):
        return RuntimeRepository.get(db, runtime_id)

    @staticmethod
    def create(
        db: Session,
        name: str,
    ):
        runtime = Runtime(
            name=name,
        )

        return RuntimeRepository.create(db, runtime)

    @staticmethod
    def delete(
        db: Session,
        runtime_id: str,
    ):
        runtime = RuntimeRepository.get(db, runtime_id)

        if not runtime:
            return False

        RuntimeRepository.delete(db, runtime)

        return True
