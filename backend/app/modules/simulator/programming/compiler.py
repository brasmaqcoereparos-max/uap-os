from app.modules.simulator.programming.canvas.canvas import (
    canvas,
)


class BlockCompiler:

    def compile(self):

        graph = []

        for node in canvas.nodes.values():

            outputs = []

            for connection in canvas.connections:

                if connection.source == node.id:

                    outputs.append(
                        connection.target
                    )

            graph.append(
                {
                    "id": node.id,
                    "name": node.name,
                    "type": node.block_type,
                    "outputs": outputs,
                }
            )

        return {
            "compiled": True,
            "nodes": len(canvas.nodes),
            "connections": len(
                canvas.connections
            ),
            "graph": graph,
        }


compiler = BlockCompiler()
