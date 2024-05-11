import io
import sys
import unittest
from unittest.mock import patch

from tictactoe.board import Board


class TestBoard(unittest.TestCase):
    def test_make_move(self):
        board = Board()
        board.make_move(0, "X")
        self.assertEqual(board.board, ["X", " ", " ", " ", " ", " ", " ", " ", " "])

        board.make_move(2, "O")
        self.assertEqual(board.board, ["X", " ", "O", " ", " ", " ", " ", " ", " "])

    def test_available_moves(self):
        board = Board()
        board.make_move(1, "X")
        self.assertEqual(board.available_moves(), [0, 2, 3, 4, 5, 6, 7, 8])

        board.make_move(0, "X")
        self.assertEqual(board.available_moves(), [2, 3, 4, 5, 6, 7, 8])

        board = Board()
        for i in range(9):
            board.make_move(i, "X" if i % 2 == 0 else "O")
        self.assertEqual(board.available_moves(), [])

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_print_board(self, mock_stdout):
        board = Board()
        expected_output = """-------------
|   |   |   |
|   |   |   |
|   |   |   |
"""
        board.print_board()
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
