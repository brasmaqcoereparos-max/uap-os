from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AISafeResult:
    accepted: bool

    status: str

    data: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    safety: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    errors: list[str] = field(
        default_factory=list
    )

    def to_dict(self):
        return {
            "accepted": (
                self.accepted
            ),
            "status": self.status,
            "data": dict(
                self.data
            ),
            "safety": dict(
                self.safety
            ),
            "errors": list(
                self.errors
            ),
        }
