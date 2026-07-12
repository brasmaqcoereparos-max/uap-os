from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectService:

    @staticmethod
    def list(db: Session):
        return db.query(Project).all()

    @staticmethod
    def get(db: Session, project_id: int):
        return db.query(Project).filter(Project.id == project_id).first()

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

    @staticmethod
    def update(
        db: Session,
        project_id: int,
        name: str,
        description: str = "",
    ):
        project = db.query(Project).filter(Project.id == project_id).first()

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
        project_id: int,
    ):
        project = db.query(Project).filter(Project.id == project_id).first()

        if not project:
            return False

        db.delete(project)
        db.commit()

        return True
