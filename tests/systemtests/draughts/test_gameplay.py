from alphadraughts import Game


class TestGameplay:
    """
    The class contains tests running through entire games.
    The purpose of this test class is to check that macro functionality, such as
    moving, promotion, taking, stalemates etc. works in practice.
    """

    def _run_gameplay_test(self, moves, result):
        game = Game()
        game.reset()

        for move in moves:
            move_made = game.move(move)
            assert move_made

        assert game.game_over()
        assert game.result == result

    def test_that_white_can_win(self):
        moves = [
            "26-23",
            "6-10",
            "23-18",
            "10-14",
            "27-23",
            "7-11",
            "23-19",
            "11-15",
            "25-22",
            "2-6",
            "28-24",
            "3-7",
            "18-9",
            "9-2",
            "19-10",
            "10-3",
            "3-12",
            "22-18",
            "1-6",
            "2-9",
            "24-19",
            "5-14",
            "4-8",
            "18-9",
            "12-3",
        ]

        self._run_gameplay_test(moves, "white")

    def test_that_stalemate_can_occur_after_forty_moves(self):
        game = Game()
        game.reset()

        moves = [
            "26-23",
            "6-9",
            "23-18",
            "9-13",
            "30-26",
            "2-6",
            "26-23",
            "6-9",
            "18-14",
            "13-17",
            "14-10",
            "17-22",
            "10-6",
            "22-26",
            "6-2",
            "26-30",
        ]

        for move in moves:
            move_made = game.move(move)
            assert move_made

        # Both black and white now have a king

        # Move the kings back and forth
        repeated_moves = ["2-6", "30-26", "6-2", "26-30"]
        for _ in range(6):
            for move in repeated_moves:
                move_made = game.move(move)
                assert move_made

        # Moves without a piece taken should now be 40.
        # The next time game_over is called, the game will end in a draw
        assert game.game_over()
        assert game.result == "draw"
