from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class DriverLoader:

    def load(
        self,
        name,
        initialize=True,
    ):
        driver = hardware_registry.get(
            name
        )

        if driver is None:
            raise KeyError(
                f"Driver '{name}' não encontrado."
            )

        if initialize:
            method = getattr(
                driver,
                "initialize",
                None,
            )

            if callable(method):
                method()

        return driver

    def unload(
        self,
        name,
    ):
        driver = hardware_registry.get(
            name
        )

        if driver is None:
            return None

        method = getattr(
            driver,
            "shutdown",
            None,
        )

        if callable(method):
            method()

        return driver

    def available(self):
        return hardware_registry.all()


driver_loader = DriverLoader()
