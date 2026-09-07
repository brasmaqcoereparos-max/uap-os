from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class DeploymentUpdatePackage:
    version: str

    source: str

    checksum: str = ""

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "version": self.version,
            "source": self.source,
            "checksum": (
                self.checksum
            ),
            "metadata": dict(
                self.metadata
            ),
        }
