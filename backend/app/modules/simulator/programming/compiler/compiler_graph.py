class CompilerGraph:

    def __init__(self):

        self.nodes = {}

    def add_node(
        self,
        node,
    ):

        self.nodes.setdefault(

            node,

            set(),

        )

    def connect(
        self,
        source,
        target,
    ):

        self.add_node(source)

        self.add_node(target)

        self.nodes[source].add(target)

    def neighbors(
        self,
        node,
    ):

        return list(

            self.nodes.get(

                node,

                set(),

            )

        )

    def clear(self):

        self.nodes.clear()


compiler_graph = CompilerGraph()
