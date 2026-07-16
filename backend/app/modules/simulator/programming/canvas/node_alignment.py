class NodeAlignment:

    def left(self, nodes):

        if not nodes:
            return

        x = min(node.x for node in nodes)

        for node in nodes:

            node.x = x

    def right(self, nodes):

        if not nodes:
            return

        x = max(node.x for node in nodes)

        for node in nodes:

            node.x = x

    def top(self, nodes):

        if not nodes:
            return

        y = min(node.y for node in nodes)

        for node in nodes:

            node.y = y

    def bottom(self, nodes):

        if not nodes:
            return

        y = max(node.y for node in nodes)

        for node in nodes:

            node.y = y

    def center_horizontal(self, nodes):

        if not nodes:
            return

        cx = sum(node.x for node in nodes) / len(nodes)

        for node in nodes:

            node.x = int(cx)

    def center_vertical(self, nodes):

        if not nodes:
            return

        cy = sum(node.y for node in nodes) / len(nodes)

        for node in nodes:

            node.y = int(cy)


node_alignment = NodeAlignment()
