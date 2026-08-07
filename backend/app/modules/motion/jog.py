class JogController:

    def __init__(self):

        self.increment = 1.0

    def set_increment(

        self,

        value,

    ):

        self.increment = value

    def move_positive(

        self,

        axis,

    ):

        axis.position += self.increment

    def move_negative(

        self,

        axis,

    ):

        axis.position -= self.increment


jog_controller = JogController()
