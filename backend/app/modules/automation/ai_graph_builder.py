from app.modules.automation.graph import AutomationGraph
from app.modules.automation.node import AutomationNode


class AIGraphBuilder:

    def build(self, plan):

        graph = AutomationGraph()

        previous = None

        for index, step in enumerate(plan.steps):

            node = AutomationNode(
                node_id=f"ai_{index}",
                node_type="ai_step",
                name=step,
            )

            graph.add_node(node)

            if previous is not None:
                from app.modules.automation.connection import (
                    AutomationConnection,
                )

                connection = AutomationConnection(
                    previous,
                    "output",
                    node,
                    "input",
                )

                graph.connect(connection)

            previous = node

        return graph


ai_graph_builder = AIGraphBuilder()
