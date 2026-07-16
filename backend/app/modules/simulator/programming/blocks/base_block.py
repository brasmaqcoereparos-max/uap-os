class BaseBlock:

    def __init__(
        self,
        block_id: str,
        name: str,
    ):
        self.id = block_id
        self.name = name

    def execute(self, context):
        return context
