"""
Dispositivo virtual base da API pública do simulador UAP.
"""

import time


class VirtualDevice:

    def __init__(
        self,
        device_id,
        name,
        device_type,
    ):
        self.id = device_id
        self.name = name
        self.type = device_type

        self.state = False

        self.enabled = True

        self.metadata = {}

        self.created_at = (
            time.time()
        )

        self.updated_at = None

        self.change_count = 0

    def _touch(self):
        self.updated_at = (
            time.time()
        )

        self.change_count += 1

    def on(self):
        if not self.enabled:
            return self.state

        if not self.state:
            self.state = True
            self._touch()

        return self.state

    def off(self):
        if self.state:
            self.state = False
            self._touch()

        return self.state

    def toggle(self):
        if not self.enabled:
            return self.state

        self.state = (
            not self.state
        )

        self._touch()

        return self.state

    def set_state(
        self,
        state,
    ):
        state = bool(
            state
        )

        if self.state != state:
            self.state = state
            self._touch()

        return self.state

    def get_state(self):
        return self.state

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False
        self.off()

        return True

    def update(self):
        return self.state

    def reset(self):
        self.state = False

        self.updated_at = None
        self.change_count = 0

        return True

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

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "state": self.state,
        }

    def detailed_status(self):
        return {
            **self.status(),
            "enabled": (
                self.enabled
            ),
            "created_at": (
                self.created_at
            ),
            "updated_at": (
                self.updated_at
            ),
            "change_count": (
                self.change_count
            ),
            "metadata": dict(
                self.metadata
            ),
        }

    def to_dict(self):
        return self.status()
