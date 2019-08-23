import numpy as np
import pytest

from alphadraughts.draughts.board import Board, Direction


class TestBoard:
    def test_board_initialises_to_empty(self):
        board = Board()
        assert (board._board == np.zeros((8, 8))).all()

    def test_reset_sets_correct_board(self):
        board = Board()
        board.reset()

        expected_board = np.array(
            [
                [0, 2, 0, 2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
            ]
        )
        assert (board._board == expected_board).all()

    def test_board_printout(self):
        board = Board()
        board.reset()

        expected_printout = (
            "-X-X-X-X\n"
            "X-X-X-X-\n"
            "-X-X-X-X\n"
            "X-X-X-X-\n"
            "-O-O-O-O\n"
            "O-O-O-O-\n"
            "-O-O-O-O\n"
            "O-O-O-O-\n"
        )
        assert str(board) == expected_printout
