class PositionController:

    def __init__(self, device):

        self.device = device

    def move_to(self, position):

        self.device.position = position

    def move_by(self, distance):

        self.device.position += distance

    def get_position(self):

        return self.device.position
