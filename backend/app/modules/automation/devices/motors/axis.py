class Axis:

    def __init__(

        self,

        name,

        motor,

    ):

        self.name = name

        self.motor = motor

        self.position = 0

    def move_to(

        self,

        position,

    ):

        self.position = position

    def move_relative(

        self,

        delta,

    ):

        self.position += delta
