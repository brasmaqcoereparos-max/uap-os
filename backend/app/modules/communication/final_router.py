from fastapi import APIRouter

from app.modules.communication.ack_api import (
    router as ack_router,
)
from app.modules.communication.dead_letter_api import (
    router as dead_letter_router,
)
from app.modules.communication.final_status import (
    communication_final_status,
)
from app.modules.communication.inbound_api import (
    router as inbound_router,
)
from app.modules.communication.integration_api import (
    router as integration_router,
)
from app.modules.communication.observability_router import (
    router as observability_router,
)
from app.modules.communication.provider_api import (
    router as provider_router,
)


router = APIRouter()


@router.get("/final-status")
def final_status():
    return (
        communication_final_status
        .snapshot()
    )


router.include_router(
    provider_router
)

router.include_router(
    inbound_router
)

router.include_router(
    dead_letter_router
)

router.include_router(
    ack_router
)

router.include_router(
    integration_router
)

router.include_router(
    observability_router
  )
