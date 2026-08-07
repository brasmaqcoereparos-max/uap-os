class MotionPosition:

    def __init__(self):

        self.axes = {}

    def set_axis(

        self,

        axis,

        value,

    ):

        self.axes[axis] = value

    def get_axis(

        self,

        axis,

    ):

        return self.axes.get(axis)

    def copy(self):

        position = MotionPosition()

        position.axes = self.axes.copy()

        return position
