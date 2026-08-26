from dataclasses import dataclass, field
from typing import Any


@dataclass
class VisionState:

    enabled: bool = True
    running: bool = False

    cameras_active: int = 0

    last_event: dict[str, Any] | None = None
    last_analysis: dict[str, Any] | None = None

    statistics: dict[str, int] = field(
        default_factory=lambda: {
            "frames": 0,
            "analyses": 0,
            "detections": 0,
            "motion_events": 0,
            "person_events": 0,
        }
    )

    def record_frame(self):
        self.statistics["frames"] += 1

    def record_analysis(self):
        self.statistics["analyses"] += 1

    def record_detection(
        self,
        count: int = 1,
    ):
        self.statistics[
            "detections"
        ] += max(0, count)

    def record_motion(self):
        self.statistics[
            "motion_events"
        ] += 1

    def record_person(self):
        self.statistics[
            "person_events"
        ] += 1

    def set_event(self, event):
        self.last_event = event

    def set_analysis(self, analysis):
        self.last_analysis = analysis

    def to_dict(self):

        return {
            "enabled": self.enabled,
            "running": self.running,
            "cameras_active": (
                self.cameras_active
            ),
            "last_event": self.last_event,
            "last_analysis": self.last_analysis,
            "statistics": dict(
                self.statistics
            ),
        }


vision_state = VisionState()
