from fastapi import APIRouter

from app.modules.uhal.status import (
    uhal_status,
)


router = APIRouter(
    prefix="/uhal",
    tags=["UHAL"],
)


@router.get("/health")
def health():
    return (
        uhal_status
        .snapshot()
    )


@router.get("/status")
def status():
    return (
        uhal_status
        .snapshot()
    )
