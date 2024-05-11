import unittest
from unittest.mock import patch
from tictactoe.random import RandomAPIWrapper


class TestAPIWrapper(unittest.TestCase):
    @patch("tictactoe.random.requests.get")
    def test_get_random_choice_valid_return(self, mock_get):
        mock_response = {"value": 7}
        mock_get.return_value.json.return_value = mock_response
        api_wrapper = RandomAPIWrapper("http://localhost:5999")

        result = api_wrapper.get_random_choice([3, 5, 7])
        self.assertEqual(result, 7)
        mock_get.assert_called_once_with(
            "http://localhost:5999/random/default/choice", params={"value": [3, 5, 7]}
        )

    @patch("tictactoe.random.requests.get")
    def test_get_random_choice_invalid_return(self, mock_get):
        mock_response = {"value": "str"}
        mock_get.return_value.json.return_value = mock_response
        api_wrapper = RandomAPIWrapper("http://localhost:5999")

        with self.assertRaises(ValueError):
            api_wrapper.get_random_choice([3, 5, 7])
        mock_get.assert_called_once_with(
            "http://localhost:5999/random/default/choice", params={"value": [3, 5, 7]}
        )

    @patch("tictactoe.random.requests.get")
    def test_get_random_choice_missing_value(self, mock_get):
        mock_response = {"no_value": "str"}
        mock_get.return_value.json.return_value = mock_response
        api_wrapper = RandomAPIWrapper("http://localhost:5999")

        with self.assertRaises(KeyError):
            api_wrapper.get_random_choice([3, 5, 7])
        mock_get.assert_called_once_with(
            "http://localhost:5999/random/default/choice", params={"value": [3, 5, 7]}
        )


if __name__ == "__main__":
    unittest.main()
