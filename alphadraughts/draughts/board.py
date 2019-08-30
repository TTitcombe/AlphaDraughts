from enum import Enum

import numpy as np


class Direction(Enum):
    NE = 1
    SE = 2
    SW = 3
    NW = 4
    Invalid = 5


class Board:
    """
    A draughts board
    The board itself is represented by a 8x8 numpy array, where
    0 represents no piece, 1 represents white, 2 represents black.
    When displayed, whites are 'O' and blacks are 'X'
    """

    players = {"white": 1, "black": 2}

    board_to_print = {0: "-", 1: "O", 2: "X"}

    def __init__(self):
        self._board = np.zeros((8, 8))

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

        if not self._valid_index(start_index):
            # Start index must be on board
            return False

        if not self._valid_index(end_index):
            # End index must be on board
            return False

        start_board_index = self._square_to_board_index(start_index)
        if self._board[start_board_index] != current_move:
            # Can only move your own pieces
            return False

        end_board_index = self._square_to_board_index(end_index)
        if self._board[end_board_index] != 0:
            # Can't land on an occupied space!
            return False

        if not self._valid_move(start_index, end_index):
            # Moves must be diagonal
            return False

        # TODO check that there aren't pieces in the way

        return True

    def _valid_move(self, start_pos: int, end_pos: int) -> bool:
        """
        Check that move is of correct direction and distance.
        Currently assumes all pieces are Men
        TODO add logic for Kings
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
        difference = end_pos - start_pos
        if piece == 1 and difference > 0:
            return False
        elif piece == 2 and difference < 0:
            return False

        return True

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
        middle_pos = start_pos + int((end_pos - start_pos) / 2)
        if self._board[start_pos] == self._board[middle_pos]:
            # If they're the same piece, we can't jump
            return False
        if self._board[middle_pos] == 0:
            # If there isn't a piece in the middle, we can't jump
            return False
        return True

    def move(self, start_square: int, end_square: int) -> bool:
        start_index = self._square_to_board_index(start_square)
        end_index = self._square_to_board_index(end_square)

        piece = self._board[start_index]
        self._board[start_index] = 0
        self._board[end_index] = piece

        if abs(end_square - start_square) > 5:
            # We are making a jump
            middle_index = (
                int((start_index[0] + end_index[0]) / 2),
                int((start_index[1] + end_index[1]) / 2),
            )
            self._board[middle_index] = 0
            return True
        else:
            return False

    def reset(self):
        self._board = np.zeros((8, 8))
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
        print(start_positions)
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

    def __str__(self):
        board = ""
        for row in range(8):
            for column in range(8):
                board += self.board_to_print[self._board[row, column]]
            board += "\n"
        return board
