"""
Evento universal do Core UAP.

Contrato original preservado:
    Event(name, data=None)
    event.name
    event.data
"""

import time
import uuid


class Event:

    def __init__(
        self,
        name,
        data=None,
    ):
        self.name = str(name)
        self.data = data

        self.id = str(
            uuid.uuid4()
        )

        self.created_at = (
            time.monotonic()
        )

        self.processed = False
        self.cancelled = False

        self.metadata = {}

    def mark_processed(self):
        self.processed = True

        return True

    def cancel(self):
        self.cancelled = True

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

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "data": self.data,
            "created_at": self.created_at,
            "processed": self.processed,
            "cancelled": self.cancelled,
            "metadata": dict(
                self.metadata
            ),
        }
