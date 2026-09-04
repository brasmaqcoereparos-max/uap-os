from fastapi import APIRouter

from app.modules.ai.automation_api import (
    router as automation_router,
)
from app.modules.ai.hardware_api import (
    router as hardware_router,
)
from app.modules.ai.health import (
    ai_health,
)
from app.modules.ai.planner_api import (
    router as planner_router,
)
from app.modules.ai.project_api import (
    router as project_router,
)
from app.modules.ai.session_api import (
    router as session_router,
)
from app.modules.ai.ui_api import (
    router as ui_router,
)


router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.get("/health")
def health():
    return ai_health.check()


router.include_router(
    session_router
)

router.include_router(
    planner_router
)

router.include_router(
    project_router
)

router.include_router(
    hardware_router
)

router.include_router(
    automation_router
)

router.include_router(
    ui_router
)
