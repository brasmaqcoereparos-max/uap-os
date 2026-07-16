from app.modules.simulator.programming.blocks.base_block import BaseBlock


class DigitalReadBlock(BaseBlock):

    def __init__(
        self,
        block_id,
        pin,
    ):
        super().__init__(
            block_id,
            "Digital Read",
        )

        self.pin = pin

    def execute(self, context):
        context["value"] = context.get(
            f"D{self.pin}",
            0,
        )

        return context
