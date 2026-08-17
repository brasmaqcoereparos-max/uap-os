class RobotPosition:

    def __init__(
        self,
        x=0,
        y=0,
        angle=0,
    ):

        self.x = x
        self.y = y
        self.angle = angle

    def set(
        self,
        x,
        y,
        angle=0,
    ):

        self.x = x
        self.y = y
        self.angle = angle

    def get(self):

        return {
            "x": self.x,
            "y": self.y,
            "angle": self.angle,
        }

    def set_angle(self, angle):

        self.angle = angle
