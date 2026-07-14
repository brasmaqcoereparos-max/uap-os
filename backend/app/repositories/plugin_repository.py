from sqlalchemy.orm import Session

from app.models.plugin import Plugin


class PluginRepository:

    @staticmethod
    def list(db: Session):
        return db.query(Plugin).all()

    @staticmethod
    def get(db: Session, plugin_id: str):
        return db.query(Plugin).filter(Plugin.id == plugin_id).first()

    @staticmethod
    def create(db: Session, plugin: Plugin):
        db.add(plugin)
        db.commit()
        db.refresh(plugin)
        return plugin

    @staticmethod
    def delete(db: Session, plugin: Plugin):
        db.delete(plugin)
        db.commit()
