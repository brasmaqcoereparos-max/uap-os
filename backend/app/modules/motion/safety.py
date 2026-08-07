class MotionSafety:

    def __init__(self):

        self.enabled = True

        self.emergency_stop = False

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def stop(self):

        self.emergency_stop = True

    def reset(self):

        self.emergency_stop = False


motion_safety = MotionSafety()
