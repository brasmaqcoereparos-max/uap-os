from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIState:
    values: dict[str, Any] = field(
        default_factory=dict
    )

    def set(
        self,
        key: str,
        value: Any,
    ):
        self.values[key] = value
        return value

    def get(
        self,
        key: str,
        default: Any = None,
    ):
        return self.values.get(
            key,
            default,
        )

    def remove(
        self,
        key: str,
    ):
        return self.values.pop(
            key,
            None,
        )

    def clear(self):
        self.values.clear()

    def update(
        self,
        values: dict[str, Any],
    ):
        self.values.update(values)

        return dict(self.values)

    def snapshot(self):
        return dict(self.values)


ui_state = UIState()
