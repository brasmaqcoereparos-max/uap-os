from dataclasses import dataclass, field
from typing import Any


@dataclass
class AutomationFlow:

    name: str

    conditions: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    actions: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    enabled: bool = True

    def to_dict(self):

        return {
            "name": self.name,
            "conditions": list(
                self.conditions
            ),
            "actions": list(
                self.actions
            ),
            "enabled": self.enabled,
        }
