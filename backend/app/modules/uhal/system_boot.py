from app.modules.uhal.auto_loader import (
    auto_loader,
)

from app.modules.uhal.register_builtin_drivers import (
    register_builtin_drivers,
)


def initialize_hardware(
    board=None,
):

    register_builtin_drivers()

    return auto_loader.load(
        board=board
    )
