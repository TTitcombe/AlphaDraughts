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
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
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
            "--------\n"
            "--------\n"
            "--------\n"
            "--------\n"
            "-O-O-O-O\n"
            "O-O-O-O-\n"
        )
        assert str(board) == expected_printout

    def test_can_get_correct_move_directions(self):
        board = Board()
        assert board._get_move_direction(3, 7) == Direction.SW
        assert board._get_move_direction(3, 10) == Direction.SW

        assert board._get_move_direction(2, 7) == Direction.SE
        assert board._get_move_direction(2, 11) == Direction.SE

        assert board._get_move_direction(30, 26) == Direction.NE
        assert board._get_move_direction(30, 23) == Direction.NE

        assert board._get_move_direction(31, 26) == Direction.NW
        assert board._get_move_direction(31, 22) == Direction.NW

        assert board._get_move_direction(31, 32) == Direction.Invalid
        assert board._get_move_direction(31, 23) == Direction.Invalid

    def test_that_whites_can_only_move_up(self):
        board = Board()
        board.reset()

        assert board._valid_move(26, 23)

    def test_that_blacks_can_only_move_down(self):
        board = Board()
        board.reset()

        assert board._valid_move(6, 10)

    def test_that_cant_move_into_existing_piece(self):
        board = Board()
        board.reset()

        assert not board.validate_move(29, 25, "white")
        assert not board.validate_move(1, 6, "black")

    def test_cant_move_other_teams_pieces(self):
        board = Board()
        board.reset()

        assert not board.validate_move(26, 23, "black")
        assert not board.validate_move(6, 10, "white")

    def test_cant_move_into_occupied_space(self):
        board = Board()
        board.reset()

        assert not board.validate_move(29, 25, "white")
        assert not board.validate_move(1, 6, "black")

    def test_can_move_pieces(self):
        board = Board()
        board.reset()

        piece_taken = board.move(26, 23)
        assert not piece_taken
        assert board._board[(6, 3)] == 0
        assert board._board[(5, 4)] == 1

        piece_taken = board.move(6, 10)
        assert not piece_taken
        assert board._board[(1, 2)] == 0
        assert board._board[(2, 3)] == 2

    def test_move_removes_taken_pieces(self):
        board = Board()
        board.reset()

        # Put a black piece next to a white
        board._board[(5, 4)] = 2

        piece_taken = board.move(26, 19)
        assert piece_taken
        assert board._board[(6, 3)] == 0
        assert board._board[(5, 4)] == 0
        assert board._board[(4, 5)] == 1
