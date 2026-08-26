from typing import Any


class VisionDetector:

    def detect(
        self,
        frame: Any,
    ):
        if frame is None:
            return []

        return []

    def detect_persons(
        self,
        frame: Any,
    ):
        detections = self.detect(frame)

        return [
            item
            for item in detections
            if item.get("class") == "person"
        ]

    def detect_objects(
        self,
        frame: Any,
    ):
        return self.detect(frame)

    def count_persons(
        self,
        frame: Any,
    ):
        return len(
            self.detect_persons(frame)
        )

    def has_person(
        self,
        frame: Any,
    ):
        return bool(
            self.detect_persons(frame)
        )


vision_detector = VisionDetector()
