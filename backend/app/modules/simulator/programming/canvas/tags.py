class TagManager:

    def __init__(self):

        self.tags = {}

    def add(
        self,
        node_id,
        tag,
    ):

        self.tags.setdefault(
            node_id,
            set(),
        ).add(tag)

    def remove(
        self,
        node_id,
        tag,
    ):

        if node_id in self.tags:

            self.tags[node_id].discard(tag)

    def get(
        self,
        node_id,
    ):

        return sorted(
            self.tags.get(
                node_id,
                set(),
            )
        )

    def clear(
        self,
        node_id,
    ):

        self.tags.pop(
            node_id,
            None,
        )


tags = TagManager()
