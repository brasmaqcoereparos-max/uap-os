class SelectionManager:

    def __init__(self):

        self.selected = set()

    def clear(self):

        self.selected.clear()

    def add(self, node_id):

        self.selected.add(node_id)

    def remove(self, node_id):

        self.selected.discard(node_id)

    def toggle(self, node_id):

        if node_id in self.selected:
            self.selected.remove(node_id)
        else:
            self.selected.add(node_id)

    def all(self):

        return list(self.selected)

    def contains(self, node_id):

        return node_id in self.selected


selection = SelectionManager()
