from fastapi import APIRouter

from app.modules.deployment.api_models import (
    DeploymentPreflightRequest,
)
from app.modules.deployment.preflight_service import (
    deployment_preflight_service,
)


router = APIRouter()


@router.post("/preflight")
def preflight(
    data: DeploymentPreflightRequest,
):
    return (
        deployment_preflight_service
        .run(
            target=data.target,
            root_path=data.root_path,
        )
    )
