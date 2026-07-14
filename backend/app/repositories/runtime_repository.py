from sqlalchemy.orm import Session

from app.models.runtime import Runtime


class RuntimeRepository:

    @staticmethod
    def list(db: Session):
        return db.query(Runtime).all()

    @staticmethod
    def get(db: Session, runtime_id: str):
        return db.query(Runtime).filter(Runtime.id == runtime_id).first()

    @staticmethod
    def create(db: Session, runtime: Runtime):
        db.add(runtime)
        db.commit()
        db.refresh(runtime)
        return runtime

    @staticmethod
    def delete(db: Session, runtime: Runtime):
        db.delete(runtime)
        db.commit()
