class PoseNavigation:

    def __init__(self, pose_list):

        self.pose_list = pose_list

    def next(self):

        index = self.pose_list.selected_index

        if index is None:
            return None

        return self.pose_list.select(
            index + 1
        )

    def previous(self):

        index = self.pose_list.selected_index

        if index is None:
            return None

        return self.pose_list.select(
            index - 1
        )

    def first(self):

        if not self.pose_list.items:
            return None

        return self.pose_list.select(0)

    def last(self):

        if not self.pose_list.items:
            return None

        return self.pose_list.select(
            len(self.pose_list.items) - 1
        )
