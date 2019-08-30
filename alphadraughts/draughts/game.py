from .board import Board


class Game:
    def __init__(self, white, black):
        self.white = white
        self.black = black
        self.turn = "white"  # Start with white
        self._board = Board()
        self._move_list = []
        self._pieces_remaining = {"white": 8, "black": 8}

    def play(self):
        """
        Play a game via the command line
        """
        self.reset()
        while not self.game_over():
            print(self._board)
            move = input("{} to move: ".format(self.turn))
            did_move = self.move(move)
            if not did_move:
                print("Move {} invalid. {} to move again.".format(move, self.turn))

    def move(self, move: str) -> bool:
        # VALIDATE THE MOVE
        # MAKE THE MOVE
        if self.game_over():
            return False

        start, end = self._parse_move(move)
        if not self._board.validate_move(start, end, self.turn):
            return False
        else:
            self._move_list.append(move)
        piece_taken = self._board.move(start, end)
        if not piece_taken:
            self.change_turn()
        else:
            self._remove_piece()

        return True

    def change_turn(self) -> None:
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def _remove_piece(self) -> None:
        player = "black" if self.turn == "white" else "white"
        self._pieces_remaining[player] -= 1

    def game_over(self) -> bool:
        if min(self._pieces_remaining.values()) == 0:
            return True
        else:
            return False

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

    def reset(self):
        """
        Create a new game
        """
        self._move_list = []
        self._pieces_remaining = {"white": 8, "black": 8}
        self.turn = "white"
        self._board.reset()
