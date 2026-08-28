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

    @staticmethod
    def validate(seconds):
        try:
            value = float(seconds)
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

        return {
            "requested_seconds": (
                seconds
            ),
            "elapsed_seconds": (
                elapsed
            ),
            "completed": True,
        }


automation_delay = AutomationDelay()
