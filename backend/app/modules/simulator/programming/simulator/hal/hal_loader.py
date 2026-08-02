from app.modules.simulator.programming.simulator.hal.hal_manager import (
    hal_manager,
)

from app.modules.simulator.programming.simulator.hal.simulator_hal import (
    SimulatorHAL,
)


class HALLoader:

    loaded = False

    @classmethod
    def load(cls):

        if cls.loaded:

            return

        hal_manager.set_driver(

            SimulatorHAL(),

        )

        cls.loaded = True
