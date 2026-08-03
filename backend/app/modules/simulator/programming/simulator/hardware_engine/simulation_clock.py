import time


class SimulationClock:

    def __init__(self):

        self.start_time = time.time()

        self.current_time = 0.0

    def update(self):

        self.current_time = time.time() - self.start_time

    def reset(self):

        self.start_time = time.time()

        self.current_time = 0.0

    def seconds(self):

        return self.current_time


simulation_clock = SimulationClock()
