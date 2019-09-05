from alphadraughts import Game, RandomBot

if __name__ == "__main__":
    game = Game(black=RandomBot())
    game.play()
