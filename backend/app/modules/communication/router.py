from fastapi import APIRouter

from app.modules.communication.bus_api import (
    router as bus_router,
)
from app.modules.communication.connection_api import (
    router as connection_router,
)
from app.modules.communication.final_router import (
    router as final_router,
)
from app.modules.communication.secure_api import (
    router as secure_router,
)
from app.modules.communication.status import (
    communication_status,
)
from app.modules.communication.transport_api import (
    router as transport_router,
)


router = APIRouter(
    prefix="/communication",
    tags=["Communication"],
)


@router.get("/health")
def health():
    return (
        communication_status
        .snapshot()
    )


router.include_router(
    bus_router
)

router.include_router(
    connection_router
)

router.include_router(
    secure_router
)

router.include_router(
    transport_router
)

router.include_router(
    final_router
)
