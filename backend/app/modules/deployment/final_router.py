from fastapi import APIRouter

from app.modules.deployment.boundary_api import (
    router as boundary_router,
)
from app.modules.deployment.distribution_api import (
    router as distribution_router,
)
from app.modules.deployment.distribution_status_api import (
    router as distribution_status_router,
)
from app.modules.deployment.final_status_api import (
    router as final_status_router,
)
from app.modules.deployment.release_summary_api import (
    router as release_summary_router,
)
from app.modules.deployment.summary_api import (
    router as summary_router,
)


router = APIRouter()


router.include_router(
    boundary_router
)

router.include_router(
    distribution_router
)

router.include_router(
    distribution_status_router
)

router.include_router(
    release_summary_router
)

router.include_router(
    summary_router
)

router.include_router(
    final_status_router
)
