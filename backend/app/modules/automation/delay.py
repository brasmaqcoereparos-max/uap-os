"""
Temporização básica da automação UAP.

O contrato original de wait(seconds) foi preservado.
"""

import time


class AutomationDelay:

    def __init__(
        self,
        sleep_function=None,
    ):
        self.sleep_function = (
            sleep_function
            or time.sleep
        )

        self.wait_count = 0

        self.total_requested = 0.0
        self.total_elapsed = 0.0

        self.last_result = None

    @staticmethod
    def validate(
        seconds,
    ):
        try:
            value = float(
                seconds
            )

        except (
            TypeError,
            ValueError,
        ) as exc:
            raise ValueError(
                "Tempo de espera inválido."
            ) from exc

        if value < 0:
            raise ValueError(
                "O tempo de espera "
                "não pode ser negativo."
            )

        return value

    def wait(
        self,
        seconds,
    ):
        seconds = self.validate(
            seconds
        )

        started_at = (
            time.monotonic()
        )

        self.sleep_function(
            seconds
        )

        elapsed = (
            time.monotonic()
            - started_at
        )

        self.wait_count += 1

        self.total_requested += (
            seconds
        )

        self.total_elapsed += (
            elapsed
        )

        self.last_result = {
            "requested_seconds": (
                seconds
            ),
            "elapsed_seconds": (
                elapsed
            ),
            "completed": True,
        }

        return dict(
            self.last_result
        )

    def reset_statistics(self):
        self.wait_count = 0

        self.total_requested = 0.0
        self.total_elapsed = 0.0

        self.last_result = None

        return True

    def status(self):
        return {
            "wait_count": (
                self.wait_count
            ),
            "total_requested": (
                self.total_requested
            ),
            "total_elapsed": (
                self.total_elapsed
            ),
            "last_result": (
                self.last_result
            ),
        }


automation_delay = (
    AutomationDelay()
        )
