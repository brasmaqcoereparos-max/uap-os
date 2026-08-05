class ModbusTCP:

    def __init__(

        self,

        host="127.0.0.1",

        port=502,

    ):

        self.host = host

        self.port = port

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def read_register(

        self,

        address,

    ):

        return None

    def write_register(

        self,

        address,

        value,

    ):

        pass
