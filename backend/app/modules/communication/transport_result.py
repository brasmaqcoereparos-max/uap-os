from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class CommunicationTransportResult:
    transport: str

    success: bool

    destination: str

    response: Any = None

    error: str | None = None

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "transport": self.transport,
            "success": self.success,
            "destination": (
                self.destination
            ),
            "response": self.response,
            "error": self.error,
            "metadata": dict(
                self.metadata
            ),
        }
