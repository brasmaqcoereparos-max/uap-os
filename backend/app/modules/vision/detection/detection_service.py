from app.modules.vision.detection.person_detector import (
    person_detector,
)

from app.modules.vision.detection.object_detector import (
    object_detector,
)


class DetectionService:

    def persons(self, frame):

        return person_detector.detect(
            frame
        )

    def objects(self, frame):

        return object_detector.detect(
            frame
        )

    def all(self, frame):

        persons = self.persons(
            frame
        )

        objects = self.objects(
            frame
        )

        return persons + objects

    def count_persons(self, frame):

        return len(
            self.persons(frame)
        )

    def model_loaded(self):

        return object_detector.is_loaded()


detection_service = DetectionService()
