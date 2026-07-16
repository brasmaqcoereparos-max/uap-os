from app.modules.simulator.programming.canvas.canvas import canvas
from app.modules.simulator.programming.canvas.clipboard import clipboard


class CanvasCommands:

    def copy(self, node_id):

        node = canvas.get_node(node_id)

        if node is None:
            return False

        clipboard.copy(node)

        return True

    def paste(self):

        node = clipboard.paste()

        if node is None:
            return None

        canvas.add_node(node)

        return node

    def duplicate(self, node_id):

        ok = self.copy(node_id)

        if not ok:
            return None

        return self.paste()


commands = CanvasCommands()
