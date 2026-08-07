class MotionAxis:

    def __init__(

        self,

        name,

    ):

        self.name = name

        self.position = 0.0

        self.target = 0.0

        self.enabled = True

        self.homed = False

        self.limit_min = None

        self.limit_max = None

        self.velocity = 100.0

        self.acceleration = 100.0

    def set_home(self):

        self.position = 0.0

        self.target = 0.0

        self.homed = True
