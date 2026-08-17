class TrajectoryPoint:

    def __init__(
        self,
        x=0,
        y=0,
        angle=0,
        speed=0,
    ):

        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed

    def set_position(
        self,
        x,
        y,
    ):

        self.x = x
        self.y = y

    def set_angle(self, angle):

        self.angle = angle

    def set_speed(self, speed):

        self.speed = speed

    def to_dict(self):

        return {
            "x": self.x,
            "y": self.y,
            "angle": self.angle,
            "speed": self.speed,
        }
