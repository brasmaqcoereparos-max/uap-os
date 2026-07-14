from sqlalchemy.orm import Session

from app.models.plugin import Plugin
from app.repositories.plugin_repository import PluginRepository


class PluginService:

    @staticmethod
    def list(db: Session):
        return PluginRepository.list(db)

    @staticmethod
    def get(db: Session, plugin_id: str):
        return PluginRepository.get(db, plugin_id)

    @staticmethod
    def create(
        db: Session,
        name: str,
        version: str,
        author: str,
    ):
        plugin = Plugin(
            name=name,
            version=version,
            author=author,
        )

        return PluginRepository.create(db, plugin)

    @staticmethod
    def delete(
        db: Session,
        plugin_id: str,
    ):
        plugin = PluginRepository.get(db, plugin_id)

        if not plugin:
            return False

        PluginRepository.delete(db, plugin)

        return True
