from app.modules.communication.message_filter import (
    CommunicationMessageFilter,
)


class CommunicationFilterRegistry:

    def __init__(self):
        self._filters: dict[
            str,
            CommunicationMessageFilter,
        ] = {}

    def register(
        self,
        name: str,
        message_filter: (
            CommunicationMessageFilter
        ),
    ):
        self._filters[
            name
        ] = message_filter

        return message_filter

    def get(
        self,
        name: str,
    ):
        return self._filters.get(
            name
        )

    def remove(
        self,
        name: str,
    ):
        return self._filters.pop(
            name,
            None,
        )

    def list_all(self):
        return dict(
            self._filters
        )

    def clear(self):
        self._filters.clear()


communication_filter_registry = (
    CommunicationFilterRegistry()
)
