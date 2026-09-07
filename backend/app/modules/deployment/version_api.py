from fastapi import APIRouter

from app.modules.deployment.update_service import (
    deployment_update_service,
)
from app.modules.deployment.version_registry import (
    deployment_version_registry,
)


router = APIRouter()


@router.get("/versions")
def versions():
    return [
        version.to_dict()
        for version
        in deployment_version_registry
        .list_all()
    ]


@router.post("/versions/{version}")
def register_version(
    version: str,
    build: str = "",
):
    record = (
        deployment_update_service
        .register_version(
            version=version,
            build=build,
        )
    )

    return record.to_dict()
