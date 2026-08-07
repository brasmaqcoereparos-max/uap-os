from uuid import uuid4


class Device:

    def __init__(

        self,

        name,

        device_type,

    ):

        self.id = str(uuid4())

        self.name = name

        self.device_type = device_type

        self.enabled = True

        self.connected = False

        self.properties = {}

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False"""
Universal Device Engine
"""
