from app.modules.deployment.deployment_paths_service import (
    deployment_paths_service,
)
from app.modules.deployment.device_profile_service import (
    deployment_device_profile_service,
)
from app.modules.deployment.environment_service import (
    deployment_environment_service,
)
from app.modules.deployment.installation_identity_service import (
    installation_identity_service,
)
from app.modules.deployment.readiness_service import (
    deployment_readiness_service,
)


class DeploymentPreflightService:

    def run(
        self,
        target: str,
        root_path: str = ".uap",
    ):
        environment = (
            deployment_environment_service
            .load()
        )

        profile = (
            deployment_device_profile_service
            .detect(
                target
            )
        )

        identity = (
            installation_identity_service
            .generate(
                target
            )
        )

        paths = (
            deployment_paths_service
            .build(
                root=root_path
            )
        )

        readiness = (
            deployment_readiness_service
            .check(
                target=target,
                root_path=root_path,
            )
        )

        return {
            "environment": (
                environment.to_dict()
            ),
            "profile": (
                profile.to_dict()
            ),
            "identity": (
                identity.to_dict()
            ),
            "paths": (
                paths.to_dict()
            ),
            "readiness": (
                readiness.to_dict()
            ),
        }


deployment_preflight_service = (
    DeploymentPreflightService()
      )
