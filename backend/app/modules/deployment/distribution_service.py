from app.modules.deployment.archive_builder import (
    deployment_archive_builder,
)
from app.modules.deployment.distribution_layout_service import (
    deployment_distribution_layout_service,
)
from app.modules.deployment.distribution_manifest import (
    DeploymentDistributionManifest,
)
from app.modules.deployment.distribution_manifest_writer import (
    deployment_distribution_manifest_writer,
)
from app.modules.deployment.distribution_validator import (
    deployment_distribution_validator,
)


class DeploymentDistributionService:

    def build(
        self,
        name: str,
        version: str,
        target: str,
        architecture: str,
        source_directory: str,
        output_root: str,
    ):
        layout = (
            deployment_distribution_layout_service
            .build(
                output_root
            )
        )

        deployment_distribution_layout_service.ensure(
            layout
        )

        package_path = (
            layout.package
            / (
                f"{name}-"
                f"{version}.zip"
            )
        )

        archive = (
            deployment_archive_builder
            .build_zip(
                source_directory=(
                    source_directory
                ),
                output_path=str(
                    package_path
                ),
            )
        )

        manifest = (
            DeploymentDistributionManifest(
                name=name,
                version=version,
                target=target,
                architecture=architecture,
                package_path=archive.path,
                package_checksum=(
                    archive.checksum
                ),
            )
        )

        manifest_path = (
            deployment_distribution_manifest_writer
            .write(
                manifest=manifest,
                output_directory=str(
                    layout.manifest
                ),
            )
        )

        validation = (
            deployment_distribution_validator
            .validate(
                manifest
            )
        )

        return {
            "created": (
                validation["valid"]
            ),
            "archive": (
                archive.to_dict()
            ),
            "manifest": (
                manifest.to_dict()
            ),
            "manifest_path": (
                manifest_path
            ),
            "validation": (
                validation
            ),
            "layout": (
                layout.to_dict()
            ),
        }


deployment_distribution_service = (
    DeploymentDistributionService()
)
