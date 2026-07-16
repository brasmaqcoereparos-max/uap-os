from app.modules.simulator.programming.blocks.base_block import BaseBlock


class StartBlock(BaseBlock):

    def execute(self, context):
        context["started"] = True
        return context
