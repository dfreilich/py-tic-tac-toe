from typing import List


class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        """Prints the current state of the board."""
        print("-------------")
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def make_move(self, square: int, letter: str) -> bool:
        """Marks a move on the board."""
        if self.board[square] == " ":
            self.board[square] = letter
            return True
        return False

    def available_moves(self) -> List[int]:
        """Returns a list of available moves."""
        return [i for i, spot in enumerate(self.board) if spot == " "]
