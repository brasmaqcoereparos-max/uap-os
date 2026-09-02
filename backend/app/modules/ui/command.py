from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Callable


@dataclass
class UICommand:
    id: str
    name: str

    handler: Callable[
        [dict[str, Any]],
        Any,
    ]

    description: str = ""

    enabled: bool = True

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def execute(
        self,
        parameters: (
            dict[str, Any] | None
        ) = None,
    ):
        if not self.enabled:
            raise RuntimeError(
                "Command disabled: "
                f"{self.id}"
            )

        return self.handler(
            dict(parameters or {})
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": (
                self.description
            ),
            "enabled": self.enabled,
            "metadata": dict(
                self.metadata
            ),
  }
