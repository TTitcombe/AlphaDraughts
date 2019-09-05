import pytest

from alphadraughts.draughts.players import BasePlayer


class TestBasePlayer:
    def test_that_win_rate_default_to_zero(self):
        player = BasePlayer()
        assert player.win_rate == 0.0

    def test_that_win_rate_is_wins_over_games_played(self):
        player = BasePlayer()
        player.wins = 10
        assert player.win_rate == 1.0

        player.draws = 10
        assert player.win_rate == 0.5

        player.losses = 80
        assert player.win_rate == 0.1

        player.wins = 90
        assert player.win_rate == 0.5
