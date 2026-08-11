class TrajectoryChecker:

    def check(
        self,
        poses,
    ):

        errors = []

        if not poses:
            errors.append(
                "Trajectory has no positions"
            )
            return errors

        for index in range(
            len(poses) - 1
        ):

            current = poses[index]
            next_pose = poses[index + 1]

            if not current.axes:
                errors.append(
                    f"Pose {index} has no axes"
                )

            if not next_pose.axes:
                errors.append(
                    f"Pose {index + 1} has no axes"
                )

        return errors

    def is_valid(
        self,
        poses,
    ):

        return not self.check(
            poses
        )


trajectory_checker = TrajectoryChecker()
