from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class DeploymentReleaseArtifact:
    name: str
    path: str

    artifact_type: str

    required: bool = True

    checksum: str = ""

    size: int = 0

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "name": self.name,
            "path": self.path,
            "artifact_type": (
                self.artifact_type
            ),
            "required": self.required,
            "checksum": self.checksum,
            "size": self.size,
            "metadata": dict(
                self.metadata
            ),
        }
