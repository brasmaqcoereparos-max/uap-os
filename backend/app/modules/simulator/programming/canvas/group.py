import uuid


class CanvasGroup:

    def __init__(
        self,
        name,
        nodes,
    ):

        self.id = str(uuid.uuid4())

        self.name = name

        self.nodes = list(nodes)

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "nodes": self.nodes,
        }


class GroupManager:

    def __init__(self):

        self.groups = {}

    def create(
        self,
        name,
        nodes,
    ):

        group = CanvasGroup(
            name,
            nodes,
        )

        self.groups[group.id] = group

        return group

    def remove(self, group_id):

        self.groups.pop(
            group_id,
            None,
        )

    def all(self):

        return [
            g.to_dict()
            for g in self.groups.values()
        ]


groups = GroupManager()
