class BlockSequence:

    def __init__(self):

        self.blocks = []

    def add(self, block):

        self.blocks.append(block)

        return len(self.blocks) - 1

    def insert(
        self,
        index,
        block,
    ):

        index = max(
            0,
            min(index, len(self.blocks)),
        )

        self.blocks.insert(
            index,
            block,
        )

        return index

    def remove(self, index):

        if not (
            0 <= index < len(self.blocks)
        ):
            return False

        self.blocks.pop(index)

        return True

    def move(
        self,
        source,
        target,
    ):

        if not (
            0 <= source < len(self.blocks)
        ):
            return False

        block = self.blocks.pop(source)

        target = max(
            0,
            min(target, len(self.blocks)),
        )

        self.blocks.insert(
            target,
            block,
        )

        return True

    def get_all(self):

        return list(self.blocks)
