from app.modules.simulator.programming.compiler.compiler_node_registry import (
    compiler_node_registry,
)


class CompilerDispatcher:

    def dispatch(

        self,

        node,

        context,

    ):

        handler = compiler_node_registry.get(

            node.block_type

        )

        if handler is None:

            return

        handler.compile(

            node,

            context,

        )


compiler_dispatcher = CompilerDispatcher()
