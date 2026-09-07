from app.modules.deployment.deployment_status import (
    deployment_status,
)
from app.modules.deployment.preflight_service import (
    deployment_preflight_service,
)
from app.modules.deployment.version_registry import (
    deployment_version_registry,
)


class DeploymentFinalStatus:

    def snapshot(
        self,
        target: str = "uap-box",
        root_path: str = ".uap",
    ):
        status = (
            deployment_status
            .snapshot()
        )

        preflight = (
            deployment_preflight_service
            .run(
                target=target,
                root_path=root_path,
            )
        )

        current = (
            deployment_version_registry
            .current()
        )

        return {
            "status": status,
            "preflight": preflight,
            "current_version": (
                current.to_dict()
                if current
                else None
            ),
            "block": {
                "name": "deployment",
                "ready": (
                    preflight[
                        "readiness"
                    ][
                        "ready"
                    ]
                ),
            },
        }


deployment_final_status = (
    DeploymentFinalStatus()
)
