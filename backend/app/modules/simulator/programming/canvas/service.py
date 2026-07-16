from app.modules.simulator.programming.canvas.canvas import canvas
from app.modules.simulator.programming.canvas.history import history
from app.modules.simulator.programming.canvas.commands import commands


class CanvasService:

    def status(self):
        return canvas.status()

    def save_history(self):
        history.save(canvas)

    def undo(self):
        return history.undo()

    def redo(self):
        return history.redo()

    def copy(self, node_id):

        return commands.copy(node_id)

    def paste(self):

        self.save_history()

        node = commands.paste()

        if node:
            return node.to_dict()

        return None

    def duplicate(self, node_id):

        self.save_history()

        node = commands.duplicate(node_id)

        if node:
            return node.to_dict()

        return None

    def get_node(self, node_id):

        node = canvas.get_node(node_id)

        if node:
            return node.to_dict()

        return None

    def move_node(self, node_id, x, y):

        node = canvas.get_node(node_id)

        if node is None or node.locked:
            return None

        self.save_history()

        node.x = x
        node.y = y

        return node.to_dict()

    def select_node(self, node_id):

        for n in canvas.all_nodes():
            n.selected = False

        node = canvas.get_node(node_id)

        if node is None:
            return None

        node.selected = True

        return node.to_dict()

    def lock_node(self, node_id):

        node = canvas.get_node(node_id)

        if node is None:
            return None

        self.save_history()
        node.locked = True

        return node.to_dict()

    def unlock_node(self, node_id):

        node = canvas.get_node(node_id)

        if node is None:
            return None

        self.save_history()
        node.locked = False

        return node.to_dict()

    def hide_node(self, node_id):

        node = canvas.get_node(node_id)

        if node is None:
            return None

        self.save_history()
        node.visible = False

        return node.to_dict()

    def show_node(self, node_id):

        node = canvas.get_node(node_id)

        if node is None:
            return None

        self.save_history()
        node.visible = True

        return node.to_dict()

    def rename_node(self, node_id, name):

        node = canvas.get_node(node_id)

        if node is None:
            return None

        self.save_history()
        node.name = name

        return node.to_dict()

    def update_config(self, node_id, config):

        node = canvas.get_node(node_id)

        if node is None:
            return None

        self.save_history()
        node.config.update(config)

        return node.to_dict()

    def set_zoom(self, zoom):

        canvas.set_zoom(zoom)

        return canvas.status()

    def move_view(self, dx, dy):

        canvas.move_view(dx, dy)

        return canvas.status()

    def disconnect(self, source, target):

        self.save_history()

        canvas.disconnect(source, target)

        return {
            "message": "Disconnected"
        }


canvas_service = CanvasService()
