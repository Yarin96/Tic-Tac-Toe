import time
from player import HumanPlayer, ComputerAiPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_numbers():
            number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
            for row in number_board:
                print(' | ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        # enumerate creates a list of (index, value) items.
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def number_of_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, symbol):
        is_valid_move = False
        if self.board[square] == ' ':
            self.board[square] = symbol
            if self.winner(square, symbol):
                self.current_winner = symbol
            is_valid_move = True
        return is_valid_move

    def winner(self, square, symbol):
        row_index = square // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == symbol for spot in row]):
            return True

        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == symbol for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == symbol for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == symbol for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_numbers()

    symbol = 'X'
    while game.empty_squares():
        if symbol == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, symbol):
            if print_game:
                print(symbol + f' chose square {square}\n')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(symbol + ' has won the game!')
                return symbol

            symbol = 'O' if symbol == 'X' else 'X'

        time.sleep(0.5)

    if print_game:
        print('The game is tied!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerAiPlayer('O')
    tic_tac_toe = TicTacToe()
    play(tic_tac_toe, x_player, o_player, print_game=True)