class VisionDetection:

    def __init__(
        self,
        detection_type,
        confidence=0.0,
    ):

        self.detection_type = detection_type
        self.confidence = max(
            0.0,
            min(1.0, confidence),
        )

        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def set_area(
        self,
        x,
        y,
        width,
        height,
    ):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def to_dict(self):

        return {
            "type": self.detection_type,
            "confidence": self.confidence,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
        }
