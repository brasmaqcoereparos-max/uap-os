import os

from app.modules.deployment.deployment_mode import (
    DeploymentMode,
)
from app.modules.deployment.environment_profile import (
    DeploymentEnvironmentProfile,
)


class DeploymentEnvironmentService:

    def load(self):
        raw_mode = (
            os.getenv(
                "UAP_DEPLOYMENT_MODE",
                DeploymentMode
                .DEVELOPMENT
                .value,
            )
        )

        try:
            mode = (
                DeploymentMode(
                    raw_mode
                )
            )

        except ValueError:
            mode = (
                DeploymentMode
                .DEVELOPMENT
            )

        debug = (
            os.getenv(
                "UAP_DEBUG",
                "false",
            )
            .strip()
            .lower()
            in {
                "1",
                "true",
                "yes",
                "on",
            }
        )

        safe_mode = (
            os.getenv(
                "UAP_SAFE_MODE",
                "true",
            )
            .strip()
            .lower()
            not in {
                "0",
                "false",
                "no",
                "off",
            }
        )

        return (
            DeploymentEnvironmentProfile(
                mode=mode.value,
                debug=debug,
                safe_mode=safe_mode,
            )
        )


deployment_environment_service = (
    DeploymentEnvironmentService()
)
