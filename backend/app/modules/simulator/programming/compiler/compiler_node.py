class CompilerNode:

    def __init__(self, node):

        self.node = node

    @property
    def id(self):

        return self.node.get("id")

    @property
    def name(self):

        return self.node.get("name")

    @property
    def block_type(self):

        return self.node.get("block_type")

    @property
    def config(self):

        return self.node.get("config", {})

    def value(self, key, default=None):

        return self.config.get(key, default)
