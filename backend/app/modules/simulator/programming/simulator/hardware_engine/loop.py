from app.modules.simulator.programming.simulator.hardware_engine.engine import (
    hardware_engine,
)

from app.modules.simulator.programming.simulator.hardware_engine.device_runner import (
    device_runner,
)

from app.modules.simulator.programming.simulator.hardware_engine.tick import (
    tick,
)

from app.modules.simulator.programming.simulator.hardware_engine.simulation_clock import (
    simulation_clock,
)

from app.modules.simulator.programming.simulator.hardware_engine.statistics import (
    statistics,
)


class HardwareLoop:

    def run(self):

        hardware_engine.start()

        simulation_clock.reset()

        while hardware_engine.is_running():

            simulation_clock.update()

            device_runner.update()

            statistics.frame()

            tick.wait()


hardware_loop = HardwareLoop()
