from dataclasses import dataclass, field
from typing import Any


@dataclass
class VisionConfig:

    enabled: bool = True

    frame_width: int = 640
    frame_height: int = 480

    fps: int = 15

    motion_enabled: bool = True
    object_detection_enabled: bool = True
    person_detection_enabled: bool = True

    detection_confidence: float = 0.5

    extra: dict[str, Any] = field(
        default_factory=dict
    )

    def update(
        self,
        values: dict[str, Any],
    ):

        if not isinstance(
            values,
            dict,
        ):
            raise TypeError(
                "Configuração inválida."
            )

        for key, value in values.items():

            if hasattr(
                self,
                key,
            ):
                setattr(
                    self,
                    key,
                    value,
                )

            else:
                self.extra[key] = value

        return self.to_dict()

    def to_dict(self):

        return {
            "enabled": self.enabled,
            "frame_width": self.frame_width,
            "frame_height": self.frame_height,
            "fps": self.fps,
            "motion_enabled": self.motion_enabled,
            "object_detection_enabled": (
                self.object_detection_enabled
            ),
            "person_detection_enabled": (
                self.person_detection_enabled
            ),
            "detection_confidence": (
                self.detection_confidence
            ),
            "extra": dict(self.extra),
        }


vision_config = VisionConfig()
