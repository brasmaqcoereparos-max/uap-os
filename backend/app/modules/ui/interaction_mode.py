from __future__ import annotations

from dataclasses import dataclass


VALID_UI_LEVELS = {
    "beginner",
    "intermediate",
    "professional",
}


@dataclass
class UIInteractionMode:
    name: str = "select"

    allow_selection: bool = True
    allow_move: bool = True
    allow_resize: bool = True

    allow_pan: bool = True
    allow_zoom: bool = True

    readonly: bool = False

    user_level: str = "beginner"

    show_advanced_properties: bool = False
    show_hardware_details: bool = False
    show_code_details: bool = False

    def __post_init__(self) -> None:
        self.set_user_level(
            self.user_level
        )

    def can_edit(self) -> bool:
        return not self.readonly

    def set_user_level(
        self,
        level: str,
    ) -> str:
        normalized = str(
            level
        ).strip().lower()

        if normalized not in VALID_UI_LEVELS:
            raise ValueError(
                f"Unsupported UI level: {level}"
            )

        self.user_level = normalized

        if normalized == "beginner":
            self.show_advanced_properties = False
            self.show_hardware_details = False
            self.show_code_details = False

        elif normalized == "intermediate":
            self.show_advanced_properties = True
            self.show_hardware_details = False
            self.show_code_details = False

        else:
            self.show_advanced_properties = True
            self.show_hardware_details = True
            self.show_code_details = True

        return self.user_level

    def is_beginner(self) -> bool:
        return self.user_level == "beginner"

    def is_intermediate(self) -> bool:
        return (
            self.user_level
            == "intermediate"
        )

    def is_professional(self) -> bool:
        return (
            self.user_level
            == "professional"
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "allow_selection": (
                self.allow_selection
            ),
            "allow_move": (
                self.allow_move
            ),
            "allow_resize": (
                self.allow_resize
            ),
            "allow_pan": (
                self.allow_pan
            ),
            "allow_zoom": (
                self.allow_zoom
            ),
            "readonly": (
                self.readonly
            ),
            "user_level": (
                self.user_level
            ),
            "show_advanced_properties": (
                self.show_advanced_properties
            ),
            "show_hardware_details": (
                self.show_hardware_details
            ),
            "show_code_details": (
                self.show_code_details
            ),
        }
