from sqlalchemy.orm import Session

from app.models.flow import Flow
from app.repositories.flow_repository import FlowRepository


class FlowService:

    @staticmethod
    def list(db: Session):
        return FlowRepository.list(db)

    @staticmethod
    def get(db: Session, flow_id: str):
        return FlowRepository.get(db, flow_id)

    @staticmethod
    def create(
        db: Session,
        name: str,
        description: str,
    ):
        flow = Flow(
            name=name,
            description=description,
        )

        return FlowRepository.create(db, flow)

    @staticmethod
    def delete(
        db: Session,
        flow_id: str,
    ):
        flow = FlowRepository.get(db, flow_id)

        if not flow:
            return False

        FlowRepository.delete(db, flow)

        return True
