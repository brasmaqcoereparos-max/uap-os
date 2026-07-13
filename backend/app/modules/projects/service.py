from sqlalchemy.orm import Session

from app.models.project import Project
from app.repositories.project_repository import ProjectRepository


class ProjectService:

    @staticmethod
    def list(db: Session):
        return ProjectRepository.list(db)

    @staticmethod
    def get(db: Session, project_id: str):
        return ProjectRepository.get(db, project_id)

    @staticmethod
    def create(
        db: Session,
        name: str,
        description: str = "",
    ):
        project = Project(
            name=name,
            description=description,
        )

        return ProjectRepository.create(db, project)

    @staticmethod
    def update(
        db: Session,
        project_id: str,
        name: str,
        description: str = "",
    ):
        project = ProjectRepository.get(db, project_id)

        if not project:
            return None

        project.name = name
        project.description = description

        db.commit()
        db.refresh(project)

        return project

    @staticmethod
    def delete(
        db: Session,
        project_id: str,
    ):
        project = ProjectRepository.get(db, project_id)

        if not project:
            return False

        ProjectRepository.delete(db, project)

        return True
