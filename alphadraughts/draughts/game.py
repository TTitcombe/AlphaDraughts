from .board import Board
from .players import BasePlayer, HumanPlayer


class Game:
    def __init__(self, white=HumanPlayer("white"), black=HumanPlayer("black")):
        """
        Create a game object. The default is human vs human.
        """
        self.white = white
        self.black = black
        self.turn = "white"  # Start with white
        self._board = Board()
        self._move_list = []
        self._pieces_remaining = {"white": 8, "black": 8}
        self.result = None
        self._moves_since_take = 0

    def play(self):
        """
        Play a game via user input
        """
        self.reset()
        while not self.game_over():
            print(self._board)
            if self.turn == "white":
                move = self.white.choose_move(self.valid_moves())
            else:
                move = self.black.choose_move(self.valid_moves())
            did_move = self.move(move)
            if not did_move:
                print(
                    "Move {} invalid. {} to move again.\n"
                    "Type `help` to see valid moves".format(move, self.turn)
                )
        print(self._board)
        if self.result == "draw":
            print("It's a draw!")
        else:
            print("{} wins!".format(self.result))

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
            self._moves_since_take += 1
            self.change_turn()
        else:
            self._moves_since_take = 0
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
        white_remaining = self._pieces_remaining["white"]
        black_remaining = self._pieces_remaining["black"]

        if self._moves_since_take >= 40:
            self.result = "draw"
            return True
        elif not self.valid_moves():
            # No valid moves, so the other player wins
            if self.turn == "white":
                self.result = "black"
            else:
                self.result = "white"
            return True
        elif white_remaining == 0:
            self.result = "black"
            return True
        elif black_remaining == 0:
            self.result = "white"
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
        self.result = None
        self._moves_since_take = 0
