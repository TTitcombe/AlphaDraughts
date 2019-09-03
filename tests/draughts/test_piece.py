import numpy as np
import pytest

from alphadraughts.draughts.enums import Direction
from alphadraughts.draughts.piece import Piece, King, EmptyPiece


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
