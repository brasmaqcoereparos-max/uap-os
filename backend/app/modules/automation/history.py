import time


class AutomationHistory:

    def __init__(self):

        self.entries = []

    def add(
        self,
        action,
        data=None,
    ):

        self.entries.append(
            {
                "action": action,
                "data": data or {},
                "timestamp": time.time(),
            }
        )

    def list(self):

        return list(self.entries)


automation_history = AutomationHistory()
