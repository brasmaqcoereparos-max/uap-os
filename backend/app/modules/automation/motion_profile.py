class MotionProfile:

    def __init__(self):

        self.max_speed = 100
        self.acceleration = 10
        self.deceleration = 10

    def configure(
        self,
        max_speed=None,
        acceleration=None,
        deceleration=None,
    ):

        if max_speed is not None:
            self.max_speed = max_speed

        if acceleration is not None:
            self.acceleration = acceleration

        if deceleration is not None:
            self.deceleration = deceleration
