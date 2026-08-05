class LoRaInterface:

    def __init__(

        self,

        frequency=915000000,

    ):

        self.frequency = frequency

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def status(self):

        return self.connected
