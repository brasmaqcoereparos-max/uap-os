class BluetoothInterface:

    def __init__(

        self,

        device_name="UAP",

    ):

        self.device_name = device_name

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def status(self):

        return self.connected
