class RobotSequence:

    def __init__(
        self,
        name="Robot Sequence",
    ):

        self.name = name
        self.poses = []
        self.loop = False

    def add_pose(
        self,
        pose,
    ):

        self.poses.append(pose)

    def remove_pose(
        self,
        index,
    ):

        if 0 <= index < len(self.poses):

            self.poses.pop(index)

    def set_loop(
        self,
        enabled,
    ):

        self.loop = enabled

    def get_poses(self):

        return list(self.poses)
