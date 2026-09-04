from app.modules.communication.channel import (
    CommunicationChannel,
)


class CommunicationChannelRegistry:

    def __init__(self):
        self._channels: dict[
            str,
            CommunicationChannel,
        ] = {}

    def register(
        self,
        channel: CommunicationChannel,
    ):
        self._channels[
            channel.name
        ] = channel

        return channel

    def get(
        self,
        name: str,
    ):
        return self._channels.get(
            name
        )

    def get_or_create(
        self,
        name: str,
    ):
        channel = self.get(
            name
        )

        if channel:
            return channel

        return self.register(
            CommunicationChannel(
                name=name
            )
        )

    def remove(
        self,
        name: str,
    ):
        return self._channels.pop(
            name,
            None,
        )

    def list_all(self):
        return list(
            self._channels.values()
        )

    def clear(self):
        self._channels.clear()


communication_channel_registry = (
    CommunicationChannelRegistry()
)
