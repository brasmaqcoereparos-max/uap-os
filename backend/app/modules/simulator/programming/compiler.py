from app.modules.simulator.programming.workspace import workspace


class BlockCompiler:

    def compile(self):

        return {
            "compiled": True,
            "blocks": len(workspace.blocks),
            "connections": len(
                workspace.connections
            ),
        }


compiler = BlockCompiler()
