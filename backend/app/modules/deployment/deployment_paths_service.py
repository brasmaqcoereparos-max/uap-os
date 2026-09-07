from pathlib import Path

from app.modules.deployment.deployment_paths import (
    DeploymentPaths,
)


class DeploymentPathsService:

    def build(
        self,
        root: str = ".uap",
    ):
        base = Path(
            root
        )

        return DeploymentPaths(
            root=base,
            config=(
                base / "config"
            ),
            data=(
                base / "data"
            ),
            logs=(
                base / "logs"
            ),
            cache=(
                base / "cache"
            ),
            runtime=(
                base / "runtime"
            ),
            backups=(
                base / "backups"
            ),
        )

    def ensure(
        self,
        paths: DeploymentPaths,
    ):
        for path in [
            paths.root,
            paths.config,
            paths.data,
            paths.logs,
            paths.cache,
            paths.runtime,
            paths.backups,
        ]:
            path.mkdir(
                parents=True,
                exist_ok=True,
            )

        return paths


deployment_paths_service = (
    DeploymentPathsService()
          )
