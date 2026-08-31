from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIAppManifest:
    id: str
    name: str

    version: str = "1.0.0"

    description: str = ""

    start_screen_id: str | None = None

    theme_id: str | None = None

    fullscreen: bool = False

    orientation: str = "responsive"

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "start_screen_id": (
                self.start_screen_id
            ),
            "theme_id": self.theme_id,
            "fullscreen": self.fullscreen,
            "orientation": self.orientation,
            "metadata": dict(self.metadata),
        }
