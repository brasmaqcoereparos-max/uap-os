class RobotUIModel:

    def __init__(self):

        self.name = "Robot"
        self.axes = {}
        self.selected_pose = None
        self.mode = "idle"

    def set_name(self, name):

        self.name = name

    def set_axes(self, axes):

        self.axes = dict(axes)

    def select_pose(self, index):

        self.selected_pose = index

    def set_mode(self, mode):

        self.mode = mode

    def get_state(self):

        return {
            "name": self.name,
            "axes": dict(self.axes),
            "selected_pose": self.selected_pose,
            "mode": self.mode,
        }
