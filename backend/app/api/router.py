from fastapi import APIRouter

from app.api.routes import auth
from app.api.routes import devices
from app.api.routes import drivers
from app.api.routes import projects
from app.api.routes import users

from app.modules.ai.router import (
    router as ai_router,
)
from app.modules.automation.router import (
    router as automation_router,
)
from app.modules.communication.router import (
    router as communication_router,
)
from app.modules.dashboard.router import (
    router as dashboard_router,
)
from app.modules.education.router import (
    router as education_router,
)
from app.modules.events.router import (
    router as events_router,
)
from app.modules.flows.router import (
    router as flows_router,
)
from app.modules.plugins.router import (
    router as plugins_router,
)
from app.modules.runtime.router import (
    router as runtime_router,
)
from app.modules.simulator.codegen.router import (
    router as codegen_router,
)
from app.modules.simulator.programming.canvas.router import (
    router as canvas_router,
)
from app.modules.simulator.programming.router import (
    router as programming_router,
)
from app.modules.simulator.router import (
    router as simulator_router,
)
from app.modules.ui.router import (
    router as ui_router,
)
from app.modules.ui.studio_router import (
    router as ui_studio_router,
)
from app.modules.voice.router import (
    router as voice_router,
)


router = APIRouter()


# ============================================================
# CORE API
# ============================================================

router.include_router(
    auth.router
)

router.include_router(
    projects.router
)

router.include_router(
    devices.router
)

router.include_router(
    drivers.router
)

router.include_router(
    users.router
)


# ============================================================
# PLATFORM MODULES
# ============================================================

router.include_router(
    plugins_router
)

router.include_router(
    automation_router
)

router.include_router(
    events_router
)

router.include_router(
    flows_router
)

router.include_router(
    runtime_router
)

router.include_router(
    dashboard_router
)

router.include_router(
    education_router
)

router.include_router(
    communication_router
)


# ============================================================
# SIMULATOR / VISUAL PROGRAMMING
# ============================================================

router.include_router(
    simulator_router
)

router.include_router(
    programming_router
)

router.include_router(
    canvas_router
)

router.include_router(
    codegen_router
)


# ============================================================
# APP / UI / GRAPHICS
# ============================================================

router.include_router(
    ui_router
)

router.include_router(
    ui_studio_router
)


# ============================================================
# VOICE
# ============================================================

router.include_router(
    voice_router
)


# ============================================================
# AI
# ============================================================

router.include_router(
    ai_router
)


# ============================================================
# PLATFORM INFORMATION
# ============================================================

@router.get(
    "/health",
    tags=["Platform"],
)
def health():
    return {
        "status": "ok",
        "service": "uap-api",
    }


@router.get(
    "/version",
    tags=["Platform"],
)
def version():
    return {
        "name": "UAP OS",
        "version": "0.1.0",
    }
