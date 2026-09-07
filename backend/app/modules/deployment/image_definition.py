from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class DeploymentImageDefinition:
    name: str

    version: str

    target: str

    base_image: str = ""

    filesystem: str = "ext4"

    architecture: str = ""

    packages: list[str] = field(
        default_factory=list
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
            "base_image": (
                self.base_image
            ),
            "filesystem": (
                self.filesystem
            ),
            "architecture": (
                self.architecture
            ),
            "packages": list(
                self.packages
            ),
            "metadata": dict(
                self.metadata
            ),
        }
