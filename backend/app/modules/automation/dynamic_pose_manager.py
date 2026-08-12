class DynamicPoseManager:

    def __init__(self):

        self.poses = []

    def add(self, pose):

        self.poses.append(pose)

        return len(self.poses) - 1

    def insert(
        self,
        index,
        pose,
    ):

        if index < 0:
            index = 0

        if index > len(self.poses):
            index = len(self.poses)

        self.poses.insert(
            index,
            pose,
        )

        return index

    def replace(
        self,
        index,
        pose,
    ):

        if not (
            0 <= index < len(self.poses)
        ):
            return False

        self.poses[index] = pose

        return True

    def delete(self, index):

        if not (
            0 <= index < len(self.poses)
        ):
            return False

        self.poses.pop(index)

        return True

    def get_all(self):

        return list(self.poses)


dynamic_pose_manager = DynamicPoseManager()
