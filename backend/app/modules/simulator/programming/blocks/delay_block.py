import time

from app.modules.simulator.programming.blocks.base_block import BaseBlock


class DelayBlock(BaseBlock):

    def __init__(
        self,
        block_id,
        milliseconds,
    ):
        super().__init__(
            block_id,
            "Delay",
        )

        self.milliseconds = milliseconds

    def execute(self, context):
        time.sleep(
            self.milliseconds / 1000
        )

        return context
