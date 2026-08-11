class RobotConfiguration:

    def __init__(
        self,
        name="Robot",
    ):

        self.name = name

        self.axes = {}

        self.payload = 0

        self.units = "degrees"

    def add_axis(
        self,
        axis,
    ):

        self.axes[
            axis.axis_id
        ] = axis

    def get_axis(
        self,
        axis_id,
    ):

        return self.axes.get(
            axis_id
        )

    def set_payload(
        self,
        payload,
    ):

        self.payload = max(
            0,
            payload,
        )
