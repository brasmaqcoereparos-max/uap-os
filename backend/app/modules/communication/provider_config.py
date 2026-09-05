from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class CommunicationProviderConfig:
    name: str

    enabled: bool = True

    settings: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "name": self.name,
            "enabled": self.enabled,
            "settings": dict(
                self.settings
            ),
        }
