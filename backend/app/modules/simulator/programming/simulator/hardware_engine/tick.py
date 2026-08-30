"""
Controle temporal de ticks do simulador UAP.

Mantém:
    Tick(fps=60)
    set_fps()
    wait()
    tick
"""

import time

from app.modules.simulator.programming.simulator.hardware_engine.fps_controller import (
    FPSController,
)


class Tick:

    def __init__(
        self,
        fps=60,
    ):
        self.fps_controller = (
            FPSController(
                fps
            )
        )

        self.tick_count = 0

        self.last_tick = None

        self.last_wait = 0.0

        self.enabled = True

    def set_fps(
        self,
        fps,
    ):
        return (
            self.fps_controller.set_fps(
                fps
            )
        )

    def get_fps(self):
        return (
            self.fps_controller.get_fps()
        )

    def interval(self):
        return (
            self.fps_controller.interval()
        )

    def wait(self):
        if not self.enabled:
            return 0.0

        interval = (
            self.fps_controller.interval()
        )

        start = (
            time.monotonic()
        )

        time.sleep(
            interval
        )

        end = (
            time.monotonic()
        )

        self.last_wait = (
            end - start
        )

        self.last_tick = end
        self.tick_count += 1

        return self.last_wait

    def step(self):
        self.last_tick = (
            time.monotonic()
        )

        self.tick_count += 1

        return self.tick_count

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False

        return True

    def reset(self):
        self.tick_count = 0
        self.last_tick = None
        self.last_wait = 0.0

        return True

    def status(self):
        return {
            "fps": (
                self.get_fps()
            ),
            "interval": (
                self.interval()
            ),
            "tick_count": (
                self.tick_count
            ),
            "last_tick": (
                self.last_tick
            ),
            "last_wait": (
                self.last_wait
            ),
            "enabled": (
                self.enabled
            ),
        }

    def to_dict(self):
        return self.status()


tick = Tick()
