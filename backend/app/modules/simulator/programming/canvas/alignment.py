from app.modules.simulator.programming.canvas.canvas import canvas


class Alignment:

    def left(self):

        nodes = [
            n
            for n in canvas.all_nodes()
            if n.selected
        ]

        if not nodes:
            return

        x = min(
            node.x
            for node in nodes
        )

        for node in nodes:
            node.x = x

    def right(self):

        nodes = [
            n
            for n in canvas.all_nodes()
            if n.selected
        ]

        if not nodes:
            return

        x = max(
            node.x
            for node in nodes
        )

        for node in nodes:
            node.x = x

    def top(self):

        nodes = [
            n
            for n in canvas.all_nodes()
            if n.selected
        ]

        if not nodes:
            return

        y = min(
            node.y
            for node in nodes
        )

        for node in nodes:
            node.y = y

    def bottom(self):

        nodes = [
            n
            for n in canvas.all_nodes()
            if n.selected
        ]

        if not nodes:
            return

        y = max(
            node.y
            for node in nodes
        )

        for node in nodes:
            node.y = y


alignment = Alignment()
