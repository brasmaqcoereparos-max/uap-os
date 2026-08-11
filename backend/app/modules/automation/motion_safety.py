class MotionSafety:

    def __init__(self):

        self.enabled = True
        self.emergency_stop = False
        self.limits_ok = True

    def emergency(self):

        self.emergency_stop = True

    def reset_emergency(self):

        self.emergency_stop = False

    def set_limits(
        self,
        status,
    ):

        self.limits_ok = status

    def can_move(self):

        return (
            self.enabled
            and not self.emergency_stop
            and self.limits_ok
        )


motion_safety = MotionSafety()
