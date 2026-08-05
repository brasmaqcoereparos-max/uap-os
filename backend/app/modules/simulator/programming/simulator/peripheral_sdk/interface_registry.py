class InterfaceRegistry:

    def __init__(self):

        self.interfaces = {}

    def register(

        self,

        interface,

    ):

        self.interfaces[interface.name] = interface

    def get(

        self,

        name,

    ):

        return self.interfaces.get(name)

    def all(self):

        return self.interfaces.copy()


interface_registry = InterfaceRegistry()
