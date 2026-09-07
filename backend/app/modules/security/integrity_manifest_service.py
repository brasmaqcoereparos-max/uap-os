from app.modules.security.file_integrity_service import (
    file_integrity_service,
)
from app.modules.security.integrity_manifest import (
    IntegrityManifest,
)


class IntegrityManifestService:

    def build(
        self,
        paths: list[str],
    ):
        manifest = (
            IntegrityManifest()
        )

        for path in paths:
            record = (
                file_integrity_service
                .calculate(
                    path
                )
            )

            manifest.add(
                record
            )

        return manifest

    def verify(
        self,
        manifest: IntegrityManifest,
    ):
        results = []

        valid = True

        for record in manifest.files:
            result = (
                file_integrity_service
                .verify(
                    path=record.path,
                    expected_sha256=(
                        record.sha256
                    ),
                )
            )

            results.append(
                result
            )

            if not result[
                "valid"
            ]:
                valid = False

        return {
            "valid": valid,
            "files": results,
        }


integrity_manifest_service = (
    IntegrityManifestService()
)
