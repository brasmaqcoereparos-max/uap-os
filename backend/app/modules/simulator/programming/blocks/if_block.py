from app.modules.simulator.programming.blocks.base_block import BaseBlock


class IfBlock(BaseBlock):

    def __init__(
        self,
        block_id,
        variable,
        value,
    ):
        super().__init__(
            block_id,
            "If",
        )

        self.variable = variable
        self.value = value

    def execute(self, context):
        context["condition"] = (
            context.get(self.variable)
            == self.value
        )

        return context
