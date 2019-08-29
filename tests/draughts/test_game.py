import pytest

from alphadraughts.draughts.game import Game


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
