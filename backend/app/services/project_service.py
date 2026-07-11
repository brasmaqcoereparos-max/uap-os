from sqlalchemy.orm import Session

from app.models.project import Project


def create_project(db: Session, name: str, description: str):
    project = Project(
        name=name,
        description=description,
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project
