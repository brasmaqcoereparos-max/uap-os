import time
from threading import Lock


class Scheduler:

    def __init__(self):
        self.jobs = []
        self.lock = Lock()

    def add_job(self, interval: float, callback):
        with self.lock:
            self.jobs.append(
                {
                    "interval": interval,
                    "callback": callback,
                    "last_run": 0,
                }
            )

    def remove_all(self):
        with self.lock:
            self.jobs.clear()

    def execute(self):
        now = time.time()

        with self.lock:
            for job in self.jobs:
                if now - job["last_run"] >= job["interval"]:
                    job["last_run"] = now
                    job["callback"]()


scheduler = Scheduler()
