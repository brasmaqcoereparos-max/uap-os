from app.modules.deployment.environment_service import (
    deployment_environment_service,
)
from app.modules.deployment.version_registry import (
    deployment_version_registry,
)


class DeploymentStatus:

    def snapshot(self):
        environment = (
            deployment_environment_service
            .load()
        )

        current = (
            deployment_version_registry
            .current()
        )

        return {
            "service": "deployment",
            "healthy": True,
            "environment": (
                environment.to_dict()
            ),
            "current_version": (
                current.to_dict()
                if current
                else None
            ),
        }


deployment_status = (
    DeploymentStatus()
)
