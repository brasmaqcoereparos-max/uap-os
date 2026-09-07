from fastapi import APIRouter

from app.modules.deployment.summary import (
    deployment_summary,
)


router = APIRouter()


@router.get("/summary")
def summary():
    return (
        deployment_summary
        .snapshot()
    )
