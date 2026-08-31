from dataclasses import dataclass


@dataclass
class UIPoint:
    x: float = 0
    y: float = 0

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
        }


@dataclass
class UISize:
    width: float = 0
    height: float = 0

    def to_dict(self):
        return {
            "width": self.width,
            "height": self.height,
        }


@dataclass
class UIRect:
    x: float = 0
    y: float = 0
    width: float = 0
    height: float = 0

    def contains(
        self,
        point: UIPoint,
    ):
        return (
            self.x <= point.x
            <= self.x + self.width
            and
            self.y <= point.y
            <= self.y + self.height
        )

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
  }
