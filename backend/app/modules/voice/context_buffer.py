from app.modules.voice.context_item import (
    VoiceContextItem,
)


class VoiceContextBuffer:

    def __init__(
        self,
        max_items: int = 12,
    ):
        self.max_items = max(
            1,
            int(max_items),
        )

        self._items: list[
            VoiceContextItem
        ] = []

    def add(
        self,
        item: VoiceContextItem,
    ):
        self._items.append(
            item
        )

        if (
            len(self._items)
            > self.max_items
        ):
            excess = (
                len(self._items)
                - self.max_items
            )

            del self._items[
                :excess
            ]

        return item

    def list_all(self):
        return list(
            self._items
        )

    def latest(self):
        if not self._items:
            return None

        return self._items[-1]

    def clear(self):
        self._items.clear()

    def to_dict(self):
        return [
            item.to_dict()
            for item
            in self._items
        ]
