import time

from app.modules.simulator.programming.simulator.hardware_engine.fps_controller import (
    fps_controller,
)


class Tick:

    def wait(self):

        time.sleep(

            fps_controller.interval,

        )


tick = Tick()
