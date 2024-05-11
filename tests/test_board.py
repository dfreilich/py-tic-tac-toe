import unittest
from tictactoe.board import Board


class TestBoard(unittest.TestCase):
    def test_make_move(self):
        board = Board()
        board.make_move(0, "X")
        self.assertEqual(board.board, ["X", " ", " ", " ", " ", " ", " ", " ", " "])

    def test_available_moves(self):
        board = Board()
        board.make_move(0, "X")
        self.assertEqual(board.available_moves(), [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == "__main__":
    unittest.main()
