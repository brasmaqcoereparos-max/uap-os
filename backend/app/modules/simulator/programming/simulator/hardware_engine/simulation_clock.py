"""
Relógio virtual do simulador UAP.

Utiliza relógio monotônico para evitar alterações no relógio
do sistema afetarem a simulação.
"""

import time


class SimulationClock:

    def __init__(self):
        self.started_at = None
        self.paused = False
        self.elapsed = 0.0

        self.time_scale = 1.0

    def start(self):
        if self.started_at is None:
            self.started_at = (
                time.monotonic()
            )

        self.paused = False

        return True

    def resume(self):
        return self.start()

    def pause(self):
        if self.started_at is None:
            self.paused = True

            return False

        self.elapsed += (
            time.monotonic()
            - self.started_at
        ) * self.time_scale

        self.started_at = None
        self.paused = True

        return True

    def stop(self):
        return self.pause()

    def reset(self):
        self.started_at = None
        self.paused = False
        self.elapsed = 0.0

        return True

    def now(self):
        if self.started_at is None:
            return self.elapsed

        delta = (
            time.monotonic()
            - self.started_at
        )

        return (
            self.elapsed
            + (
                delta
                * self.time_scale
            )
        )

    def is_running(self):
        return (
            self.started_at
            is not None
            and not self.paused
        )

    def is_paused(self):
        return self.paused

    def set_time_scale(
        self,
        scale,
    ):
        scale = float(scale)

        if scale <= 0:
            raise ValueError(
                "time_scale precisa ser "
                "maior que zero."
            )

        if self.is_running():
            current = self.now()

            self.elapsed = current

            self.started_at = (
                time.monotonic()
            )

        self.time_scale = scale

        return self.time_scale

    def get_time_scale(self):
        return self.time_scale

    def status(self):
        return {
            "time": self.now(),
            "running": (
                self.is_running()
            ),
            "paused": (
                self.paused
            ),
            "time_scale": (
                self.time_scale
            ),
        }


simulation_clock = (
    SimulationClock()
        )
