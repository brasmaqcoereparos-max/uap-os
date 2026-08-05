class MQTTClient:

    def __init__(

        self,

        broker="localhost",

        port=1883,

    ):

        self.broker = broker

        self.port = port

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def publish(

        self,

        topic,

        payload,

    ):

        pass

    def subscribe(

        self,

        topic,

    ):

        pass
