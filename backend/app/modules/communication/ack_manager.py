from app.modules.communication.ack import (
    CommunicationAck,
)


class CommunicationAckManager:

    def __init__(self):
        self._acks: dict[
            str,
            CommunicationAck,
        ] = {}

    def create(
        self,
        message_id: str,
        acknowledged: bool = True,
        reason: str | None = None,
    ):
        ack = CommunicationAck(
            message_id=message_id,
            acknowledged=(
                acknowledged
            ),
            reason=reason,
        )

        self._acks[
            message_id
        ] = ack

        return ack

    def get(
        self,
        message_id: str,
    ):
        return self._acks.get(
            message_id
        )

    def list_all(self):
        return [
            ack.to_dict()
            for ack
            in self._acks.values()
        ]

    def clear(self):
        self._acks.clear()


communication_ack_manager = (
    CommunicationAckManager()
)
