import random


class Player:

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def add_wins(self):
        self.wins += 1

    def add_losses(self):
        self.losses += 1

    def add_ties(self):
        self.ties += 1


class HumanPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        self.play = Strategy


class ComputerPlayer(Player):
    """ Purpose: This class is for a computer opponent.

        The strategy for the ComputerPlayer needs to use a random choose function from StrategyList object.

    """

    def __init__(self):
        super().__init__(name)
        self.play = Strategy

    def set_random(self, a_strategy: Strategy):
        """

        :type a_strategy: Strategy
        """
        self.play = a_strategy

    @property
    def play(self):
        return self.play

    @play.setter
    def play(self, value):
        self._play = value


class StrategyList(list):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.options = []

    def add_strategy(self, a_strategy: Strategy):
        self.options.append(a_strategy)


class Strategy:

    def __init__(self, name):
        self.name = name
        self.defeats = Strategy

    @self.defeats.setter
    def defeats(self, other):
        self.defeats = other
