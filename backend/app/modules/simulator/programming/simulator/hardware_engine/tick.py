import time

from app.modules.simulator.programming.simulator.hardware_engine.fps_controller import (
    FPSController,
)


class Tick:

    def __init__(
        self,
        fps=60,
    ):

        self.fps_controller = FPSController(
            fps
        )

    def set_fps(
        self,
        fps,
    ):

        self.fps_controller.set_fps(
            fps
        )

    def wait(self):

        time.sleep(
            self.fps_controller.interval()
        )


tick = Tick()
