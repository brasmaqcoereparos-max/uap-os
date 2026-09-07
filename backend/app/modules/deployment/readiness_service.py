from app.modules.deployment.dependency_check import (
    deployment_dependency_check,
)
from app.modules.deployment.disk_check import (
    deployment_disk_check,
)
from app.modules.deployment.platform_check import (
    deployment_platform_check,
)
from app.modules.deployment.python_check import (
    deployment_python_check,
)
from app.modules.deployment.readiness_result import (
    DeploymentReadinessResult,
)
from app.modules.deployment.resource_check import (
    deployment_resource_check,
)
from app.modules.deployment.system_requirements import (
    deployment_system_requirements,
)


class DeploymentReadinessService:

    def check(
        self,
        target: str,
        root_path: str = ".uap",
    ):
        requirements = (
            deployment_system_requirements
        )

        checks = [
            deployment_python_check.check(
                minimum_major=(
                    requirements
                    .minimum_python_major
                ),
                minimum_minor=(
                    requirements
                    .minimum_python_minor
                ),
            ),
            deployment_platform_check.check(
                require_linux=(
                    requirements
                    .require_linux
                ),
            ),
            deployment_resource_check.cpu(
                minimum_cpu_count=(
                    requirements
                    .minimum_cpu_count
                ),
                target=target,
            ),
            deployment_resource_check.memory(
                minimum_memory_mb=(
                    requirements
                    .minimum_memory_mb
                ),
                target=target,
            ),
            deployment_disk_check.check(
                path=root_path,
                minimum_mb=(
                    requirements
                    .minimum_disk_mb
                ),
            ),
        ]

        checks.extend(
            deployment_dependency_check
            .check_many(
                [
                    (
                        "fastapi",
                        True,
                    ),
                    (
                        "pydantic",
                        True,
                    ),
                    (
                        "sqlalchemy",
                        True,
                    ),
                    (
                        "httpx",
                        False,
                    ),
                    (
                        "serial",
                        False,
                    ),
                    (
                        "paho.mqtt.client",
                        False,
                    ),
                ]
            )
        )

        ready = not any(
            check.required
            and not check.passed
            for check in checks
        )

        return (
            DeploymentReadinessResult(
                ready=ready,
                checks=checks,
            )
        )


deployment_readiness_service = (
    DeploymentReadinessService()
      )
