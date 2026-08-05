class ConnectionManager:

    def __init__(self):

        self.connections = []

    def add(

        self,

        connection,

    ):

        self.connections.append(connection)

    def remove(

        self,

        connection,

    ):

        if connection in self.connections:

            self.connections.remove(connection)

    def all(self):

        return self.connections.copy()


connection_manager = ConnectionManager()
