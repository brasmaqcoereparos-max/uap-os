class SCurveProfile:

    def __init__(self):

        self.jerk = 0

        self.acceleration = 100

        self.max_speed = 1000

    def configure(

        self,

        jerk,

        acceleration,

        max_speed,

    ):

        self.jerk = jerk

        self.acceleration = acceleration

        self.max_speed = max_speed
