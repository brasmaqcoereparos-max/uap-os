class BlockSequence:
    def __init__(self):
        self.blocks = []

    def add(
        self,
        block,
    ):
        self.blocks.append(
            block
        )

        return (
            len(self.blocks) - 1
        )

    def insert(
        self,
        index,
        block,
    ):
        index = max(
            0,
            min(
                int(index),
                len(self.blocks),
            ),
        )

        self.blocks.insert(
            index,
            block,
        )

        return index

    def remove(
        self,
        index,
    ):
        if not (
            0
            <= int(index)
            < len(self.blocks)
        ):
            return False

        self.blocks.pop(
            int(index)
        )

        return True

    def remove_by_id(
        self,
        block_id,
    ):
        expected = str(
            block_id
        )

        for index, block in enumerate(
            self.blocks
        ):
            current = getattr(
                block,
                "block_id",
                None,
            )

            if str(current) == expected:
                self.blocks.pop(
                    index
                )

                return True

        return False

    def move(
        self,
        source,
        target,
    ):
        source = int(source)
        target = int(target)

        if not (
            0
            <= source
            < len(self.blocks)
        ):
            return False

        block = self.blocks.pop(
            source
        )

        target = max(
            0,
            min(
                target,
                len(self.blocks),
            ),
        )

        self.blocks.insert(
            target,
            block,
        )

        return True

    def get(
        self,
        index,
    ):
        if not (
            0
            <= int(index)
            < len(self.blocks)
        ):
            return None

        return self.blocks[
            int(index)
        ]

    def get_by_id(
        self,
        block_id,
    ):
        expected = str(
            block_id
        )

        for block in self.blocks:
            if (
                str(
                    getattr(
                        block,
                        "block_id",
                        None,
                    )
                )
                == expected
            ):
                return block

        return None

    def get_all(self):
        return list(
            self.blocks
        )

    def clear(self):
        self.blocks.clear()

    def count(self):
        return len(
            self.blocks
        )

    def to_dict(self):
        result = []

        for block in self.blocks:
            serializer = getattr(
                block,
                "to_dict",
                None,
            )

            result.append(
                serializer()
                if callable(
                    serializer
                )
                else str(block)
            )

        return result
