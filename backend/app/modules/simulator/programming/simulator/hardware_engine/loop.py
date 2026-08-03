from app.modules.simulator.programming.simulator.hardware_engine.engine import (
    hardware_engine,
)

from app.modules.simulator.programming.simulator.hardware_engine.device_runner import (
    device_runner,
)

from app.modules.simulator.programming.simulator.hardware_engine.tick import (
    tick,
)


class HardwareLoop:

    def run(self):

        hardware_engine.start()

        while hardware_engine.is_running():

            device_runner.update()

            tick.wait()


hardware_loop = HardwareLoop() o 
