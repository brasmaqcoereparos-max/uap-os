import hashlib
from pathlib import Path

from app.modules.deployment.release_artifact import (
    DeploymentReleaseArtifact,
)


class DeploymentArtifactInspector:

    def inspect(
        self,
        name: str,
        path: str,
        artifact_type: str,
        required: bool = True,
    ):
        artifact_path = Path(
            path
        )

        if not artifact_path.exists():
            return (
                DeploymentReleaseArtifact(
                    name=name,
                    path=str(
                        artifact_path
                    ),
                    artifact_type=(
                        artifact_type
                    ),
                    required=required,
                    checksum="",
                    size=0,
                    metadata={
                        "exists": False,
                    },
                )
            )

        if artifact_path.is_file():
            data = (
                artifact_path
                .read_bytes()
            )

            checksum = (
                hashlib.sha256(
                    data
                )
                .hexdigest()
            )

            size = len(
                data
            )

        else:
            checksum = ""
            size = 0

        return (
            DeploymentReleaseArtifact(
                name=name,
                path=str(
                    artifact_path
                ),
                artifact_type=(
                    artifact_type
                ),
                required=required,
                checksum=checksum,
                size=size,
                metadata={
                    "exists": True,
                    "is_directory": (
                        artifact_path
                        .is_dir()
                    ),
                },
            )
        )


deployment_artifact_inspector = (
    DeploymentArtifactInspector()
      )
