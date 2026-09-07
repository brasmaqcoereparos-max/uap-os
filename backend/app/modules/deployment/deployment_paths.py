from dataclasses import dataclass
from pathlib import Path


@dataclass
class DeploymentPaths:
    root: Path

    config: Path

    data: Path

    logs: Path

    cache: Path

    runtime: Path

    backups: Path

    def to_dict(self):
        return {
            "root": str(
                self.root
            ),
            "config": str(
                self.config
            ),
            "data": str(
                self.data
            ),
            "logs": str(
                self.logs
            ),
            "cache": str(
                self.cache
            ),
            "runtime": str(
                self.runtime
            ),
            "backups": str(
                self.backups
            ),
        }
