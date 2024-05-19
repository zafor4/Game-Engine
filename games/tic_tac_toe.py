# games/tic_tac_toe.py

from .game_base import GameBase

class TicTacToe(GameBase):
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # Print the current board state
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def print_board_nums(self):
        # Prints the board with numbers to indicate positions
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        # Returns a list of available moves (indices)
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return len(self.available_moves())

    def make_move(self, square, letter):
        # Make a move if the square is available
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check if there's a winner
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def start(self):
        # Start a new game
        print("Starting Tic Tac Toe")
        self.board = [" " for _ in range(9)]
        self.current_winner = None
        letter = "X"  # Starting letter
        while self.empty_squares():
            if self.num_empty_squares() == 9:
                self.print_board_nums()
            else:
                self.print_board()
            square = int(input(f"{letter}'s turn. Input move (0-8): "))
            if square not in self.available_moves():
                print("Invalid move. Try again.")
                continue
            if self.make_move(square, letter):
                if self.current_winner:
                    self.print_board()
                    print(f"{letter} wins!")
                    return
                letter = "O" if letter == "X" else "X"  # Switch player
        self.print_board()
        print("It's a tie!")

    def get_name(self):
        return "Tic Tac Toe"
