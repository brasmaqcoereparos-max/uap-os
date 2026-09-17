from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any


VALID_PROPERTY_TYPES = {
    "any",
    "string",
    "number",
    "integer",
    "boolean",
    "list",
    "dict",
}


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

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError(
                "Property name cannot be empty"
            )

        self.value_type = str(
            self.value_type
        ).lower()

        if (
            self.value_type
            not in VALID_PROPERTY_TYPES
        ):
            raise ValueError(
                "Unsupported property type: "
                f"{self.value_type}"
            )

        if (
            self.minimum is not None
            and self.maximum is not None
            and self.minimum > self.maximum
        ):
            raise ValueError(
                "minimum cannot be greater "
                "than maximum"
            )

    def coerce(
        self,
        value: Any,
    ) -> Any:
        if value is None:
            if self.required:
                raise ValueError(
                    f"Property '{self.name}' "
                    "is required"
                )

            return None

        if self.value_type == "any":
            result = value

        elif self.value_type == "string":
            result = str(value)

        elif self.value_type == "number":
            if isinstance(
                value,
                bool,
            ):
                raise ValueError(
                    f"Invalid number for "
                    f"'{self.name}'"
                )

            result = float(value)

        elif self.value_type == "integer":
            if isinstance(
                value,
                bool,
            ):
                raise ValueError(
                    f"Invalid integer for "
                    f"'{self.name}'"
                )

            result = int(value)

        elif self.value_type == "boolean":
            if isinstance(
                value,
                str,
            ):
                normalized = (
                    value.strip().lower()
                )

                if normalized in {
                    "true",
                    "1",
                    "yes",
                    "on",
                }:
                    result = True

                elif normalized in {
                    "false",
                    "0",
                    "no",
                    "off",
                }:
                    result = False

                else:
                    raise ValueError(
                        "Invalid boolean for "
                        f"'{self.name}'"
                    )
            else:
                result = bool(value)

        elif self.value_type == "list":
            if not isinstance(
                value,
                list,
            ):
                raise ValueError(
                    f"Property '{self.name}' "
                    "must be a list"
                )

            result = value

        elif self.value_type == "dict":
            if not isinstance(
                value,
                dict,
            ):
                raise ValueError(
                    f"Property '{self.name}' "
                    "must be a dict"
                )

            result = value

        else:
            result = value

        if (
            self.options
            and result not in self.options
        ):
            raise ValueError(
                f"Invalid option for "
                f"'{self.name}': {result}"
            )

        if isinstance(
            result,
            (int, float),
        ) and not isinstance(
            result,
            bool,
        ):
            if (
                self.minimum is not None
                and result < self.minimum
            ):
                result = self.minimum

            if (
                self.maximum is not None
                and result > self.maximum
            ):
                result = self.maximum

        return result

    def validate(
        self,
        value: Any,
    ) -> bool:
        self.coerce(value)
        return True

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
