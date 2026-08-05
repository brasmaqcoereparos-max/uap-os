class EthernetInterface:

    def __init__(

        self,

        ip="192.168.0.100",

        mask="255.255.255.0",

        gateway="192.168.0.1",

    ):

        self.ip = ip

        self.mask = mask

        self.gateway = gateway

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def status(self):

        return self.connected
