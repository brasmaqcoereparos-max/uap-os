class GraphExecutor:

    def __init__(self):

        self.running = False

    def start(self):

        self.running = True

    def stop(self):

        self.running = False

    def execute(self, graph):

        if not self.running:
            return False

        for connection in graph.connections:

            connection.transfer()

        return True


graph_executor = GraphExecutor()
