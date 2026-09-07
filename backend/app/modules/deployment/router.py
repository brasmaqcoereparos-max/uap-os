from fastapi import APIRouter

from app.modules.deployment.final_router import (
    router as final_router,
)
from app.modules.deployment.installation_api import (
    router as installation_router,
)
from app.modules.deployment.lifecycle_api import (
    router as lifecycle_router,
)
from app.modules.deployment.preflight_api import (
    router as preflight_router,
)
from app.modules.deployment.release_api import (
    router as release_router,
)
from app.modules.deployment.service_api import (
    router as service_router,
)
from app.modules.deployment.status import (
    deployment_status,
)
from app.modules.deployment.version_api import (
    router as version_router,
)


router = APIRouter(
    prefix="/deployment",
    tags=["Deployment"],
)


@router.get("/health")
def health():
    return (
        deployment_status
        .snapshot()
    )


router.include_router(
    preflight_router
)

router.include_router(
    installation_router
)

router.include_router(
    release_router
)

router.include_router(
    version_router
)

router.include_router(
    lifecycle_router
)

router.include_router(
    service_router
)

router.include_router(
    final_router
)
