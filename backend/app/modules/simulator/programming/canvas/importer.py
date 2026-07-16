import json

from app.modules.simulator.programming.canvas.canvas import canvas
from app.modules.simulator.programming.canvas.node import Node


class CanvasImporter:

    def import_json(
        self,
        text,
    ):

        data = json.loads(text)

        canvas.clear()

        for item in data["nodes"]:

            node = Node(

                name=item["name"],

                block_type=item["block_type"],

                x=item["x"],

                y=item["y"],

                config=item["config"],

            )

            node.id = item["id"]

            node.selected = item["selected"]

            node.visible = item["visible"]

            node.locked = item["locked"]

            canvas.add_node(node)

        return canvas.status()


importer = CanvasImporter()
