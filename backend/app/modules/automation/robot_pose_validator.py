class RobotPoseValidator:

    def validate(
        self,
        pose,
        configuration,
    ):

        errors = []

        for axis_id, position in pose.axes.items():

            axis = configuration.get_axis(
                axis_id
            )

            if axis is None:

                errors.append(
                    f"Axis {axis_id} not configured"
                )

                continue

            if position < axis.minimum:

                errors.append(
                    f"Axis {axis_id} below limit"
                )

            if position > axis.maximum:

                errors.append(
                    f"Axis {axis_id} above limit"
                )

        return errors

    def is_valid(
        self,
        pose,
        configuration,
    ):

        return not self.validate(
            pose,
            configuration,
        )


robot_pose_validator = (
    RobotPoseValidator()
)
