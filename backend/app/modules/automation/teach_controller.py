from app.modules.automation.robot_pose import (
    RobotPose,
)

from app.modules.automation.position_sequence import (
    PositionSequence,
)


class TeachController:

    def __init__(self):

        self.sequence = PositionSequence(
            "Teach Program"
        )

    def record_current_position(
        self,
        robot,
        speed=0,
        wait=0,
    ):

        pose = RobotPose(
            f"Position {len(self.sequence.positions) + 1}"
        )

        positions = robot.get_positions()

        for axis_id, position in positions.items():

            pose.set_axis(
                axis_id,
                position,
            )

        pose.speed = speed
        pose.wait = wait

        self.sequence.add_position(
            pose
        )

        return pose

    def get_sequence(self):

        return self.sequence


teach_controller = TeachController()
