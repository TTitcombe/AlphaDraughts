from unittest import mock

import numpy as np
import pytest

from alphadraughts.draughts.board import Board
from alphadraughts.draughts.game import Game
from tests.draughts.utils import new_board


class TestGame:
    def test_can_parse_valid_move(self):
        game = Game(None, None)
        assert game._parse_move("7-11") == (7, 11)
        assert game._parse_move("11-7") == (11, 7)

    def test_that_move_without_hyphen_returns_None(self):
        game = Game(None, None)
        assert game._parse_move("7.11") == (None, None)

    def test_that_move_without_integers_returns_None(self):
        game = Game(None, None)
        assert game._parse_move("Seven-Eleven") == (None, None)

    def test_can_change_turn(self):
        game = Game(None, None)

        # Check that turn starts on white
        assert game.turn == "white"

        # Check that can change to black
        game.change_turn()
        assert game.turn == "black"

        # Check that can change back to white
        game.change_turn()
        assert game.turn == "white"

    def test_remove_piece_removes_from_opposite_player(self):
        game = Game(None, None)
        assert game._pieces_remaining == {"white": 8, "black": 8}

        game._remove_piece()
        assert game._pieces_remaining == {"white": 8, "black": 7}

        game.change_turn()
        game._remove_piece()
        assert game._pieces_remaining == {"white": 7, "black": 7}

    def test_game_is_over_if_no_pieces_remaining(self):
        game = Game(None, None)
        assert not game.game_over()

        for _ in range(8):
            game._remove_piece()

        assert game.game_over()

    def test_that_move_returns_True_if_move_made(self):
        game = Game(None, None)
        game._board.reset()

        move_made = game.move("25-22")
        assert move_made
        assert game.turn == "black"

        move_made = game.move("11-1")
        assert not move_made
        assert game.turn == "black"

    def test_that_cant_move_if_game_is_over(self):
        game = Game(None, None)
        game._board = mock.Mock(autospec=Board)

        for _ in range(8):
            game._remove_piece()

        move_made = game.move("25-22")
        assert not move_made

        # Confirm that move wasn't validated (because the game was over anyway)
        assert game._board.validate_move.call_count == 0

    def test_move_returns_False_if_move_string_is_not_a_move(self):
        game = Game(None, None)
        game.reset()

        assert not game.move("invalid move")
        assert not game.move("5.5-4.4")
        assert not game.move("18 14")
        assert not game.move("18_14")

    def test_that_move_removes_piece_if_white_takes_black(self):
        # TODO Move this to a gameplay test later
        game = Game(None, None)
        game.reset()

        game.move("25-22")
        game.move("5-9")
        game.move("22-18")
        game.move("9-14")

        # White takes black in this move
        game.move("18-9")

        assert game.turn == "white"
        assert game._pieces_remaining["black"] == 7

    def test_that_move_removes_piece_if_black_takes_white(self):
        # TODO Move this to a gameplay test later
        game = Game(None, None)
        game.reset()

        game.move("25-22")
        game.move("5-9")
        game.move("22-18")
        game.move("9-14")
        game.move("29-25")

        # Black takes white in this move
        game.move("14-23")

        assert game.turn == "black"
        assert game._pieces_remaining["white"] == 7

    def test_that_reset_resets_game(self):
        game = Game(None, None)
        game._board._board[5, 4] = 1
        game._move_list = [1, 2, 3, 4]
        game.turn = "black"
        game._pieces_remaining = {"white": 5, "black": 6}

        game.reset()

        assert np.array_equal(game._board._board, new_board)
        assert game._move_list == []
        assert game.turn == "white"
        assert game._pieces_remaining == {"white": 8, "black": 8}

    def test_valid_moves_considers_player_turn(self):
        game = Game(None, None)
        game.turn = "black"

        # Remove existing black pieces
        game._board._board[:, :2] = 0
        game._board._board[0, 3] = 2

        assert game.valid_moves() == ["2-6", "2-7"]

    def test_valid_moves_can_accept_other_piece(self):
        game = Game(None, None)

        # Remove all black pieces, but keep game turn as white
        game._board._board[:, :2] = 0

        assert game.valid_moves("black") == []

    def test_valid_moves_returns_empty_list_if_no_moves(self):
        game = Game(None, None)
        # game._board is initialised to an empty array
        # no pieces == no moves
        assert game.valid_moves() == []
