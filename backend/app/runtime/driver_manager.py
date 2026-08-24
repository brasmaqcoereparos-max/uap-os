"""
Gerenciador de drivers do Runtime UAP.
"""


class DriverManager:

    def __init__(self):
        self.drivers = {}

    def register(self, driver):
        if driver is None:
            raise ValueError(
                "Driver não informado."
            )

        driver_id = getattr(
            driver,
            "id",
            None,
        )

        if driver_id is None:
            raise ValueError(
                "Driver sem id."
            )

        self.drivers[driver_id] = driver

        return driver

    def unregister(self, driver_id):
        return self.drivers.pop(
            driver_id,
            None,
        )

    def get(self, driver_id):
        return self.drivers.get(
            driver_id
        )

    def list(self):
        return list(
            self.drivers.values()
        )

    def connect_all(self):

        results = {}

        for driver_id, driver in list(
            self.drivers.items()
        ):

            connect = getattr(
                driver,
                "connect",
                None,
            )

            if callable(connect):

                try:
                    results[driver_id] = connect()

                except Exception as exc:
                    results[driver_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def disconnect_all(self):

        results = {}

        for driver_id, driver in list(
            self.drivers.items()
        ):

            disconnect = getattr(
                driver,
                "disconnect",
                None,
            )

            if callable(disconnect):

                try:
                    results[driver_id] = disconnect()

                except Exception as exc:
                    results[driver_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def update(self):

        results = {}

        for driver_id, driver in list(
            self.drivers.items()
        ):

            update = getattr(
                driver,
                "update",
                None,
            )

            if callable(update):

                try:
                    results[driver_id] = update()

                except Exception as exc:
                    results[driver_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def clear(self):
        self.drivers.clear()

    def count(self):
        return len(
            self.drivers
        )


driver_manager = DriverManager()
