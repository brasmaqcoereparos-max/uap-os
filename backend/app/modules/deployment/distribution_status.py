from app.modules.deployment.deployment_status import (
    deployment_status,
)


class DeploymentDistributionStatus:

    def snapshot(self):
        return {
            "service": "deployment-distribution",
            "healthy": True,
            "deployment": (
                deployment_status
                .snapshot()
            ),
        }


deployment_distribution_status = (
    DeploymentDistributionStatus()
)
