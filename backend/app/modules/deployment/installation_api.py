from fastapi import APIRouter

from app.modules.deployment.api_models import (
    DeploymentInstallRequest,
)
from app.modules.deployment.installation_service import (
    deployment_installation_service,
)


router = APIRouter()


@router.post("/installation/plan")
def installation_plan(
    data: DeploymentInstallRequest,
):
    return (
        deployment_installation_service
        .plan(
            target=data.target,
            root_path=data.root_path,
        )
    )


@router.post("/installation/run")
def installation_run(
    data: DeploymentInstallRequest,
):
    return (
        deployment_installation_service
        .install(
            target=data.target,
            root_path=data.root_path,
        )
    )
