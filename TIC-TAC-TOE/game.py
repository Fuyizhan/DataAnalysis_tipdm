from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None #keep track of winner

    def print_board(self):
        # getting each row
        for row in [self.board[ i * 3 : (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_move(self):
        # moves = []
        # for i, spot in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_square(self):
        if ' ' in self.board:
            return True
        return False


    def make_move(self, square, letter):
        #because the move could be invalid(praise ValueError)
        #so need to judge
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind+1)*3]
        if all([letter == spot for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([letter == spot for spot in column]):
            return True

        #check diagonals
        #(0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([letter == spot for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([letter == spot for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player):
    letter = 'x'
    while game.empty_square():
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            print(letter + f'makes a move to square {square}')
            game.print_board()
            print(' ')

            if game.current_winner:
                print(letter + 'win')
                return letter
        #after made a move, we need to alternate letters
        letter = 'o' if letter == 'x' else 'x'

    if game.current_winner is None:
        print('Tie')

if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player)
