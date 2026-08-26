from typing import Any


class PersonDetector:

    def __init__(self):
        self._classifier = None

    def load(self):

        try:
            import cv2
        except ImportError as exc:
            raise RuntimeError(
                "OpenCV não está instalado."
            ) from exc

        if self._classifier is not None:
            return self._classifier

        cascade = cv2.data.haarcascades + (
            "haarcascade_fullbody.xml"
        )

        classifier = cv2.CascadeClassifier(
            cascade
        )

        if classifier.empty():
            raise RuntimeError(
                "Classificador de pessoa "
                "não pôde ser carregado."
            )

        self._classifier = classifier

        return classifier

    def detect(self, frame: Any):

        if frame is None:
            return []

        classifier = self.load()

        import cv2

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY,
        )

        bodies = classifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(30, 60),
        )

        results = []

        for x, y, width, height in bodies:

            results.append(
                {
                    "class": "person",
                    "confidence": None,
                    "bbox": {
                        "x": int(x),
                        "y": int(y),
                        "width": int(width),
                        "height": int(height),
                    },
                }
            )

        return results

    def count(self, frame: Any):
        return len(
            self.detect(frame)
        )


person_detector = PersonDetector()
