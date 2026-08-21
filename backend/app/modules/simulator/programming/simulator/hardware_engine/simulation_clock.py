"""
Relógio virtual do simulador UAP.
"""

import time


class SimulationClock:

    def __init__(self):

        self.started_at = None
        self.paused = False
        self.elapsed = 0.0

    def start(self):

        if self.started_at is None:
            self.started_at = time.monotonic()

        self.paused = False

    def pause(self):

        if self.started_at is None:
            return

        self.elapsed += (
            time.monotonic()
            - self.started_at
        )

        self.started_at = None
        self.paused = True

    def reset(self):

        self.started_at = None
        self.paused = False
        self.elapsed = 0.0

    def now(self):

        if self.started_at is None:
            return self.elapsed

        return (
            self.elapsed
            + (
                time.monotonic()
                - self.started_at
            )
        )

    def is_running(self):

        return (
            self.started_at is not None
            and not self.paused
    )
