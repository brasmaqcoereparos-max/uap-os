from app.modules.uhal.auto_loader import (
    auto_loader,
)

from app.modules.uhal.register_builtin_drivers import (
    register_builtin_drivers,
)


def initialize_hardware():

    register_builtin_drivers()

    driver = auto_loader.load()

    if driver:

        driver.initialize()

    return driver
