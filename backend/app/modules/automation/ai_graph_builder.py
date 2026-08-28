from app.modules.automation.graph import (
    AutomationGraph,
)

from app.modules.automation.node import (
    AutomationNode,
)

from app.modules.automation.connection import (
    AutomationConnection,
)


class AIGraphBuilder:
    @staticmethod
    def _step_data(
        step,
        index,
    ):
        if isinstance(step, dict):
            return {
                "id": str(
                    step.get(
                        "id",
                        f"ai_{index}",
                    )
                ),
                "name": str(
                    step.get(
                        "name",
                        step.get(
                            "description",
                            f"Etapa {index + 1}",
                        ),
                    )
                ),
                "type": str(
                    step.get(
                        "type",
                        "ai_step",
                    )
                ),
                "metadata": dict(
                    step.get(
                        "metadata",
                        {},
                    )
                ),
            }

        return {
            "id": f"ai_{index}",
            "name": str(step),
            "type": "ai_step",
            "metadata": {},
        }

    def build(self, plan):
        if plan is None:
            raise ValueError(
                "Plano não informado."
            )

        graph = AutomationGraph()

        previous = None

        for index, step in enumerate(
            getattr(
                plan,
                "steps",
                [],
            )
        ):
            data = self._step_data(
                step,
                index,
            )

            node = AutomationNode(
                node_id=data["id"],
                node_type=data["type"],
                name=data["name"],
                metadata=data[
                    "metadata"
                ],
            )

            node.set_output(
                "output",
                None,
            )

            node.set_input(
                "input",
                None,
            )

            graph.add_node(node)

            if previous is not None:
                connection = (
                    AutomationConnection(
                        source_node=(
                            previous
                        ),
                        source_output=(
                            "output"
                        ),
                        target_node=node,
                        target_input=(
                            "input"
                        ),
                    )
                )

                graph.connect(
                    connection
                )

            previous = node

        return graph


ai_graph_builder = (
    AIGraphBuilder()
)
