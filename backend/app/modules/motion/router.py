from fastapi import APIRouter

from app.modules.motion.status import (
    motion_status,
)


router = APIRouter(
    prefix="/motion",
    tags=["Motion"],
)


@router.get("/health")
def health():
    return (
        motion_status
        .snapshot()
    )


@router.get("/status")
def status():
    return (
        motion_status
        .snapshot()
    )
