from app.modules.deployment.release_manifest import (
    DeploymentReleaseManifest,
)


class DeploymentReleaseValidator:

    def validate(
        self,
        manifest: DeploymentReleaseManifest,
    ):
        errors = []
        warnings = []

        for artifact in (
            manifest.artifacts
        ):
            exists = bool(
                artifact.metadata.get(
                    "exists",
                    False,
                )
            )

            if (
                artifact.required
                and not exists
            ):
                errors.append(
                    (
                        "Required artifact "
                        f"missing: "
                        f"{artifact.name}"
                    )
                )

            elif (
                not artifact.required
                and not exists
            ):
                warnings.append(
                    (
                        "Optional artifact "
                        f"missing: "
                        f"{artifact.name}"
                    )
                )

        return {
            "valid": not errors,
            "errors": errors,
            "warnings": warnings,
        }


deployment_release_validator = (
    DeploymentReleaseValidator()
          )
