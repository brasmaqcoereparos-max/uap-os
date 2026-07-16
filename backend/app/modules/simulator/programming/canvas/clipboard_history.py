class ClipboardHistory:

    def __init__(self):

        self.items = []

        self.limit = 20

    def add(self, node):

        self.items.insert(0, node)

        self.items = self.items[: self.limit]

    def clear(self):

        self.items.clear()

    def all(self):

        return self.items


clipboard_history = ClipboardHistory()
