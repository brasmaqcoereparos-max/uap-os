"""
Dispositivo virtual base do Hardware Virtual Engine.

Todo elemento executável dentro do VirtualWorld pode herdar
desta classe.

Contrato original preservado:

    VirtualDevice(name)
    device.name
    device.enabled
    device.update()
    device.reset()
"""

import uuid


class VirtualDevice:

    def __init__(
        self,
        name,
    ):
        self.name = str(
            name
        )

        self.enabled = True

        self.id = str(
            uuid.uuid4()
        )

        self.initialized = False
        self.running = False

        self.update_count = 0
        self.reset_count = 0

        self.state = {}
        self.metadata = {}

        self.last_error = None

    def initialize(self):
        self.initialized = True

        self.last_error = None

        return True

    def start(self):
        if not self.enabled:
            return False

        if not self.initialized:
            self.initialize()

        self.running = True

        return True

    def stop(self):
        self.running = False

        return True

    def shutdown(self):
        self.running = False
        self.initialized = False

        return True

    def update(self):
        if not self.enabled:
            return None

        self.update_count += 1

        return self.state

    def reset(self):
        self.state.clear()

        self.running = False

        self.update_count = 0
        self.reset_count += 1

        self.last_error = None

        return True

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False
        self.running = False

        return True

    def set_state(
        self,
        key,
        value,
    ):
        self.state[
            str(key)
        ] = value

        return value

    def get_state(
        self,
        key,
        default=None,
    ):
        return self.state.get(
            str(key),
            default,
        )

    def remove_state(
        self,
        key,
    ):
        return self.state.pop(
            str(key),
            None,
        )

    def clear_state(self):
        count = len(
            self.state
        )

        self.state.clear()

        return count

    def set_metadata(
        self,
        key,
        value,
    ):
        self.metadata[
            str(key)
        ] = value

        return value

    def get_metadata(
        self,
        key,
        default=None,
    ):
        return self.metadata.get(
            str(key),
            default,
        )

    def add_error(
        self,
        error,
    ):
        self.last_error = str(
            error
        )

        return self.last_error

    def clear_error(self):
        self.last_error = None

        return True

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "enabled": self.enabled,
            "initialized": (
                self.initialized
            ),
            "running": self.running,
            "update_count": (
                self.update_count
            ),
            "reset_count": (
                self.reset_count
            ),
            "state": dict(
                self.state
            ),
            "last_error": (
                self.last_error
            ),
        }

    def snapshot(self):
        return {
            **self.status(),
            "metadata": dict(
                self.metadata
            ),
        }

    def restore(
        self,
        snapshot,
    ):
        if not isinstance(
            snapshot,
            dict,
        ):
            raise TypeError(
                "Snapshot do dispositivo "
                "precisa ser um dicionário."
            )

        self.enabled = bool(
            snapshot.get(
                "enabled",
                True,
            )
        )

        self.initialized = bool(
            snapshot.get(
                "initialized",
                False,
            )
        )

        self.running = bool(
            snapshot.get(
                "running",
                False,
            )
        )

        self.update_count = int(
            snapshot.get(
                "update_count",
                0,
            )
        )

        self.reset_count = int(
            snapshot.get(
                "reset_count",
                0,
            )
        )

        self.state = dict(
            snapshot.get(
                "state",
                {},
            )
        )

        self.metadata = dict(
            snapshot.get(
                "metadata",
                {},
            )
        )

        self.last_error = (
            snapshot.get(
                "last_error"
            )
        )

        return True

    def to_dict(self):
        return self.snapshot()
