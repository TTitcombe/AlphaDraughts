"""Monte-Carlo tree search"""
import random


class RolloutPolicy:
    def __init__(self):
        pass

    def select_action(self, actions):
        raise NotImplementedError()


class UniformRolloutPolicy(RolloutPolicy):
    def select_action(self, actions):
        return random.choice(actions)


# ----- Tree search alg ----- #
class MCTS:
    def __init__(self):
        self._policy = UniformRolloutPolicy()

    def choose_move(self, state, actions):
        raise NotImplementedError("MCTS is in progress")
