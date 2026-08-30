"""
Gerenciador de interrupções virtuais do simulador UAP.
"""

from app.modules.simulator.programming.simulator.hardware_engine.interrupt import (
    Interrupt,
)


class InterruptManager:

    def __init__(self):
        self.interrupts = {}

        self.trigger_count = 0

    def register(
        self,
        pin,
        callback,
        mode="change",
        replace=True,
    ):
        if (
            pin in self.interrupts
            and not replace
        ):
            return False

        interrupt = Interrupt(
            pin=pin,
            callback=callback,
            mode=mode,
        )

        self.interrupts[
            pin
        ] = interrupt

        return interrupt

    def unregister(
        self,
        pin,
    ):
        return self.interrupts.pop(
            pin,
            None,
        )

    def get(
        self,
        pin,
    ):
        return self.interrupts.get(
            pin
        )

    def trigger(
        self,
        pin,
        *args,
        **kwargs,
    ):
        interrupt = (
            self.interrupts.get(
                pin
            )
        )

        if interrupt is None:
            return False

        result = (
            interrupt.trigger(
                *args,
                **kwargs,
            )
        )

        if result:
            self.trigger_count += 1

        return result

    def evaluate(
        self,
        pin,
        old_value,
        new_value,
    ):
        interrupt = (
            self.interrupts.get(
                pin
            )
        )

        if interrupt is None:
            return False

        result = (
            interrupt.evaluate(
                old_value,
                new_value,
            )
        )

        if result:
            self.trigger_count += 1

        return result

    def enable(
        self,
        pin,
    ):
        interrupt = self.get(
            pin
        )

        if interrupt is None:
            return False

        return interrupt.enable()

    def disable(
        self,
        pin,
    ):
        interrupt = self.get(
            pin
        )

        if interrupt is None:
            return False

        return interrupt.disable()

    def clear(self):
        count = len(
            self.interrupts
        )

        self.interrupts.clear()

        return count

    def count(self):
        return len(
            self.interrupts
        )

    def all(self):
        return list(
            self.interrupts.values()
        )

    def reset(self):
        for interrupt in (
            self.interrupts.values()
        ):
            interrupt.reset()

        self.trigger_count = 0

        return True

    def status(self):
        return {
            "count": self.count(),
            "trigger_count": (
                self.trigger_count
            ),
            "interrupts": {
                str(pin): (
                    interrupt.to_dict()
                )
                for pin, interrupt
                in self.interrupts.items()
            },
        }


interrupt_manager = (
    InterruptManager()
        )
