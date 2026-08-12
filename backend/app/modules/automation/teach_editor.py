from app.modules.automation.pose_list import (
    PoseList,
)

from app.modules.automation.pose_reorder import (
    PoseReorder,
)

from app.modules.automation.pose_navigation import (
    PoseNavigation,
)


class TeachEditor:

    def __init__(self):

        self.pose_list = PoseList()

        self.navigation = PoseNavigation(
            self.pose_list
        )

        self.reorder = PoseReorder()

    def load(self, poses):

        self.pose_list.load(poses)

    def select(self, index):

        return self.pose_list.select(
            index
        )

    def delete_selected(self):

        return self.pose_list.delete_selected()

    def next(self):

        return self.navigation.next()

    def previous(self):

        return self.navigation.previous()

    def first(self):

        return self.navigation.first()

    def last(self):

        return self.navigation.last()

    def reorder_pose(
        self,
        source,
        target,
    ):

        return self.reorder.move(
            self.pose_list.items,
            source,
            target,
        )

    def get_poses(self):

        return self.pose_list.get_all()


teach_editor = TeachEditor()
