from fastapi import APIRouter

from app.modules.communication.observability_api import (
    router as observability_router,
)


router = APIRouter()

router.include_router(
    observability_router
)
