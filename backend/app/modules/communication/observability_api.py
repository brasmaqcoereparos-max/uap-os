from fastapi import APIRouter

from app.modules.communication.observability_service import (
    communication_observability_service,
)


router = APIRouter()


@router.get("/observability")
def observability():
    return (
        communication_observability_service
        .snapshot()
    )


@router.delete("/observability")
def clear_observability():
    return {
        "cleared": (
            communication_observability_service
            .clear()
        )
    }
