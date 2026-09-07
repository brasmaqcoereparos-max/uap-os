from fastapi import APIRouter

from app.modules.deployment.deployment_lifecycle_service import (
    deployment_lifecycle_service,
)


router = APIRouter()


@router.get("/lifecycle/versions")
def lifecycle_versions():
    return (
        deployment_lifecycle_service
        .versions()
    )


@router.post("/lifecycle/update")
def prepare_update(
    version: str,
    source: str,
    current_path: str,
    backup_directory: str,
    checksum: str = "",
):
    return (
        deployment_lifecycle_service
        .prepare_update(
            version=version,
            source=source,
            current_path=current_path,
            backup_directory=(
                backup_directory
            ),
            checksum=checksum,
        )
    )


@router.post("/lifecycle/rollback")
def prepare_rollback(
    backup_path: str,
    target_path: str,
    version: str = "",
):
    return (
        deployment_lifecycle_service
        .prepare_rollback(
            backup_path=backup_path,
            target_path=target_path,
            version=version,
        )
  )
