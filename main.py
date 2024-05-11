import os

from tictactoe.random import RandomAPIWrapper
from tictactoe.game import Game
from tictactoe.player import Player


def main():
    random_url = os.getenv("RANDOM_API", "http://localhost:5050")
    random_api = RandomAPIWrapper(random_url)

    x_player = Player("X", random_api)
    o_player = Player("O", random_api)
    game = Game(x_player, o_player)
    game.play()


if __name__ == "__main__":
    main()
