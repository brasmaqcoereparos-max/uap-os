class NodeBreakpoints:

    def __init__(self):

        self.breakpoints = set()

    def add(
        self,
        node_id,
    ):

        self.breakpoints.add(node_id)

    def remove(
        self,
        node_id,
    ):

        self.breakpoints.discard(node_id)

    def toggle(
        self,
        node_id,
    ):

        if node_id in self.breakpoints:

            self.breakpoints.remove(node_id)

        else:

            self.breakpoints.add(node_id)

    def has(
        self,
        node_id,
    ):

        return node_id in self.breakpoints

    def clear(self):

        self.breakpoints.clear()

    def all(self):

        return list(self.breakpoints)


node_breakpoints = NodeBreakpoints()
