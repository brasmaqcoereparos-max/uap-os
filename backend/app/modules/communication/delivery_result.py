from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class CommunicationDeliveryResult:
    delivered: bool

    topic: str

    recipients: list[str] = field(
        default_factory=list
    )

    results: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    errors: dict[
        str,
        str,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "delivered": self.delivered,
            "topic": self.topic,
            "recipients": list(
                self.recipients
            ),
            "results": dict(
                self.results
            ),
            "errors": dict(
                self.errors
            ),
        }
