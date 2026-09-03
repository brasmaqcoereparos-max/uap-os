from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIStructuredResult:
    result_type: str

    data: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    valid: bool = True

    warnings: list[str] = field(
        default_factory=list
    )

    errors: list[str] = field(
        default_factory=list
    )

    def to_dict(self):
        return {
            "result_type": (
                self.result_type
            ),
            "data": dict(
                self.data
            ),
            "valid": self.valid,
            "warnings": list(
                self.warnings
            ),
            "errors": list(
                self.errors
            ),
        }
