"""
Executor dos blocos visuais do UAP.

Executa diretamente o Canvas atual e mantém o contexto
da simulação separado do compilador de código.
"""

from app.modules.simulator.programming.canvas.canvas import (
    canvas,
)

from app.modules.simulator.programming.blocks.start_block import (
    StartBlock,
)
from app.modules.simulator.programming.blocks.delay_block import (
    DelayBlock,
)
from app.modules.simulator.programming.blocks.if_block import (
    IfBlock,
)
from app.modules.simulator.programming.blocks.loop_block import (
    LoopBlock,
)
from app.modules.simulator.programming.blocks.digital_write_block import (
    DigitalWriteBlock,
)
from app.modules.simulator.programming.blocks.digital_read_block import (
    DigitalReadBlock,
)
from app.modules.simulator.programming.blocks.analog_write_block import (
    AnalogWriteBlock,
)
from app.modules.simulator.programming.blocks.analog_read_block import (
    AnalogReadBlock,
)


class BlockExecutor:

    def __init__(self):

        self.context = {}

    def execute(
        self,
        source_canvas=None,
    ):

        active_canvas = (
            source_canvas
            if source_canvas is not None
            else canvas
        )

        self.context = {}

        execution = []

        nodes = self._execution_order(
            active_canvas
        )

        for node in nodes:

            execution.append(
                self.execute_block(
                    node
                )
            )

        return {
            "context": dict(
                self.context
            ),
            "execution": execution,
        }

    def _execution_order(
        self,
        active_canvas,
    ):

        nodes = {
            node.id: node
            for node in active_canvas.all_nodes()
        }

        connections = (
            active_canvas.all_connections()
        )

        previous = {
            node_id: []
            for node_id in nodes
        }

        next_nodes = {
            node_id: []
            for node_id in nodes
        }

        for connection in connections:

            source = connection.source
            target = connection.target

            if source not in nodes:
                continue

            if target not in nodes:
                continue

            next_nodes[
                source
            ].append(target)

            previous[
                target
            ].append(source)

        queue = [
            node_id
            for node_id in nodes
            if not previous[node_id]
        ]

        order = []

        while queue:

            current = queue.pop(0)

            order.append(
                nodes[current]
            )

            for target in next_nodes[current]:

                previous[target].remove(
                    current
                )

                if not previous[target]:
                    queue.append(target)

        if len(order) != len(nodes):

            raise ValueError(
                "O Canvas contém um ciclo "
                "ou uma conexão inválida."
            )

        return order

    def execute_block(
        self,
        block,
    ):

        block_type = (
            getattr(
                block,
                "block_type",
                None,
            )
            or getattr(
                block,
                "type",
                None,
            )
            or ""
        )

        block_type = str(
            block_type
        ).lower().replace(
            " ",
            "_",
        )

        block_id = getattr(
            block,
            "id",
            None,
        )

        block_name = getattr(
            block,
            "name",
            block_type,
        )

        config = getattr(
            block,
            "config",
            {},
        )

        if not isinstance(
            config,
            dict,
        ):
            config = {}

        if block_type == "start":

            obj = StartBlock(
                block_id,
                block_name,
            )

        elif block_type == "delay":

            obj = DelayBlock(
                block_id,
                config.get(
                    "milliseconds",
                    1000,
                ),
            )

        elif block_type == "if":

            obj = IfBlock(
                block_id,
                config.get(
                    "variable",
                    "",
                ),
                config.get(
                    "value",
                    0,
                ),
            )

        elif block_type == "loop":

            obj = LoopBlock(
                block_id,
                config.get(
                    "count",
                    1,
                ),
            )

        elif block_type == "digital_write":

            obj = DigitalWriteBlock(
                block_id,
                config.get(
                    "pin",
                    0,
                ),
                config.get(
                    "value",
                    0,
                ),
            )

        elif block_type == "digital_read":

            obj = DigitalReadBlock(
                block_id,
                config.get(
                    "pin",
                    0,
                ),
            )

        elif block_type == "analog_write":

            obj = AnalogWriteBlock(
                block_id,
                config.get(
                    "pin",
                    0,
                ),
                config.get(
                    "value",
                    0,
                ),
            )

        elif block_type == "analog_read":

            obj = AnalogReadBlock(
                block_id,
                config.get(
                    "pin",
                    0,
                ),
            )

        else:

            return {
                "id": block_id,
                "status": "unknown",
                "block_type": block_type,
            }

        self.context = obj.execute(
            self.context
        )

        return {
            "id": block_id,
            "name": block_name,
            "status": "executed",
            "block_type": block_type,
        }


executor = BlockExecutor()
