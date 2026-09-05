from fastapi import APIRouter

from app.modules.communication.transport_manager import (
    communication_transport_manager,
)


router = APIRouter()


@router.get("/transports")
def transports():
    return (
        communication_transport_manager
        .transports()
    )
