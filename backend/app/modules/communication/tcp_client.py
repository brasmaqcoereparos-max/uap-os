class TCPClient:

    def __init__(

        self,

        host="127.0.0.1",

        port=0,

    ):

        self.host = host

        self.port = port

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def send(

        self,

        data,

    ):

        pass

    def receive(self):

        return None
