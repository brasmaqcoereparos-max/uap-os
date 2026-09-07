from dataclasses import dataclass
from dataclasses import field


@dataclass
class DeploymentPackageDefinition:
    name: str

    version: str

    target: str

    include_paths: list[str] = field(
        default_factory=list
    )

    output_path: str = ""

    compression: str = "zip"

    def to_dict(self):
        return {
            "name": self.name,
            "version": self.version,
            "target": self.target,
            "include_paths": list(
                self.include_paths
            ),
            "output_path": (
                self.output_path
            ),
            "compression": (
                self.compression
            ),
        }
