from enum import Enum
import numpy as np

from alphadraughts.draughts.enums import Direction
from alphadraughts.draughts.piece import EmptyPiece, Piece, King


class Board:
    """
    A draughts board
    The board itself is represented by a 8x8 numpy array, where
    0 represents no piece, 1 represents white, 2 represents black.
    When displayed, whites are 'O' and blacks are 'X'
    """

    players = {"white": Piece("white", None), "black": Piece("black", None)}

    board_to_print = {0: "-", 1: "O", 2: "X"}

    def __init__(self):
        self._board = np.full((8, 8), EmptyPiece(), dtype=object)

    def _square_to_board_index(self, square_number: int) -> tuple:
        row = (square_number - 1) // 4
        column = (square_number - 1) % 4
        if row % 2 == 0:
            column = 2 * column + 1
        elif row % 2 == 1:
            column = 2 * column
        return row, column

    def _board_index_to_square(self, index: tuple) -> int:
        max_square_on_row = 4 * (index[0] + 1)
        if index[0] % 2 == 0:
            column = index[1] - 1
        else:
            column = index[1]

        return max_square_on_row - (3 - int(column // 2))

    def validate_move(self, start_index: int, end_index: int, turn: str) -> bool:
        current_move = self.players[turn]

        # Check that the start square exists
        if not self._valid_index(start_index):
            return False

        # Check that the end square exists
        if not self._valid_index(end_index):
            return False

        # Check that the moving piece is on the current side
        start_board_index = self._square_to_board_index(start_index)
        if self._board[start_board_index] != current_move:
            return False

        # Check that end square isn't occupied
        end_board_index = self._square_to_board_index(end_index)
        if self._board[end_board_index] != EmptyPiece():
            return False

        # Check that the move direction is diagonal
        # and valid for the piece type
        if not self._valid_move(start_index, end_index):
            return False

        # TODO check that there aren't pieces in the way

        return True

    def _valid_move(self, start_pos: int, end_pos: int) -> bool:
        """
        Check that move is of correct direction and distance.
        Currently assumes all pieces are Men
        """
        move_direction = self._get_move_direction(start_pos, end_pos)
        if move_direction == Direction.Invalid:
            return False

        if abs(end_pos - start_pos) > 5:
            # Then we're trying to take a piece
            if not self._check_can_take(start_pos, end_pos):
                return False

        # Check that we're moving in the correct direction
        piece = self._board[self._square_to_board_index(start_pos)]
        return piece.move(move_direction)

    def _get_move_direction(self, start_pos: int, end_pos: int) -> Enum:
        difference = end_pos - start_pos
        if difference in (-3, -7):
            return Direction.NE
        elif difference in (5, 9):
            return Direction.SE
        elif difference in (3, 7):
            return Direction.SW
        elif difference in (-5, -9):
            return Direction.NW
        elif difference == 4:
            if start_pos % 2 == 0:
                return Direction.SE
            else:
                return Direction.SW
        elif difference == -4:
            if start_pos % 2 == 0:
                return Direction.NE
            else:
                return Direction.NW
        else:
            return Direction.Invalid

    def _valid_index(self, index: int) -> bool:
        if index < 1 or index > 32:
            return False
        return True

    def _check_can_take(self, start_pos: int, end_pos: int) -> bool:
        start_index = self._square_to_board_index(start_pos)
        end_index = self._square_to_board_index(end_pos)
        middle_index = tuple(int((e + s) / 2) for s, e in zip(start_index, end_index))

        if self._board[start_index] == self._board[middle_index]:
            # If they're the same piece, we can't jump
            return False
        if self._board[middle_index] == EmptyPiece():
            # If there isn't a piece in the middle, we can't jump
            return False
        return True

    def move(self, start_square: int, end_square: int) -> bool:
        start_index = self._square_to_board_index(start_square)
        end_index = self._square_to_board_index(end_square)

        piece = self._board[start_index]
        self._board[start_index] = EmptyPiece()
        self._board[end_index] = piece

        # See if a piece can be promoted
        self._promote(end_index)

        if abs(end_square - start_square) > 5:
            # We are making a jump
            middle_index = (
                int((start_index[0] + end_index[0]) / 2),
                int((start_index[1] + end_index[1]) / 2),
            )
            self._board[middle_index] = EmptyPiece()
            return True
        else:
            return False

    def reset(self):
        self._board = np.full((8, 8), EmptyPiece(), dtype=object)
        for row in [0, 1, 6, 7]:
            piece = self.players["black"] if row < 2 else self.players["white"]
            if row % 2 == 0:
                locations = [i for i in range(8) if i % 2 == 1]
            else:
                locations = [i for i in range(8) if i % 2 == 0]
            self._board[row, locations] = piece

    def valid_moves(self, turn: str) -> list:
        moves = []
        piece = self.players[turn]
        start_positions = list(np.argwhere(self._board == piece))
        for start_position in start_positions:
            start_square = self._board_index_to_square(tuple(start_position))
            for x_move in [-1, 1]:
                for y_move in [-1, 1]:
                    end_position = tuple(start_position + np.array([x_move, y_move]))
                    if 0 <= end_position[0] <= 7 and 0 <= end_position[1] <= 7:
                        # If we don't do this, 29-24 becomes a valid starting move for white
                        # TODO investigate why
                        end_square = self._board_index_to_square(end_position)
                        if self.validate_move(start_square, end_square, turn):
                            moves.append("{}-{}".format(start_square, end_square))
        return moves

    def _promote(self, index: tuple) -> None:
        piece = self._board[index]
        if index[0] == 0 and piece == "white" or index[0] == 7 and piece == "black":
            # White piece on top row becomes a King
            # or black piece on bottom row
            self._board[index] = piece.promote()

    def __str__(self):
        board = ""
        for row in range(8):
            for column in range(8):
                board += str(self._board[row, column])
            board += "\n"
        return board
