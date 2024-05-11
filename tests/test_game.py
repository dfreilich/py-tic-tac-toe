import unittest
from tictactoe.game import Game
from tictactoe.player import Player
from unittest.mock import MagicMock


class TestGame(unittest.TestCase):
    def test_check_winner(self):
        api_wrapper = MagicMock()
        api_wrapper.get_random_choice.return_value = 0
        x_player = Player("X", api_wrapper)
        o_player = Player("O", api_wrapper)
        game = Game(x_player, o_player)

        game.board.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertTrue(game.check_winner())

        game.board.board = ["", "X", "X", "Y", "Y", "Y", " ", " ", " "]
        self.assertTrue(game.check_winner())


if __name__ == "__main__":
    unittest.main()
