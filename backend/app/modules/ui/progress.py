from dataclasses import dataclass


@dataclass
class UIProgress:
    id: str
    name: str

    value: float = 0

    minimum: float = 0
    maximum: float = 100

    label: str = ""

    def set_value(
        self,
        value: float,
    ):
        self.value = max(
            self.minimum,
            min(
                self.maximum,
                float(value),
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
            "label": self.label,
            "percentage": (
                self.percentage()
            ),
        }
