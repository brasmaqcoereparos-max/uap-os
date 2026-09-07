from fastapi import APIRouter

from app.modules.security.rate_limiter import (
    security_rate_limiter,
)
from app.modules.security.security_access_protection_service import (
    security_access_protection_service,
)


router = APIRouter()


@router.get(
    "/rate-limit/{key}"
)
def rate_limit_check(
    key: str,
):
    return (
        security_access_protection_service
        .check(
            principal_id=key,
            rate_key=key,
        )
    )


@router.delete(
    "/rate-limit/{key}"
)
def rate_limit_reset(
    key: str,
):
    security_rate_limiter.reset(
        key
    )

    return {
        "reset": True,
        "key": key,
    }
