class RobotPose:

    def __init__(
        self,
        name="Position",
    ):

        self.name = name
        self.axes = {}
        self.speed = 0
        self.wait = 0

    def set_axis(
        self,
        axis_id,
        position,
    ):

        self.axes[axis_id] = position

    def get_axis(
        self,
        axis_id,
        default=None,
    ):

        return self.axes.get(
            axis_id,
            default,
        )

    def get_all(self):

        return dict(self.axes)
