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

from app.modules.simulator.programming.simulator.hardware_engine.state_manager import (
    state_manager,
)

from app.modules.simulator.programming.simulator.hardware_engine.event_processor import (
    event_processor,
)


class HardwareLoop:

    def run(self):

        hardware_engine.start()

        state_manager.start()

        simulation_clock.reset()

        while hardware_engine.is_running():

            if state_manager.is_paused():

                tick.wait()

                continue

            simulation_clock.update()

            event_processor.process()

            device_runner.update()

            statistics.frame()

            tick.wait()


hardware_loop = HardwareLoop()
