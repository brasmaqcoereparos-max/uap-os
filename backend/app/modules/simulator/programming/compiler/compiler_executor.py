from app.modules.simulator.programming.compiler.compiler_dispatcher import (
    compiler_dispatcher,
)
from app.modules.simulator.programming.compiler.compiler_node_factory import (
    compiler_node_factory,
)


class CompilerExecutor:

    def execute(

        self,

        nodes,

        context,

    ):

        for item in nodes:

            node = compiler_node_factory.create(item)

            compiler_dispatcher.dispatch(

                node,

                context,

            )


compiler_executor = CompilerExecutor()
