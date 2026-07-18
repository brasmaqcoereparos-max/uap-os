class DeviceConnection:

    def __init__(self):

        self.connections = {}

    def connect(
        self,
        device,
        port,
    ):

        self.connections[device] = port

    def disconnect(
        self,
        device,
    ):

        self.connections.pop(
            device,
            None,
        )

    def port(
        self,
        device,
    ):

        return self.connections.get(device)

    def connected(
        self,
        device,
    ):

        return device in self.connections

    def clear(self):

        self.connections.clear()

    def all(self):

        return self.connections.copy()


device_connection = DeviceConnection()
