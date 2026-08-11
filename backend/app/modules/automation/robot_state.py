from enum import Enum


class RobotState(Enum):

    DISABLED = "disabled"

    READY = "ready"

    MOVING = "moving"

    PAUSED = "paused"

    ERROR = "error"

    EMERGENCY_STOP = "emergency_stop"


class RobotStateManager:

    def __init__(self):

        self.state = RobotState.DISABLED

    def set(
        self,
        state,
    ):

        self.state = state

    def get(self):

        return self.state

    def is_moving(self):

        return (
            self.state
            == RobotState.MOVING
        )


robot_state = RobotStateManager()
