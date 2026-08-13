class BlockFlow:

    def __init__(self):

        self.connections = []

    def connect(
        self,
        source,
        target,
    ):

        connection = {
            "source": source,
            "target": target,
        }

        self.connections.append(
            connection
        )

        return connection

    def disconnect(
        self,
        source,
        target,
    ):

        self.connections = [
            item
            for item in self.connections
            if not (
                item["source"] == source
                and item["target"] == target
            )
        ]

    def get_connections(self):

        return list(
            self.connections
        )
