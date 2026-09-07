from fastapi import APIRouter
from pydantic import BaseModel


from app.modules.deployment.distribution_service import (
    deployment_distribution_service,
)


class DeploymentDistributionRequest(
    BaseModel
):
    name: str

    version: str

    target: str

    architecture: str

    source_directory: str

    output_root: str


router = APIRouter()


@router.post(
    "/distribution/build"
)
def build_distribution(
    data: (
        DeploymentDistributionRequest
    ),
):
    return (
        deployment_distribution_service
        .build(
            name=data.name,
            version=data.version,
            target=data.target,
            architecture=(
                data.architecture
            ),
            source_directory=(
                data.source_directory
            ),
            output_root=(
                data.output_root
            ),
        )
    )
