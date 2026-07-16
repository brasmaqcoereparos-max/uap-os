import copy


class Clipboard:

    def __init__(self):

        self.data = None

    def copy(self, node):

        self.data = copy.deepcopy(node)

    def paste(self):

        if self.data is None:
            return None

        node = copy.deepcopy(self.data)

        node.id = None

        node.x += 40

        node.y += 40

        return node

    def clear(self):

        self.data = None


clipboard = Clipboard()
