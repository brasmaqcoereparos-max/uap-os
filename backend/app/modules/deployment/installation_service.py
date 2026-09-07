from app.modules.deployment.box_bootstrap_service import (
    uap_box_bootstrap_service,
)
from app.modules.deployment.installation_planner import (
    deployment_installation_planner,
)


class DeploymentInstallationService:

    def plan(
        self,
        target: str,
        root_path: str = ".uap",
    ):
        plan = (
            deployment_installation_planner
            .create(
                target=target,
                root_path=root_path,
            )
        )

        return plan.to_dict()

    def install(
        self,
        target: str,
        root_path: str = ".uap",
    ):
        return (
            uap_box_bootstrap_service
            .bootstrap(
                target=target,
                root_path=root_path,
            )
        )


deployment_installation_service = (
    DeploymentInstallationService()
)
