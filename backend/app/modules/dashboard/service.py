from sqlalchemy.orm import Session

from app.models.dashboard import Dashboard
from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def list(db: Session):
        return DashboardRepository.list(db)

    @staticmethod
    def get(db: Session, dashboard_id: str):
        return DashboardRepository.get(db, dashboard_id)

    @staticmethod
    def create(
        db: Session,
        name: str,
        description: str,
    ):
        dashboard = Dashboard(
            name=name,
            description=description,
        )

        return DashboardRepository.create(db, dashboard)

    @staticmethod
    def delete(
        db: Session,
        dashboard_id: str,
    ):
        dashboard = DashboardRepository.get(db, dashboard_id)

        if not dashboard:
            return False

        DashboardRepository.delete(db, dashboard)

        return True
