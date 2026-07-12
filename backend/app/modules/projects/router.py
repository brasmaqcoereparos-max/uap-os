from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.modules.projects.service import ProjectService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get("/")
def list_projects(db: Session = Depends(get_db)):
    return ProjectService.list(db)


@router.get("/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = ProjectService.get(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


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


@router.put("/{project_id}")
def update_project(
    project_id: int,
    project: ProjectUpdate, 
    db: Session = Depends(get_db),
):
    updated = ProjectService.update(
        db=db,
        project_id=project_id,
        name=project.name,
        description=project.description,
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")

    return updated


@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
):
    deleted = ProjectService.delete(db, project_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")

    return {"message": "Project deleted successfully"}
