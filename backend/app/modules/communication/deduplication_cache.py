from collections import deque


class CommunicationDeduplicationCache:

    def __init__(
        self,
        max_size: int = 2000,
    ):
        self.max_size = max(
            1,
            int(max_size),
        )

        self._order = deque()
        self._keys: set[str] = set()

    def contains(
        self,
        key: str,
    ):
        return key in self._keys

    def add(
        self,
        key: str,
    ):
        if key in self._keys:
            return False

        self._keys.add(
            key
        )

        self._order.append(
            key
        )

        while (
            len(self._order)
            > self.max_size
        ):
            oldest = (
                self._order
                .popleft()
            )

            self._keys.discard(
                oldest
            )

        return True

    def clear(self):
        self._order.clear()
        self._keys.clear()

    def size(self):
        return len(
            self._keys
        )


communication_deduplication_cache = (
    CommunicationDeduplicationCache()
)
