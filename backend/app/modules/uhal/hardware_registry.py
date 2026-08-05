class HardwareRegistry:

    def __init__(self):

        self.drivers = {}

    def register(

        self,

        name,

        driver,

    ):

        self.drivers[name] = driver

    def get(

        self,

        name,

    ):

        return self.drivers.get(name)

    def all(self):

        return self.drivers.copy()


hardware_registry = HardwareRegistry()
