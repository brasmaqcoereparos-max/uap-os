class BlockPort:

    def __init__(
        self,
        name,
        port_type="generic",
    ):

        self.name = name
        self.port_type = port_type

    def to_dict(self):

        return {
            "name": self.name,
            "type": self.port_type,
        }
