import time


class AutomationDelay:

    def wait(
        self,
        seconds,
    ):

        if seconds < 0:
            raise ValueError(
                "Delay cannot be negative"
            )

        time.sleep(seconds)


automation_delay = AutomationDelay()
