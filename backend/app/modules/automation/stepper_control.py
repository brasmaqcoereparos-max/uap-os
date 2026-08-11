class StepperController:

    def __init__(self, device):

        self.device = device
        self.steps = 0

    def move_steps(self, steps):

        self.steps += steps
        self.device.position += steps

    def move_to_step(self, step):

        self.steps = step
        self.device.position = step

    def get_step(self):

        return self.steps
