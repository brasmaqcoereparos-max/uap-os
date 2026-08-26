class PinManager:

    def __init__(self):
        self._pins = {}

    def reserve(self, pin, owner):
        if pin in self._pins:
            raise RuntimeError(
                f"GPIO {pin} já está reservado."
            )

        self._pins[pin] = owner
        return True

    def release(self, pin):
        return self._pins.pop(
            pin,
            None,
        )

    def owner(self, pin):
        return self._pins.get(pin)

    def is_reserved(self, pin):
        return pin in self._pins

    def available(self, pin):
        return not self.is_reserved(pin)

    def clear(self):
        self._pins.clear()

    def all(self):
        return dict(self._pins)


pin_manager = PinManager()
