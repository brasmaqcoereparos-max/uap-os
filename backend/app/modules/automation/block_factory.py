from app.modules.automation.block import (
    AutomationBlock,
)

from app.modules.automation.block_library import (
    block_library,
)


class BlockFactory:

    def create(
        self,
        block_type,
    ):

        template = block_library.get(
            block_type
        )

        if template is None:
            return None

        block = AutomationBlock(
            template.block_type,
            template.name,
            template.description,
        )

        block.inputs = list(
            template.inputs
        )

        block.outputs = list(
            template.outputs
        )

        block.parameters = dict(
            template.parameters
        )

        return block


block_factory = BlockFactory()
