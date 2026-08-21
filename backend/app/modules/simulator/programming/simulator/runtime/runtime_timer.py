"""
Temporizadores do runtime UAP.
"""

import time


class RuntimeTimer:

    def __init__(self):

        self._timers = {}
        self._next_id = 1

    def create(
        self,
        duration,
        callback=None,
        repeat=False,
    ):

        timer_id = self._next_id
        self._next_id += 1

        duration = max(
            0.0,
            float(duration),
        )

        self._timers[timer_id] = {
            "duration": duration,
            "started": time.monotonic(),
            "callback": callback,
            "repeat": bool(repeat),
            "active": True,
        }

        return timer_id

    def cancel(
        self,
        timer_id,
    ):

        timer = self._timers.get(
            timer_id
        )

        if timer is None:
            return False

        timer["active"] = False

        return True

    def exists(
        self,
        timer_id,
    ):

        return timer_id in self._timers

    def update(self):

        now = time.monotonic()

        expired = []

        for timer_id, timer in list(
            self._timers.items()
        ):

            if not timer["active"]:
                expired.append(timer_id)
                continue

            elapsed = (
                now
                - timer["started"]
            )

            if elapsed < timer["duration"]:
                continue

            callback = timer["callback"]

            if callable(callback):
                callback()

            if timer["repeat"]:

                timer["started"] = now

            else:

                timer["active"] = False
                expired.append(timer_id)

        for timer_id in expired:
            self._timers.pop(
                timer_id,
                None,
            )

    def clear(self):

        self._timers.clear()

    def reset(self):

        self.clear()
        self._next_id = 1


runtime_timer = RuntimeTimer()
