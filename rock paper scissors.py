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

    def __str__(self):
        return f"{self.name} with {self.wins} wins, and {self.losses}"


class HumanPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        self.play = Strategy

    def get_name(self):
        temp = input('Please enter the name you would like to be called by: ')
        self.name = temp


class ComputerPlayer(Player):
    """ Purpose: This class is for a computer opponent.

        The strategy for the ComputerPlayer needs to use a random choose function from StrategyList object.

    """

    def __init__(self, name):
        super().__init__(name)
        self.play = Strategy

    def set_random(self, a_strategy):
        """

        :type a_strategy: Strategy
        """
        self.play = a_strategy

    @property
    def play(self):
        return self.play

    def play(self, a_strategy):
        self.play = a_strategy


class StrategyList(list):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.options = []

    def add_strategy(self, a_strategy):
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

    def dominates(self, other):
        self.defeats = other

    def __repr__(self):
        return f"Strategy ({self.name})"

    def __str__(self):
        return f"{self.name}, defeats {self.defeats.name}"


class Controller:

    def __init__(self):
        self.strategy_list = StrategyList('Basic')
        self.human = HumanPlayer('temp')
        self.human.get_name()
        self.computer = ComputerPlayer('HAL')
        self.tie = ComputerPlayer('Tie')
        self.winner = Player
        self.build_strategy_list()

    def build_strategy_list(self):
        rock = Strategy('rock')
        paper = Strategy('paper')
        scissors = Strategy('scissors')
        quit = Strategy('quit')
        rock.dominates(scissors)
        paper.dominates(rock)
        scissors.dominates(paper)
        self.strategy_list.add_strategy(rock)
        self.strategy_list.add_strategy(paper)
        self.strategy_list.add_strategy(scissors)
        self.strategy_list.add_strategy(quit)

    def do_computer_random(self):
        play = self.strategy_list.get_random()
        self.computer.set_random(play)

    def get_human_play(self):
        choice = int(input('Please choose a strategy:\n1) Rock, \n2) Paper, \n3)Scissors, or \n4) Quit.'))
        if choice == 1:
            self.human.play = self.strategy_list[0]
        elif choice == 2:
            self.human.play = self.strategy_list[1]
        elif choice == 3:
            self.human.play = self.strategy_list[2]
        elif choice == 4:
            self.human.play = self.strategy_list[3]

    def set_winner(self):
        if self.computer.play.dominates(self.human.play):
            self.winner = self.computer
        elif self.human.play.dominates(self.computer.play):
            self.winner = self.human
        else:
            self.winner = self.tie

    def do_round_with_ties(self):
        self.do_computer_random()
        self.get_human_play()
        if self.human.play != self.strategy_list[3]:
            self.set_winner()
            self.update_scores()

    def update_scores(self):
        if self.winner == self.human:
            self.human.add_wins()
            self.computer.add_losses()
        elif self.winner == self.computer:
            self.computer.add_wins()
            self.human.add_losses()
        else:
            self.computer.add_ties()
            self.human.add_ties()


game = Controller()
print(game.human.name)
print(game.computer.name)

print(game.computer.play)
print(game.human.play)
print(game.winner)
