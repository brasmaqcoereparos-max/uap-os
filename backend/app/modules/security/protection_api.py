from fastapi import APIRouter

from app.modules.security.protection_status import (
    security_protection_status,
)


router = APIRouter()


@router.get(
    "/protection/status"
)
def protection_status():
    return (
        security_protection_status
        .snapshot()
    )
