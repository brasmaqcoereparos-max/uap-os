class PoseList:

    def __init__(self):

        self.items = []
        self.selected_index = None

    def load(self, poses):

        self.items = list(poses)
        self.selected_index = None

    def select(self, index):

        if 0 <= index < len(self.items):

            self.selected_index = index
            return self.items[index]

        return None

    def get_selected(self):

        if self.selected_index is None:
            return None

        return self.items[
            self.selected_index
        ]

    def delete_selected(self):

        if self.selected_index is None:
            return False

        self.items.pop(
            self.selected_index
        )

        if not self.items:

            self.selected_index = None

        elif self.selected_index >= len(self.items):

            self.selected_index = len(
                self.items
            ) - 1

        return True

    def get_all(self):

        return list(self.items)
