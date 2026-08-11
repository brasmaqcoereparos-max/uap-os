class HomingController:

    def __init__(self, device):

        self.device = device
        self.homed = False

    def home(self):

        self.device.position = 0
        self.homed = True

    def is_homed(self):

        return self.homed

    def reset(self):

        self.homed = False
