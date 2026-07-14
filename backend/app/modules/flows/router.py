from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.flow import FlowCreate
from app.modules.flows.service import FlowService

router = APIRouter(
    prefix="/flows",
    tags=["Flows"],
)


@router.get("/")
def list_flows(db: Session = Depends(get_db)):
    return FlowService.list(db)


@router.get("/{flow_id}")
def get_flow(flow_id: str, db: Session = Depends(get_db)):
    flow = FlowService.get(db, flow_id)

    if not flow:
        raise HTTPException(status_code=404, detail="Flow not found")

    return flow


@router.post("/")
def create_flow(
    flow: FlowCreate,
    db: Session = Depends(get_db),
):
    return FlowService.create(
        db=db,
        name=flow.name,
        description=flow.description,
    )


@router.delete("/{flow_id}")
def delete_flow(
    flow_id: str,
    db: Session = Depends(get_db),
):
    deleted = FlowService.delete(db, flow_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Flow not found")

    return {"message": "Flow deleted successfully"}
