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
            if move.lower() == "help":
                print("Valid moves for {}: ".format(self.turn))
                valid_moves = self.valid_moves()
                for move in valid_moves:
                    print(move)
            else:
                did_move = self.move(move)
                if not did_move:
                    print(
                        "Move {} invalid. {} to move again.\n"
                        "Type `help` to see valid moves".format(move, self.turn)
                    )

    def move(self, move: str) -> bool:
        # CHECK THAT GAME IS OVER
        if self.game_over():
            return False

        # VALIDATE THE MOVE
        start, end = self._parse_move(move)
        if start is None or end is None:
            return False

        if not self._board.validate_move(start, end, self.turn):
            return False
        else:
            self._move_list.append(move)

        # MAKE THE MOVE
        piece_taken = self._board.move(start, end)

        # POST-MOVE DECISION
        if not piece_taken:
            self.change_turn()
        else:
            self._remove_piece()

        return True

    def valid_moves(self, turn="") -> list:
        turn = turn if turn else self.turn
        if self._pieces_remaining[turn] == 0:
            return []
        else:
            return self._board.valid_moves(turn)

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
