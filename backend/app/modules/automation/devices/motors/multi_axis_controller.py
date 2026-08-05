class MultiAxisController:

    def __init__(self):

        self.axes = {}

    def add_axis(

        self,

        axis,

    ):

        self.axes[axis.name] = axis

    def get_axis(

        self,

        name,

    ):

        return self.axes.get(name)

    def all_axes(self):

        return list(self.axes.values())


multi_axis_controller = MultiAxisController()
