class ServoController:

    def __init__(self, device):

        self.device = device
        self.angle = 0

    def set_angle(self, angle):

        if angle < 0:
            angle = 0

        if angle > 180:
            angle = 180

        self.angle = angle
        self.device.position = angle

    def get_angle(self):

        return self.angle
