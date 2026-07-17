import time


class ExecutionTimer:

    def __init__(self):

        self.started = None

        self.finished = None

    def start(self):

        self.started = time.perf_counter()

    def stop(self):

        self.finished = time.perf_counter()

    def elapsed(self):

        if self.started is None:

            return 0

        end = self.finished or time.perf_counter()

        return round(

            end - self.started,

            6,

        )

    def reset(self):

        self.started = None

        self.finished = None


execution_timer = ExecutionTimer()
