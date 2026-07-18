class DeviceStatistics:

    def __init__(self):

        self.reset()

    def reset(self):

        self.executions = 0
        self.errors = 0

    def executed(self):

        self.executions += 1

    def error(self):

        self.errors += 1

    def to_dict(self):

        return {
            "executions": self.executions,
            "errors": self.errors,
            "success": self.executions - self.errors,
            "success_rate": (
                100
                if self.executions == 0
                else round(
                    ((self.executions - self.errors) / self.executions) * 100,
                    2,
                )
            ),
        }


device_statistics = DeviceStatistics()
