from fastapi import APIRouter

from app.modules.deployment.api_models import (
    DeploymentReleaseRequest,
)
from app.modules.deployment.release_service import (
    deployment_release_service,
)


router = APIRouter()


@router.post("/release/prepare")
def prepare_release(
    data: DeploymentReleaseRequest,
):
    return (
        deployment_release_service
        .prepare_release(
            name=data.name,
            version=data.version,
            target=data.target,
            architecture=(
                data.architecture
            ),
            artifacts=(
                data.artifacts
            ),
            include_paths=(
                data.include_paths
            ),
            output_path=(
                data.output_path
            ),
            base_image=(
                data.base_image
            ),
            packages=(
                data.packages
            ),
        )
    )
