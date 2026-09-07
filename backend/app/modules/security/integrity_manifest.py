from dataclasses import dataclass
from dataclasses import field

from app.modules.security.file_integrity_record import (
    FileIntegrityRecord,
)


@dataclass
class IntegrityManifest:
    files: list[
        FileIntegrityRecord
    ] = field(
        default_factory=list
    )

    def add(
        self,
        record: FileIntegrityRecord,
    ):
        self.files.append(
            record
        )

        return record

    def to_dict(self):
        return {
            "files": [
                record.to_dict()
                for record
                in self.files
            ]
        }
