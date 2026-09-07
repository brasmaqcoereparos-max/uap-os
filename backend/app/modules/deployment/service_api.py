from fastapi import APIRouter

from app.modules.deployment.service_manager import (
    deployment_service_manager,
)


router = APIRouter()


@router.get(
    "/service/{service_name}/command/{action}"
)
def service_command(
    service_name: str,
    action: str,
):
    return (
        deployment_service_manager
        .command(
            service_name=service_name,
            action=action,
        )
    )


@router.get(
    "/service/{service_name}/logs"
)
def service_logs(
    service_name: str,
    lines: int = 100,
):
    return (
        deployment_service_manager
        .logs(
            service_name=service_name,
            lines=lines,
        )
    )
