from app.modules.automation.block import (
    AutomationBlock,
)


class BlockLibrary:

    def __init__(self):

        self.blocks = {}

    def register(
        self,
        block,
    ):

        self.blocks[
            block.block_type
        ] = block

    def get(
        self,
        block_type,
    ):

        return self.blocks.get(
            block_type
        )

    def list(self):

        return list(
            self.blocks.values()
        )


block_library = BlockLibrary()
