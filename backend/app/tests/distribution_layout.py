from dataclasses import dataclass
from pathlib import Path


@dataclass
class DeploymentDistributionLayout:
    root: Path

    package: Path

    manifest: Path

    checksums: Path

    image: Path

    def to_dict(self):
        return {
            "root": str(
                self.root
            ),
            "package": str(
                self.package
            ),
            "manifest": str(
                self.manifest
            ),
            "checksums": str(
                self.checksums
            ),
            "image": str(
                self.image
            ),
        }
