class GraphValidator:

    def validate(self, graph):

        errors = []

        if not graph.nodes:
            errors.append(
                "Automation graph is empty"
            )

        for connection in graph.connections:

            if connection.source_node.node_id not in graph.nodes:
                errors.append(
                    "Source node not found"
                )

            if connection.target_node.node_id not in graph.nodes:
                errors.append(
                    "Target node not found"
                )

        return errors

    def is_valid(self, graph):

        return len(
            self.validate(graph)
        ) == 0


graph_validator = GraphValidator()
