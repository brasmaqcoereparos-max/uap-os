import shutil
from pathlib import Path

from app.modules.deployment.requirement_check import (
    DeploymentRequirementCheck,
)


class DeploymentDiskCheck:

    def check(
        self,
        path: str,
        minimum_mb: int,
    ):
        target = Path(
            path
        )

        try:
            target.mkdir(
                parents=True,
                exist_ok=True,
            )

            usage = shutil.disk_usage(
                target
            )

            free_mb = int(
                usage.free
                / (
                    1024
                    * 1024
                )
            )

            passed = (
                free_mb
                >= minimum_mb
            )

            return (
                DeploymentRequirementCheck(
                    name="disk",
                    passed=passed,
                    message=(
                        "Disk space OK"
                        if passed
                        else (
                            "Insufficient "
                            "disk space"
                        )
                    ),
                    details={
                        "free_mb": (
                            free_mb
                        ),
                        "minimum_mb": (
                            minimum_mb
                        ),
                        "path": str(
                            target
                        ),
                    },
                )
            )

        except OSError as exc:
            return (
                DeploymentRequirementCheck(
                    name="disk",
                    passed=False,
                    message=str(exc),
                    details={
                        "path": str(
                            target
                        ),
                    },
                )
            )


deployment_disk_check = (
    DeploymentDiskCheck()
          )
