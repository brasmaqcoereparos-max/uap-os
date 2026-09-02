from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIEditorOperation:
    operation_type: str

    screen_id: str

    target_ids: list[str] = field(
        default_factory=list
    )

    parameters: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "operation_type": (
                self.operation_type
            ),
            "screen_id": (
                self.screen_id
            ),
            "target_ids": list(
                self.target_ids
            ),
            "parameters": dict(
                self.parameters
            ),
        }
