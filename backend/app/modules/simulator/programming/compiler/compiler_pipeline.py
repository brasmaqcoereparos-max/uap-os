"""
Pipeline principal do compilador UAP.

Canvas
  ↓
Parser
  ↓
Optimizer
  ↓
IR Builder
  ↓
IR
"""

from app.modules.simulator.programming.compiler.compiler_parser import (
    compiler_parser,
)

from app.modules.simulator.programming.compiler.compiler_optimizer import (
    compiler_optimizer,
)

from app.modules.simulator.programming.compiler.compiler_ir_builder import (
    IRBuilder,
)


class CompilerPipeline:

    def process(
        self,
        canvas,
    ):

        nodes = compiler_parser.parse(
            canvas
        )

        nodes = compiler_optimizer.optimize(
            nodes
        )

        builder = IRBuilder()

        for node in nodes:

            node_type = (
                node.get("type")
                or node.get("block_type")
                or "unknown"
            )

            builder.emit(
                opcode=node_type,
                operands=[
                    node.get("id")
                ],
                metadata={
                    "name": node.get(
                        "name"
                    ),
                    "config": node.get(
                        "config",
                        {},
                    ),
                    "x": node.get(
                        "x"
                    ),
                    "y": node.get(
                        "y"
                    ),
                },
            )

        return builder.build()


compiler_pipeline = CompilerPipeline()
