class VirtualDevice:

    def __init__(
        self,
        device_id,
        name,
        device_type,
    ):
        self.id = device_id
        self.name = name
        self.type = device_type
        self.state = False

    def on(self):
        self.state = True

    def off(self):
        self.state = False

    def toggle(self):
        self.state = not self.state

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "state": self.state,
        }
