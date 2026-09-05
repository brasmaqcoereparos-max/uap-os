import hashlib
import json

from app.modules.communication.deduplication_cache import (
    communication_deduplication_cache,
)


class CommunicationMessageDeduplicator:

    def key_for(
        self,
        message,
    ):
        data = {
            "source": message.source,
            "channel": message.channel,
            "payload": message.payload,
        }

        raw = json.dumps(
            data,
            sort_keys=True,
            default=str,
        ).encode(
            "utf-8"
        )

        return hashlib.sha256(
            raw
        ).hexdigest()

    def is_duplicate(
        self,
        message,
    ):
        key = self.key_for(
            message
        )

        if (
            communication_deduplication_cache
            .contains(key)
        ):
            return True

        communication_deduplication_cache.add(
            key
        )

        return False


communication_message_deduplicator = (
    CommunicationMessageDeduplicator()
)
