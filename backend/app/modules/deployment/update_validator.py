import hashlib
from pathlib import Path

from app.modules.deployment.update_package import (
    DeploymentUpdatePackage,
)


class DeploymentUpdateValidator:

    def validate(
        self,
        package: DeploymentUpdatePackage,
    ):
        source = Path(
            package.source
        )

        if not source.exists():
            return {
                "valid": False,
                "reason": (
                    "package_not_found"
                ),
            }

        if not package.checksum:
            return {
                "valid": True,
                "reason": None,
            }

        if source.is_file():
            digest = (
                hashlib.sha256(
                    source.read_bytes()
                )
                .hexdigest()
            )

            if digest != package.checksum:
                return {
                    "valid": False,
                    "reason": (
                        "checksum_mismatch"
                    ),
                }

        return {
            "valid": True,
            "reason": None,
        }


deployment_update_validator = (
    DeploymentUpdateValidator()
)
