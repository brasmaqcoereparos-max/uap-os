from app.modules.deployment.installation_plan import (
    DeploymentInstallationPlan,
)


class DeploymentInstallationPlanner:

    def create(
        self,
        target: str,
        root_path: str = ".uap",
    ):
        plan = DeploymentInstallationPlan(
            target=target,
            root_path=root_path,
        )

        plan.add_step(
            name="preflight",
            action=(
                "validate_system"
            ),
        )

        plan.add_step(
            name="directories",
            action=(
                "create_directories"
            ),
        )

        plan.add_step(
            name="configuration",
            action=(
                "create_configuration"
            ),
        )

        plan.add_step(
            name="runtime",
            action=(
                "prepare_runtime"
            ),
        )

        plan.add_step(
            name="startup",
            action=(
                "prepare_startup"
            ),
        )

        return plan


deployment_installation_planner = (
    DeploymentInstallationPlanner()
)
