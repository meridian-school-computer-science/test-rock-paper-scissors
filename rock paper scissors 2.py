import random


class Player:
    """ Purpose: This the super class for both the human player and computer player Classes.

    """
    def __init__(self, name):
        self.name = name
        self.play = Strategy
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.rock_plays = 1
        self.paper_plays = 1
        self.scissors_plays = 1

    def add_wins(self):
        self.wins += 1

    def add_losses(self):
        self.losses += 1

    def add_ties(self):
        self.ties += 1

    def add_rock_plays(self):
        self.rock_plays += 1

    def add_paper_plays(self):
        self.paper_plays += 1

    def add_scissors_plays(self):
        self.scissors_plays += 1

    @property
    def get_rock_plays(self):
        return self.rock_plays - 1         # returns the real number of plays by removing artificial 1

    @property
    def get_paper_plays(self):
        return self.paper_plays - 1        # returns the real number of plays by removing artificial 1

    @property
    def get_scissors_plays(self):
        return self.scissors_plays - 1     # returns the real number of plays by removing artificial 1

    @property
    def total_plays(self):
        return self.rock_plays + self.paper_plays + self.scissors_plays

    @property
    def rock_ratio(self):
        return self.rock_plays/self.total_plays

    @property
    def paper_ratio(self):
        return self.paper_plays/self.total_plays

    @property
    def scissors_ratio(self):
        return self.scissors_plays/self.total_plays

    @property
    def list_of_play_ratios(self):
        return [self.rock_ratio, self.paper_ratio, self.scissors_ratio]

    def __str__(self):
        if self.name == 'Tie':
            return f"Neither, we tied."
        else:
            return f"{self.name} with {self.wins} wins, {self.losses} losses, and {self.ties} ties."


class HumanPlayer(Player):
    """ Purpose: This class is for a human player. Sub-class of Player Class.

        The strategy for the ComputerPlayer needs to use a random choose function from StrategyList object.


    """
    def __init__(self, name):
        super().__init__(name)

    def get_name(self):
        temp = input('Please enter the name you would like to be called by: ')
        self.name = temp

    def get_play(self, the_strategy):
        correct = False
        while not correct:
            choice = int(input('Please choose a strategy:\n1) Rock, \n2) Paper, \n3) Scissors.\nSelection: '))
            if choice == 1:
                self.play = the_strategy.options[0]
                correct = True
            elif choice == 2:
                self.play = the_strategy.options[1]
                correct = True
            elif choice == 3:
                self.play = the_strategy.options[2]
                correct = True
            else:
                print('Sorry, improper choice detected. Please enter only 1 - 3.')

class ComputerPlayer(Player):
    """ Purpose: This class is for a computer opponent. Sub-class of Player Class.

        The strategy for the ComputerPlayer needs to use a random choose function from StrategyList object.
        in version 2 there is a trend based computer play in the Controller class

    """
    def __init__(self, name):
        super().__init__(name)

    def set_play(self, a_strategy):
        self.play = a_strategy

    def get_play(self, the_strategy_list):
        play = the_strategy_list.get_random()
        self.set_play(play)


class StrategyList(list):
    """ Purpose: This class is to hold all possible Strategy class objects.

    """
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.options = []
        self.build_strategy_list()

    def add_strategy(self, a_strategy):
        self.options.append(a_strategy)

    def __repr__(self):
        return f"StrategyList ({self.name})"

    def __str__(self):
        message = f"{self.name} ="
        for e in self.options:
            message = message + " " + str(e) + ","
        return message [:-1]

    def get_random(self):
        return random.choice(self.options)

    def build_strategy_list(self):
        rock = Strategy('rock')
        paper = Strategy('paper')
        scissors = Strategy('scissors')
        rock.dominates(scissors)
        paper.dominates(rock)
        scissors.dominates(paper)
        self.add_strategy(rock)
        self.add_strategy(paper)
        self.add_strategy(scissors)


class Strategy:
    """ Purpose: This class is for each possible strategy.


    """
    def __init__(self, name):
        self.name = name
        self.defeats = Strategy

    def dominates(self, other):
        self.defeats = other

    def __repr__(self):
        return f"Strategy ({self.name})"

    def __str__(self):
        return f"{self.name}"

    def get_strategy_description(self):
        temp = f"{self.name}"
        if self.name != 'quit':
            temp = temp + f" defeats {self.defeats.name}"
        return temp


class Controller:
    """ Purpose: This class is for the overarching control of the game.
        builds the players and the strategies and puts the strategies in a list.

    """
    def __init__(self):
        self.strategy_list = StrategyList('Basic')
        self.human = HumanPlayer('temp')
        self.human.get_name()
        self.computer = ComputerPlayer('HAL')
        self.tie = ComputerPlayer('Tie')
        self.winner = Player
        self.want_to_quit = False

    def do_computer_random(self):
        self.computer.get_play(self.strategy_list)

    def update_player_trend_data(self, which_player):
        if which_player.play == self.strategy_list.options[0]:
            which_player.add_rock_plays()
        elif which_player.play == self.strategy_list.options[1]:
            which_player.add_paper_plays()
        else:
            which_player.add_scissors_plays()

    def do_computer_based_on_trend(self):
        user_trend = self.human.list_of_play_ratios
        print(user_trend)
        die_roll = random.random()
        if die_roll <= user_trend[0]:                               # user random to rock
            self.computer.set_play(self.strategy_list.options[1])      # play paper
        elif die_roll <= (user_trend[0] + user_trend[1]):           # greater than rock less than paper so paper
            self.computer.set_play(self.strategy_list.options[2])      # play scissors
        else:                                                       # so scissors
            self.computer.set_play(self.strategy_list.options[0])      # play rock

    def get_human_play(self):
        self.human.get_play(self.strategy_list)

    def set_winner(self):
        if self.computer.play.defeats == self.human.play:
            self.winner = self.computer
        elif self.human.play.defeats == self.computer.play:
            self.winner = self.human
        else:
            self.winner = self.tie

    def do_round_with_ties(self):
        # self.do_computer_random()
        self.do_computer_based_on_trend()
        self.get_human_play()
        self.update_player_trend_data(self.human)
        self.update_player_trend_data(self.computer)
        self.set_winner()
        print(self.show_plays())
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

    def show_plays(self):
        return f"Round complete, you chose {self.human.play.name}, and I chose {self.computer.play.name}."

    def ask_to_play_round(self):
        correct = False
        while not correct:
            choice = input('Prepare for round...\nAre you ready? (y/n): ')
            if choice.lower() == 'n':
                self.want_to_quit = True
                correct = True
            elif choice.lower() == 'y':
                self.want_to_quit = False
                correct = True
            else:
                print('Improper input detected, please enter only a y or n.')

"""
                Main Program
"""
game = Controller()
while not game.want_to_quit:
    game.ask_to_play_round()
    if not game.want_to_quit:
        game.do_round_with_ties()
        print(f"The winner was: {game.winner}")
    else:
        print('ok, goodbye.')
