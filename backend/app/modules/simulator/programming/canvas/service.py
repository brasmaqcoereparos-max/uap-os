from app.modules.simulator.programming.canvas.canvas import canvas


class CanvasService:

    def status(self):
        return canvas.status()

    def move_node(
        self,
        node_id: str,
        x: int,
        y: int,
    ):
        node = canvas.nodes.get(node_id)

        if node is None:
            return None

        node.x = x
        node.y = y

        return node.to_dict()

    def rename_node(
        self,
        node_id: str,
        name: str,
    ):
        node = canvas.nodes.get(node_id)

        if node is None:
            return None

        node.name = name

        return node.to_dict()

    def update_config(
        self,
        node_id: str,
        config: dict,
    ):
        node = canvas.nodes.get(node_id)

        if node is None:
            return None

        node.config.update(config)

        return node.to_dict()


canvas_service = CanvasService()
