class TrajectoryValidator:

    def validate_limits(
        self,
        poses,
        limits,
    ):

        errors = []

        for index, pose in enumerate(poses):

            for axis_id, position in pose.axes.items():

                axis_limits = limits.get(
                    axis_id
                )

                if axis_limits is None:
                    continue

                minimum = axis_limits.get(
                    "min"
                )

                maximum = axis_limits.get(
                    "max"
                )

                if minimum is not None and position < minimum:
                    errors.append(
                        f"Pose {index}: axis {axis_id} "
                        f"below minimum"
                    )

                if maximum is not None and position > maximum:
                    errors.append(
                        f"Pose {index}: axis {axis_id} "
                        f"above maximum"
                    )

        return errors

    def is_valid(
        self,
        poses,
        limits,
    ):

        return not self.validate_limits(
            poses,
            limits,
        )


trajectory_validator = TrajectoryValidator()
