from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
)
from app.services.project_service import (
    project_service,
)


router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get(
    "/",
    response_model=list[ProjectResponse],
)
def list_projects(
    db: Session = Depends(get_db),
):
    return project_service.list(
        db
    )


@router.post(
    "/",
    response_model=ProjectResponse,
)
def create_project(
    data: ProjectCreate,
    db: Session = Depends(get_db),
):
    return project_service.create(
        db,
        data,
    )


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def get_project(
    project_id: str,
    db: Session = Depends(get_db),
):
    project = project_service.get(
        db,
        project_id,
    )

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Projeto não encontrado.",
        )

    return project
