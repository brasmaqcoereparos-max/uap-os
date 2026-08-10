from app.modules.automation.block_description import (
    BlockDescription,
)


class BlockCatalog:

    def __init__(self):

        self.items = {}

    def register(
        self,
        block_type,
        name,
        simple_description,
        technical_description="",
    ):

        self.items[block_type] = (
            BlockDescription(
                name,
                simple_description,
                technical_description,
            )
        )

    def get(
        self,
        block_type,
    ):

        return self.items.get(
            block_type
        )

    def list(self):

        return dict(self.items)


block_catalog = BlockCatalog()
