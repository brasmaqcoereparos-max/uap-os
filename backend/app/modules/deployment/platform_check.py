import platform

from app.modules.deployment.requirement_check import (
    DeploymentRequirementCheck,
)


class DeploymentPlatformCheck:

    def check(
        self,
        require_linux: bool = True,
    ):
        system = (
            platform.system()
        )

        passed = True

        if require_linux:
            passed = (
                system.lower()
                == "linux"
            )

        return (
            DeploymentRequirementCheck(
                name="platform",
                passed=passed,
                message=(
                    "Platform OK"
                    if passed
                    else (
                        "Linux platform "
                        "required"
                    )
                ),
                details={
                    "system": system,
                    "machine": (
                        platform.machine()
                    ),
                    "release": (
                        platform.release()
                    ),
                },
            )
        )


deployment_platform_check = (
    DeploymentPlatformCheck()
      )
