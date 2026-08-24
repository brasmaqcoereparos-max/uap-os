import time
from threading import Lock


class Scheduler:

    def __init__(self):
        self.jobs = []
        self.lock = Lock()

    def add_job(
        self,
        interval: float,
        callback,
    ):

        try:
            interval = max(
                0.0,
                float(interval),
            )
        except (
            TypeError,
            ValueError,
        ):
            raise ValueError(
                "Intervalo inválido."
            )

        if not callable(callback):
            raise TypeError(
                "Callback deve ser chamável."
            )

        with self.lock:

            self.jobs.append(
                {
                    "interval": interval,
                    "callback": callback,
                    "last_run": 0.0,
                }
            )

    def remove_all(self):

        with self.lock:
            self.jobs.clear()

    def execute(self):

        now = time.monotonic()

        with self.lock:
            jobs = list(
                self.jobs
            )

        for job in jobs:

            if (
                now
                - job["last_run"]
                >= job["interval"]
            ):

                job["last_run"] = now

                try:
                    job["callback"]()
                except Exception:
                    # Um job não pode derrubar
                    # todo o Runtime.
                    continue


scheduler = Scheduler()
