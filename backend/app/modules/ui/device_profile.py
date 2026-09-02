from dataclasses import dataclass


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
