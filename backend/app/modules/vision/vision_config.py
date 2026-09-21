from dataclasses import dataclass
from dataclasses import field
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

    ai_enabled: bool = False

    ai_models: list[str] = field(
        default_factory=list
    )

    ai_fail_safe: bool = True

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

        self._normalize()

        return self.to_dict()

    def _normalize(self):

        self.frame_width = max(
            1,
            int(
                self.frame_width
            ),
        )

        self.frame_height = max(
            1,
            int(
                self.frame_height
            ),
        )

        self.fps = max(
            1,
            int(
                self.fps
            ),
        )

        self.detection_confidence = max(
            0.0,
            min(
                1.0,
                float(
                    self.detection_confidence
                ),
            ),
        )

        self.ai_models = [
            str(
                model
            ).strip()
            for model
            in self.ai_models
            if str(
                model
            ).strip()
        ]

    def to_dict(self):

        return {
            "enabled": self.enabled,
            "frame_width": self.frame_width,
            "frame_height": (
                self.frame_height
            ),
            "fps": self.fps,
            "motion_enabled": (
                self.motion_enabled
            ),
            "object_detection_enabled": (
                self.object_detection_enabled
            ),
            "person_detection_enabled": (
                self.person_detection_enabled
            ),
            "ai_enabled": (
                self.ai_enabled
            ),
            "ai_models": list(
                self.ai_models
            ),
            "ai_fail_safe": (
                self.ai_fail_safe
            ),
            "detection_confidence": (
                self.detection_confidence
            ),
            "extra": dict(
                self.extra
            ),
        }


vision_config = VisionConfig()
