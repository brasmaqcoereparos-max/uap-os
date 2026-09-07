import hashlib
from pathlib import Path

from app.modules.security.file_integrity_record import (
    FileIntegrityRecord,
)


class FileIntegrityService:

    def calculate(
        self,
        path: str,
    ):
        file_path = Path(
            path
        )

        if not file_path.exists():
            raise FileNotFoundError(
                path
            )

        data = (
            file_path.read_bytes()
        )

        digest = (
            hashlib.sha256(
                data
            )
            .hexdigest()
        )

        return FileIntegrityRecord(
            path=str(
                file_path
            ),
            sha256=digest,
            size=len(data),
        )

    def verify(
        self,
        path: str,
        expected_sha256: str,
    ):
        record = self.calculate(
            path
        )

        return {
            "valid": (
                record.sha256
                == expected_sha256
            ),
            "record": (
                record.to_dict()
            ),
        }


file_integrity_service = (
    FileIntegrityService()
  )
