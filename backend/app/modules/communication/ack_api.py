from fastapi import APIRouter

from app.modules.communication.ack_manager import (
    communication_ack_manager,
)


router = APIRouter()


@router.get("/acks")
def list_acks():
    return (
        communication_ack_manager
        .list_all()
    )


@router.delete("/acks")
def clear_acks():
    communication_ack_manager.clear()

    return {
        "cleared": True
    }
