from abc import ABC, abstractmethod
from typing import List

from alphadraughts.algorithms import choose_random_moves


class BasePlayer(ABC):
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0

    @abstractmethod
    def choose_move(self, possible_moves: List) -> str:
        pass

    @property
    def win_rate(self):
        return self.wins / max(1, self.wins + self.losses + self.draws)


class HumanPlayer(BasePlayer):
    def __init__(self, name):
        self.name = name
        super(HumanPlayer, self).__init__()

    def choose_move(self, possible_moves: List) -> str:
        while True:
            move = input("{} to move: ".format(self.name))
            if move.lower() == "help":
                print("Valid moves for {}: ".format(self.name))
                for move in possible_moves:
                    print(move)
            elif move.lower() in ("quit", "abandon", "leave"):
                return "abandon"
            else:
                return move


class RandomBot(BasePlayer):
    def choose_move(self, possible_moves: List) -> str:
        return choose_random_moves(possible_moves)
