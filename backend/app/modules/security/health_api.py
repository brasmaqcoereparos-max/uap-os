from fastapi import APIRouter

from app.modules.security.security_health_service import (
    security_health_service,
)


router = APIRouter()


@router.get("/health")
def health():
    return (
        security_health_service
        .check()
    )
