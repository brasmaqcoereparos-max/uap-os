class EmergencyStop:

    def __init__(self):

        self.active = False

    def activate(self):

        self.active = True

    def reset(self):

        self.active = False

    def is_active(self):

        return self.active

    def check(self):

        if self.active:

            return False

        return True


emergency_stop = EmergencyStop()class RobotEmergencyStop:

    def __init__(self):

        self.active = False

    def activate(self):

        self.active = True

    def reset(self):

        self.active = False

    def can_continue(self):

        return not self.active


robot_emergency_stop = RobotEmergencyStop()
