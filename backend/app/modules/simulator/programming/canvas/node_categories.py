class NodeCategories:

    def __init__(self):

        self.categories = {}

    def register(
        self,
        block_type,
        category,
    ):

        self.categories[block_type] = category

    def get(
        self,
        block_type,
    ):

        return self.categories.get(
            block_type,
            "General",
        )

    def all(self):

        return self.categories.copy()

    def blocks(
        self,
        category,
    ):

        return [

            block

            for block, value

            in self.categories.items()

            if value == category

        ]


node_categories = NodeCategories()
