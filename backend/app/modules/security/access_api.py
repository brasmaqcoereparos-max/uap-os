from fastapi import APIRouter

from app.modules.security.security_access_protection_service import (
    security_access_protection_service,
)


router = APIRouter()


@router.get("/access/check")
def access_check(
    principal_id: str,
    rate_key: str | None = None,
):
    return (
        security_access_protection_service
        .check(
            principal_id=(
                principal_id
            ),
            rate_key=rate_key,
        )
    )


@router.post(
    "/access/login-result"
)
def login_result(
    principal_id: str,
    success: bool,
):
    return (
        security_access_protection_service
        .record_login(
            principal_id=(
                principal_id
            ),
            success=success,
        )
    )
