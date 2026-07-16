class FavoriteBlocks:

    def __init__(self):

        self.blocks = set()

    def add(self, block):

        self.blocks.add(block)

    def remove(self, block):

        self.blocks.discard(block)

    def all(self):

        return sorted(self.blocks)


favorites = FavoriteBlocks()
