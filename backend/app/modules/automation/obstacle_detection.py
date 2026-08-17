class ObstacleDetection:

    def __init__(self):

        self.detected = False
        self.distance = None
        self.direction = None
        self.source = None

    def detect(
        self,
        distance,
        direction=None,
        source=None,
    ):

        self.detected = True
        self.distance = distance
        self.direction = direction
        self.source = source

    def clear(self):

        self.detected = False
        self.distance = None
        self.direction = None
        self.source = None

    def is_detected(self):

        return self.detected

    def get(self):

        return {
            "detected": self.detected,
            "distance": self.distance,
            "direction": self.direction,
            "source": self.source,
        }


obstacle_detection = ObstacleDetection()
