import random
import pickle


class Player:
    """ Purpose: This the super class for both the human player and computer player Classes.

        User fields: username, (password not available), rock_plays, paper_plays, scissors_plays, wins, losses, ties
    """
    def __init__(self, the_user):
        self.name = the_user.username
        self.play = Strategy
        self.wins = the_user.wins
        self.losses = the_user.losses
        self.ties = the_user.ties
        self.rock_plays = the_user.rock_plays
        self.paper_plays = the_user.paper_plays
        self.scissors_plays = the_user.scissors_plays

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
        return self.rock_plays         # returns the real number of plays by removing artificial 1

    @property
    def get_paper_plays(self):
        return self.paper_plays        # returns the real number of plays by removing artificial 1

    @property
    def get_scissors_plays(self):
        return self.scissors_plays     # returns the real number of plays by removing artificial 1

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
        if self.rock_ratio == 0 or self.paper_ratio == 0 or self.scissors_ratio == 0:
            return [.33, .33, .33]
        else:
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
    def __init__(self, the_user):
        super().__init__(the_user)

    def get_play_from_user(self, the_strategy):
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

    def get_play(self):
        return self.play

    def set_play(self, a_strategy):
        self.play = a_strategy

    def select_random_play(self, the_strategy_list):
        play = the_strategy_list.get_random()
        self.set_play(play)


class StrategyList(list):
    """ Purpose: This class is to hold all possible Strategy class objects.

    """
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
            message = message + " " + str(e) + ","
        return message [:-1]

    def get_random(self):
        return random.choice(self.options)


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
    def __init__(self, the_user):
        self.strategy_list = StrategyList('Basic')
        self.human = HumanPlayer(the_user)
        hal = User('HAL', 'hal', 0, 0, 0, 0, 0, 0)
        self.computer = ComputerPlayer(hal)
        tie = User('Tie', 'tie', 0, 0, 0, 0, 0, 0)
        self.tie = ComputerPlayer(tie)
        self.winner = Player
        self.want_to_quit = False
        self.build_strategy_list()

    def build_strategy_list(self):
        rock = Strategy('rock')
        paper = Strategy('paper')
        scissors = Strategy('scissors')
        rock.dominates(scissors)
        paper.dominates(rock)
        scissors.dominates(paper)
        self.strategy_list.add_strategy(rock)
        self.strategy_list.add_strategy(paper)
        self.strategy_list.add_strategy(scissors)

    def do_computer_random(self):
        self.computer.select_random_play(self.strategy_list)

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
        self.human.get_play_from_user(self.strategy_list)

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


class RawData:
    """ Purpose: This class if to read and dump file data to be parsed by other class.

    """
    def __init__(self, the_filename):
        self.data = None
        self.filename = the_filename
        self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.filename, 'br') as f:
            self.data = pickle.load(f)

    def dump_data_to_file(self):
        with open(self.filename, 'bw') as f:
            pickle.dump(self.data, f)

    def __str__(self):
        return f" {self.data}"

    def __repr__(self):
        return f"Raw data object ({self.filename})."


class UserList(list):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.items = []

    def add_a_user(self, a_user):
        self.items.append(a_user)

    @property
    def data_for_pickle(self):
        temp_list = []
        for user in self.items:
            temp_user = user.user_dictionary
            print(temp_user)
            temp_list.append(temp_user)
        return temp_list

    def is_an_existing_username(self, test_name):
        return test_name in self.existing_user_names

    @property
    def existing_user_names(self):
        return [each_user.username for each_user in self.items]

    def get_a_user_based_on_username(self, the_username):
        for user in self.items:
            if user.username == the_username:
                return user

    def pop_a_user(self, the_username):
        i = 0
        while i < len(self.items):
            if self.items[i].username == the_username:
                return self.items.pop(i)
            else:
                i += 1


class User:

    def __init__(self, name, password, rock, paper, scissors, wins, losses, ties):
        self.username = name
        self.__password = password
        self.rock_plays = rock
        self.paper_plays = paper
        self.scissors_plays = scissors
        self.wins = wins
        self.losses = losses
        self.ties = ties

    def __repr__(self):
        return f"User({self.username})"

    def __str__(self):
        return f"Username: {self.username}, W/L/T: {self.wins}/{self.losses}/{self.ties}"

    @property
    def list_of_wins_losses_ties(self):
        return [self.wins, self.losses, self.ties]

    @property
    def list_of_plays(self):
        return [self.rock_plays, self.paper_plays, self.scissors_plays]

    @property
    def user_dictionary(self):
        return {'username': self.username,
                'password': self.__password,
                'rock': self.rock_plays,
                'paper': self.paper_plays,
                'scissors': self.scissors_plays,
                'wins': self.wins,
                'losses': self.losses,
                'ties': self.ties}

    def password_ok(self, test):
        return test == self.__password

    def update_game_data(self, the_controller):
        #         self.username = name
        #         self.__password = password
        #         self.rock_plays = rock
        #         self.paper_plays = paper
        #         self.scissors_plays = scissors
        #         self.wins = wins
        #         self.losses = losses
        #         self.ties = ties
        self.wins = the_controller.human.wins
        self.losses = the_controller.human.losses
        self.ties = the_controller.human.ties
        self.rock_plays = the_controller.human.rock_plays
        self.paper_plays = the_controller.human.paper_plays
        self.scissors_plays = the_controller.human.scissors_plays


class ManageUser:

    def __init__(self, the_filename):
        self.raw_data = RawData(the_filename)
        self.user_list = UserList('Registered Users')
        self.build_user_list()
        self.registered_user = User
        self.user_confirmed = False

    def build_user_list(self):
        # (self, name, password, rock, paper, scissors, wins, losses, ties)
        for user in self.raw_data.data:
            temp_user = User(user['username'],
                             user['password'],
                             user['rock'],
                             user['paper'],
                             user['scissors'],
                             user['wins'],
                             user['losses'],
                             user['ties'])
            self.user_list.add_a_user(temp_user)

    def store_all_user_data(self):
        self.raw_data.data = self.user_list.data_for_pickle
        self.raw_data.dump_data_to_file()

    def ask_for_login(self):
        valid = False
        while not valid:
            choice = input(f"Welcome. Please select the number that applies:"
                    f"\n1) Returning user.\n2) New user. \nSelect #: ")
            if choice == '1':
                self.do_login()
                valid = True
            elif choice == '2':
                new_user_name = self.new_login()
                new_password = self.create_new_password()
                self.build_new_user(new_user_name, new_password)
                valid = True
            else:
                print(f"Invalid input. Please just enter the number.")

    def do_login(self):
        print('\n\n\nLogin for existing users.\n')
        i = 1
        while i < 3:
            test_name = input("Please enter your username: ")
            if self.user_list.is_an_existing_username(test_name):
                self.verify_password(test_name)
                if self.user_confirmed:
                    self.registered_user = self.user_list.pop_a_user(test_name)
                    break
            else:
                i += 1
        while not self.user_confirmed:
            print("Sorry. User could not be confirmed. Please login as a new user.")
            new_user_name = self.new_login()
            new_password = self.create_new_password()
            self.build_new_user(new_user_name, new_password)

    def new_login(self):
        print('\n\n\nLogin for new users.\n')
        # username
        new_user = self.user_list.items[0]["username"]
        while self.user_list.is_an_existing_username(new_user):
            new_user = input("Please enter a new username: ")
        return new_user

    def create_new_password(self):
        #passwords
        new_password = ""
        confirm_password = "zz"
        while new_password != confirm_password:
            new_password = input("Please enter your password: ")
            confirm_password = input("Please reconfirm your password: ")
        return new_password

    def build_new_user(self, the_user_name, the_new_password):
        self.registered_user = User(the_user_name, the_new_password, 0, 0, 0, 0, 0, 0)
        self.user_confirmed = True

    def verify_password(self, the_username):
        the_user = self.user_list.get_a_user_based_on_username(the_username)
        i = 1
        while i < 3:
            test_password = input(f"Please enter your password try #{i}: ")
            if the_user.password_ok(test_password):
                print("Password confirmed, thank you.")
                self.user_confirmed = True
                break
            else:
                print("Password incorrect.")
                i += 1


"""
                Main Program
"""
print('Test with users: alpha password: alpha1, or bravo password: bravo2\n pattern is all the way to hotel8')
filename = 'rpsUserData3.txt'
login_manager = ManageUser(filename)

while not login_manager.user_confirmed:
    login_manager.ask_for_login()

the_player = login_manager.registered_user
game = Controller(the_player)

while not game.want_to_quit:
    game.ask_to_play_round()
    if not game.want_to_quit:
        game.do_round_with_ties()
        print(f"The winner was: {game.winner}")
    else:
        print('ok, goodbye.')
        # save data from this game to the storage file
        the_player.update_game_data(game)
        login_manager.user_list.add_a_user(the_player)
        login_manager.store_all_user_data()
