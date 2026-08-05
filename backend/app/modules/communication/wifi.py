class WiFiInterface:

    def __init__(

        self,

        ssid="",

        password="",

    ):

        self.ssid = ssid

        self.password = password

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def status(self):

        return self.connected
