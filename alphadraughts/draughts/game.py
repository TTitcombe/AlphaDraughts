from .board import Board


class Game:
    def __init__(self, white, black):
        self.white = white
        self.black = black
        self.turn = "white"  # Start with white
        self._board = Board()
        self.move_list = []

    def move(self, move: str) -> None:
        # VALIDATE THE MOVE
        # MAKE THE MOVE
        start, end = self._parse_move(move)
        if self._board.validate_move(start, end, self.turn):
            pass

        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    @staticmethod
    def _parse_move(move: str) -> tuple:
        if "-" not in move:
            return None, None

        start, end = move.split("-")
        try:
            start = int(start)
            end = int(end)
        except ValueError:
            # Either start or end is not an int
            return None, None
        else:
            return start, end
