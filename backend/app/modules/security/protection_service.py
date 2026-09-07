from app.modules.security.config_guard import (
    security_config_guard,
)
from app.modules.security.integrity_manifest_service import (
    integrity_manifest_service,
)
from app.modules.security.tamper_detector import (
    tamper_detector,
)


class SecurityProtectionService:

    def sanitize_config(
        self,
        config: dict,
    ):
        return (
            security_config_guard
            .sanitize(
                config
            )
        )

    def build_manifest(
        self,
        paths: list[str],
    ):
        manifest = (
            integrity_manifest_service
            .build(
                paths
            )
        )

        return manifest.to_dict()

    def verify_manifest(
        self,
        manifest,
    ):
        return (
            tamper_detector
            .inspect(
                manifest
            )
        )


security_protection_service = (
    SecurityProtectionService()
)
