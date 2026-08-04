class BoardManager:

    def __init__(self):

        self.current = None

    def set_board(

        self,

        board,

    ):

        self.current = board

    def get_board(self):

        return self.current

    def has_board(self):

        return self.current is not None


board_manager = BoardManager()
