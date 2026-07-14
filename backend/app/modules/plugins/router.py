from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.plugin import PluginCreate
from app.modules.plugins.service import PluginService

router = APIRouter(
    prefix="/plugins",
    tags=["Plugins"],
)


@router.get("/")
def list_plugins(db: Session = Depends(get_db)):
    return PluginService.list(db)


@router.get("/{plugin_id}")
def get_plugin(plugin_id: str, db: Session = Depends(get_db)):
    plugin = PluginService.get(db, plugin_id)

    if not plugin:
        raise HTTPException(status_code=404, detail="Plugin not found")

    return plugin


@router.post("/")
def create_plugin(
    plugin: PluginCreate,
    db: Session = Depends(get_db),
):
    return PluginService.create(
        db=db,
        name=plugin.name,
        version=plugin.version,
        author=plugin.author,
    )


@router.delete("/{plugin_id}")
def delete_plugin(
    plugin_id: str,
    db: Session = Depends(get_db),
):
    deleted = PluginService.delete(db, plugin_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Plugin not found")

    return {"message": "Plugin deleted successfully"}
