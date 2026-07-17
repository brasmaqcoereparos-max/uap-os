class NodeSelection:

    def __init__(self):

        self.selected = set()

    def select(
        self,
        node_id,
    ):

        self.selected.add(node_id)

    def deselect(
        self,
        node_id,
    ):

        self.selected.discard(node_id)

    def clear(self):

        self.selected.clear()

    def is_selected(
        self,
        node_id,
    ):

        return node_id in self.selected

    def all(self):

        return list(self.selected)


node_selection = NodeSelection()
