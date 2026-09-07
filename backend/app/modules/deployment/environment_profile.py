from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class DeploymentEnvironmentProfile:
    mode: str

    debug: bool = False

    safe_mode: bool = True

    settings: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "mode": self.mode,
            "debug": self.debug,
            "safe_mode": (
                self.safe_mode
            ),
            "settings": dict(
                self.settings
            ),
        }
