"""
Representação de interrupção virtual do simulador UAP.
"""


class Interrupt:

    def __init__(
        self,
        pin,
        callback,
        mode="change",
        enabled=True,
        metadata=None,
    ):
        self.pin = pin
        self.callback = callback

        self.mode = str(
            mode
        ).lower()

        self.enabled = bool(
            enabled
        )

        self.metadata = dict(
            metadata or {}
        )

        self.trigger_count = 0
        self.last_value = None

    def trigger(
        self,
        *args,
        **kwargs,
    ):
        if not self.enabled:
            return False

        if not callable(
            self.callback
        ):
            return False

        self.trigger_count += 1

        self.callback(
            *args,
            **kwargs,
        )

        return True

    def should_trigger(
        self,
        old_value,
        new_value,
    ):
        mode = self.mode

        if mode == "change":
            return (
                old_value
                != new_value
            )

        if mode == "rising":
            return (
                not bool(old_value)
                and bool(new_value)
            )

        if mode == "falling":
            return (
                bool(old_value)
                and not bool(new_value)
            )

        if mode == "high":
            return bool(
                new_value
            )

        if mode == "low":
            return not bool(
                new_value
            )

        return (
            old_value
            != new_value
        )

    def evaluate(
        self,
        old_value,
        new_value,
    ):
        self.last_value = (
            new_value
        )

        if not self.should_trigger(
            old_value,
            new_value,
        ):
            return False

        return self.trigger()

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False

        return True

    def reset(self):
        self.trigger_count = 0
        self.last_value = None

        return True

    def to_dict(self):
        return {
            "pin": self.pin,
            "mode": self.mode,
            "enabled": (
                self.enabled
            ),
            "trigger_count": (
                self.trigger_count
            ),
            "last_value": (
                self.last_value
            ),
            "metadata": dict(
                self.metadata
            ),
        }
