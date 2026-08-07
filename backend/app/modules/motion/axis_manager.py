from app.modules.motion.axis import MotionAxis


class AxisManager:

    def __init__(self):

        self.axes = {}

    def add(

        self,

        name,

    ):

        axis = MotionAxis(name)

        self.axes[name] = axis

        return axis

    def get(

        self,

        name,

    ):

        return self.axes.get(name)

    def list(self):

        return list(self.axes.keys())


axis_manager = AxisManager()
