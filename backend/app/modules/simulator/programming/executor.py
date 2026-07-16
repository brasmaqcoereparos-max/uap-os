from app.modules.simulator.programming.workspace import workspace


class BlockExecutor:

    def execute(self):

        execution = []

        for block in workspace.blocks:

            execution.append(
                f"Executing {block.name}"
            )

        return execution


executor = BlockExecutor()
