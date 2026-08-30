"""
Timer virtual do simulador UAP.

Mantém o contrato original:

    VirtualTimer(
        interval,
        callback,
    )

    update()

Agora utiliza relógio monotônico para evitar problemas
causados por alteração do horário do sistema.
"""

import time


class VirtualTimer:

    def __init__(
        self,
        interval,
        callback,
    ):
        self.interval = float(
            interval
        )

        if self.interval < 0:
            raise ValueError(
                "O intervalo do timer "
                "não pode ser negativo."
            )

        self.callback = callback

        self.last = (
            time.monotonic()
        )

        self.enabled = True
        self.running = True

        self.repeat = True

        self.fire_count = 0

        self.last_fire = None

    def start(self):
        self.running = True
        self.enabled = True

        self.last = (
            time.monotonic()
        )

        return True

    def stop(self):
        self.running = False

        return True

    def pause(self):
        return self.stop()

    def resume(self):
        return self.start()

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False

        return True

    def ready(
        self,
        now=None,
    ):
        if (
            not self.enabled
            or not self.running
        ):
            return False

        if now is None:
            now = (
                time.monotonic()
            )

        return (
            now - self.last
            >= self.interval
        )

    def trigger(self):
        if not callable(
            self.callback
        ):
            return False

        self.callback()

        self.fire_count += 1

        self.last_fire = (
            time.monotonic()
        )

        if not self.repeat:
            self.running = False

        return True

    def update(self):
        now = (
            time.monotonic()
        )

        if not self.ready(
            now
        ):
            return False

        self.last = now

        return self.trigger()

    def reset(self):
        self.last = (
            time.monotonic()
        )

        self.fire_count = 0
        self.last_fire = None

        self.running = True

        return True

    def set_interval(
        self,
        interval,
    ):
        interval = float(
            interval
        )

        if interval < 0:
            raise ValueError(
                "O intervalo do timer "
                "não pode ser negativo."
            )

        self.interval = interval

        return self.interval

    def elapsed(self):
        return max(
            0.0,
            (
                time.monotonic()
                - self.last
            ),
        )

    def remaining(self):
        return max(
            0.0,
            (
                self.interval
                - self.elapsed()
            ),
        )

    def status(self):
        return {
            "interval": (
                self.interval
            ),
            "enabled": (
                self.enabled
            ),
            "running": (
                self.running
            ),
            "repeat": (
                self.repeat
            ),
            "fire_count": (
                self.fire_count
            ),
            "last_fire": (
                self.last_fire
            ),
            "elapsed": (
                self.elapsed()
            ),
            "remaining": (
                self.remaining()
            ),
        }

    def to_dict(self):
        return self.status()
