from fastapi import APIRouter

from app.modules.ude.status import (
    ude_status,
)


router = APIRouter(
    prefix="/ude",
    tags=["UDE"],
)


@router.get("/health")
def health():
    return (
        ude_status
        .snapshot()
    )


@router.get("/status")
def status():
    return (
        ude_status
        .snapshot()
    )
