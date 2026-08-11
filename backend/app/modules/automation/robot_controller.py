from app.modules.automation.robot_execution import (
    RobotExecution,
)

from app.modules.automation.trajectory_validator import (
    trajectory_validator,
)

from app.modules.automation.trajectory_checker import (
    trajectory_checker,
)

from app.modules.automation.emergency_stop import (
    robot_emergency_stop,
)


class RobotController:

    def __init__(self):

        self.execution = RobotExecution()

    def prepare(
        self,
        poses,
        limits,
    ):

        if robot_emergency_stop.active:

            return {
                "success": False,
                "reason": "emergency_stop_active",
            }

        errors = trajectory_checker.check(
            poses
        )

        errors.extend(
            trajectory_validator.validate_limits(
                poses,
                limits,
            )
        )

        if errors:

            return {
                "success": False,
                "errors": errors,
            }

        return {
            "success": True,
        }

    def start(self):

        if robot_emergency_stop.active:
            return False

        self.execution.start()

        return True

    def pause(self):

        self.execution.pause()

    def resume(self):

        if robot_emergency_stop.active:
            return False

        self.execution.resume()

        return True

    def stop(self):

        self.execution.stop()


robot_controller = RobotController()
