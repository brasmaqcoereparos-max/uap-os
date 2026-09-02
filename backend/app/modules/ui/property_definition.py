from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIPropertyDefinition:
    name: str

    value_type: str = "string"

    label: str = ""

    category: str = "general"

    default: Any = None

    editable: bool = True

    required: bool = False

    minimum: float | None = None
    maximum: float | None = None

    options: list[Any] = field(
        default_factory=list
    )

    def to_dict(self):
        return {
            "name": self.name,
            "value_type": (
                self.value_type
            ),
            "label": (
                self.label
                or self.name
            ),
            "category": (
                self.category
            ),
            "default": self.default,
            "editable": self.editable,
            "required": self.required,
            "minimum": self.minimum,
            "maximum": self.maximum,
            "options": list(
                self.options
            ),
        }
