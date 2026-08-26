from dataclasses import dataclass
from typing import Any


@dataclass
class AutomationCondition:

    type: str
    value: Any = None
    operator: str = "=="

    def evaluate(
        self,
        context: dict[str, Any],
    ) -> bool:

        actual = context.get(
            self.type
        )

        if self.operator == "==":
            return actual == self.value

        if self.operator == "!=":
            return actual != self.value

        if self.operator == ">":
            return actual > self.value

        if self.operator == ">=":
            return actual >= self.value

        if self.operator == "<":
            return actual < self.value

        if self.operator == "<=":
            return actual <= self.value

        return False

    def to_dict(self):

        return {
            "type": self.type,
            "value": self.value,
            "operator": self.operator,
        }
