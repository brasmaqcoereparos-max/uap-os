class CompilerNodeRegistry:

    def __init__(self):

        self.registry = {}

    def register(

        self,

        block_type,

        handler,

    ):

        self.registry[block_type] = handler

    def get(self, block_type):

        return self.registry.get(block_type)

    def exists(self, block_type):

        return block_type in self.registry

    def clear(self):

        self.registry.clear()


compiler_node_registry = CompilerNodeRegistry()
