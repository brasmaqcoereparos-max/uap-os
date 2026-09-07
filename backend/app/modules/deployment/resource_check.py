import os

from app.modules.deployment.device_profile_service import (
    deployment_device_profile_service,
)
from app.modules.deployment.requirement_check import (
    DeploymentRequirementCheck,
)


class DeploymentResourceCheck:

    def cpu(
        self,
        minimum_cpu_count: int,
        target: str,
    ):
        cpu_count = (
            os.cpu_count()
            or 0
        )

        return (
            DeploymentRequirementCheck(
                name="cpu",
                passed=(
                    cpu_count
                    >= minimum_cpu_count
                ),
                message=(
                    "CPU capacity OK"
                    if (
                        cpu_count
                        >= minimum_cpu_count
                    )
                    else (
                        "Insufficient "
                        "CPU capacity"
                    )
                ),
                details={
                    "cpu_count": (
                        cpu_count
                    ),
                    "minimum": (
                        minimum_cpu_count
                    ),
                },
            )
        )

    def memory(
        self,
        minimum_memory_mb: int,
        target: str,
    ):
        profile = (
            deployment_device_profile_service
            .detect(
                target
            )
        )

        memory_mb = (
            profile.memory_mb
        )

        passed = (
            memory_mb == 0
            or memory_mb
            >= minimum_memory_mb
        )

        return (
            DeploymentRequirementCheck(
                name="memory",
                passed=passed,
                message=(
                    "Memory capacity OK"
                    if passed
                    else (
                        "Insufficient "
                        "memory"
                    )
                ),
                details={
                    "memory_mb": (
                        memory_mb
                    ),
                    "minimum_mb": (
                        minimum_memory_mb
                    ),
                },
            )
        )


deployment_resource_check = (
    DeploymentResourceCheck()
    )
