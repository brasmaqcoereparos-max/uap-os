from app.modules.uhal.register_builtin_drivers import (
    register_builtin_drivers,
)

from app.modules.uhal.drivers.raspberry_pi.raspberry_pi_gpio_driver import (
    raspberry_pi_gpio_driver,
)

from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


def bootstrap_hardware():

    register_builtin_drivers()

    if hardware_registry.get(
        "raspberry_pi_gpio"
    ) is None:

        hardware_registry.register(
            "raspberry_pi_gpio",
            raspberry_pi_gpio_driver,
        )

    return hardware_registry.all()
