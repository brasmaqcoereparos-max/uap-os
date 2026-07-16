from app.modules.simulator.programming.workspace import workspace

from app.modules.simulator.programming.blocks.start_block import StartBlock
from app.modules.simulator.programming.blocks.delay_block import DelayBlock
from app.modules.simulator.programming.blocks.if_block import IfBlock
from app.modules.simulator.programming.blocks.loop_block import LoopBlock
from app.modules.simulator.programming.blocks.digital_write_block import DigitalWriteBlock
from app.modules.simulator.programming.blocks.digital_read_block import DigitalReadBlock
from app.modules.simulator.programming.blocks.analog_write_block import AnalogWriteBlock
from app.modules.simulator.programming.blocks.analog_read_block import AnalogReadBlock


class BlockExecutor:

    def __init__(self):
        self.context = {}

    def execute(self):

        execution = []

        self.context = {}

        for block in workspace.blocks:

            execution.append(
                self.execute_block(block)
            )

        return {
            "context": self.context,
            "execution": execution,
        }

    def execute_block(self, block):

        block_type = block.block_type.lower()

        if block_type == "start":
            obj = StartBlock(
                block.id,
                block.name,
            )

        elif block_type == "delay":
            obj = DelayBlock(
                block.id,
                block.config.get(
                    "milliseconds",
                    1000,
                ),
            )

        elif block_type == "if":
            obj = IfBlock(
                block.id,
                block.config.get(
                    "variable",
                    "",
                ),
                block.config.get(
                    "value",
                    0,
                ),
            )

        elif block_type == "loop":
            obj = LoopBlock(
                block.id,
                block.config.get(
                    "count",
                    1,
                ),
            )

        elif block_type == "digital_write":
            obj = DigitalWriteBlock(
                block.id,
                block.config.get(
                    "pin",
                    0,
                ),
                block.config.get(
                    "value",
                    0,
                ),
            )

        elif block_type == "digital_read":
            obj = DigitalReadBlock(
                block.id,
                block.config.get(
                    "pin",
                    0,
                ),
            )

        elif block_type == "analog_write":
            obj = AnalogWriteBlock(
                block.id,
                block.config.get(
                    "pin",
                    0,
                ),
                block.config.get(
                    "value",
                    0,
                ),
            )

        elif block_type == "analog_read":
            obj = AnalogReadBlock(
                block.id,
                block.config.get(
                    "pin",
                    0,
                ),
            )

        else:
            return f"Unknown block: {block.block_type}"

        self.context = obj.execute(self.context)

        return f"Executed: {block.name}"


executor = BlockExecutor()
