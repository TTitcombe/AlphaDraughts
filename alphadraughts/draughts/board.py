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

    def validate_move(self, start_index: tuple, end_index: tuple, turn: str) -> bool:
        current_move = self.players[turn]

        if not self._valid_index(start_index):
            # Start index must be on board
            return False

        if not self._valid_index(end_index):
            # End index must be on board
            return False

        if self._board[start_index] != current_move:
            # Can only move your own pieces
            return False

        if self._board[end_index] != 0:
            # Can't land on an occupied space!
            return False

        if not self._valid_move(start_index, end_index):
            # Moves must be diagonal
            return False

        # TODO check that there aren't pieces in the way

        return True

    def _valid_move(self, start_pos: int, end_pos: int) -> bool:
        move_direction = self._get_move_direction(start_pos, end_pos)
        # TODO check that the piece can move in that direction
        return False

    @staticmethod
    def _get_move_direction(start_pos: int, end_pos: int) -> Enum:
        difference = end_pos - start_pos
        if difference == -7:
            return Direction.NE
        elif difference == 9:
            return Direction.SE
        elif difference == 7:
            return Direction.SW
        elif difference == -9:
            return Direction.NW
        else:
            return Direction.Invalid

    def _valid_index(self, index: tuple) -> bool:
        for position in index:
            if position < 0 or position > (self._board.shape[0] - 1):
                return False
        return True

    def move(self, start_index: tuple, end_index: tuple) -> int:
        # TODO
        # update the board and remove taken pieces
        # return the number of pieces removed
        return 0

    def reset(self):
        self._board = np.zeros((8, 8))
        for row in range(8):
            piece = self.players["black"] if row < 4 else self.players["white"]
            if row % 2 == 0:
                locations = [i for i in range(8) if i % 2 == 1]
            else:
                locations = [i for i in range(8) if i % 2 == 0]
            self._board[row, locations] = piece

    def __str__(self):
        board = ""
        for row in range(8):
            for column in range(8):
                board += self.board_to_print[self._board[row, column]]
            board += "\n"
        return board
