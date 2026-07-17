import copy


class NodeHistory:

    def __init__(self):

        self.history = []

        self.limit = 100

    def save(
        self,
        node,
    ):

        self.history.append(
            copy.deepcopy(node)
        )

        if len(self.history) > self.limit:

            self.history.pop(0)

    def last(self):

        if not self.history:

            return None

        return copy.deepcopy(
            self.history[-1]
        )

    def clear(self):

        self.history.clear()


node_history = NodeHistory()
