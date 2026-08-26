from app.modules.vision.vision_detector import (
    vision_detector,
)

from app.modules.vision.motion_detector import (
    motion_detector,
)


class VisionAnalyzer:

    def analyze(self, frame):

        if frame is None:
            return {
                "success": False,
                "motion": False,
                "detections": [],
                "persons": 0,
            }

        motion = motion_detector.detect(
            frame
        )

        detections = vision_detector.detect(
            frame
        )

        persons = [
            item
            for item in detections
            if isinstance(item, dict)
            and item.get("class") == "person"
        ]

        return {
            "success": True,
            "motion": motion,
            "detections": detections,
            "persons": len(persons),
        }


vision_analyzer = VisionAnalyzer()
