from app.modules.automation.block_graph import (
    BlockGraph,
)

from app.modules.automation.graph_validator import (
    graph_validator,
)


class VisualFlow:

    def __init__(
        self,
        name="Visual Flow",
    ):
        self.name = str(name)
        self.description = ""
        self.graph = BlockGraph()

    def set_graph(
        self,
        graph,
    ):
        if graph is None:
            self.graph = BlockGraph()
        else:
            self.graph = graph

        return self

    def set_description(
        self,
        description,
    ):
        self.description = str(
            description
        )

        return self

    def add_block(
        self,
        block,
        block_id=None,
    ):
        selected_id = (
            block_id
            or getattr(
                block,
                "block_id",
                None,
            )
        )

        if selected_id is None:
            raise ValueError(
                "Bloco não possui ID."
            )

        self.graph.add_block(
            selected_id,
            block,
        )

        return block

    def remove_block(
        self,
        block_id,
    ):
        return self.graph.remove_block(
            block_id
        )

    def connect(
        self,
        source,
        target,
        source_port=None,
        target_port=None,
    ):
        return self.graph.connect(
            source=source,
            target=target,
            source_port=source_port,
            target_port=target_port,
        )

    def disconnect(
        self,
        source,
        target,
        source_port=None,
        target_port=None,
    ):
        return self.graph.disconnect(
            source=source,
            target=target,
            source_port=source_port,
            target_port=target_port,
        )

    def validate(self):
        return graph_validator.report(
            self.graph
        )

    def get_flow(self):
        return {
            "name": self.name,
            "description": (
                self.description
            ),
            "blocks": (
                self.graph.get_blocks()
            ),
            "connections": (
                self.graph.get_connections()
            ),
            "validation": (
                self.validate()
            ),
        }

    def to_dict(self):
        blocks = {}

        for block_id, block in (
            self.graph.blocks.items()
        ):
            serializer = getattr(
                block,
                "to_dict",
                None,
            )

            blocks[block_id] = (
                serializer()
                if callable(serializer)
                else str(block)
            )

        return {
            "name": self.name,
            "description": (
                self.description
            ),
            "blocks": blocks,
            "connections": (
                self.graph.get_connections()
            ),
            "validation": (
                self.validate()
            ),
        }

    def clear(self):
        self.graph.clear()
