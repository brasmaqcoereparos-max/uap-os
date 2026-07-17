class NodeIconManager:

    def __init__(self):

        self.icons = {}

    def register(
        self,
        block_type,
        icon,
    ):

        self.icons[block_type] = icon

    def get(
        self,
        block_type,
    ):

        return self.icons.get(
            block_type,
            "mdi-help-circle",
        )

    def remove(
        self,
        block_type,
    ):

        self.icons.pop(
            block_type,
            None,
        )

    def all(self):

        return self.icons.copy()


node_icons = NodeIconManager()
