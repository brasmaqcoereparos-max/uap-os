from fastapi import APIRouter

from app.modules.deployment.deployment_boundary_service import (
    deployment_boundary_service,
)


router = APIRouter()


@router.get(
    "/boundary/install"
)
def boundary_install(
    target: str = "uap-box",
    root_path: str = ".uap",
):
    return (
        deployment_boundary_service
        .check_installation(
            target=target,
            root_path=root_path,
        )
    )
