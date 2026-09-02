from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIRenderContext:
    width: float = 1280
    height: float = 720

    device_type: str = "desktop"

    scale: float = 1.0

    preview: bool = False

    variables: dict[
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

    def to_dict(self):
        return {
            "width": self.width,
            "height": self.height,
            "device_type": (
                self.device_type
            ),
            "scale": self.scale,
            "preview": self.preview,
            "variables": dict(
                self.variables
            ),
        }
