class TrapezoidalProfile:

    def __init__(self):

        self.max_speed = 1000

        self.acceleration = 100

        self.deceleration = 100

    def configure(

        self,

        max_speed,

        acceleration,

        deceleration,

    ):

        self.max_speed = max_speed

        self.acceleration = acceleration

        self.deceleration = deceleration
