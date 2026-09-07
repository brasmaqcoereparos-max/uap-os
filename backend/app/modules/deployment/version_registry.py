from app.modules.deployment.deployment_version import (
    DeploymentVersion,
)


class DeploymentVersionRegistry:

    def __init__(self):
        self._versions: list[
            DeploymentVersion
        ] = []

    def register(
        self,
        version: DeploymentVersion,
    ):
        self._versions.append(
            version
        )

        return version

    def current(self):
        if not self._versions:
            return None

        return self._versions[-1]

    def previous(self):
        if len(self._versions) < 2:
            return None

        return self._versions[-2]

    def list_all(self):
        return list(
            self._versions
        )


deployment_version_registry = (
    DeploymentVersionRegistry()
)
