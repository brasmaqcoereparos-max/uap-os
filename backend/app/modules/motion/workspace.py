class Workspace:

    def __init__(self):

        self.x_min = None

        self.x_max = None

        self.y_min = None

        self.y_max = None

        self.z_min = None

        self.z_max = None

    def set_limits(

        self,

        x_min,

        x_max,

        y_min,

        y_max,

        z_min,

        z_max,

    ):

        self.x_min = x_min

        self.x_max = x_max

        self.y_min = y_min

        self.y_max = y_max

        self.z_min = z_min

        self.z_max = z_max


workspace = Workspace()
