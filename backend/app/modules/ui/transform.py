from dataclasses import dataclass


@dataclass
class UITransform:
    translate_x: float = 0
    translate_y: float = 0

    scale_x: float = 1
    scale_y: float = 1

    rotation: float = 0

    anchor_x: float = 0.5
    anchor_y: float = 0.5

    def reset(self):
        self.translate_x = 0
        self.translate_y = 0

        self.scale_x = 1
        self.scale_y = 1

        self.rotation = 0

        self.anchor_x = 0.5
        self.anchor_y = 0.5

    def to_dict(self):
        return {
            "translate_x": (
                self.translate_x
            ),
            "translate_y": (
                self.translate_y
            ),
            "scale_x": self.scale_x,
            "scale_y": self.scale_y,
            "rotation": self.rotation,
            "anchor_x": self.anchor_x,
            "anchor_y": self.anchor_y,
        }
