from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.runtime import RuntimeCreate
from app.modules.runtime.service import RuntimeService

router = APIRouter(
    prefix="/runtime",
    tags=["Runtime"],
)


@router.get("/")
def list_runtime(db: Session = Depends(get_db)):
    return RuntimeService.list(db)


@router.get("/{runtime_id}")
def get_runtime(runtime_id: str, db: Session = Depends(get_db)):
    runtime = RuntimeService.get(db, runtime_id)

    if not runtime:
        raise HTTPException(status_code=404, detail="Runtime not found")

    return runtime


@router.post("/")
def create_runtime(
    runtime: RuntimeCreate,
    db: Session = Depends(get_db),
):
    return RuntimeService.create(
        db=db,
        name=runtime.name,
    )


@router.delete("/{runtime_id}")
def delete_runtime(
    runtime_id: str,
    db: Session = Depends(get_db),
):
    deleted = RuntimeService.delete(db, runtime_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Runtime not found")

    return {"message": "Runtime deleted successfully"}
