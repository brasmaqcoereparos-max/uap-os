from app.modules.automation.robot_configuration import (
    RobotConfiguration,
)

from app.modules.automation.robot_state import (
    robot_state,
    RobotState,
)


class RobotManager:

    def __init__(self):

        self.robot = None

    def configure(
        self,
        name="Robot",
    ):

        self.robot = RobotConfiguration(
            name
        )

        robot_state.set(
            RobotState.READY
        )

        return self.robot

    def get(self):

        return self.robot

    def disable(self):

        robot_state.set(
            RobotState.DISABLED
        )

    def error(self):

        robot_state.set(
            RobotState.ERROR
        )


robot_manager = RobotManager()
