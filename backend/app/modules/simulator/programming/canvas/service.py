from app.modules.simulator.programming.canvas.canvas import canvas
from app.modules.simulator.programming.canvas.history import history
from app.modules.simulator.programming.canvas.commands import commands
from app.modules.simulator.programming.canvas.grid import grid
from app.modules.simulator.programming.canvas.ruler import ruler


class CanvasService:

    def status(self):

        data = canvas.status()

        data["ruler"] = ruler.to_dict()

        return data

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

    def grid_status():
        return grid.to_dict()

    def show_grid():
        grid.show()
        return grid.to_dict()

    def hide_grid():
        grid.hide()
        return grid.to_dict()

    def enable_snap():
        grid.enable_snap()
        return grid.to_dict()

    def disable_snap():
        grid.disable_snap()
        return grid.to_dict()

    def set_grid_size(size):
        grid.set_size(size)
        return grid.to_dict()

    def ruler_status(self):

        return ruler.to_dict()

    def enable_ruler(self):

        ruler.enable()

        return ruler.to_dict()

    def disable_ruler(self):

        ruler.disable()

        return ruler.to_dict()

    def move_ruler(self, x, y):

        ruler.set_origin(x, y)

        return ruler.to_dict()

    def get_node(self, node_id):

        node = canvas.get_node(node_id)

        if node:
            return node.to_dict()

        return None

    def move_node(self, node_id, x, y):

        node = canvas.get_node(node_id)

        if node is None:
            return None

        if node.locked:
            return None

        self.save_history()

        if grid.snap:

            x = round(x / grid.size) * grid.size
            y = round(y / grid.size) * grid.size

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
