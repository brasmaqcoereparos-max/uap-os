from dataclasses import dataclass, field
from typing import Any


@dataclass
class DecisionRule:

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

    mode: str = "all"

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
            "mode": self.mode,
        }
