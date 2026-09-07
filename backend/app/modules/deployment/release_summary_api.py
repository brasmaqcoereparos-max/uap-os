from fastapi import APIRouter

from app.modules.deployment.release_summary import (
    deployment_release_summary,
)


router = APIRouter()


@router.get(
    "/release/summary"
)
def release_summary():
    return (
        deployment_release_summary
        .snapshot()
    )
