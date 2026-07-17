from app.modules.simulator.programming.canvas.node import Node
from app.modules.simulator.programming.canvas.node_style import node_style


class NodeFactory:

    def create(

        self,

        name,

        block_type,

        x,

        y,

        config=None,

    ):

        node = Node(

            name=name,

            block_type=block_type,

            x=x,

            y=y,

            config=config or {},

        )

        node.style = node_style.get()

        return node


node_factory = NodeFactory()
