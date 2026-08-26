from typing import Any


class ObjectDetector:

    def __init__(self):
        self._model = None
        self._classes = []

    def load(
        self,
        model=None,
        classes=None,
    ):

        self._model = model

        self._classes = list(
            classes or []
        )

        return self._model

    def is_loaded(self):
        return self._model is not None

    def detect(self, frame: Any):

        if frame is None:
            return []

        if self._model is None:
            return []

        predict = getattr(
            self._model,
            "predict",
            None,
        )

        if not callable(predict):
            return []

        results = predict(
            frame
        )

        if results is None:
            return []

        return results

    def classes(self):
        return list(
            self._classes
        )

    def clear(self):
        self._model = None
        self._classes = []


object_detector = ObjectDetector()
