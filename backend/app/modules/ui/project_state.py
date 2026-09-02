from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIProjectState:
    project_id: str

    app_id: str | None = None

    active_screen_id: (
        str | None
    ) = None

    selected_theme_id: (
        str | None
    ) = None

    variables: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def set_variable(
        self,
        key: str,
        value: Any,
    ):
        self.variables[key] = value

        return value

    def get_variable(
        self,
        key: str,
        default: Any = None,
    ):
        return self.variables.get(
            key,
            default,
        )

    def to_dict(self):
        return {
            "project_id": (
                self.project_id
            ),
            "app_id": self.app_id,
            "active_screen_id": (
                self.active_screen_id
            ),
            "selected_theme_id": (
                self.selected_theme_id
            ),
            "variables": dict(
                self.variables
            ),
            "metadata": dict(
                self.metadata
            ),
        }
