from fastapi import APIRouter

from app.modules.deployment.distribution_status import (
    deployment_distribution_status,
)


router = APIRouter()


@router.get(
    "/distribution/status"
)
def distribution_status():
    return (
        deployment_distribution_status
        .snapshot()
    )
