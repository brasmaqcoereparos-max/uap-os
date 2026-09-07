from app.modules.deployment.backup_service import (
    deployment_backup_service,
)
from app.modules.deployment.deployment_version import (
    DeploymentVersion,
)
from app.modules.deployment.update_package import (
    DeploymentUpdatePackage,
)
from app.modules.deployment.update_validator import (
    deployment_update_validator,
)
from app.modules.deployment.version_registry import (
    deployment_version_registry,
)


class DeploymentUpdateService:

    def prepare(
        self,
        package: DeploymentUpdatePackage,
        current_path: str,
        backup_directory: str,
    ):
        validation = (
            deployment_update_validator
            .validate(
                package
            )
        )

        if not validation[
            "valid"
        ]:
            return {
                "prepared": False,
                "validation": validation,
                "backup": None,
            }

        backup = (
            deployment_backup_service
            .create(
                source=current_path,
                backup_directory=(
                    backup_directory
                ),
                version=(
                    deployment_version_registry
                    .current()
                    .version
                    if (
                        deployment_version_registry
                        .current()
                    )
                    else ""
                ),
            )
        )

        return {
            "prepared": True,
            "validation": validation,
            "backup": (
                backup.to_dict()
            ),
            "package": (
                package.to_dict()
            ),
            "update_applied": False,
        }

    def register_version(
        self,
        version: str,
        build: str = "",
    ):
        return (
            deployment_version_registry
            .register(
                DeploymentVersion(
                    version=version,
                    build=build,
                )
            )
        )


deployment_update_service = (
    DeploymentUpdateService()
      )
