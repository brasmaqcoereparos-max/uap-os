from app.modules.automation.emergency_stop import (
    emergency_stop,
)

from app.modules.automation.safety_manager import (
    safety_manager,
)

from app.modules.automation.robot_safety_controller import (
    RobotSafetyController,
)


class MobileRobotSafety:

    def __init__(self):

        self.controller = RobotSafetyController(
            safety_manager,
            emergency_stop,
        )

    def allow_movement(
        self,
        distance=None,
    ):

        return self.controller.can_move(
            distance
        )

    def emergency_stop(self):

        emergency_stop.activate()

    def reset_emergency_stop(self):

        emergency_stop.reset()

    def is_stopped(self):

        return emergency_stop.is_active()


mobile_robot_safety = MobileRobotSafety()
