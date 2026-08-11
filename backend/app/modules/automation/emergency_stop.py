class RobotEmergencyStop:

    def __init__(self):

        self.active = False

    def activate(self):

        self.active = True

    def reset(self):

        self.active = False

    def can_continue(self):

        return not self.active


robot_emergency_stop = RobotEmergencyStop()
