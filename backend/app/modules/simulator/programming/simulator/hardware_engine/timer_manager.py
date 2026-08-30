"""
Gerenciador dos timers virtuais do Hardware Engine.

Mantém:
    timers
    add(timer)
    update()
    clear()
    timer_manager
"""


class TimerManager:

    def __init__(self):
        self.timers = []

        self.update_count = 0
        self.fire_count = 0

        self.last_error = None

    def add(
        self,
        timer,
    ):
        if timer is None:
            return None

        if timer not in self.timers:
            self.timers.append(
                timer
            )

        return timer

    def remove(
        self,
        timer,
    ):
        if timer not in self.timers:
            return False

        self.timers.remove(
            timer
        )

        return True

    def get(
        self,
        index,
    ):
        try:
            return self.timers[
                int(index)
            ]

        except (
            IndexError,
            ValueError,
            TypeError,
        ):
            return None

    def update(self):
        results = []

        self.update_count += 1

        for timer in list(
            self.timers
        ):
            try:
                result = (
                    timer.update()
                )

                results.append(
                    result
                )

                if result:
                    self.fire_count += 1

            except Exception as exc:
                self.last_error = (
                    str(exc)
                )

                raise

        self.last_error = None

        return results

    def start_all(self):
        results = []

        for timer in self.timers:
            method = getattr(
                timer,
                "start",
                None,
            )

            if callable(method):
                results.append(
                    method()
                )

        return results

    def stop_all(self):
        results = []

        for timer in self.timers:
            method = getattr(
                timer,
                "stop",
                None,
            )

            if callable(method):
                results.append(
                    method()
                )

        return results

    def reset_all(self):
        results = []

        for timer in self.timers:
            method = getattr(
                timer,
                "reset",
                None,
            )

            if callable(method):
                results.append(
                    method()
                )

        self.fire_count = 0
        self.update_count = 0
        self.last_error = None

        return results

    def clear(self):
        count = len(
            self.timers
        )

        self.timers.clear()

        return count

    def count(self):
        return len(
            self.timers
        )

    def all(self):
        return list(
            self.timers
        )

    def status(self):
        return {
            "count": (
                self.count()
            ),
            "update_count": (
                self.update_count
            ),
            "fire_count": (
                self.fire_count
            ),
            "last_error": (
                self.last_error
            ),
        }

    def to_dict(self):
        return self.status()


timer_manager = TimerManager()
