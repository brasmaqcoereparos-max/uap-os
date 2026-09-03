from fastapi import APIRouter

from app.modules.voice.command_api import (
    router as command_router,
)
from app.modules.voice.confirmation_api import (
    router as confirmation_router,
)
from app.modules.voice.execution_api import (
    router as execution_router,
)
from app.modules.voice.health_api import (
    router as health_router,
)
from app.modules.voice.session_api import (
    router as session_router,
)
from app.modules.voice.stream_api import (
    router as stream_router,
)
from app.modules.voice.text_api import (
    router as text_router,
)


router = APIRouter(
    prefix="/voice",
    tags=["Voice"],
)


router.include_router(
    health_router
)

router.include_router(
    session_router
)

router.include_router(
    text_router
)

router.include_router(
    stream_router
)

router.include_router(
    command_router
)

router.include_router(
    confirmation_router
)

router.include_router(
    execution_router
)
