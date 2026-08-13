class BlockGraph:

    def __init__(self):

        self.blocks = {}
        self.connections = []

    def add_block(
        self,
        block_id,
        block,
    ):

        self.blocks[
            block_id
        ] = block

    def remove_block(
        self,
        block_id,
    ):

        self.blocks.pop(
            block_id,
            None,
        )

        self.connections = [
            connection
            for connection in self.connections
            if connection["source"] != block_id
            and connection["target"] != block_id
        ]

    def connect(
        self,
        source,
        target,
    ):

        if source not in self.blocks:
            return False

        if target not in self.blocks:
            return False

        self.connections.append(
            {
                "source": source,
                "target": target,
            }
        )

        return True

    def get_blocks(self):

        return dict(self.blocks)

    def get_connections(self):

        return list(
            self.connections
        )
