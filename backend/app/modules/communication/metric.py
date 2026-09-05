from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class CommunicationMetric:
    name: str

    value: float = 0.0

    labels: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def increment(
        self,
        amount: float = 1.0,
    ):
        self.value += amount

        return self.value

    def set(
        self,
        value: float,
    ):
        self.value = value

        return self.value

    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value,
            "labels": dict(
                self.labels
            ),
        }
