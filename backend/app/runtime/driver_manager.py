"""
Gerenciador de drivers do Runtime UAP.
"""


class DriverManager:

    def __init__(self):

        self.drivers = {}

    def register(
        self,
        driver_id,
        driver,
    ):

        if not driver_id:
            raise ValueError(
                "driver_id obrigatório."
            )

        if driver is None:
            raise ValueError(
                "Driver não informado."
            )

        self.drivers[
            str(driver_id)
        ] = driver

        return driver

    def unregister(
        self,
        driver_id,
    ):

        return self.drivers.pop(
            str(driver_id),
            None,
        )

    def get(
        self,
        driver_id,
    ):

        return self.drivers.get(
            str(driver_id)
        )

    def list(self):

        return list(
            self.drivers.values()
        )

    def count(self):

        return len(
            self.drivers
        )

    def clear(self):

        self.drivers.clear()

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

            if not callable(connect):
                continue

            try:

                results[
                    driver_id
                ] = connect()

            except Exception as exc:

                results[
                    driver_id
                ] = {
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

            if not callable(disconnect):
                continue

            try:

                results[
                    driver_id
                ] = disconnect()

            except Exception as exc:

                results[
                    driver_id
                ] = {
                    "success": False,
                    "error": str(exc),
                }

        return results


driver_manager = DriverManager()
