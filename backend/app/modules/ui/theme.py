from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UITheme:
    id: str
    name: str

    mode: str = "light"

    primary_color: str = "#2563EB"
    secondary_color: str = "#64748B"

    background_color: str = "#FFFFFF"
    surface_color: str = "#F8FAFC"

    text_color: str = "#0F172A"
    muted_text_color: str = "#64748B"

    success_color: str = "#16A34A"
    warning_color: str = "#D97706"
    error_color: str = "#DC2626"

    border_radius: int = 8

    font_family: str = "sans-serif"

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "mode": self.mode,
            "primary_color": self.primary_color,
            "secondary_color": self.secondary_color,
            "background_color": self.background_color,
            "surface_color": self.surface_color,
            "text_color": self.text_color,
            "muted_text_color": (
                self.muted_text_color
            ),
            "success_color": self.success_color,
            "warning_color": self.warning_color,
            "error_color": self.error_color,
            "border_radius": self.border_radius,
            "font_family": self.font_family,
            "metadata": dict(self.metadata),
        }
