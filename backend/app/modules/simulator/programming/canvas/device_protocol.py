
class DeviceProtocol:

    def __init__(self):

        self.protocols = {}

    def register(
        self,
        device,
        protocol,
    ):

        self.protocols[device] = protocol

    def protocol(
        self,
        device,
    ):

        return self.protocols.get(
            device,
            "UNKNOWN",
        )

    def remove(
        self,
        device,
    ):

        self.protocols.pop(
            device,
            None,
        )

    def clear(self):

        self.protocols.clear()

    def all(self):

        return self.protocols.copy()


device_protocol = DeviceProtocol()
