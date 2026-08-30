"""
Conexão lógica entre componentes do circuito visual UAP.
"""

import uuid


class Connection:

    def __init__(
        self,
        source,
        source_pin,
        target,
        target_pin,
        connection_id=None,
        enabled=True,
        metadata=None,
    ):
        self.connection_id = (
            str(connection_id)
            if connection_id
            is not None
            else str(uuid.uuid4())
        )

        self.id = self.connection_id

        self.source = source
        self.source_pin = (
            source_pin
        )

        self.target = target
        self.target_pin = (
            target_pin
        )

        self.enabled = bool(
            enabled
        )

        self.metadata = dict(
            metadata or {}
        )

    @staticmethod
    def _component_id(
        component,
    ):
        return str(
            getattr(
                component,
                "id",
                getattr(
                    component,
                    "component_id",
                    component,
                ),
            )
        )

    @property
    def source_id(self):
        return self._component_id(
            self.source
        )

    @property
    def target_id(self):
        return self._component_id(
            self.target
        )

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def matches(
        self,
        source,
        source_pin,
        target,
        target_pin,
    ):
        return (
            self.source_id
            == self._component_id(
                source
            )
            and self.source_pin
            == source_pin
            and self.target_id
            == self._component_id(
                target
            )
            and self.target_pin
            == target_pin
        )

    def involves(
        self,
        component,
    ):
        component_id = (
            self._component_id(
                component
            )
        )

        return component_id in {
            self.source_id,
            self.target_id,
        }

    def reverse(self):
        (
            self.source,
            self.target,
        ) = (
            self.target,
            self.source,
        )

        (
            self.source_pin,
            self.target_pin,
        ) = (
            self.target_pin,
            self.source_pin,
        )

        return self

    def to_dict(self):
        return {
            "id": (
                self.connection_id
            ),
            "source": (
                self.source_id
            ),
            "source_pin": (
                self.source_pin
            ),
            "target": (
                self.target_id
            ),
            "target_pin": (
                self.target_pin
            ),
            "enabled": (
                self.enabled
            ),
            "metadata": dict(
                self.metadata
            ),
        }
