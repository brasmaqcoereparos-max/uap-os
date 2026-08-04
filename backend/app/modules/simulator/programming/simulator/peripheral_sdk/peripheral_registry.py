class PeripheralRegistry:

    def __init__(self):

        self._registry = {}

    def register(

        self,

        peripheral_class,

    ):

        self._registry[peripheral_class.name] = peripheral_class

    def get(

        self,

        name,

    ):

        return self._registry.get(name)

    def all(self):

        return self._registry.copy()


peripheral_registry = PeripheralRegistry()
