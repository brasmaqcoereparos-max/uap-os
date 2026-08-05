class WireManager:

    def __init__(self):

        self.wires = []

    def add(

        self,

        wire,

    ):

        self.wires.append(wire)

    def remove(

        self,

        wire,

    ):

        if wire in self.wires:

            self.wires.remove(wire)

    def all(self):

        return self.wires.copy()


wire_manager = WireManager()
