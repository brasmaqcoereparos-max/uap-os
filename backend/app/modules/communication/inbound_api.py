from fastapi import APIRouter

from app.modules.communication.inbound_pipeline import (
    communication_inbound_pipeline,
)
from app.modules.communication.inbound_service import (
    communication_inbound_service,
)


router = APIRouter()


@router.get("/inbound/status")
def inbound_status():
    return {
        "pending": (
            communication_inbound_service
            .pending()
        )
    }


@router.post("/inbound/process")
def process_next():
    return (
        communication_inbound_pipeline
        .process_next()
    )


@router.delete("/inbound")
def clear_inbound():
    return {
        "cleared": (
            communication_inbound_service
            .clear()
        )
    }
