"""
Estatísticas do Hardware Virtual Engine.

Mantém:
    frame()
    reset()
    frames

e acrescenta métricas básicas de desempenho e erros.
"""

import time


class Statistics:

    def __init__(self):
        self.frames = 0

        self.started_at = (
            time.monotonic()
        )

        self.last_frame_at = None

        self.errors = 0

        self.events = 0
        self.timer_fires = 0

    def frame(self):
        self.frames += 1

        self.last_frame_at = (
            time.monotonic()
        )

        return self.frames

    def error(self):
        self.errors += 1

        return self.errors

    def event(self):
        self.events += 1

        return self.events

    def timer_fire(self):
        self.timer_fires += 1

        return self.timer_fires

    def uptime(self):
        return max(
            0.0,
            (
                time.monotonic()
                - self.started_at
            ),
        )

    def fps(self):
        uptime = self.uptime()

        if uptime <= 0:
            return 0.0

        return (
            self.frames
            / uptime
        )

    def reset(self):
        self.frames = 0
        self.errors = 0
        self.events = 0
        self.timer_fires = 0

        self.started_at = (
            time.monotonic()
        )

        self.last_frame_at = None

        return True

    def status(self):
        return {
            "frames": (
                self.frames
            ),
            "errors": (
                self.errors
            ),
            "events": (
                self.events
            ),
            "timer_fires": (
                self.timer_fires
            ),
            "uptime": (
                self.uptime()
            ),
            "fps": (
                self.fps()
            ),
            "last_frame_at": (
                self.last_frame_at
            ),
        }

    def to_dict(self):
        return self.status()


statistics = Statistics()
