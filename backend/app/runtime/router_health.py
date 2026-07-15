from fastapi import APIRouter

from app.runtime.health import runtime_health

router = APIRouter(
    prefix="/engine",
    tags=["Runtime Engine"],
)


@router.get("/health")
def health():
    return runtime_health.status()
