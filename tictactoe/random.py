import requests
from typing import List


class RandomAPIWrapper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_random_choice(self, values: List[int]) -> int:
        """Makes a request to the external API to get a random choice."""
        url = f"{self.base_url}/random/default/choice"
        response = requests.get(url, params={"value": values})
        string_number = response.json()["value"]
        try:
            return int(string_number)
        except (ValueError, KeyError) as e:
            raise ValueError(
                f"Unable to parse move from random API (response: {response})"
            ) from e
