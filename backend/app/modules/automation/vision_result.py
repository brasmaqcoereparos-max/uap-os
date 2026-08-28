import time


class VisionResult:
    def __init__(
        self,
        detections=None,
        timestamp=None,
        metadata=None,
    ):
        self.detections = list(
            detections or []
        )

        self.timestamp = (
            float(timestamp)
            if timestamp is not None
            else time.time()
        )

        self.metadata = dict(
            metadata or {}
        )

    def add_detection(
        self,
        detection,
    ):
        self.detections.append(
            detection
        )

        return detection

    def remove_detection(
        self,
        detection,
    ):
        try:
            self.detections.remove(
                detection
            )

            return True

        except ValueError:
            return False

    def clear(self):
        self.detections.clear()

    def get_detections(self):
        return list(
            self.detections
        )

    @staticmethod
    def _type_of(detection):
        if isinstance(
            detection,
            dict,
        ):
            return detection.get(
                "detection_type",
                detection.get("type"),
            )

        return getattr(
            detection,
            "detection_type",
            getattr(
                detection,
                "type",
                None,
            ),
        )

    def find_by_type(
        self,
        detection_type,
    ):
        expected = str(
            detection_type
        ).strip().lower()

        return [
            detection
            for detection
            in self.detections
            if str(
                self._type_of(
                    detection
                )
            ).strip().lower()
            == expected
        ]

    def has_type(
        self,
        detection_type,
    ):
        return bool(
            self.find_by_type(
                detection_type
            )
        )

    def count(self):
        return len(
            self.detections
        )

    def to_dict(self):
        result = []

        for detection in (
            self.detections
        ):
            serializer = getattr(
                detection,
                "to_dict",
                None,
            )

            if callable(serializer):
                result.append(
                    serializer()
                )
            elif isinstance(
                detection,
                dict,
            ):
                result.append(
                    dict(detection)
                )
            else:
                result.append(
                    str(detection)
                )

        return {
            "timestamp": (
                self.timestamp
            ),
            "count": self.count(),
            "detections": result,
            "metadata": dict(
                self.metadata
            ),
    }
