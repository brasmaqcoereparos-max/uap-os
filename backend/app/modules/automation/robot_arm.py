class RobotArm:

    def __init__(self, name="Robot Arm"):

        self.name = name
        self.axes = {}
        self.enabled = False

    def add_axis(
        self,
        axis_id,
        position=0,
    ):

        self.axes[axis_id] = {
            "position": position,
            "speed": 0,
        }

    def set_position(
        self,
        axis_id,
        position,
    ):

        if axis_id not in self.axes:
            return False

        self.axes[axis_id]["position"] = position

        return True

    def get_position(
        self,
        axis_id,
    ):

        axis = self.axes.get(axis_id)

        if axis is None:
            return None

        return axis["position"]

    def get_positions(self):

        return {
            axis_id: data["position"]
            for axis_id, data in self.axes.items()
        }
