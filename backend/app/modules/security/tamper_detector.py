from app.modules.security.integrity_manifest import (
    IntegrityManifest,
)
from app.modules.security.integrity_manifest_service import (
    integrity_manifest_service,
)
from app.modules.security.tamper_event import (
    TamperEvent,
)


class TamperDetector:

    def inspect(
        self,
        manifest: IntegrityManifest,
    ):
        result = (
            integrity_manifest_service
            .verify(
                manifest
            )
        )

        if result["valid"]:
            return {
                "tampered": False,
                "event": None,
                "integrity": result,
            }

        event = TamperEvent(
            event_type=(
                "file_integrity_mismatch"
            ),
            target="uap",
            details={
                "integrity": result,
            },
        )

        return {
            "tampered": True,
            "event": event.to_dict(),
            "integrity": result,
        }


tamper_detector = (
    TamperDetector()
)
