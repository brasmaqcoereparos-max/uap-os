from app.modules.simulator.programming.compiler.compiler_parser import (
    compiler_parser,
)
from app.modules.simulator.programming.compiler.compiler_optimizer import (
    compiler_optimizer,
)


class CompilerPipeline:

    def process(self, canvas):

        nodes = compiler_parser.parse(canvas)

        nodes = compiler_optimizer.optimize(nodes)

        return nodes


compiler_pipeline = CompilerPipeline()
