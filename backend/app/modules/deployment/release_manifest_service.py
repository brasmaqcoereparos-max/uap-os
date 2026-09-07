from app.modules.deployment.artifact_inspector import (
    deployment_artifact_inspector,
)
from app.modules.deployment.release_manifest import (
    DeploymentReleaseManifest,
)


class DeploymentReleaseManifestService:

    def build(
        self,
        version: str,
        target: str,
        artifacts: list[dict],
    ):
        manifest = (
            DeploymentReleaseManifest(
                version=version,
                target=target,
            )
        )

        for item in artifacts:
            artifact = (
                deployment_artifact_inspector
                .inspect(
                    name=str(
                        item.get(
                            "name",
                            "",
                        )
                    ),
                    path=str(
                        item.get(
                            "path",
                            "",
                        )
                    ),
                    artifact_type=str(
                        item.get(
                            "artifact_type",
                            "file",
                        )
                    ),
                    required=bool(
                        item.get(
                            "required",
                            True,
                        )
                    ),
                )
            )

            manifest.add(
                artifact
            )

        return manifest


deployment_release_manifest_service = (
    DeploymentReleaseManifestService()
          )
