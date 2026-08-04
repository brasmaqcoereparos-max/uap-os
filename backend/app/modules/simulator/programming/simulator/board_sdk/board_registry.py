class BoardRegistry:

    def __init__(self):

        self.boards = {}

    def register(

        self,

        board_class,

    ):

        self.boards[board_class.name] = board_class

    def get(

        self,

        name,

    ):

        return self.boards.get(name)

    def all(self):

        return self.boards.copy()


board_registry = BoardRegistry()
