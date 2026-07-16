from app.modules.simulator.programming.canvas.canvas import canvas


class CanvasService:

    def status(self):
        return canvas.status()

    def get_node(self, node_id):

        node = canvas.get_node(node_id)

        if node:
            return node.to_dict()

        return None

    def move_node(self, node_id, x, y):

        node = canvas.get_node(node_id)

        if node is None:
            return None

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

    def rename_node(self, node_id, name):

        node = canvas.get_node(node_id)

        if node is None:
            return None

        node.name = name

        return node.to_dict()

    def update_config(
        self,
        node_id,
        config,
    ):

        node = canvas.get_node(node_id)

        if node is None:
            return None

        node.config.update(config)

        return node.to_dict()

    def disconnect(
        self,
        source,
        target,
    ):

        canvas.disconnect(
            source,
            target,
        )

        return {
            "message": "Disconnected"
        }


canvas_service = CanvasService()
