from app.modules.deployment.rollback_service import (
    deployment_rollback_service,
)
from app.modules.deployment.update_package import (
    DeploymentUpdatePackage,
)
from app.modules.deployment.update_service import (
    deployment_update_service,
)
from app.modules.deployment.version_registry import (
    deployment_version_registry,
)


class DeploymentLifecycleService:

    def versions(self):
        return [
            version.to_dict()
            for version
            in deployment_version_registry
            .list_all()
        ]

    def prepare_update(
        self,
        version: str,
        source: str,
        current_path: str,
        backup_directory: str,
        checksum: str = "",
    ):
        package = (
            DeploymentUpdatePackage(
                version=version,
                source=source,
                checksum=checksum,
            )
        )

        return (
            deployment_update_service
            .prepare(
                package=package,
                current_path=(
                    current_path
                ),
                backup_directory=(
                    backup_directory
                ),
            )
        )

    def prepare_rollback(
        self,
        backup_path: str,
        target_path: str,
        version: str = "",
    ):
        return (
            deployment_rollback_service
            .prepare(
                backup_path=(
                    backup_path
                ),
                target_path=(
                    target_path
                ),
                version=version,
            )
        )


deployment_lifecycle_service = (
    DeploymentLifecycleService()
  )
