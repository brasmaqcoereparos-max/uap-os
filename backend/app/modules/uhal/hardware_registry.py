class HardwareRegistry:

    def __init__(self):

        self._drivers = {}

    def register(

        self,

        name,

        driver,

    ):

        self._drivers[name.lower()] = driver

    def unregister(

        self,

        name,

    ):

        self._drivers.pop(

            name.lower(),

            None,

        )

    def get(

        self,

        name,

    ):

        return self._drivers.get(

            name.lower(),

        )

    def all(self):

        return dict(

            self._drivers,

        )


hardware_registry = HardwareRegistry()
