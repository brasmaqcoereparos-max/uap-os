import sys

from app.modules.deployment.requirement_check import (
    DeploymentRequirementCheck,
)


class DeploymentPythonCheck:

    def check(
        self,
        minimum_major: int,
        minimum_minor: int,
    ):
        current = (
            sys.version_info
        )

        passed = (
            current.major
            > minimum_major
            or (
                current.major
                == minimum_major
                and current.minor
                >= minimum_minor
            )
        )

        return (
            DeploymentRequirementCheck(
                name="python",
                passed=passed,
                message=(
                    "Python version OK"
                    if passed
                    else (
                        "Python version "
                        "is too old"
                    )
                ),
                details={
                    "current": (
                        f"{current.major}."
                        f"{current.minor}."
                        f"{current.micro}"
                    ),
                    "minimum": (
                        f"{minimum_major}."
                        f"{minimum_minor}"
                    ),
                },
            )
        )


deployment_python_check = (
    DeploymentPythonCheck()
)
