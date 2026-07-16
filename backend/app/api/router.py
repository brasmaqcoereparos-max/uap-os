from fastapi import APIRouter

# ==========================================================
# Runtime
# ==========================================================

from app.runtime.router import router as runtime_engine_router
from app.runtime.router_health import router as runtime_health_router
from app.runtime.router_ws import router as websocket_router

# ==========================================================
# Authentication
# ==========================================================

from app.modules.auth.router import router as auth_router

# ==========================================================
# Core Modules
# ==========================================================

from app.modules.projects.router import router as project_router
from app.modules.devices.router import router as devices_router
from app.modules.drivers.router import router as drivers_router
from app.modules.users.router import router as users_router
from app.modules.plugins.router import router as plugins_router
from app.modules.automation.router import router as automation_router
from app.modules.events.router import router as events_router
from app.modules.flows.router import router as flows_router
from app.modules.runtime.router import router as runtime_router
from app.modules.dashboard.router import router as dashboard_router

# ==========================================================
# Education
# ==========================================================

from app.modules.education.router import router as education_router

# ==========================================================
# Simulator
# ==========================================================

from app.modules.simulator.router import router as simulator_router

# ==========================================================
# Visual Programming
# ==========================================================

from app.modules.simulator.programming.router import (
    router as programming_router,
)

# ==========================================================
# Canvas
# ==========================================================

from app.modules.simulator.programming.canvas.router import (
    router as canvas_router,
)

# ==========================================================
# Code Generator
# ==========================================================

from app.modules.simulator.codegen.router import (
    router as codegen_router,
)

# ==========================================================
# API
# ==========================================================

router = APIRouter()

# Runtime
router.include_router(runtime_engine_router)
router.include_router(runtime_health_router)
router.include_router(websocket_router)

# Authentication
router.include_router(auth_router)

# Core
router.include_router(project_router)
router.include_router(devices_router)
router.include_router(drivers_router)
router.include_router(users_router)
router.include_router(plugins_router)
router.include_router(automation_router)
router.include_router(events_router)
router.include_router(flows_router)
router.include_router(runtime_router)
router.include_router(dashboard_router)

# Education
router.include_router(education_router)

# Simulator
router.include_router(simulator_router)

# Visual Programming
router.include_router(programming_router)

# Canvas
router.include_router(canvas_router)

# Code Generator
router.include_router(codegen_router)


@router.get("/health")
def health():
    return {
        "status": "ok",
        "application": "UAP OS",
        "runtime": True,
        "education": True,
        "simulator": True,
        "visual_programming": True,
        "canvas": True,
        "code_generator": True,
    }


@router.get("/version")
def version():
    return {
        "application": "UAP OS",
        "version": "0.8.0",
        "runtime": "enabled",
        "education": "enabled",
        "simulator": "enabled",
        "visual_programming": "enabled",
        "canvas": "enabled",
        "code_generator": "enabled",
        "websocket": "enabled",
    }
