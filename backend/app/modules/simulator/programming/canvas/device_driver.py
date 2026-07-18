class DeviceDriver:

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

    def remove(
        self,
        name,
    ):

        self.drivers.pop(
            name,
            None,
        )

    def clear(self):

        self.drivers.clear()

    def all(self):

        return list(self.drivers.keys())


device_driver = DeviceDriver()
