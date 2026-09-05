from dataclasses import dataclass
from typing import Any


@dataclass
class CommunicationProviderHealth:
    name: str

    available: bool

    state: str

    details: dict[str, Any]

    def to_dict(self):
        return {
            "name": self.name,
            "available": self.available,
            "state": self.state,
            "details": dict(
                self.details
            ),
        }
