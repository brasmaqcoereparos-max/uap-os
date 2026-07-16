import copy


class ClipboardManager:

    def __init__(self):

        self.data = None

    def copy_nodes(self, nodes):

        self.data = copy.deepcopy(nodes)

    def paste_nodes(self):

        if self.data is None:
            return []

        nodes = copy.deepcopy(self.data)

        for node in nodes:

            node.id = None

            node.x += 40

            node.y += 40

        return nodes

    def clear(self):

        self.data = None

    def has_data(self):

        return self.data is not None


clipboard_manager = ClipboardManager()
