from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.dashboard import DashboardCreate
from app.modules.dashboard.service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/")
def list_dashboards(db: Session = Depends(get_db)):
    return DashboardService.list(db)


@router.get("/{dashboard_id}")
def get_dashboard(dashboard_id: str, db: Session = Depends(get_db)):
    dashboard = DashboardService.get(db, dashboard_id)

    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")

    return dashboard


@router.post("/")
def create_dashboard(
    dashboard: DashboardCreate,
    db: Session = Depends(get_db),
):
    return DashboardService.create(
        db=db,
        name=dashboard.name,
        description=dashboard.description,
    )


@router.delete("/{dashboard_id}")
def delete_dashboard(
    dashboard_id: str,
    db: Session = Depends(get_db),
):
    deleted = DashboardService.delete(db, dashboard_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Dashboard not found")

    return {"message": "Dashboard deleted successfully"}
