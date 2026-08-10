class DeviceTag:

    def __init__(
        self,
        name,
        value=None,
        description="",
    ):

        self.name = name
        self.value = value
        self.description = description

    def set(self, value):

        self.value = value

    def get(self):

        return self.value
