from fastapi import APIRouter

from app.modules.deployment.final_status import (
    deployment_final_status,
)


router = APIRouter()


@router.get("/final-status")
def final_status(
    target: str = "uap-box",
    root_path: str = ".uap",
):
    return (
        deployment_final_status
        .snapshot(
            target=target,
            root_path=root_path,
        )
    )
