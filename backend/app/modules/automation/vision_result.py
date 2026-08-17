class VisionResult:

    def __init__(self):

        self.detections = []
        self.timestamp = None

    def add_detection(
        self,
        detection,
    ):

        self.detections.append(
            detection
        )

    def clear(self):

        self.detections.clear()

    def get_detections(self):

        return list(
            self.detections
        )

    def find_by_type(
        self,
        detection_type,
    ):

        return [
            detection
            for detection in self.detections
            if detection.detection_type
            == detection_type
        ]

    def to_dict(self):

        return {
            "timestamp": self.timestamp,
            "detections": [
                detection.to_dict()
                for detection in self.detections
            ],
        }
