class FunctionBlockRegistry:

    def __init__(self):

        self.blocks = {}

    def register(
        self,
        block_type,
        factory,
    ):

        self.blocks[
            block_type
        ] = factory

    def unregister(
        self,
        block_type,
    ):

        self.blocks.pop(
            block_type,
            None,
        )

    def get(
        self,
        block_type,
    ):

        return self.blocks.get(
            block_type
        )

    def exists(
        self,
        block_type,
    ):

        return block_type in self.blocks

    def get_all(self):

        return dict(
            self.blocks
        )


function_block_registry = (
    FunctionBlockRegistry()
)
