"""
Gerenciador da placa ativa no simulador UAP.
"""


class BoardManager:

    def __init__(self):
        self.current = None

        self.boards = {}

        self.history = []

    def set_board(
        self,
        board,
    ):
        if board is None:
            self.current = None

            return None

        self.current = board

        board_id = getattr(
            board,
            "id",
            None,
        )

        if board_id is not None:
            self.boards[
                str(board_id)
            ] = board

        self.history.append(
            getattr(
                board,
                "name",
                type(board).__name__,
            )
        )

        return board

    def get_board(self):
        return self.current

    def has_board(self):
        return (
            self.current
            is not None
        )

    def add_board(
        self,
        board,
    ):
        if board is None:
            raise ValueError(
                "Placa não informada."
            )

        board_id = getattr(
            board,
            "id",
            None,
        )

        if board_id is None:
            raise ValueError(
                "Placa não possui ID."
            )

        self.boards[
            str(board_id)
        ] = board

        return board

    def get(
        self,
        board_id,
    ):
        return self.boards.get(
            str(board_id)
        )

    def exists(
        self,
        board_id,
    ):
        return (
            str(board_id)
            in self.boards
        )

    def remove(
        self,
        board_id,
    ):
        board_id = str(
            board_id
        )

        board = self.boards.pop(
            board_id,
            None,
        )

        if (
            board is not None
            and board is self.current
        ):
            self.current = None

        return board

    def select(
        self,
        board_id,
    ):
        board = self.get(
            board_id
        )

        if board is None:
            return None

        return self.set_board(
            board
        )

    def initialize_current(self):
        if self.current is None:
            return False

        method = getattr(
            self.current,
            "initialize",
            None,
        )

        if not callable(method):
            return False

        return method()

    def shutdown_current(self):
        if self.current is None:
            return False

        method = getattr(
            self.current,
            "shutdown",
            None,
        )

        if not callable(method):
            return False

        return method()

    def clear_current(self):
        previous = self.current

        self.current = None

        return previous

    def all(self):
        return list(
            self.boards.values()
        )

    def count(self):
        return len(
            self.boards
        )

    def clear(self):
        count = len(
            self.boards
        )

        self.boards.clear()
        self.current = None

        return count

    def status(self):
        return {
            "has_board": (
                self.has_board()
            ),
            "current": (
                self.current.status()
                if (
                    self.current
                    is not None
                    and hasattr(
                        self.current,
                        "status",
                    )
                )
                else None
            ),
            "board_count": (
                self.count()
            ),
            "history": list(
                self.history
            ),
        }


board_manager = BoardManager()
