class JogController:

    def __init__(self, robot):

        self.robot = robot
        self.speed = 20

    def set_speed(self, speed):

        self.speed = max(
            0,
            min(100, speed),
        )

    def jog_axis(
        self,
        axis_id,
        direction,
    ):

        if direction not in (-1, 1):
            return False

        axis = self.robot.axes.get(
            axis_id
        )

        if axis is None:
            return False

        step = self.speed * direction

        return axis.set_position(
            axis.position + step
        )
