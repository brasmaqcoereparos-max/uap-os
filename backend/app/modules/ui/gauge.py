from dataclasses import dataclass
from typing import Any


@dataclass
class UIGauge:
    id: str
    name: str

    value: float = 0

    minimum: float = 0
    maximum: float = 100

    unit: str = ""

    label: str = ""

    def set_value(
        self,
        value: Any,
    ):
        numeric = float(value)

        self.value = max(
            self.minimum,
            min(
                self.maximum,
                numeric,
            ),
        )

        return self.value

    def percentage(self):
        span = (
            self.maximum
            - self.minimum
        )

        if span <= 0:
            return 0.0

        return (
            (
                self.value
                - self.minimum
            )
            / span
        ) * 100

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "minimum": self.minimum,
            "maximum": self.maximum,
            "unit": self.unit,
            "label": self.label,
            "percentage": (
                self.percentage()
            ),
  }
