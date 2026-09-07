from fastapi import APIRouter

from app.modules.security.final_status import (
    security_final_status,
)


router = APIRouter()


@router.get("/final-status")
def final_status():
    return (
        security_final_status
        .snapshot()
    )
