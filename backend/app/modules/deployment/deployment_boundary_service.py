from app.modules.deployment.preflight_service import (
    deployment_preflight_service,
)
from app.modules.deployment.release_service import (
    deployment_release_service,
)


class DeploymentBoundaryService:

    def check_installation(
        self,
        target: str,
        root_path: str = ".uap",
    ):
        preflight = (
            deployment_preflight_service
            .run(
                target=target,
                root_path=root_path,
            )
        )

        return {
            "allowed": (
                preflight[
                    "readiness"
                ][
                    "ready"
                ]
            ),
            "preflight": preflight,
        }

    def check_release(
        self,
        **kwargs,
    ):
        result = (
            deployment_release_service
            .prepare_release(
                **kwargs
            )
        )

        return {
            "allowed": (
                result["ready"]
            ),
            "release": result,
        }


deployment_boundary_service = (
    DeploymentBoundaryService()
      )
