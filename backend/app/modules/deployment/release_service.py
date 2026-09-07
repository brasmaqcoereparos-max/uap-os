from app.modules.deployment.image_builder_service import (
    deployment_image_builder_service,
)
from app.modules.deployment.package_builder import (
    deployment_package_builder,
)
from app.modules.deployment.package_definition import (
    DeploymentPackageDefinition,
)
from app.modules.deployment.release_manifest_service import (
    deployment_release_manifest_service,
)
from app.modules.deployment.release_validator import (
    deployment_release_validator,
)


class DeploymentReleaseService:

    def prepare_release(
        self,
        name: str,
        version: str,
        target: str,
        architecture: str,
        artifacts: list[dict],
        include_paths: list[str],
        output_path: str,
        base_image: str = "",
        packages: (
            list[str] | None
        ) = None,
    ):
        manifest = (
            deployment_release_manifest_service
            .build(
                version=version,
                target=target,
                artifacts=artifacts,
            )
        )

        validation = (
            deployment_release_validator
            .validate(
                manifest
            )
        )

        package_definition = (
            DeploymentPackageDefinition(
                name=name,
                version=version,
                target=target,
                include_paths=list(
                    include_paths
                ),
                output_path=(
                    output_path
                ),
            )
        )

        package = (
            deployment_package_builder
            .prepare(
                package_definition
            )
        )

        image = (
            deployment_image_builder_service
            .prepare(
                name=name,
                version=version,
                target=target,
                architecture=(
                    architecture
                ),
                base_image=(
                    base_image
                ),
                packages=packages,
            )
        )

        return {
            "ready": (
                validation["valid"]
                and package[
                    "prepared"
                ]
            ),
            "manifest": (
                manifest.to_dict()
            ),
            "validation": (
                validation
            ),
            "package": package,
            "image": image,
        }


deployment_release_service = (
    DeploymentReleaseService()
      )
