from tictactoe.board import Board
from tictactoe.player import Player


class Game:
    def __init__(self, x_player: Player, o_player: Player):
        self.board = Board()
        self.x_player = x_player
        self.o_player = o_player
        self.current_player = x_player

    def print_board(self):
        """Prints the current state of the board."""
        self.board.print_board()

    def play(self):
        """Starts the game."""
        while self.board.available_moves():
            self.print_board()
            move = self.current_player.get_move(self.board)
            self.board.make_move(move, self.current_player.letter)
            if self.check_winner():
                self.print_board()
                print(f"{self.current_player.letter} wins!")
                return self.current_player.letter
            self.current_player = (
                self.o_player if self.current_player == self.x_player else self.x_player
            )
        print("It's a tie!")

    def check_winner(self) -> bool:
        """Checks if the current player has won."""
        b = self.board.board
        return (
            (b[0] == b[1] == b[2] != " ")
            or (b[3] == b[4] == b[5] != " ")
            or (b[6] == b[7] == b[8] != " ")
            or (b[0] == b[3] == b[6] != " ")
            or (b[1] == b[4] == b[7] != " ")
            or (b[2] == b[5] == b[8] != " ")
            or (b[0] == b[4] == b[8] != " ")
            or (b[2] == b[4] == b[6] != " ")
        )
