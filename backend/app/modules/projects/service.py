from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectService:

    @staticmethod
    def list(db: Session):
        return db.query(Project).all()

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

        db.add(project)
        db.commit()
        db.refresh(project)

        return project
