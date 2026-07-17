class NodeGroup:

    def __init__(self):

        self.groups = {}

    def create(
        self,
        name,
        node_ids,
    ):

        self.groups[name] = list(node_ids)

    def add(
        self,
        name,
        node_id,
    ):

        self.groups.setdefault(
            name,
            []
        )

        if node_id not in self.groups[name]:

            self.groups[name].append(node_id)

    def remove(
        self,
        name,
        node_id,
    ):

        if name in self.groups:

            if node_id in self.groups[name]:

                self.groups[name].remove(node_id)

    def delete(
        self,
        name,
    ):

        self.groups.pop(
            name,
            None,
        )

    def get(
        self,
        name,
    ):

        return self.groups.get(
            name,
            [],
        )

    def all(self):

        return self.groups.copy()


node_group = NodeGroup()
