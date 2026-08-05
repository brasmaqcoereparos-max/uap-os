class MotionProfile:

    def __init__(self):

        self.acceleration = 100

        self.deceleration = 100

        self.max_speed = 1000

    def configure(

        self,

        acceleration,

        deceleration,

        max_speed,

    ):

        self.acceleration = acceleration

        self.deceleration = deceleration

        self.max_speed = max_speed
