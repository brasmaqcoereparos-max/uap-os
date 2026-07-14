from sqlalchemy.orm import Session

from app.models.flow import Flow


class FlowRepository:

    @staticmethod
    def list(db: Session):
        return db.query(Flow).all()

    @staticmethod
    def get(db: Session, flow_id: str):
        return db.query(Flow).filter(Flow.id == flow_id).first()

    @staticmethod
    def create(db: Session, flow: Flow):
        db.add(flow)
        db.commit()
        db.refresh(flow)
        return flow

    @staticmethod
    def delete(db: Session, flow: Flow):
        db.delete(flow)
        db.commit()
