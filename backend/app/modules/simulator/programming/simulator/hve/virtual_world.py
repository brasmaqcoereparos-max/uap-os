"""
Mundo virtual do Hardware Virtual Engine.

O VirtualWorld mantém os dispositivos virtuais e executa
seus ciclos de atualização.

Contrato original preservado:

    world.devices
    world.add(device)
    world.update()
    world.reset()
"""

from app.modules.simulator.programming.simulator.hve.virtual_clock import (
    virtual_clock,
)


class VirtualWorld:

    def __init__(self):
        self.devices = []

        self.clock = (
            virtual_clock
        )

        self.enabled = True
        self.running = False

        self.update_count = 0

        self.last_error = None

    def add(
        self,
        device,
    ):
        if device is None:
            return None

        if device not in self.devices:
            self.devices.append(
                device
            )

        return device

    def remove(
        self,
        device,
    ):
        if device not in self.devices:
            return False

        self.devices.remove(
            device
        )

        return True

    def remove_by_name(
        self,
        name,
    ):
        device = self.get(
            name
        )

        if device is None:
            return None

        self.devices.remove(
            device
        )

        return device

    def get(
        self,
        name,
    ):
        name = str(
            name
        )

        for device in self.devices:
            if str(
                getattr(
                    device,
                    "name",
                    "",
                )
            ) == name:
                return device

        return None

    def get_by_id(
        self,
        device_id,
    ):
        device_id = str(
            device_id
        )

        for device in self.devices:
            if str(
                getattr(
                    device,
                    "id",
                    "",
                )
            ) == device_id:
                return device

        return None

    def exists(
        self,
        name,
    ):
        return (
            self.get(name)
            is not None
        )

    def all(self):
        return list(
            self.devices
        )

    def count(self):
        return len(
            self.devices
        )

    def initialize(self):
        results = []

        for device in self.devices:
            method = getattr(
                device,
                "initialize",
                None,
            )

            if callable(method):
                results.append(
                    method()
                )

        return results

    def start(self):
        if not self.enabled:
            return False

        self.initialize()

        for device in self.devices:
            method = getattr(
                device,
                "start",
                None,
            )

            if callable(method):
                method()

        self.running = True

        return True

    def stop(self):
        for device in self.devices:
            method = getattr(
                device,
                "stop",
                None,
            )

            if callable(method):
                method()

        self.running = False

        return True

    def update(self):
        if not self.enabled:
            return []

        results = []

        try:
            self.clock.next()

            for device in list(
                self.devices
            ):
                if not getattr(
                    device,
                    "enabled",
                    True,
                ):
                    continue

                result = (
                    device.update()
                )

                results.append(
                    result
                )

            self.update_count += 1

            self.last_error = None

            return results

        except Exception as exc:
            self.last_error = str(
                exc
            )

            raise

    def reset(self):
        results = []

        for device in list(
            self.devices
        ):
            result = (
                device.reset()
            )

            results.append(
                result
            )

        self.clock.reset()

        self.running = False

        self.update_count = 0

        self.last_error = None

        return results

    def clear(self):
        count = len(
            self.devices
        )

        self.devices.clear()

        return count

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False
        self.running = False

        return True

    def snapshot(self):
        devices = []

        for device in self.devices:
            snapshot = getattr(
                device,
                "snapshot",
                None,
            )

            devices.append({
                "id": getattr(
                    device,
                    "id",
                    None,
                ),
                "name": getattr(
                    device,
                    "name",
                    None,
                ),
                "state": (
                    snapshot()
                    if callable(snapshot)
                    else None
                ),
            })

        return {
            "enabled": self.enabled,
            "running": self.running,
            "update_count": (
                self.update_count
            ),
            "clock": (
                self.clock.snapshot()
            ),
            "devices": devices,
            "last_error": (
                self.last_error
            ),
        }

    def status(self):
        return {
            "enabled": self.enabled,
            "running": self.running,
            "device_count": (
                self.count()
            ),
            "update_count": (
                self.update_count
            ),
            "tick": (
                self.clock.tick
            ),
            "time": (
                self.clock.time()
            ),
            "last_error": (
                self.last_error
            ),
        }

    def to_dict(self):
        return self.snapshot()


virtual_world = VirtualWorld()
