from app.modules.deployment.deployment_paths_service import (
    deployment_paths_service,
)
from app.modules.deployment.environment_service import (
    deployment_environment_service,
)


class DeploymentRuntimeBootstrap:

    def prepare(
        self,
        root_path: str,
    ):
        paths = (
            deployment_paths_service
            .build(
                root=root_path
            )
        )

        deployment_paths_service.ensure(
            paths
        )

        environment = (
            deployment_environment_service
            .load()
        )

        return {
            "prepared": True,
            "environment": (
                environment.to_dict()
            ),
            "paths": (
                paths.to_dict()
            ),
        }


deployment_runtime_bootstrap = (
    DeploymentRuntimeBootstrap()
)
