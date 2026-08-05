class WebSocketClient:

    def __init__(

        self,

        url="ws://localhost",

    ):

        self.url = url

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def send(

        self,

        message,

    ):

        pass

    def receive(self):

        return None
