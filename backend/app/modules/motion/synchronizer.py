class MotionSynchronizer:

    def __init__(self):

        self.axes = []

    def add_axis(

        self,

        axis,

    ):

        if axis not in self.axes:

            self.axes.append(axis)

    def clear(self):

        self.axes.clear()

    def synchronized_axes(self):

        return list(self.axes)


motion_synchronizer = MotionSynchronizer()
