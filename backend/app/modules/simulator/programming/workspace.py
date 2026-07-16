class Workspace:

    def __init__(self):
        self.blocks = []
        self.connections = []

    def add_block(self, block):
        self.blocks.append(block)

    def connect(
        self,
        source,
        target,
    ):
        self.connections.append(
            {
                "source": source,
                "target": target,
            }
        )

    def clear(self):
        self.blocks.clear()
        self.connections.clear()

    def status(self):
        return {
            "blocks": [
                b.to_dict()
                for b in self.blocks
            ],
            "connections": self.connections,
        }


workspace = Workspace()
