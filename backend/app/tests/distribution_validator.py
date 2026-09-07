import hashlib
from pathlib import Path

from app.modules.deployment.distribution_manifest import (
    DeploymentDistributionManifest,
)


class DeploymentDistributionValidator:

    def validate(
        self,
        manifest: (
            DeploymentDistributionManifest
        ),
    ):
        package = Path(
            manifest.package_path
        )

        if not package.exists():
            return {
                "valid": False,
                "reason": (
                    "package_not_found"
                ),
            }

        data = (
            package.read_bytes()
        )

        checksum = (
            hashlib.sha256(
                data
            )
            .hexdigest()
        )

        if (
            checksum
            != manifest
            .package_checksum
        ):
            return {
                "valid": False,
                "reason": (
                    "checksum_mismatch"
                ),
            }

        return {
            "valid": True,
            "reason": None,
            "size": len(
                data
            ),
        }


deployment_distribution_validator = (
    DeploymentDistributionValidator()
)
