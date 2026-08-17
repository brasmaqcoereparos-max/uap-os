from app.modules.automation.function_block import (
    FunctionBlock,
)


class FunctionBlockFactory:

    def create(
        self,
        block_type,
        name=None,
    ):

        return FunctionBlock(
            block_type,
            name,
        )


function_block_factory = (
    FunctionBlockFactory()
)
