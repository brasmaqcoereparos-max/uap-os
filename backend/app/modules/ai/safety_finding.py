from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AISafetyFinding:
    code: str
    message: str

    level: str = "warning"

    path: str | None = None

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "level": self.level,
            "path": self.path,
            "metadata": dict(
                self.metadata
            ),
        }
