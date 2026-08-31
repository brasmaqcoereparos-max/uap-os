from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIFormField:
    id: str
    name: str

    field_type: str = "text"

    label: str = ""
    placeholder: str = ""

    value: Any = None
    default_value: Any = None

    required: bool = False
    disabled: bool = False
    readonly: bool = False

    options: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def reset(self):
        self.value = self.default_value

        return self.value

    def set_value(
        self,
        value: Any,
    ):
        self.value = value

        return self.value

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "field_type": self.field_type,
            "label": self.label,
            "placeholder": (
                self.placeholder
            ),
            "value": self.value,
            "default_value": (
                self.default_value
            ),
            "required": self.required,
            "disabled": self.disabled,
            "readonly": self.readonly,
            "options": [
                dict(option)
                for option in self.options
            ],
            "metadata": dict(
                self.metadata
            ),
  }
