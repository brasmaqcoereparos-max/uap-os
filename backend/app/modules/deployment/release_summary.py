from app.modules.deployment.deployment_summary import (
    deployment_summary,
)
from app.modules.deployment.version_registry import (
    deployment_version_registry,
)


class DeploymentReleaseSummary:

    def snapshot(self):
        current = (
            deployment_version_registry
            .current()
        )

        return {
            "deployment": (
                deployment_summary
                .snapshot()
            ),
            "release": {
                "current_version": (
                    current.to_dict()
                    if current
                    else None
                ),
                "package_enabled": True,
                "distribution_enabled": True,
                "image_preparation_enabled": True,
            },
        }


deployment_release_summary = (
    DeploymentReleaseSummary()
)
