class NodeRegistry:

    def __init__(self):

        self.registry = {}

    def register(
        self,
        block_type,
        metadata,
    ):

        self.registry[block_type] = metadata

    def unregister(
        self,
        block_type,
    ):

        self.registry.pop(
            block_type,
            None,
        )

    def get(
        self,
        block_type,
    ):

        return self.registry.get(
            block_type,
        )

    def all(self):

        return self.registry.copy()


node_registry = NodeRegistry()
