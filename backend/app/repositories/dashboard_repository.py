from sqlalchemy.orm import Session

from app.models.dashboard import Dashboard


class DashboardRepository:

    @staticmethod
    def list(db: Session):
        return db.query(Dashboard).all()

    @staticmethod
    def get(db: Session, dashboard_id: str):
        return db.query(Dashboard).filter(
            Dashboard.id == dashboard_id
        ).first()

    @staticmethod
    def create(db: Session, dashboard: Dashboard):
        db.add(dashboard)
        db.commit()
        db.refresh(dashboard)
        return dashboard

    @staticmethod
    def delete(db: Session, dashboard: Dashboard):
        db.delete(dashboard)
        db.commit()
