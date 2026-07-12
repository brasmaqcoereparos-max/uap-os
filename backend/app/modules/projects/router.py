from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.project import ProjectCreate
from app.modules.projects.service import ProjectService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get("/")
def list_projects(
    db: Session = Depends(get_db),
):
    return ProjectService.list(db)


@router.post("/")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
):
    return ProjectService.create(
        db=db,
        name=project.name,
        description=project.description,
    )
