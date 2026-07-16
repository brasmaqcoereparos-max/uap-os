from app.modules.simulator.programming.blocks.base_block import BaseBlock


class DigitalWriteBlock(BaseBlock):

    def __init__(
        self,
        block_id,
        pin,
        value,
    ):
        super().__init__(
            block_id,
            "Digital Write",
        )

        self.pin = pin
        self.value = value

    def execute(self, context):
        context[f"D{self.pin}"] = self.value
        return context
