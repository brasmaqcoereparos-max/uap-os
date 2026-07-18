class DeviceBus:

    def __init__(self):

        self.messages = []

    def send(
        self,
        source,
        target,
        payload,
    ):

        self.messages.append(

            {

                "source": source,

                "target": target,

                "payload": payload,

            }

        )

    def receive(self):

        if not self.messages:

            return None

        return self.messages.pop(0)

    def clear(self):

        self.messages.clear()

    def size(self):

        return len(self.messages)


device_bus = DeviceBus()
