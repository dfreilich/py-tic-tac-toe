from tictactoe.random import RandomAPIWrapper
from tictactoe.board import Board


class Player:
    def __init__(self, letter: str, api_wrapper: RandomAPIWrapper):
        self.letter = letter
        self.api_wrapper = api_wrapper

    def get_move(self, board: Board) -> int:
        return self.api_wrapper.get_random_choice(board.available_moves())
