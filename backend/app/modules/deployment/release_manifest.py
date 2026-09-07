from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone

from app.modules.deployment.release_artifact import (
    DeploymentReleaseArtifact,
)


@dataclass
class DeploymentReleaseManifest:
    version: str

    target: str

    artifacts: list[
        DeploymentReleaseArtifact
    ] = field(
        default_factory=list
    )

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    def add(
        self,
        artifact: DeploymentReleaseArtifact,
    ):
        self.artifacts.append(
            artifact
        )

        return artifact

    def to_dict(self):
        return {
            "version": self.version,
            "target": self.target,
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "artifacts": [
                artifact.to_dict()
                for artifact
                in self.artifacts
            ],
        }
