from fastapi import APIRouter

from app.modules.communication.integration_status import (
    communication_integration_status,
)


router = APIRouter()


@router.get("/integration")
def integration():
    return (
        communication_integration_status
        .snapshot()
    )
