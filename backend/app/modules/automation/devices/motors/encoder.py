class Encoder:

    def __init__(

        self,

        pulses_per_turn=1024,

    ):

        self.position = 0

        self.pulses_per_turn = pulses_per_turn

    def reset(self):

        self.position = 0

    def update(

        self,

        pulses,

    ):

        self.position += pulses

    def get_position(self):

        return self.position
