from pathlib import Path

from app.modules.deployment.package_definition import (
    DeploymentPackageDefinition,
)


class DeploymentPackageBuilder:

    def prepare(
        self,
        definition: (
            DeploymentPackageDefinition
        ),
    ):
        existing = []
        missing = []

        for item in (
            definition.include_paths
        ):
            path = Path(
                item
            )

            if path.exists():
                existing.append(
                    str(path)
                )

            else:
                missing.append(
                    str(path)
                )

        return {
            "prepared": (
                len(missing) == 0
            ),
            "definition": (
                definition.to_dict()
            ),
            "existing": existing,
            "missing": missing,
            "package_created": False,
        }


deployment_package_builder = (
    DeploymentPackageBuilder()
)
