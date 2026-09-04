from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Callable


@dataclass
class CommunicationSubscriber:
    id: str

    handler: Callable[
        [dict[str, Any]],
        Any,
    ]

    enabled: bool = True

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def handle(
        self,
        message: dict[
            str,
            Any,
        ],
    ):
        if not self.enabled:
            return None

        return self.handler(
            message
        )

    def to_dict(self):
        return {
            "id": self.id,
            "enabled": self.enabled,
            "metadata": dict(
                self.metadata
            ),
        }
