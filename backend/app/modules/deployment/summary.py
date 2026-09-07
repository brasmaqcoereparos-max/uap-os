from app.modules.deployment.deployment_status import (
    deployment_status,
)
from app.modules.deployment.version_registry import (
    deployment_version_registry,
)


class DeploymentSummary:

    def snapshot(self):
        current = (
            deployment_version_registry
            .current()
        )

        return {
            "service": "deployment",
            "healthy": True,
            "current_version": (
                current.to_dict()
                if current
                else None
            ),
            "versions": [
                version.to_dict()
                for version
                in deployment_version_registry
                .list_all()
            ],
            "status": (
                deployment_status
                .snapshot()
            ),
        }


deployment_summary = (
    DeploymentSummary()
)
