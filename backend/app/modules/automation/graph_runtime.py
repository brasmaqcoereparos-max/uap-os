class GraphRuntime:

    def __init__(self):

        self.active = False
        self.graph = None

    def load(self, graph):

        self.graph = graph

    def start(self):

        if self.graph is None:
            return False

        self.active = True

        return True

    def stop(self):

        self.active = False

    def is_active(self):

        return self.active


graph_runtime = GraphRuntime()
