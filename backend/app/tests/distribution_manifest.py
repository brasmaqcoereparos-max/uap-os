from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class DeploymentDistributionManifest:
    name: str

    version: str

    target: str

    architecture: str

    package_path: str

    package_checksum: str

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "name": self.name,
            "version": self.version,
            "target": self.target,
            "architecture": (
                self.architecture
            ),
            "package_path": (
                self.package_path
            ),
            "package_checksum": (
                self.package_checksum
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
        }
