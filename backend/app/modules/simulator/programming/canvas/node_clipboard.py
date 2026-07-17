import copy


class NodeClipboard:

    def __init__(self):

        self.nodes = []

    def copy(
        self,
        nodes,
    ):

        self.nodes = copy.deepcopy(nodes)

    def paste(self):

        result = copy.deepcopy(
            self.nodes
        )

        for node in result:

            node.id = None

            node.x += 30

            node.y += 30

        return result

    def clear(self):

        self.nodes.clear()

    def empty(self):

        return len(self.nodes) == 0


node_clipboard = NodeClipboard()
