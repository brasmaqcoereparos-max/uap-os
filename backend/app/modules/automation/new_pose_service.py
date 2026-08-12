from app.modules.automation.robot_pose import (
    RobotPose,
)


class NewPoseService:

    def create(
        self,
        robot,
        name=None,
        speed=0,
        wait=0,
    ):

        if name is None:

            name = (
                f"Position "
                f"{len(robot.axes)}"
            )

        pose = RobotPose(name)

        for axis_id, axis in robot.axes.items():

            pose.set_axis(
                axis_id,
                axis.position,
            )

        pose.speed = speed
        pose.wait = wait

        return pose


new_pose_service = NewPoseService()
