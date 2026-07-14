from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.automation import AutomationCreate
from app.modules.automation.service import AutomationService

router = APIRouter(
    prefix="/automation",
    tags=["Automation"],
)


@router.get("/")
def list_automation(db: Session = Depends(get_db)):
    return AutomationService.list(db)


@router.get("/{automation_id}")
def get_automation(automation_id: str, db: Session = Depends(get_db)):
    automation = AutomationService.get(db, automation_id)

    if not automation:
        raise HTTPException(status_code=404, detail="Automation not found")

    return automation


@router.post("/")
def create_automation(
    automation: AutomationCreate,
    db: Session = Depends(get_db),
):
    return AutomationService.create(
        db=db,
        name=automation.name,
        description=automation.description,
    )


@router.delete("/{automation_id}")
def delete_automation(
    automation_id: str,
    db: Session = Depends(get_db),
):
    deleted = AutomationService.delete(db, automation_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Automation not found")

    return {"message": "Automation deleted successfully"}
