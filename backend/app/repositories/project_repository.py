from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectRepository:

    @staticmethod
    def list(db: Session):
        return db.query(Project).all()

    @staticmethod
    def get(db: Session, project_id: str):
        return db.query(Project).filter(Project.id == project_id).first()

    @staticmethod
    def create(db: Session, project: Project):
        db.add(project)
        db.commit()
        db.refresh(project)
        return project

    @staticmethod
    def delete(db: Session, project: Project):
        db.delete(project)
        db.commit()
