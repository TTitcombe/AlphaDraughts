import numpy as np

from alphadraughts.draughts.board import Board
from alphadraughts.draughts.enums import Direction
from alphadraughts.draughts.piece import EmptyPiece, King, Piece
from tests.unittests.draughts.utils import new_board


class TestBoard:
    def test_board_initialises_to_empty(self):
        board = Board()
        assert (board._board == np.full((8, 8), EmptyPiece(), dtype=object)).all()

    def test_reset_sets_correct_board(self):
        board = Board()
        board.reset()

        expected_board = new_board
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
        assert board._board[(6, 3)] == EmptyPiece()
        assert board._board[(5, 4)] == Piece("white", None)

        piece_taken = board.move(6, 10)
        assert not piece_taken
        assert board._board[(1, 2)] == EmptyPiece()
        assert board._board[(2, 3)] == Piece("black", None)

    def test_move_removes_taken_pieces(self):
        board = Board()
        board.reset()

        # Put a black piece next to a white
        board._board[(5, 4)] = Piece("black", None)

        piece_taken = board.move(26, 19)
        assert piece_taken
        assert board._board[(6, 3)] == EmptyPiece()
        assert board._board[(5, 4)] == EmptyPiece()
        assert board._board[(4, 5)] == Piece("white", None)

    def test_that_white_pieces_can_be_promoted_on_move(self):
        board = Board()
        board.reset()

        # put a white piece within a move of end row
        board._board[(1, 0)] = Piece("white", None)

        # remove the black piece in its way
        board._board[(0, 1)] = EmptyPiece(None)

        # Move the white piece into the top row
        board.move(5, 1)

        assert board._board[(1, 0)] == EmptyPiece()
        assert board._board[(0, 1)] == King("white", None)

    def test_that_black_pieces_can_be_promoted_on_move(self):
        board = Board()
        board.reset()

        # put a black piece within a move of bottom row
        board._board[(6, 1)] = Piece("black", None)

        # remove the black piece in its way
        board._board[(7, 0)] = EmptyPiece(None)

        # Move the white piece into the bottom row
        board.move(25, 29)

        assert board._board[(6, 1)] == EmptyPiece()
        assert board._board[(7, 0)] == King("black", None)

    def test_board_index_to_square(self):
        board = Board()

        assert board._board_index_to_square((0, 1)) == 1
        assert board._board_index_to_square((7, 6)) == 32
        assert board._board_index_to_square((2, 5)) == 11
        assert board._board_index_to_square((3, 2)) == 14

    def test_finds_valid_starting_moves_for_white(self):
        board = Board()
        board.reset()

        expected_starting_moves = [
            "25-21",
            "25-22",
            "26-22",
            "26-23",
            "27-23",
            "27-24",
            "28-24",
        ]
        assert board.valid_moves("white") == expected_starting_moves

    def test_finds_valid_starting_moves_for_black(self):
        board = Board()
        board.reset()

        expected_starting_moves = ["5-9", "6-9", "6-10", "7-10", "7-11", "8-11", "8-12"]
        assert board.valid_moves("black") == expected_starting_moves

    def test_cant_take_if_middle_piece_is_same_as_taking_piece(self):
        board = Board()
        board.reset()

        # Put white pieces next to one another
        board._board[4, 3] = Piece("white", None)
        board._board[3, 2] = Piece("white", None)

        assert not board._check_can_take(18, 9)

    def test_cant_take_if_no_middle_piece(self):
        board = Board()
        board.reset()

        board._board[4, 3] = Piece("white", None)

        assert not board._check_can_take(18, 9)

    def test_white_can_take_black(self):
        board = Board()
        board.reset()

        board._board[4, 3] = Piece("white", None)
        board._board[3, 2] = Piece("black", None)

        assert board._check_can_take(18, 9)

    def test_black_can_take_white(self):
        board = Board()
        board.reset()

        board._board[2, 1] = Piece("black", None)
        board._board[3, 2] = Piece("white", None)

        assert board._check_can_take(9, 18)

    def test_white_pieces_not_promoted_on_non_top_row(self):
        board = Board()
        board.reset()

        board._promote((7, 0))
        assert not isinstance(board._board[(7, 0)], King)

        board._promote((6, 1))
        assert not isinstance(board._board[(6, 1)], King)

    def test_black_pieces_not_promoted_on_non_bottom_row(self):
        board = Board()
        board.reset()

        board._promote((0, 1))
        assert not isinstance(board._board[(0, 1)], King)

        board._promote((1, 2))
        assert not isinstance(board._board[(1, 2)], King)

    def test_that_white_piece_on_top_row_can_be_promoted(self):
        board = Board()
        board.reset()

        board._board[(0, 1)] = Piece("white", 1)
        board._promote((0, 1))
        assert isinstance(board._board[(0, 1)], King)

    def test_that_black_piece_on_bottom_row_can_be_promoted(self):
        board = Board()
        board.reset()

        board._board[(7, 0)] = Piece("black", 29)
        board._promote((7, 0))
        assert isinstance(board._board[(7, 0)], King)
