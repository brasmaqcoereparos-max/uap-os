from dataclasses import dataclass


@dataclass
class FileIntegrityRecord:
    path: str

    sha256: str

    size: int

    def to_dict(self):
        return {
            "path": self.path,
            "sha256": self.sha256,
            "size": self.size,
        }
