class MobileRobotState:

    IDLE = "idle"
    MOVING = "moving"
    STOPPED = "stopped"
    TURNING = "turning"
    PAUSED = "paused"
    DOCKING = "docking"
    ERROR = "error"

    def __init__(self):

        self.state = self.IDLE

    def set(self, state):

        self.state = state

    def get(self):

        return self.state

    def is_moving(self):

        return self.state == self.MOVING

    def is_stopped(self):

        return self.state == self.STOPPED
