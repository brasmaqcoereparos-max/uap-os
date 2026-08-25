class HardwareRegistry:

    def __init__(self):

        self._drivers = {}

    def register(
        self,
        name,
        driver,
    ):

        if not name:
            raise ValueError(
                "Nome do driver obrigatório."
            )

        if driver is None:
            raise ValueError(
                "Driver não informado."
            )

        key = str(
            name
        ).strip().lower()

        self._drivers[key] = driver

        return driver

    def unregister(
        self,
        name,
    ):

        key = str(
            name
        ).strip().lower()

        return self._drivers.pop(
            key,
            None,
        )

    def get(
        self,
        name,
    ):

        if name is None:
            return None

        key = str(
            name
        ).strip().lower()

        return self._drivers.get(
            key
        )

    def all(self):

        return dict(
            self._drivers
        )

    def names(self):

        return list(
            self._drivers.keys()
        )

    def clear(self):

        self._drivers.clear()

    def count(self):

        return len(
            self._drivers
        )


hardware_registry = HardwareRegistry()
