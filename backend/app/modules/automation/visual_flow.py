class VisualFlow:

    def __init__(self):

        self.graph = None

    def set_graph(
        self,
        graph,
    ):

        self.graph = graph

    def get_flow(self):

        if self.graph is None:

            return {
                "blocks": {},
                "connections": [],
            }

        return {
            "blocks": self.graph.get_blocks(),
            "connections": self.graph.get_connections(),
        }

    def clear(self):

        self.graph = None
