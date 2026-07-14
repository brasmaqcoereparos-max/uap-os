from fastapi import APIRouter

from app.modules.projects.router import router as project_router
from app.modules.devices.router import router as devices_router
from app.modules.drivers.router import router as drivers_router
from app.modules.users.router import router as users_router
from app.modules.plugins.router import router as plugins_router
from app.modules.automation.router import router as automation_router

router = APIRouter()

router.include_router(project_router)
router.include_router(devices_router)
router.include_router(drivers_router)
router.include_router(users_router)
router.include_router(plugins_router)
router.include_router(automation_router)


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/version")
def version():
    return {
        "application": "UAP OS",
        "version": "0.1.0",
    }
