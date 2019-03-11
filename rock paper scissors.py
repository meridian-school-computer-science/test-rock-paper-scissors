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
    def play(self, a_strategy):
        self.play = a_strategy


class StrategyList(list):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.options = []

    def add_strategy(self, a_strategy: Strategy):
        self.options.append(a_strategy)

    def __repr__(self):
        return f"StrategyList ({self.name})"

    def __str__(self):
        message = f"{self.name} ="
        for e in self.options:
            message = message + " " + e + ","
        return message [:-1]

    def get_random(self):
        return random.choice(self.options)


class Strategy:

    def __init__(self, name):
        self.name = name
        self.defeats = Strategy

    @self.defeats.setter
    def defeats(self, other):
        self.defeats = other

    def __repr__(self):
        return f"Strategy ({self.name})"

    def __str__(self):
        return f"{self.name}, defeats {self.defeats}"


class Controller:

    def __init__(self):
        self.strategy_list = StrategyList('Basic')
        self.human = HumanPlayer('temp')
        self.computer = ComputerPlayer('HAL')

    def build_strategy_list(self):
        rock = Strategy('rock')
        paper = Strategy('paper')
        scissors = Strategy('scissors')
        rock.defeats = scissors
        paper.defeats = rock
        scissors.defeats = paper
        self.strategy_list.add_strategy(rock)
        self.strategy_list.add_strategy(paper)
        self.strategy_list.add_strategy(scissors)

    def do_computer_random(self):
        play = self.strategy_list.get_random()
        self.computer.set_random(play)
