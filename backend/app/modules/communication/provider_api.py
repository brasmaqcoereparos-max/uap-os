from fastapi import APIRouter

from app.modules.communication.provider_health_service import (
    communication_provider_health_service,
)
from app.modules.communication.provider_manager import (
    communication_provider_manager,
)


router = APIRouter()


@router.get("/providers")
def providers():
    return (
        communication_provider_manager
        .providers()
    )


@router.get("/providers/health")
def provider_health():
    return (
        communication_provider_health_service
        .check()
    )
