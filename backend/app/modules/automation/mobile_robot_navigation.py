class MobileRobotNavigation:

    def __init__(
        self,
        motion,
        state,
    ):

        self.motion = motion
        self.state = state

    def forward(self, speed):

        self.motion.forward(speed)
        self.state.set("moving")

    def backward(self, speed):

        self.motion.backward(speed)
        self.state.set("moving")

    def left(self, speed):

        self.motion.turn_left(speed)
        self.state.set("turning")

    def right(self, speed):

        self.motion.turn_right(speed)
        self.state.set("turning")

    def stop(self):

        self.motion.stop()
        self.state.set("stopped")

    def get_state(self):

        return self.state.get()
