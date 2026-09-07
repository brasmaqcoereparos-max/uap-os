from fastapi import APIRouter

from app.modules.security.activation_api import (
    router as activation_router,
)
from app.modules.security.feature_api import (
    router as feature_router,
)
from app.modules.security.health_api import (
    router as health_router,
)
from app.modules.security.identity_api import (
    router as identity_router,
)
from app.modules.security.license_api import (
    router as license_router,
)
from app.modules.security.module_access_api import (
    router as module_access_router,
)
from app.modules.security.signing_api import (
    router as signing_router,
)


router = APIRouter(
    prefix="/security",
    tags=["Security"],
)


router.include_router(
    health_router
)

router.include_router(
    identity_router
)

router.include_router(
    license_router
)

router.include_router(
    activation_router
)

router.include_router(
    signing_router
)

router.include_router(
    feature_router
)

router.include_router(
    module_access_router
)
