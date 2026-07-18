class CompilerParser:

    def parse(self, canvas):

        nodes = []

        for node in canvas.all_nodes():

            nodes.append(node.to_dict())

        return nodes


compiler_parser = CompilerParser()
