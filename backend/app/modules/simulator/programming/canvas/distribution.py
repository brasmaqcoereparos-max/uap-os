class Distribution:

    def horizontal(self, nodes):

        if len(nodes) < 3:
            return

        nodes.sort(key=lambda n: n.x)

        left = nodes[0].x

        right = nodes[-1].x

        spacing = (right - left) / (len(nodes) - 1)

        for i, node in enumerate(nodes):

            node.x = int(left + spacing * i)

    def vertical(self, nodes):

        if len(nodes) < 3:
            return

        nodes.sort(key=lambda n: n.y)

        top = nodes[0].y

        bottom = nodes[-1].y

        spacing = (bottom - top) / (len(nodes) - 1)

        for i, node in enumerate(nodes):

            node.y = int(top + spacing * i)


distribution = Distribution()
