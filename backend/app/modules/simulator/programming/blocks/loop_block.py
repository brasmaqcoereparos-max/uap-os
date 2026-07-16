from app.modules.simulator.programming.blocks.base_block import BaseBlock


class LoopBlock(BaseBlock):

    def __init__(
        self,
        block_id,
        count,
    ):
        super().__init__(
            block_id,
            "Loop",
        )

        self.count = count

    def execute(self, context):
        context["loop"] = self.count
        return context
