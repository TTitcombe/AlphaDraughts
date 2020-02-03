import numpy as np
import pytest

from alphadraughts.draughts.enums import Direction
from alphadraughts.draughts.piece import EmptyPiece, King, Piece


class TestBasePiece:
    pass


class TestPiece:
    def test_piece_can_be_promoted(self):
        piece = Piece("white", 10)
        new_piece = piece.promote()

        assert isinstance(new_piece, King)
        assert new_piece.player == "white"
        assert new_piece.square == 10

    def test_white_piece_cannot_move_southeast(self):
        piece = Piece("white", 10)
        assert not piece.move(Direction.SE)

    def test_white_piece_cannot_move_southwest(self):
        piece = Piece("white", 10)
        assert not piece.move(Direction.SW)

    def test_white_piece_can_move_northeast(self):
        piece = Piece("white", 10)
        assert piece.move(Direction.NE)

    def test_white_piece_can_move_northwest(self):
        piece = Piece("white", 10)
        assert piece.move(Direction.NW)

    def test_black_piece_can_move_southeast(self):
        piece = Piece("black", 10)
        assert piece.move(Direction.SE)

    def test_black_piece_can_move_southwest(self):
        piece = Piece("black", 10)
        assert piece.move(Direction.SW)

    def test_black_piece_cannot_move_northeast(self):
        piece = Piece("black", 10)
        assert not piece.move(Direction.NE)

    def test_black_piece_cannot_move_northwest(self):
        piece = Piece("black", 10)
        assert not piece.move(Direction.NW)

    def test_that_white_piece_prints_to_O(self):
        piece = Piece("white", 10)
        assert str(piece) == "O"

    def test_that_black_piece_prints_to_X(self):
        piece = Piece("black", 10)
        assert str(piece) == "X"

    def test_that_piece_equates_to_str(self):
        piece = Piece("white", 32)
        black_piece = Piece("black", 1)

        assert piece == "white"
        assert not piece == "black"

        assert black_piece == "black"
        assert not black_piece == "white"

    def test_that_piece_equates_to_piece(self):
        piece = Piece("white", 32)
        king = King("white", 1)
        black_piece = Piece("black", 2)
        black_king = King("black", 31)

        assert piece == piece
        assert piece == king
        assert not piece == black_piece
        assert not piece == black_king

        assert black_piece == black_piece
        assert black_piece == black_king
        assert not black_piece == piece
        assert not black_piece == king


class TestKing:
    def test_that_white_king_can_move_in_any_direction(self):
        piece = King("white", 10)
        assert piece.move(Direction.SE)
        assert piece.move(Direction.SW)
        assert piece.move(Direction.NE)
        assert piece.move(Direction.NW)

    def test_that_black_king_can_move_in_any_direction(self):
        piece = King("black", 10)
        assert piece.move(Direction.SE)
        assert piece.move(Direction.SW)
        assert piece.move(Direction.NE)
        assert piece.move(Direction.NW)

    def test_that_white_king_prints_to_KO(self):
        piece = King("white", 10)
        assert str(piece) == "KO"

    def test_that_black_king_prints_to_KX(self):
        piece = King("black", 10)
        assert str(piece) == "KX"

    def test_that_king_equates_to_pieces(self):
        king = King("white", 10)
        king2 = King("white", 12)
        piece = Piece("white", 11)
        black_king = King("black", 1)
        black_piece = Piece("black", 2)

        assert king == piece
        assert king == king2
        assert king == king
        assert not king == black_king
        assert not king == black_piece

        assert black_king == black_piece
        assert not black_king == piece
        assert not black_king == king

    def test_that_king_equates_to_str(self):
        king = King("white", 1)
        black_king = King("black", 32)

        assert king == "white"
        assert not king == "black"

        assert black_king == "black"
        assert not black_king == "white"


class TestEmptyPiece:
    def test_that_empty_piece_prints_to_hyphen(self):
        piece = EmptyPiece(10)
        assert str(piece) == "-"

    def test_that_empty_piece_cannot_be_moved(self):
        piece = EmptyPiece(10)

        assert not piece.move(Direction.SE)
        assert not piece.move(Direction.SW)
        assert not piece.move(Direction.NE)
        assert not piece.move(Direction.NW)

    def test_that_empty_peice_equates_to_piece(self):
        empty = EmptyPiece(10)
        empty2 = EmptyPiece(11)
        piece = Piece("white", 32)
        black_piece = Piece("black", 1)
        king = King("white", 2)
        black_king = King("black", 31)

        assert empty == empty2
        assert not empty == piece
        assert not empty == black_piece
        assert not empty == king
        assert not empty == black_king
