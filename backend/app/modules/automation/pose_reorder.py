class PoseReorder:

    def move(
        self,
        poses,
        source_index,
        target_index,
    ):

        if not (
            0 <= source_index < len(poses)
        ):
            return False

        if not (
            0 <= target_index < len(poses)
        ):
            return False

        pose = poses.pop(
            source_index
        )

        poses.insert(
            target_index,
            pose
        )

        return True
