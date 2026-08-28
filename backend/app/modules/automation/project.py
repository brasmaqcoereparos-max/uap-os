import uuid

from app.modules.automation.graph import (
    AutomationGraph,
)


class AutomationProject:
    def __init__(
        self,
        name,
        project_id=None,
        description="",
        settings=None,
        metadata=None,
    ):
        self.project_id = (
            str(project_id)
            if project_id is not None
            else str(uuid.uuid4())
        )

        self.name = str(name)
        self.description = str(
            description
        )

        self.graph = AutomationGraph()

        self.settings = dict(
            settings or {}
        )

        self.metadata = dict(
            metadata or {}
        )

        self.enabled = True

    @property
    def id(self):
        return self.project_id

    def set_setting(
        self,
        name,
        value,
    ):
        self.settings[
            str(name)
        ] = value

        return value

    def get_setting(
        self,
        name,
        default=None,
    ):
        return self.settings.get(
            str(name),
            default,
        )

    def remove_setting(
        self,
        name,
    ):
        return self.settings.pop(
            str(name),
            None,
        )

    def set_graph(self, graph):
        if graph is None:
            raise ValueError(
                "Grafo não informado."
            )

        self.graph = graph
        return graph

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def to_dict(self):
        graph_data = (
            self.graph.to_dict()
            if hasattr(
                self.graph,
                "to_dict",
            )
            else None
        )

        return {
            "id": self.project_id,
            "name": self.name,
            "description": (
                self.description
            ),
            "enabled": self.enabled,
            "settings": dict(
                self.settings
            ),
            "metadata": dict(
                self.metadata
            ),
            "graph": graph_data,
    }
