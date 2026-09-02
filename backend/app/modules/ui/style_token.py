from dataclasses import dataclass
from typing import Any


@dataclass
class UIStyleToken:
    name: str
    value: Any

    category: str = "general"

    description: str = ""

    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value,
            "category": self.category,
            "description": (
                self.description
            ),
        }
