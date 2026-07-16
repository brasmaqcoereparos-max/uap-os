from app.modules.simulator.programming.compiler import (
    compiler,
)

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

        for block in compiler.execution_order():

            execution.append(
                self.execute_block(block)
            )

        return {
            "context": self.context,
            "execution": execution,
        }

    def execute_block(self, block):

        t = block.block_type.lower()

        if t == "start":
            obj = StartBlock(block.id, block.name)

        elif t == "delay":
            obj = DelayBlock(
                block.id,
                block.config.get(
                    "milliseconds",
                    1000,
                ),
            )

        elif t == "if":
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

        elif t == "loop":
            obj = LoopBlock(
                block.id,
                block.config.get(
                    "count",
                    1,
                ),
            )

        elif t == "digital_write":
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

        elif t == "digital_read":
            obj = DigitalReadBlock(
                block.id,
                block.config.get(
                    "pin",
                    0,
                ),
            )

        elif t == "analog_write":
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

        elif t == "analog_read":
            obj = AnalogReadBlock(
                block.id,
                block.config.get(
                    "pin",
                    0,
                ),
            )

        else:
            return f"Unknown block {t}"

        self.context = obj.execute(
            self.context
        )

        return f"Executed {block.name}"


executor = BlockExecutor()
