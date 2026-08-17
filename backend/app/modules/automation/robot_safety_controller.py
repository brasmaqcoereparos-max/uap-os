class RobotSafetyController:

    def __init__(
        self,
        safety_manager,
        emergency_stop,
    ):

        self.safety_manager = safety_manager
        self.emergency_stop = emergency_stop

    def can_move(
        self,
        distance=None,
    ):

        if self.emergency_stop.is_active():

            return False

        if distance is None:

            return True

        return self.safety_manager.check_distance(
            distance
        )

    def stop_if_unsafe(
        self,
        robot,
        distance=None,
    ):

        if not self.can_move(distance):

            robot.stop()

            return True

        return False
