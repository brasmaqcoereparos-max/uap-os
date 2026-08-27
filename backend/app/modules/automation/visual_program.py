from app.modules.automation.block_graph import (
    BlockGraph,
)

from app.modules.automation.graph_validator import (
    graph_validator,
)

from app.modules.automation.user_level import (
    UserLevel,
)


class VisualProgram:

    def __init__(
        self,
        name="Visual Program",
        user_level=UserLevel.BEGINNER,
    ):
        self.name = str(name)
        self.description = ""

        self.sequence = None
        self.graph = BlockGraph()

        self.user_level = (
            user_level.value
            if isinstance(
                user_level,
                UserLevel,
            )
            else str(user_level)
        )

        self.metadata = {}

    def set_sequence(
        self,
        sequence,
    ):
        self.sequence = sequence
        return self

    def set_graph(
        self,
        graph,
    ):
        self.graph = (
            graph
            if graph is not None
            else BlockGraph()
        )

        return self

    def set_description(
        self,
        description,
    ):
        self.description = str(
            description
        )

        return self

    def set_user_level(
        self,
        level,
    ):
        self.user_level = (
            level.value
            if isinstance(
                level,
                UserLevel,
            )
            else str(level)
        )

        return self

    def set_metadata(
        self,
        name,
        value,
    ):
        self.metadata[
            str(name)
        ] = value

        return self

    def get_blocks(self):
        if self.graph.blocks:
            return list(
                self.graph.blocks.values()
            )

        if self.sequence is None:
            return []

        return self.sequence.get_all()

    def validate(self):
        if self.graph.blocks:
            return graph_validator.report(
                self.graph
            )

        return {
            "valid": True,
            "errors": [],
            "error_count": 0,
        }

    def to_dict(self):
        blocks = []

        for block in self.get_blocks():
            serializer = getattr(
                block,
                "to_dict",
                None,
            )

            blocks.append(
                serializer()
                if callable(serializer)
                else str(block)
            )

        return {
            "name": self.name,
            "description": (
                self.description
            ),
            "user_level": (
                self.user_level
            ),
            "blocks": blocks,
            "connections": (
                self.graph.get_connections()
            ),
            "metadata": dict(
                self.metadata
            ),
            "validation": (
                self.validate()
            ),
            }
