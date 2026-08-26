from dataclasses import dataclass
from typing import Any


@dataclass
class DecisionAction:

    name: str
    action: str
    data: Any = None
    enabled: bool = True

    def to_dict(self):

        return {
            "name": self.name,
            "action": self.action,
            "data": self.data,
            "enabled": self.enabled,
        }
