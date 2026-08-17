from app.modules.automation.mobile_robot_motion import (
    MobileRobotMotion,
)

from app.modules.automation.mobile_robot_state import (
    MobileRobotState,
)

from app.modules.automation.mobile_robot_navigation import (
    MobileRobotNavigation,
)


class MobileRobotController:

    def __init__(self):

        self.motion = MobileRobotMotion()

        self.state = MobileRobotState()

        self.navigation = MobileRobotNavigation(
            self.motion,
            self.state,
        )

    def move_forward(self, speed):

        self.navigation.forward(speed)

    def move_backward(self, speed):

        self.navigation.backward(speed)

    def turn_left(self, speed):

        self.navigation.left(speed)

    def turn_right(self, speed):

        self.navigation.right(speed)

    def stop(self):

        self.navigation.stop()

    def get_state(self):

        return self.state.get()

    def get_motion(self):

        return self.motion.get_speed()


mobile_robot_controller = (
    MobileRobotController()
)
