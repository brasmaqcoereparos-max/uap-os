"""
Editor de posições para automações robóticas do UAP.
"""

from app.modules.automation.robot_pose import (
    RobotPose,
)


class PoseEditor:

    def update_axis(
        self,
        pose,
        axis_id,
        position,
    ):

        self._validate_pose(
            pose
        )

        pose.set_axis(
            axis_id,
            position,
        )

        return pose

    def set_speed(
        self,
        pose,
        speed,
    ):

        self._validate_pose(
            pose
        )

        pose.speed = max(
            0,
            float(speed),
        )

        return pose

    def set_wait(
        self,
        pose,
        wait,
    ):

        self._validate_pose(
            pose
        )

        pose.wait = max(
            0,
            float(wait),
        )

        return pose

    def create(
        self,
        name="Position",
    ):

        return RobotPose(
            name=name
        )

    def get_axis(
        self,
        pose,
        axis_id,
        default=None,
    ):

        self._validate_pose(
            pose
        )

        return pose.get_axis(
            axis_id,
            default,
        )

    def get_axes(
        self,
        pose,
    ):

        self._validate_pose(
            pose
        )

        return pose.get_all()

    @staticmethod
    def _validate_pose(
        pose,
    ):

        if not isinstance(
            pose,
            RobotPose,
        ):
            raise TypeError(
                "O objeto fornecido não é um RobotPose."
            )


pose_editor = PoseEditor()
