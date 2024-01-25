import random


class Player:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_move())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        val = None
        valid_square = False
        while not valid_square:
            try:
                val = int(input(self.letter + '\'s turn. input move(0-8):'))
                if val not in game.available_move():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square.Try again')

        return val



