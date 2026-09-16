from __future__ import annotations

from dataclasses import dataclass


VALID_ORIENTATIONS = {
    "portrait",
    "landscape",
}


@dataclass
class UIDeviceProfile:
    id: str
    name: str

    width: int
    height: int

    device_type: str = "custom"

    pixel_ratio: float = 1.0

    touch: bool = False

    orientation: str = "landscape"

    def __post_init__(self) -> None:
        self.width = max(
            1,
            int(self.width),
        )

        self.height = max(
            1,
            int(self.height),
        )

        self.pixel_ratio = max(
            0.1,
            float(self.pixel_ratio),
        )

        if (
            self.orientation
            not in VALID_ORIENTATIONS
        ):
            raise ValueError(
                "Unsupported orientation: "
                f"{self.orientation}"
            )

    def rotate(self):
        self.width, self.height = (
            self.height,
            self.width,
        )

        if (
            self.orientation
            == "landscape"
        ):
            self.orientation = "portrait"
        else:
            self.orientation = (
                "landscape"
            )

        return self

    def logical_width(self) -> float:
        return (
            self.width
            / self.pixel_ratio
        )

    def logical_height(self) -> float:
        return (
            self.height
            / self.pixel_ratio
        )

    def is_touch(self) -> bool:
        return self.touch

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "width": self.width,
            "height": self.height,
            "device_type": (
                self.device_type
            ),
            "pixel_ratio": (
                self.pixel_ratio
            ),
            "touch": self.touch,
            "orientation": (
                self.orientation
            ),
        }
