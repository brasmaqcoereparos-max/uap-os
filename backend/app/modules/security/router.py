from fastapi import APIRouter

from app.modules.security.access_api import (
    router as access_router,
)
from app.modules.security.activation_api import (
    router as activation_router,
)
from app.modules.security.boundary_api import (
    router as boundary_router,
)
from app.modules.security.feature_api import (
    router as feature_router,
)
from app.modules.security.final_status_api import (
    router as final_status_router,
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
from app.modules.security.lockout_api import (
    router as lockout_router,
)
from app.modules.security.module_access_api import (
    router as module_access_router,
)
from app.modules.security.protection_api import (
    router as protection_router,
)
from app.modules.security.rate_limit_api import (
    router as rate_limit_router,
)
from app.modules.security.runtime_security_api import (
    router as runtime_security_router,
)
from app.modules.security.security_audit_api import (
    router as audit_router,
)
from app.modules.security.security_event_api import (
    router as event_router,
)
from app.modules.security.session_api import (
    router as session_router,
)
from app.modules.security.signing_api import (
    router as signing_router,
)
from app.modules.security.summary_api import (
    router as summary_router,
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

router.include_router(
    runtime_security_router
)

router.include_router(
    audit_router
)

router.include_router(
    session_router
)

router.include_router(
    lockout_router
)

router.include_router(
    rate_limit_router
)

router.include_router(
    event_router
)

router.include_router(
    access_router
)

router.include_router(
    protection_router
)

router.include_router(
    boundary_router
)

router.include_router(
    summary_router
)

router.include_router(
    final_status_router
)
