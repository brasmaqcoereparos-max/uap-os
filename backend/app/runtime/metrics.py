from datetime import datetime


class RuntimeMetrics:

    def __init__(self):
        self.started_at = datetime.now()
        self.cycles = 0
        self.errors = 0
        self.commands = 0

    def cycle(self):
        self.cycles += 1

    def error(self):
        self.errors += 1

    def command(self):
        self.commands += 1

    def reset(self):
        self.started_at = datetime.now()
        self.cycles = 0
        self.errors = 0
        self.commands = 0

    def status(self):
        uptime = (
            datetime.now() - self.started_at
        ).total_seconds()

        return {
            "uptime_seconds": uptime,
            "cycles": self.cycles,
            "errors": self.errors,
            "commands": self.commands,
        }


runtime_metrics = RuntimeMetrics()
