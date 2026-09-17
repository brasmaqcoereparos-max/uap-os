from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any


VALID_PROJECT_UI_LEVELS = {
    "beginner",
    "intermediate",
    "professional",
}


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

    preview_profile_id: str = (
        "desktop"
    )

    user_level: str = "beginner"

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

    def __post_init__(self) -> None:
        self.set_user_level(
            self.user_level
        )

    def set_app(
        self,
        app_id: str | None,
    ):
        self.app_id = app_id

        return self.app_id

    def set_active_screen(
        self,
        screen_id: str | None,
    ):
        self.active_screen_id = (
            screen_id
        )

        return self.active_screen_id

    def set_theme(
        self,
        theme_id: str | None,
    ):
        self.selected_theme_id = (
            theme_id
        )

        return self.selected_theme_id

    def set_preview_profile(
        self,
        profile_id: str,
    ):
        if not profile_id:
            raise ValueError(
                "profile_id cannot be empty"
            )

        self.preview_profile_id = str(
            profile_id
        )

        return self.preview_profile_id

    def set_user_level(
        self,
        level: str,
    ):
        normalized = str(
            level
        ).strip().lower()

        if (
            normalized
            not in VALID_PROJECT_UI_LEVELS
        ):
            raise ValueError(
                "Unsupported project UI level: "
                f"{level}"
            )

        self.user_level = normalized

        return self.user_level

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

    def remove_variable(
        self,
        key: str,
    ):
        return self.variables.pop(
            key,
            None,
        )

    def clear_variables(self) -> None:
        self.variables.clear()

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
            "preview_profile_id": (
                self.preview_profile_id
            ),
            "user_level": (
                self.user_level
            ),
            "variables": dict(
                self.variables
            ),
            "metadata": dict(
                self.metadata
            ),
        }
