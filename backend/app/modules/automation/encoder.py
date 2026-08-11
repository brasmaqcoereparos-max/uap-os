class Encoder:

    def __init__(self):

        self.position = 0
        self.velocity = 0

    def update(
        self,
        position,
        velocity=0,
    ):

        self.position = position
        self.velocity = velocity

    def get_position(self):

        return self.position

    def get_velocity(self):

        return self.velocity
