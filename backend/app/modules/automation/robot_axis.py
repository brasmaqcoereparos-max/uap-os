class RobotAxis:

    def __init__(
        self,
        axis_id,
        name="Axis",
        minimum=-180,
        maximum=180,
    ):

        self.axis_id = axis_id
        self.name = name

        self.position = 0

        self.minimum = minimum
        self.maximum = maximum

        self.speed = 0
        self.enabled = False

    def set_position(
        self,
        position,
    ):

        if position < self.minimum:
            return False

        if position > self.maximum:
            return False

        self.position = position

        return True

    def set_speed(
        self,
        speed,
    ):

        self.speed = max(
            0,
            speed,
        )

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False
