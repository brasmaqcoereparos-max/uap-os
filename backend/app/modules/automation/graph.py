class AutomationGraph:

    def __init__(self):

        self.nodes = {}

        self.connections = []

    def add_node(
        self,
        node,
    ):

        self.nodes[node.node_id] = node

    def remove_node(
        self,
        node_id,
    ):

        self.nodes.pop(
            node_id,
            None,
        )

        self.connections = [
            connection
            for connection in self.connections
            if connection.source_node.node_id != node_id
            and connection.target_node.node_id != node_id
        ]

    def connect(
        self,
        connection,
    ):

        self.connections.append(
            connection
        )

    def get_node(
        self,
        node_id,
    ):

        return self.nodes.get(node_id)

    def list_nodes(self):

        return list(
            self.nodes.values()
        )

    def list_connections(self):

        return list(
            self.connections
    )
