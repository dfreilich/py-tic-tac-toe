import unittest
from tictactoe.board import Board
from tictactoe.player import Player
from unittest.mock import MagicMock


class TestPlayer(unittest.TestCase):
    def test_get_move(self):
        board = Board()
        api_wrapper = MagicMock()
        api_wrapper.get_random_choice.return_value = 0
        player = Player("X", api_wrapper)
        move = player.get_move(board)
        self.assertIn(move, board.available_moves())


if __name__ == "__main__":
    unittest.main()
