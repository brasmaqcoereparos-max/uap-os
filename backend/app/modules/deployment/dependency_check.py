import importlib.util

from app.modules.deployment.requirement_check import (
    DeploymentRequirementCheck,
)


class DeploymentDependencyCheck:

    def check(
        self,
        module_name: str,
        required: bool = True,
    ):
        available = (
            importlib.util
            .find_spec(
                module_name
            )
            is not None
        )

        passed = (
            available
            or not required
        )

        return (
            DeploymentRequirementCheck(
                name=(
                    f"dependency:"
                    f"{module_name}"
                ),
                passed=passed,
                required=required,
                message=(
                    "Dependency available"
                    if available
                    else (
                        "Dependency "
                        "not installed"
                    )
                ),
                details={
                    "module": (
                        module_name
                    ),
                    "available": (
                        available
                    ),
                },
            )
        )

    def check_many(
        self,
        dependencies: (
            list[
                tuple[str, bool]
            ]
        ),
    ):
        return [
            self.check(
                module_name=name,
                required=required,
            )
            for (
                name,
                required
            )
            in dependencies
        ]


deployment_dependency_check = (
    DeploymentDependencyCheck()
      )
